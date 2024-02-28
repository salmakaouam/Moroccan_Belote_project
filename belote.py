import random

class Card:
    suits = ['khal', 'copas', 'chbada', 'dhab']

    def __init__(self, value):
        self.value = value
        self.suit = random.choice(Card.suits)

    def __str__(self):
        return f"{self.value} of {self.suit}"

class BeloteGame:
    def __init__(self):
        self.table_card = None

    def determine_trump_suit(self):
        self.trump_suit = random.choice(Card.suits)

    def display_hand(self):
        print("Your hand:")
        for card in self.hand:
            print(card)

    def bidding(self):
        print("Bidding starts.")
        if not self.table_card:
            self.table_card = Card(random.choice([4, 5, 6, 7, 10, 11, 12]))
            print(f"Card on the table: {self.table_card}")
        self.hand = [Card(value) for value in random.sample([4, 5, 6, 7, 10, 11, 12], 5)]
        self.display_hand()
        choice = input("Your turn to bid. Pass or Take? ").lower()
        if choice == "take":
            print(f"You have taken {self.table_card.suit} as the trump suit.")
            # Add the card from the table to the hand
            self.hand.append(self.table_card)
            # Add 2 new cards to the hand
            self.hand.extend([Card(value) for value in random.sample([4, 5, 6, 7, 10, 11, 12], 2)])
            print("Remaining cards are dealt.")
            return "take"
        else:
            print("You passed.")
            if random.choice([True, False]):
                print("Computer passed.")
                if input("Do you want to bid again? (yes/no)").lower() == "yes":
                    return self.bidding()
            else:
                print("Computer takes the bid.")
                # Add 3 new cards to the hand
                self.hand.extend([Card(value) for value in random.sample([4, 5, 6, 7, 10, 11, 12], 3)])
                print("Remaining cards are dealt.")
                return "take"
        return choice

    def play_game(self):
        self.determine_trump_suit()
        if self.bidding() == "take":
            print("Game continues...")
            self.play_tricks()
        else:
            print("The game is over.")

    def play_tricks(self):
        print("Playing tricks starts.")
        # Logic for playing tricks

if __name__ == "__main__":
    belote_game = BeloteGame()
    belote_game.play_game()

