################################
# Program name:
#  Author: Tom Gill
#  Course: CWCT Python Essentials
#  Date: 9/9/2021
#  Assignment: MOD A
#  Purpose: This is the beginning of creating a more sophisticated card game. Create a module for a card game.
#
# The module should :
#
# 1. define an immutable collection (tuple) of card faces (ace, deuce ... king). Add three more faces of your own
# choosing (e.g. prince, knight, etc.).
#
# 2. define an immutable collection (tuple) of card suits (diamonds, hearts, spades, clubs). Add two more suits of your
# own choosing (e.g. moons, stars, etc.).
#
# 3. Create a collection (i.e. a deck of cards) consisting of one card of each face/suit. The cards should be immutable,
# but the deck should not (i.e. a list).
#
# 4. "Deal" a hand of seven cards to a player. The cards selected should be selected randomly for each hand and be
# removed from the deck as they are dealt.
#
# 5. Determine the value of each hand based on the accumulated value of the cards in the hand (number cards are worth
# their numeric value, face cards (jack, queen, king) are worth 10 (assign whatever value you want to the faces you
# created).

# When the game is finished, the cards should be returned to the deck and prompt the user if they wish to play again.

from random import shuffle
import sys

class Card:
    suits = ("Diamonds", "Hearts", "Spades", "Clubs", "Pentacles", "Crosses")
    values = ("Reaper", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Saviour")

    def __init__(self, suits, values):
        self.suit = suits
        self.value = values

    def __repr__(self):      #__repr__ is a defined method to change how the card is displayed when we call print on it
        return " of ".join((self.value, self.suit))        # This wont work on a tuple so we had to remake the deck
                                                           #    as seen below.

class Deck:
    def __init__(self):
        self.deck = [Card(s,v) for s in ["Diamonds", "Hearts", "Spades", "Clubs", "Pentacles",
                                         "Crosses"] for v in ["Reaper", "Ace", "2", "3", "4",
                                                              "5", "6", "7", "8", "9", "10", "Jack",
                                                              "Queen", "King", "Saviour"]]     # Creates deck

    def shuffle(self):
        if len(self.deck) > 1:
            shuffle(self.deck)                                 # Shuffles deck

    def deal(self):
        if len(self.deck) == 0:                                # Checks to see if deck is empty
            print("Deck empty")
            return
        else:
            return self.deck.pop(0)                             # picks a card and removes it from the deck

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):                                   # Adds card to hand
        self.cards.append(card)

    def calculate_value(self):                                  # Calculate value of the hand based on our "rules"
        self.value = 0
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "Saviour":
                    self.value += 15
                elif card.value == "Reaper":
                    self.value += 0
                else:
                    self.value += 10                            # King, Queen & Jack = 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        for card in self.cards:
            print(card)
        print("Value:", self.get_value())

class Game:
    def __init__(self):
        pass

    def play(self):
        playing = True
        while playing:
            self.deck = Deck()                                    # Creates the deck
            self.deck.shuffle()                                   # Shuffles the cards

            self.player_hand = Hand()                             # Deals the players hand of 7 cards
            for i in range (7):
                self.player_hand.add_card(self.deck.deal())

            print("Your hand is: ")
            self.player_hand.display()
            print("\nDo you want another hand?")
            again = input("Y\\N:")
            while True:
                if again == "Y":
                    self.play()
                elif again == "N":
                    sys.exit()
                else:
                    again =input("Please enter 'Y' or 'N', silly rabbit")


game = Game()
game.play()


