import random
from typing import Iterable, Optional
from blackjack.card import Card


class Deck:
    def __init__(self, cards: Optional[Iterable[Card]] = None) -> None:
        """Initializes a deck with 52 shuffled cards by default or specific
        cards if specified"""

        # Your implementation
        if cards is None:      
            self.indexes = list(range(52))
            self.shuffle()
        else:
            self.indexes: list[int] = [card.index for card in cards]
        self._indexes_orig: list[int] = self.indexes.copy()

    def count(self):
        """Number of cards currently in the deck"""
        return len(self.indexes)
        

    def reset(self):
        """Resets the deck to the original 52 cards"""
        # Your implementation
        self.indexes = self._indexes_orig

    def shuffle(self):
        """Shuffles existing cards"""
        random.shuffle(self.indexes)

    def deal(self) -> Card:
        """Deals a card from the deck"""
        if not self.indexes:
            raise RuntimeError("Deck is empty!")
        # Your implementation
        card = self.indexes.pop()
        return Card.from_index(card)
        
