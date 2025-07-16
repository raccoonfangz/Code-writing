import random
import time
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def dice_game():
    clear()
    input("Press enter to roll your dice.")
    clear()
    for _ in range(1):
        time.sleep(1)
        player_roll = random.randint(1, 6)
        print(f"You rolled: {player_roll}")
        print("\nNow it's opponent's turn")

    for _ in range(1):
        time.sleep(2)
        opponent_roll = random.randint(1, 6)
        print(f"\nOpponent rolled: {opponent_roll}")
        time.sleep(2)
        if player_roll > opponent_roll:
            print("\nYou've won!")
            time.sleep(2)
        elif player_roll < opponent_roll:
            print(
                "\nYou've lost!")
            time.sleep(2)
        else:
            print("\nIt's a tie! Try again")
            time.sleep(2)
            dice_game()


while True:
    dice_game()
