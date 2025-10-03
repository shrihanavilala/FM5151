from typing import Optional, Self

from blackjack.card import Card, Label


def _card_value(c: Card) -> int:
    """Helper function to calculate the value of a card. Aces and Face cards are
    worth 11, other cards are worth their numeric value"""
    value = c.label.value
    match c.label:
        case Label.JACK | Label.QUEEN | Label.KING:
            value = 10
        case Label.ACE:
            value = 11
    return value


class Hand:
    @classmethod
    def make_empty(cls) -> Self:
        return cls()

    @classmethod
    def make_dealt(cls, card1: Card, card2: Card) -> Self:
        return cls((card1, card2))

    def __init__(self, cards: Optional[tuple[Card, Card]] = None) -> None:
        """Initial deal"""
        if cards is None:
            self.cards = []
        else:
            self.cards = list(cards)

    def __repr__(self) -> str:
        """For debugging"""
        return "".join([str(c) + " " for c in self.cards])

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def total(self) -> int:
        """Tallies up the total of all the cards (can be > 21)"""
        # Your implementation
        return sum([_card_value(n) for n in self.cards])

    def value(self) -> int:
        """Value of all cards in deck (if bust is 0)"""
        # Your implementation
        if self.is_bust():
            return 0
        return self.total()

    def deal(self, card: Card) -> None:
        """Add a card to the hand"""
        # Your implementation
        self.cards.append(card)

    def clear(self) -> None:
        """Clear the hand"""
        # Your implementation
        self.cards = []

    def is_bust(self) -> bool:
        """Convenience function for whether hand is bust"""
        # Your implementation
        return sum([_card_value(n) for n in self.cards]) > 21

    def is_blackjack(self) -> bool:
        """Convenience function for whether hand is a blackjack"""
        # Your implementation
        return sum([_card_value(n) for n in self.cards]) == 21
