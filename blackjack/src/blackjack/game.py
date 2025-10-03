from enum import IntEnum

from blackjack.dealer import Dealer
from blackjack.gambler import Gambler


class Result(IntEnum):
    """Possible results for a round of Blackjack"""

    NATURAL_CASE_BOTH_BLACKJACK = 1
    NATURAL_CASE_GAMBLER_BLACKJACK = 2
    NATURAL_CASE_DEALER_BLACKJACK = 3
    GAMBLER_PLAY_BUST = 4
    DEALER_PLAY_BUST = 5
    SETTLEMENT_GAMBLER_WIN = 6
    SETTLEMENT_DEALER_WIN = 7
    SETTLEMENT_TIE = 8

    def __str__(self) -> str:
        match self.value:
            case self.NATURAL_CASE_BOTH_BLACKJACK:
                return "Gambler and dealer had blackjack on the deal, it's a wash 🧼🛁"
            case self.NATURAL_CASE_GAMBLER_BLACKJACK:
                return "Gambler had blackjack on the deal, woo! 🥳"
            case self.NATURAL_CASE_DEALER_BLACKJACK:
                return "Dealer had blackjack on the deal... 🤨"
            case self.GAMBLER_PLAY_BUST:
                return "Gambler went bust 😥"
            case self.DEALER_PLAY_BUST:
                return "Dealer went bust 😮‍💨"
            case self.SETTLEMENT_GAMBLER_WIN:
                return "Gambler has the better hand! 😊"
            case self.SETTLEMENT_DEALER_WIN:
                return "Dealer has the better hand... 🫠"
            case self.SETTLEMENT_TIE:
                return "Gambler and dealer have same hand, it's a wash 🧼🛁"
            case _:
                raise ValueError(f"Unhandled value {self.value}:{self.name}")



def play_round(gambler: Gambler, dealer: Dealer) -> Result:
    """Play a round of Blackjack"""
    # Your implementation
    
    # --- Possible sketch below ---

    # Natural cases

    # Check if round is handled by a natural case and we can be done

    # Gambler and dealer play
    dealer._deck.reset()
    dealer.hand.clear()
    gambler.hand.clear()
    dealer.deal_hands(gambler.hand)
    bet_amount = gambler.bet()
    
    if (dealer.hand.total() == 21 and gambler.hand.total() == 21):
        gambler.collect(bet_amount)
        return Result.NATURAL_CASE_BOTH_BLACKJACK
    elif (dealer.hand.total() == 21):
        return Result.NATURAL_CASE_DEALER_BLACKJACK
    elif (gambler.hand.total() == 21):
        gambler.collect(bet_amount*2)
        return Result.NATURAL_CASE_GAMBLER_BLACKJACK

    
    
    gambler.play(dealer)
    if(gambler.hand.total() > 21):
        return Result.GAMBLER_PLAY_BUST
    
    dealer.play()
    if(dealer.hand.total() > 21):
        gambler.collect(bet_amount*2)
        return Result.DEALER_PLAY_BUST
        
    
    if(gambler.hand.total() > dealer.hand.total()):
        gambler.collect(bet_amount*2)
        return Result.SETTLEMENT_GAMBLER_WIN
    if(gambler.hand.total() < dealer.hand.total()):
        return Result.SETTLEMENT_DEALER_WIN
    if(gambler.hand.total() == dealer.hand.total()):
        gambler.collect(bet_amount)
        return Result.SETTLEMENT_TIE
    
    
    