from blackjack.card import Card, Label, Suit
from blackjack.hand import Hand


def test_hand_hit():
    """Test that hitting a hand adds expected cards"""
    c1 = Card(Suit.CLUBS, Label.EIGHT)
    c2 = Card(Suit.DIAMONDS, Label.TEN)
    c3 = Card(Suit.SPADES, Label.ACE)
    h = Hand.make_dealt(c1, c2)
    h.deal(c3)
    assert h.cards == [c1, c2, c3]


def test_hand_value():
    """Test that total = value for <= 21 and value = 0 for total > 21"""
    c1 = Card(Suit.CLUBS, Label.EIGHT)
    c2 = Card(Suit.DIAMONDS, Label.TEN)
    c3 = Card(Suit.HEARTS, Label.THREE)
    c4 = Card(Suit.SPADES, Label.FOUR)

    h1 = Hand.make_dealt(c1, c2)
    assert h1.value() == 18
    assert h1.total() == 18
    h1.deal(c3)
    assert h1.value() == 21
    assert h1.total() == 21
    h2 = Hand.make_dealt(c1, c2)
    h2.deal(c4)
    assert h2.value() == 0
    assert h2.total() == 22
