import random
import sys
import os
import time

guess_count = 0
guess_limit = 0

difficulty = input(
    "Select your difficulty: \n1. Easy (1-10) - 3 guesses \n2. Medium (1-50) - 6 guesses \n3. Hard (1-100) - 7 guesses\n")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

if difficulty == '1' or difficulty.lower() == 'easy':
    random_number = random.randint(1, 10)
    guess_limit = 3
    print("Selected mode: Easy \n")
elif difficulty == '2' or difficulty.lower() == 'medium':
    random_number = random.randint(1, 50)
    guess_limit = 6
    print("Selected mode: Medium \n")
elif difficulty == '3' or difficulty.lower() == "hard":
    random_number = random.randint(1, 100)
    guess_limit = 7
    print("Selected mode: Hard \n")
else:
    print("Error: Wrong difficulty selection input")
    sys.exit()

print("Start guessing!")

while True and guess_count < guess_limit:
    try:
        guess = float(input("Enter your guess: "))
        guess_count += 1

        if guess > random_number:
            print("Lower⬇︎")
        elif guess < random_number:
            print("Higher⬆︎")
        elif guess == random_number:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You won :3")
            print("Guess attempts:", guess_count)
            break
        if guess_count == guess_limit:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Game over! Guess amount reached",
                  f"\nNumber was: {random_number}")
            sys.exit()
    except ValueError:
        print("Error: Please enter a valid number.")
