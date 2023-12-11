
from card import Card
import random

class Deck:
    """
    represents deck of cards
    """
    def __init__(self, num_values=13, num_suits=4):
        self.num_cards = num_values * num_suits
        #keep a list of card objects
        self.cards = []
        #call make_cards to inciate each of the cards
        self.make_cards(num_values,num_suits)
        
    def make_cards(self, num_values,  num_suits):
        """
        creates instances of card and poplautes the list of cards in the deck
        """
        for value in range(1, num_values+1):
            for suit in range (1, num_suits+1):
                card = Card(suit,value)
                self.cards.append(card)
        
    def draw(self):
        """
        first make sure that we have cards in the deck
        returns next card in deck
        """
        if not self.cards:
            return None
        #pick the first card
        card = self.cards.pop(0)
        #back on end of list
        self.cards.append(card)
        
        return card
    
    def shuffle(self):
        """
        shuffle cards
        """
        for i in range(0, self.num_cards):
            #swap postion of 2 cards
            r = random.randint(0, self.num_cards-1)
            self.cards[r], self.cards[i] =  self.cards[i], self.cards[r]

    #def deal_hand(self):

    
    #def take_turn(self):

        