from abc import ABC, abstractmethod
from datetime import datetime
from multiprocessing import Value
from typing import Optional, override

import pandas as pd

from systrade.data import BarData
from systrade.position import Position


class PortfolioActivity:
    """History of portfolio activity along with metrics"""

    def __init__(self, records: list[dict]) -> None:
        self._records = records
        self._df = pd.DataFrame.from_records(records)

    def total_return(self) -> float:
        """Total return on portfolio"""
        return self._df["value"].iloc[-1] / self._df["value"].iloc[0] - 1

    def equity_curve(self) -> pd.Series:
        """The total value of the portfolio at each point in time"""
        return self._df["value"]

    def df(self, condensed=True) -> pd.DataFrame:
        """Return all portfolio activity. If condensed, will keep individual
        position information packed in lists"""
        if condensed:
            result = self._df.copy()
        else:
            result = self._df.explode(
                ["symbols", "quantities", "prices", "asset_values"]
            )
        return result


class PortfolioView(ABC):
    """A read-only portfolio view"""

    @abstractmethod
    def cash(self) -> float:
        """Current cash balance"""

    @abstractmethod
    def asset_value(self) -> float:
        """Current market value of all assets"""

    @abstractmethod
    def asset_value_of(self, symbol: str) -> float:
        """Current market value of symbol"""

    @abstractmethod
    def value(self) -> float:
        """Current market value of assets + cash"""

    @abstractmethod
    def as_of(self) -> datetime:
        """As of timestamp"""

    @abstractmethod
    def is_invested(self) -> bool:
        """Whether portfolio currently has asset exposure"""

    @abstractmethod
    def is_invested_in(self, symbol: str) -> bool:
        """Whether portfolio is currently invested in symbol"""

    @abstractmethod
    def position(self, symbol) -> Position:
        """Return position in symbol"""

    @abstractmethod
    def activity(self) -> PortfolioActivity:
        """Return portfolio activity"""


class Portfolio(PortfolioView):
    _zero_tolerance = 1e-8

    def __init__(
        self,
        cash: float,
        current_positions: Optional[dict[str, Position]] = None,
        current_prices: Optional[BarData] = None,
    ) -> None:
        self._cash = cash
        self._current_positions = current_positions or {}
        self._current_prices = (current_prices if current_prices is not None else BarData())
        self._portfolio_activity = list[dict]()

    @override
    def cash(self) -> float:
        return self._cash

    @override
    def asset_value(self) -> float:
        # Your implementation
        total_value = 0
        for position in self._current_positions.values():
            if(position.symbol in self._current_prices.symbols()):
                price = self._current_prices[position.symbol].close
                value = position.value(price)
                total_value += value
            else:
                raise RuntimeError("Current Prices not Updated")
        return total_value
            
            
        

    @override
    def asset_value_of(self, symbol: str) -> float:
        # Your implementation
        if self.is_invested_in(symbol):
            if(symbol in self._current_prices.symbols()):
                price = self._current_prices[symbol].close
                value = self._current_positions[symbol].value(price)
                return value
            else:
                raise RuntimeError("Symbol Not In Prices.")
        else:
                raise ValueError("Symbol Not in Positions")

    @override
    def value(self) -> float:
        # Your implementation
        return self.asset_value() + self.cash()

    @override
    def as_of(self) -> datetime:
        # Your implementation
        return self._current_prices.as_of

    @override
    def is_invested(self) -> bool:
        # Your implementation
        return len(self._current_positions) != 0

    @override
    def is_invested_in(self, symbol: str) -> bool:
        # Your implementation
        return symbol in self._current_positions.keys()

    @override
    def position(self, symbol) -> Position:
        # Your implementation
        if symbol in self._current_positions.keys():
            return self._current_positions[symbol]
        else:
            raise ValueError("Symbol not in Positions")

    @override
    def activity(self) -> PortfolioActivity:
        return PortfolioActivity(self._portfolio_activity)

    def on_data(self, data: BarData) -> None:
        """Cache latest data to use in calculating latest values"""
        self._current_prices = data
        symbols = list(self._current_positions.keys())
        positions = list(self._current_positions.values())
        record = {}
        record["timestamp"] = self.as_of()
        record["cash"] = self.cash()
        record["symbols"] = symbols
        record["quantities"] = [p.qty for p in positions]
        record["prices"] = [data[sym].close for sym in symbols]
        record["asset_values"] = [self.asset_value_of(sym) for sym in symbols]
        record["asset_value"] = self.asset_value()
        record["value"] = self.value()
        self._portfolio_activity.append(record)

    def on_fill(self, symbol: str, price: float, qty: float) -> None:
        """Update portfolio with a fill information (negative qty indicates
        sell). If a fill takes the quantity down to 0 (within tolerance) it
        should be removed from tracking"""

        # Your implementation
        if not self.is_invested_in(symbol): # new stock purchase
            self._current_positions[symbol] = Position(symbol,qty)
            self._cash -= price*qty 
        elif qty <= 0:
            position = self._current_positions[symbol]
            new_quantitiy = position.qty + qty
            self._current_positions[symbol] = Position(position.symbol, new_quantitiy)
            if(new_quantitiy==0):
                self._current_positions.pop(symbol)
            if new_quantitiy < 0: #insufficient qty
                raise RuntimeError("Fill Attempted With Insufficient Quantity")
            self._cash -= price*qty
        elif qty > 0:
            position = self._current_positions[symbol]
            new_quantitiy = position.qty + qty
            self._current_positions[symbol] = Position(position.symbol, new_quantitiy)
            self._cash -= price*qty
                
                
                
