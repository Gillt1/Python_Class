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

class Card:
    suits = ("Diamonds", "Hearts", "Spades", "Clubs", "Pentacles", "Crosses")
    ids = ("Reaper", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Saviour")
    values = (0,1,2,3,4,5,6,7,8,9,10,10,10,10,15)

    def __init__(c, ids, suits, values):                      # learning to use self: c for this method = self
        c.suit = suits
        c.value = values
        c.ident = ids

    def cardName (c):
        aCard = c.ids[c.ident] + "of" + c.suits[c.suit] + "worth" + c.values[c.value]
        return aCard

class Deck:                                                   # learning to use self: d for this method = self
    def __init__(d):
        d.cards = []                                          # Creates empty deck
        for ids in range(15):                                 # Begin deck population
            for vals in range(15):
                for suit in range(6):
                    d.cards.append(Card(ids, vals, suit))     # End deck population with the face number, suite and value
        shuffle(d.cards)                                      # Shuffles deck

    def deal_card(d):
        if len(d.cards) == 0:                                 # Checks to see if deck is empty
            print("Deck empty")
            return
        else:
            return d.cards.pop()                              # picks a card and removes it from the deck

class Player:
    def __init__(self, name):
        self.name = name
        self.handValue = 0

class Deal:
    def __init__(self):
        name1 = input("Player Name:")
        self.deck = Deck()                                   # Calls the Deck object

    def dealHand (self):
        cardsToDeal = 7                                      # Dictates how many cards a player will get in the hand
        hand = []                                            # Creates empty hand for the player
        cards = self.deck.cards
        while len(cards) >= 7:
            for i in range (cardsToDeal):
                hand += self.deck.deal_card()
                print(hand)

deal = Deal()
deal.dealHand()


