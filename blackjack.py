
from deck import Deck
from player import Player

VALID_SUITS ={1:"\u2663", 2:"\u2666", 3:"\u2665", 4:"\u2660"}
FACE_CARDS = {1:"Ace", 11:"Jack", 12:"Queen", 13:"King"}

def points(hand):
    points = 0
    num_aces = 0

    for card in hand:
        if card.value in [11, 12,13]:
            points += 10
        elif card.value in [1]:  # Ace
            points += 11
            num_aces += 1
        else:
            points += card.value

    # Adjust points if there are aces and total points exceed 21
    while num_aces > 0 and points > 21:
        points -= 10
        num_aces -= 1

    return points

def show_some(player, dealer):
    """
    Show some cards, hiding the first card of the dealer.
    """
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.hand[1])

    print("\nPlayer's Hand:")
    for card in player.hand:
        print('', card)

def show_all(player, dealer):
    """
    Show all cards of both player and dealer.
    """
    print("\nDealer's Hand:")
    for card in dealer.hand:
        print('', card)
    print("Dealer's Hand =", points(dealer.hand))

    print("\nPlayer's Hand:")
    for card in player.hand:
        print('', card)
    print("Player's Hand =", points(player.hand))

def player_busts(player, dealer):
    p_bust = "{} busts!".format(player)
    print(p_bust)

def player_wins(player, dealer):
    p_wins = "{} wins!".format(player)
    print(p_wins)
  
def dealer_busts(player, dealer):
    d_bust = "Dealer busts! {} wins!".format(player)
    print(d_bust)
    
def dealer_wins(player, dealer):
    print("Dealer wins!")
    
def push(player, dealer):
    print("It's a tie! Push.")

def blackjack():
    player_wins_count = 0
    dealer_wins_count = 0
    playing = True

    player_name = input("What is your name? \n")
    player = Player(player_name, is_computer=False)
    dealer = Player("Dealer", is_computer=True)
    
    while True:

        d = Deck()
        d.shuffle()

        for _ in range(2):
            player.hand.append(d.draw())
            dealer.hand.append(d.draw())

        show_some(player, dealer)

        while playing:
            choice = input("Do you want to (h)it or (s)tand?\n")

            if choice[0].lower() == 'h':
                player.hand.append(d.draw())
                show_some(player, dealer)
                
            elif choice[0].lower() == 's':
                print("Player stands. Dealer's turn.")
                playing = False
            else:
                print("Please enter 'h' or 's' only.")
                continue

            if points(player.hand) > 21:
                player_busts(player, dealer)
                dealer_wins_count += 1
                break

        if points(player.hand) <= 21:
            while points(dealer.hand) < 17:
                dealer.hand.append(d.draw())

            show_all(player, dealer)

            if points(dealer.hand) > 21:
                dealer_busts(player, dealer)
                player_wins_count += 1
            elif points(dealer.hand) > points(player.hand):
                dealer_wins(player, dealer)
                dealer_wins_count += 1
            elif points(dealer.hand) < points(player.hand):
                player_wins(player, dealer)
                player_wins_count += 1
            else:
                push(player, dealer)

        print("\n--Win Count--\n")
        print("{} Wins: {}".format(player, player_wins_count))
        print("{} Wins: {}".format(dealer, dealer_wins_count))

        if player_wins_count >= 10 or dealer_wins_count >= 10:
            print("Game over - Win count limit reached.")
            break

        new_game = input("Do you want to play another hand? (y/n): ")

        if new_game[0].lower() == 'y':
            player.hand = []
            dealer.hand = []
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break