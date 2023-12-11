
from blackjack import blackjack
from war import war


if __name__ == '__main__':

    chose_game = input ("select # game from library: \n(1)War\n(2)Blackjack\n")

    if chose_game == '1':
        war()
    elif chose_game == '2':
        blackjack()


   