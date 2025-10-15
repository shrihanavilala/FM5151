from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, override
from zoneinfo import ZoneInfo
from datetime import datetime as dt
from datetime import timedelta
import pandas as pd
import numpy as np
from systrade.data import Bar, BarData


class Feed(ABC):
    @abstractmethod
    def start(self) -> None:
        """Start streaming"""

    @abstractmethod
    def stop(self) -> None:
        """Stop streaming"""

    @abstractmethod
    def is_running(self) -> bool:
        """Whether feed is currently running"""

    @abstractmethod
    def subscribe(self, symbol: str) -> None:
        """Subscribe to a symbol"""

    @abstractmethod
    def next_data(self) -> BarData:
        """Block until returning the next available data for subscribed
        symbols"""


class FileFeed(Feed):
    def __init__(
        self, path: str | Path, start: Optional[str] = None, end: Optional[str] = None
    ) -> None:
        """File feed initializer

        Parameters
        ----------
        path
            Full path to data file
        start, optional
            When to start the replay, in YYYY-MM-DD format
        end, optional
            When to end the replay, in YYYY-MM-DD format
        """

        # Your implementation
        self.path : pd.DataFrame = pd.read_csv(path)
        self.path["Date"] = pd.to_datetime(self.path["Date"])
        
        self._start = dt.strptime(start or "2005-01-03", "%Y-%m-%d")
        self._end = dt.strptime(end or "2025-08-29", "%Y-%m-%d")
        
        self.current = self._start
        self.subscribed = []
        self.started : bool = False
    @property
    def df(self) -> pd.DataFrame:
        # Your implementation
        mask = self.path["Date"].apply(dt.date).between(self._start.date(), self._end.date())
        return self.path.loc[mask]

    @override
    def start(self) -> None:
        # Your implementation
        self.started = True

    @override
    def stop(self) -> None:
        # Your implementation
        self.started = False

    @override
    def is_running(self) -> bool:
        return self.started

    @override
    def subscribe(self, symbol: str) -> None:
        # Your implementation
        if symbol in self.path["Symbol"].unique() and symbol not in self.subscribed:
            self.subscribed.append(symbol)
        else:
            raise ValueError("Invalid Symbolpython -m pytest tests/test_feed.py or Symbol Already in List" + symbol+self.path["Symbol"].unique()+self.subscribed)

    @override
    def next_data(self) -> BarData:
        # Your implementation
        bars = BarData(as_of=self.current)
        data = self.path.loc[self.path["Date"].apply(dt.date) == self.current.date()]
        for symbol in self.subscribed:
            symbol_price = data.loc[data["Symbol"] == symbol]
            if(data.empty):
                bars[symbol] = Bar()
                continue
            day_data = Bar(float(symbol_price["Open"].iloc[0]), float(symbol_price["High"].iloc[0]), float(symbol_price["Low"].iloc[0]), float(symbol_price["Close"].iloc[0]), float(symbol_price["Volume"].iloc[0]))
            bars[symbol] = day_data
        if self.current.date() == self._end.date():
            self.stop()
        mask = self.path["Date"].apply(dt.date) == self.current.date()
        pos = mask.idxmax()
        int_loc = self.path.index.get_loc(pos)
        self.current = self.path.iloc[int_loc + 1]["Date"]
        return bars
            
            
