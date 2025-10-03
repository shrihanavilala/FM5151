from blackjack.dealer import Dealer, DealerView
from blackjack.gambler import Gambler
from blackjack.game import Result, play_round
from blackjack.hand import Hand
from blackjack.strategy import BettingStrategy, PlayingStrategy

import traceback
_BOLD_CYAN = "\033[1m\033[96m"
_END = "\033[0m"


def get_input_str(prompt: str, lower_case: bool = True) -> str:
    """Simple wrapper to get input, stripping whitespace"""
    result = input(f"{prompt}\n> ").strip()
    if lower_case:
        result = result.lower()
    return result


def print_title(msg: str) -> None:
    frame = "-" * len(msg)
    print(f"{_BOLD_CYAN}{frame}{_END}")
    print(f"{_BOLD_CYAN}{msg}{_END}")
    print(f"{_BOLD_CYAN}{frame}{_END}")


def print_header(msg: str) -> None:
    print(f"{_BOLD_CYAN}{msg}{_END}")


def print_msg(msg: str) -> None:
    print(msg)


def print_result(
    round_num: int, result: Result, gambler: Gambler, dealer: Dealer
) -> None:
    print_msg(
        f"""
    Round {round_num} Result: ({result})
        Gambler hand: {gambler.hand} ({gambler.hand.total()} -> {gambler.hand.value()})
        Dealer hand: {dealer.hand} ({dealer.hand.total()} -> {dealer.hand.value()})
        Cash after bet: {gambler.cash}
    """.strip()
    )


class InputBettingStrategy(BettingStrategy):
    """A betting strategy that takes input from the console"""

    def __call__(self, current_cash: int) -> int:
        print_header("Decide bet")
        while True:
            result = get_input_str(f"How much to bet? (cash={current_cash})?")
            if result.isdigit():
                return int(result)
            else:
                print_msg(f"'{result}' needs to be an integer, please try again!")


class InputPlayingStrategy(PlayingStrategy):
    """A playing strategy that takes input from the console"""

    def __call__(self, hand: Hand, dealer: DealerView) -> None:
        print_header("Play hand")
        print_msg(f"The dealer face up card is: {dealer.up_card()}")
        while hand.total() < 21:
            print_msg(f"Current hand: {hand} (value={hand.value()})")
            result = get_input_str("What would you like to do? (hit/stay)")
            if result == "hit":
                dealer.hit(hand)
            elif result == "stay":
                break
            else:
                print_msg("I don't understand :(, please enter 'hit' or 'stay'")


def main():
    print_title("Blackjack")
    print_msg("Welcome to Blackjack!")
    print_msg("You can exit this game at any time by hitting Ctrl+C")
    try:
        amount = None
        while amount is None:
            result = input("How many chips would you like to buy?\n> ")
            if result.isdigit():
                amount = int(result)
            else:
                print_msg(f"{result} is invalid (integer amount is required)")

        dealer = Dealer()
        gambler = Gambler(InputBettingStrategy(), InputPlayingStrategy(), amount)

        print_msg("Okay then! Let's get started")
        i = 1
        while gambler.cash > 0:
            try:
                print_title(f"Round {i}")
                result = play_round(gambler, dealer)
                print_header("Round is complete")
                print_result(i, result, gambler, dealer)
                i += 1
            except Exception as ex:
                traceback.print_exc()
                print_header(f"Error! {ex}")
                print("Let's try again")
        print_title("Game over 😥")
    except KeyboardInterrupt:
        print_msg("\nI see you've had enough... see you later 🙂")


if __name__ == "__main__":
    main()
