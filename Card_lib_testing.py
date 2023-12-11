import unittest
from card import Card
from deck import Deck
from player import Player

VALID_SUITS = {1: "\u2663", 2: "\u2666", 3: "\u2665", 4: "\u2660"}
FACE_CARDS = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        #makes sure class can creaete a card properly
        card = Card(1, 5)
        self.assertEqual(card.suit, 1)
        self.assertEqual(card.value, 5)

    def test_str_representation(self):
        #checks to see if face card a properly represented
        card1 = Card(2, 1)
        card2 = Card(3, 11)
        card3 = Card(4, 13)
        
        self.assertEqual(str(card1), "Ace \u2666")
        self.assertEqual(str(card2), "Jack \u2665")
        self.assertEqual(str(card3), "King \u2660")
    
    def test_card_comparison(self):
        #test the values of card created and make sure card creations are consitant
        card1 = Card(1, 10)
        card2 = Card(2, 8)
        card3 = Card(1, 10)

        self.assertTrue(card1 > card2)
        self.assertFalse(card2 > card3)
        self.assertFalse(card1 > card3)
        

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_creation(self):
        # check that a standard deck has 52 cards
        self.assertEqual(len(self.deck.cards), 52) 

    def test_shuffle_deck(self):
        #check that card actually shuffle
        initial_cards = self.deck.cards.copy()
        self.deck.shuffle()
        shuffled_cards = self.deck.cards
        self.assertNotEqual(initial_cards, shuffled_cards) 

    def test_draw_from_empty_deck(self):
        #checks that drawing from an empy deck returns None
        empty_deck = Deck(num_values=0, num_suits=0)
        card = empty_deck.draw()
        self.assertIsNone(card)  


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Alice")
        self.player2 = Player("Bob", is_computer=True)

    def test_player_creation(self):
        #check to make sure name and whether or not player is a computer is properly adressed
        self.assertEqual(self.player1.name, "Alice") 
        self.assertEqual(self.player2.name, "Bob")  
        self.assertFalse(self.player1.robot)  
        self.assertTrue(self.player2.robot)  

    def test_points_initialization(self):
        #check that players start with 0 points
        self.assertEqual(self.player1.points, 0)  
        self.assertEqual(self.player2.points, 0)  

    def test_hand_initialization(self):
        # ensure each player starts with an empty list for a hand
        self.assertEqual(len(self.player1.hand), 0)  
        self.assertEqual(len(self.player2.hand), 0) 

    def test_str_representation(self):
        #make sure players are properly displayed
        self.assertEqual(str(self.player1), "Alice")  
        self.assertEqual(str(self.player2), "Bob") 

if __name__ == '__main__':
    unittest.main()