from abc import ABC, abstractmethod
from typing import Optional, override

from blackjack.card import Card
from blackjack.deck import Deck
from blackjack.hand import Hand


class DealerView(ABC):
    """Interface of dealer that a Gambler is allowed to see"""

    @abstractmethod
    def up_card(self) -> Card:
        pass

    @abstractmethod
    def hit(self, hand: Hand) -> None:
        pass


class Dealer(DealerView):
    def __init__(
        self, shuffle_at: Optional[int] = None, deck: Optional[Deck] = None
    ) -> None:
        self.hand = Hand.make_empty()
        self._deck = deck or Deck()
        self._shuffle_at = shuffle_at if shuffle_at is not None else 25

    def deal_hands(self, gambler_hand: Hand):
        """Generates the initial deal for the round. The dealer deals from the
        deck, starting with the player and alternating between player and self.
        The deck will be reset and reshuffled if it is below the shuffle_at
        threshold at the start of the deal.
        """
        if self._deck.count() <= self._shuffle_at:
            self._deck.reset()
            self._deck.shuffle()
        # Your implementation
        gambler_hand.deal(self._deck.deal())
        self.hand.deal(self._deck.deal())
        gambler_hand.deal(self._deck.deal())
        self.hand.deal(self._deck.deal())
        

    @override
    def up_card(self) -> Card:
        """The face up card that the gambler can see"""
        # Your implementation
        return self.hand.cards[0]

    @override
    def hit(self, hand: Hand) -> None:
        """Add a card to a hand"""
        # Your implementation
        hand.deal(self._deck.deal())

    def play(self) -> None:
        """Dealer play is formulaic and will hit if total < 17"""
        # Your implementation
        while self.hand.total() < 17:
            self.hit(self.hand)
