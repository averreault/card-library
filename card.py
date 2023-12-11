
VALID_SUITS ={1:"\u2663", 2:"\u2666", 3:"\u2665", 4:"\u2660"}
FACE_CARDS = {1:"Ace", 11:"Jack", 12:"Queen", 13:"King"}
class Card:
    
    def __init__(self, suit, value):
        """
        defines each indivdual card
        """
        self.suit = suit
        self.value = value
        
    def __str__(self):
        card =str(self.value)
        #check if this is a face card
        if self.value in FACE_CARDS:
            card = FACE_CARDS[self.value]
            
        #add suit
        card += " " + VALID_SUITS[self.suit]
        
        return card
    
    def __eq__(self, other_card):
        """
        check if you card is equal to the others
        """
        
        return self.value == other_card.value
    

    def __gt__(self, other_card):
        """
        check if your card is greater than the others
        """
        
        return self.value > other_card.value
    
    
    
 