import random

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return " of ".join((self.suit, self.value))


class Deck():
    def __init__(self):
        self.cards = [Card(s, v) for s in ("shapde", "heart", "club", "diamond")
                                for v in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K")]

    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards)>1:
            return self.cards.pop(0)

class Hands():
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = False
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.dealer:
            print("This is hidden: ", self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())

class Game():
    def __init__(self):
        playing = True
        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hands()
            self.dealer_hand = Hands(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
            
            print("Your Hand is:")
            self.player_hand.display()
            print("Dealer Hand is:")
            self.dealer_hand.display()

            game_over = False
            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue
                choice = input("Please choose [hit/stick] ").lower()
                while choice not in ["h", "s", "hit", "stick"]:
                    choice = input("Please choose [h] for (hit) and [s] for (stick) ").lower()
                if choice in ["h", "hit"]:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if self.player_is_over():
                        print("Player is lost")
                        has_won = True
                else:
                    print("Final Results")
                    print("Your hand:", self.player_hand.get_value())
                    print("Dealer's hand:", self.dealer_hand.get_value())
                    if self.player_hand.get_value() > self.dealer_hand.get_value():
                        print("You Win!")
                    else:
                        print("Dealer Wins!")
                        has_won = True
            
            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                again = input("Please enter Y or N ")
                if again.lower() == "n":
                    print("Thanks for playing!")
                    playing = False
                else:
                    has_won = False


    def check_for_blackjack(self):
        Player = False
        Dealer = False
        if self.player_hand.get_value() == 21:
            Player = True
        if self.dealer_hand.get_value() == 21:
            Dealer = True
        return Player, Dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both player are won, game going to Draw")
        elif player_has_blackjack:
            print("Player has won the game.")
        else:
            print("Dealer won the game.")

    def player_is_over(self):
        return self.player_hand.get_value() > 21


if __name__ == "__main__":
    game = Game()