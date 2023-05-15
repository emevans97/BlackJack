from deck import Deck
from player import Player
from art import Art
import time

def play_again():
    game_finish = False
    while not game_finish:

        Art()
        deck = Deck()
        player1 = Player()
        computer = Player()

        print('Dealing cards...')
        time.sleep(3)

        computer.hand = [deck.get_card(), deck.get_card()]
        player1.hand = [deck.get_card(), deck.get_card()]

        print(f"Your hand is:")
        player1.print_hand()

        computer_score = computer.get_score()
        player1_score = player1.get_score()

        print(f"Your score is {player1_score}")

        wanna_twist = True
        while wanna_twist:
            choice = input("\nDo you want to stick or twist?\n")
            if choice.lower() == "twist":
                print('Dealing card...')
                time.sleep(1)
                player1.hand.append(deck.twist())
                player1.print_hand()
                time.sleep(1)

                if player1.get_score() > 21:
                    wanna_twist = False
            else:
                wanna_twist = False

        player1_score = player1.get_score()
        print(player1_score)

        if player1_score > 21:
            print("Ooops you're bust, game over")
            game_finish = True
        elif computer_score > player1_score:
            print(f"Computers score is {computer_score}")
            print(f"Your score is {player1_score}")
            print("You lose")
        elif computer_score < player1_score:
            print(f"Computers score is {computer_score}")
            print(f"Your score is {player1_score}")
            print("You win")
        else:
            print(f"You both scored {player1_score}")
            print("It's a draw")

        game_finish = True
    time.sleep(3)
    if input("\nDo you want to play again? Type y/n: ").lower() == 'y':
        play_again()
    else:
        print("Goodbye")

play_again()
