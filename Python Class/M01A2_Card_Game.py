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
    values = ("15","1","2","3","4","5","6","7","8","9","10","10","10","10","15")

    def __init__(self, suits, ids, values):
        self.suit = suits
        self.value = values
        self.ident = ids

    def __repr__(self):                                        #__repr__ is a defined method
        aCard = self.ids[self.ident] + " of " + self.suits[self.suit] + " worth " + self.values[self.value]
        return aCard

class Deck:
    def __init__(self):
        self.deck = []                                         # Creates empty deck (was self.cards)
        for s in range(0,6):                                    # Begin deck population
            for id in range(0,15):
                v = Card.values[id]                             # typeError incorrect way to index?
                print(id,v)
                self.deck.append(Card(s,id,v))                 # End deck population w/the face number, suite & value
                print(self.deck)
        shuffle(self.deck)                                     # Shuffles deck

    def deal_card(self):
        if len(self.deck) == 0:                                # Checks to see if deck is empty
            print("Deck empty")
            return
        else:
            return self.deck.pop()                             # picks a card and removes it from the deck

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.handValue = 0

class Deal:
    def __init__(self):
        name1 = input("Player Name:")
        self.deck = Deck()                                    # Calls the Deck object
        self.player = Player(name1)                           # Idetifies the name to the player

    def draw(self, p1n, p1c):
        d = "{} drew {}"
        d = d.format(p1n, p1c)
        print(d)

    def dealHand (self):
        #cards = self.deck.deck            #usure why this is here, the final "deck" used to be "cards" Deck().deck was
                                           #      called "cards", but "deck" is clearer
        cardsToDeal = 7                                      # Dictates how many cards a player will get in the hand
        hand = []                                            # Creates empty hand for the player
        while len(hand) < cardsToDeal:                       # Adds the defined number of cards to the hand
            p1c = self.deck.deal_card()                      # gets card from deck
            p1n = self.player.name
            self.draw(p1n,p1c)                               # notifies what card was delt/drawn w/draw method
            hand.append(p1c)                                 # adds card to hand
            print("Current Hand",hand)                       # printing hand, shows mem location for each card

deal = Deal()
deal.dealHand()


