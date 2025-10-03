"""
Example module containing things we can test.
"""

from abc import ABC, abstractmethod
from typing import override


class Broker(ABC):
    """Base class for brokers"""

    @abstractmethod
    def post_order(self, order: str) -> None:
        # Submit to broker
        pass


class TradingStrategy:
    """Base class for all trading strategies"""

    def __init__(self, broker: Broker) -> None:
        self.history = []
        self.broker = broker

    def on_data(self, data: float) -> None:
        """Invoked when new data is received, and we append to our internal data"""
        self.history.append(data)

    def post_order(self, order: str) -> None:
        """Does some validation then submits order to broker"""
        # Do validation
        # ...
        # Submit order
        self.broker.post_order(order)

    def compute_signal(self) -> str:
        """Specific strategies would implement this"""
        return ""


class AlwaysBuyStrategy(TradingStrategy):
    """Strategy that always buys"""

    def __init__(self, broker: Broker) -> None:
        super().__init__(broker)

    @override
    def compute_signal(self) -> str:
        return "BUY"
