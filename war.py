

from deck import Deck
from player import Player

def war():
   
    # Initialize and shuffle the deck
    d = Deck()
    d.shuffle()
    
    player_name = input("What is your name? \n")
    player_1 = Player(player_name, is_computer=False)
    player_2 = Player("Computer", is_computer=True)
    
    while player_1.points < 10 and player_2.points < 10:
        prompt_str = "Your turn {}. Press d to draw. \n".format(player_1)
        key = input(prompt_str)
        if key == "d":
            player_1.hand.append(d.draw())
            player_2.hand.append(d.draw())
        
            print(player_1, "has", player_1.hand[0], "vs.", 
                  player_2, "has", player_2.hand[0])
            
            winner = None 
            if player_1.hand[0] > player_2.hand[0]:
                winner = player_1
            elif player_1.hand[0] < player_2.hand[0]:
                winner = player_2
                
            if winner is not None:
                winner.points += 1
                print("Player", winner, "wins this round!")
            else:
                print("A draw!")
                
            print("\n--points--\n")
            player_1.print_points()
            player_2.print_points()
            print()

            # Clear the hands
            player_1.hand = []
            player_2.hand = []
        else:

            print("Game Terminated")
            break
    
    print("Game over. {} had {} points; Player {} had {}."
          .format(player_1, player_1.points, player_2, player_2.points))
    
        
if __name__ == "__main__":
    war()