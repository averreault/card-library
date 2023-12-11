
class Player:
    """
    Represents a card game player.
    """   
    def __init__(self, name, is_computer=False):
       
        self.name = name
        self.robot = is_computer

        # Also initialize points and an empty hand
        self.points = 0
        self.hand = []
        
    def __str__(self):
        
        name_str = self.name
    
        return name_str

    def print_points(self):
        """
        Helper to print out the points this player has. 
        """
        print("{} has {} points.".format(self, self.points))