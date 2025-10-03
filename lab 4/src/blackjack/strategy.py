from abc import ABC, abstractmethod

from blackjack.dealer import DealerView
from blackjack.hand import Hand


class BettingStrategy(ABC):
    @abstractmethod
    def __call__(self, current_amount: int) -> int:
        """Decide how much to bet given current amount of cash. Returns the
        amount of the bet decided"""
        pass


class PlayingStrategy(ABC):
    @abstractmethod
    def __call__(self, hand: Hand, dealer: DealerView) -> None:
        """Derive to implement a strategy for how gambler should play given
        provided hand. Ask the dealer to hit the provided hand until
        satisfied, then return"""
        pass
