from blackjack.dealer import DealerView
from blackjack.hand import Hand
from blackjack.strategy import BettingStrategy, PlayingStrategy


class Gambler:
    def __init__(
        self,
        bet_strategy: BettingStrategy,
        play_strategy: PlayingStrategy,
        initial_cash=1000,
    ) -> None:
        """Initialize a gambler with specified amount of cash"""
        self.hand = Hand.make_empty()
        self.bet_strategy = bet_strategy
        self.play_strategy = play_strategy
        self.cash = int(initial_cash)

    def bet(self) -> int:
        """Gambler bets according to strategy. Decrements the cash amount for
        the amount of the bet and returns the decided bet amount."""
        # Your implementation
        bet_amount = self.bet_strategy(self.cash)
        if(self.cash < bet_amount or bet_amount==0):
            raise ValueError("Bet Amount Too High or Low!")
        self.cash -= bet_amount
        return bet_amount

    def collect(self, amount: int) -> None:
        """Collect a bet adding it to the cash level"""
        self.cash += amount

    def play(self, dealer: DealerView) -> None:
        """Gambler plays current hand according to strategy"""
        # Your implementation
        return self.play_strategy(self.hand, dealer)
