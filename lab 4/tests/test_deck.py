from blackjack.card import Card, Label, Suit
from blackjack.deck import Deck


def test_deck_init_default():
    """Default card initialization"""
    d = Deck()
    assert d.count() == 52


def test_deck_init_cards():
    """Initialize deck with cards"""
    cards = (
        Card(Suit.CLUBS, Label.FIVE),
        Card(Suit.DIAMONDS, Label.ACE),
        Card(Suit.SPADES, Label.QUEEN),
    )
    d = Deck(cards)
    assert d.count() == 3


def test_deck_deals_card():
    """Test cards deal and reset"""
    d = Deck()
    c1 = d.deal()
    c2 = d.deal()
    assert isinstance(c1, Card)
    assert isinstance(c2, Card)
    assert d.count() == 50
    d.reset()
    assert d.count() == 52


def test_deck_shuffle():
    """Test deck shuffle produces different indices"""
    d = Deck()
    idx1 = d.indexes.copy()
    d.shuffle()
    idx2 = d.indexes.copy()
    # Performs element wise compare and returns True / False
    assert list(idx1) != list(idx2)
