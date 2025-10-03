from enum import IntEnum

__all__ = ("Card", "Suit", "Label")


class Suit(IntEnum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

    def __str__(self) -> str:
        match self.value:
            case self.HEARTS:
                return "❤️"
            case self.DIAMONDS:
                return "♦️"
            case self.CLUBS:
                return "♣️"
            case self.SPADES:
                return "♠️"
            case _:
                raise ValueError(f"Unhandled value {self.value}:{self.name}")


class Label(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __str__(self) -> str:
        match self.value:
            case self.ACE | self.JACK | self.QUEEN | self.KING:
                return self.name.capitalize()
            case _:
                return str(self.value)
    


def _to_index(suit: Suit, label: Label) -> int:
    """Given a suit and label returns the index in a 52 card deck (0...51)"""
    # Your implementation
    #Hearts 0-12, Diamonds 13-25, Spades 26-38, Clubs 39-51
    match suit:
            case Suit.HEARTS:
                return label
            case Suit.DIAMONDS:
                return label + 13
            case Suit.SPADES:
                return label + 26
            case Suit.CLUBS:
                return label + 39


def _from_index(index: int) -> tuple[Suit, Label]:
    """Create a Suit and Label given a numeric index"""
    if index < 0 or index > 51:
        raise ValueError("Invalid index value, should be between 0 and 51")
    # Your implementation
    card_numbers = [
    Label.ACE,
    Label.TWO,
    Label.THREE,
    Label.FOUR,
    Label.FIVE,
    Label.SIX,
    Label.SEVEN,
    Label.EIGHT,
    Label.NINE,
    Label.TEN,
    Label.JACK,
    Label.QUEEN,
    Label.KING
    ]
    match index // 13:
            case 0:
                return Suit.HEARTS, card_numbers[index % 13]
            case 1:
                return Suit.DIAMONDS, card_numbers[index % 13]
            case 2:
                return Suit.SPADES, card_numbers[index % 13]
            case 3:
                return Suit.CLUBS, card_numbers[index % 13]


class Card:
    @classmethod
    def from_index(cls, index: int) -> "Card":
        """Return a card given an index"""
        card = cls(*_from_index(index))
        return card

    def __init__(self, suit: Suit, label: Label) -> None:
        """Initialize 'suit', 'label', and 'index' members"""
        self.suit = suit
        self.label = label
        self.index = _to_index(self.suit, self.label) - 1

    def __repr__(self) -> str:
        """For debugging"""
        return f"[{self.label.name}/{self.suit.name}]"

    def __str__(self) -> str:
        """For pretty print"""
        return f"[{str(self.label)} {str(self.suit)} ]"

    def is_face(self) -> bool:
        """Returns true if is a face card"""
        # Your implementation
        return self.label in [Label.KING, Label.QUEEN, Label.JACK]

    def is_ace(self) -> bool:
        """Returns true if is an Ace"""
        # Your implementation
        return self.label == Label.ACE

    def is_numeral(self) -> bool:
        """If numbered i.e. 'pip' card, 2-10"""
        # Your implementation
        return (not self.is_face()) and (not self.is_ace())
