import random
import sys
import os
import time

guess_count = 0
guess_limit = 0
bottom_limit = 1

difficulty = input(
    "Select your difficulty: \n1. Easy (1-10) - 3 guesses \n2. Medium (1-50) - 6 guesses \n3. Hard (1-100) - 7 guesses\n")

time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

if difficulty == '1' or difficulty.lower() == 'easy':
    random_number = random.randint(1, 10)
    guess_limit = 3
    upper_limit = 10
    print("Selected mode: Easy \n")
elif difficulty == '2' or difficulty.lower() == 'medium':
    random_number = random.randint(1, 50)
    guess_limit = 6
    upper_limit = 50
    print("Selected mode: Medium \n")
elif difficulty == '3' or difficulty.lower() == "hard":
    random_number = random.randint(1, 100)
    guess_limit = 7
    upper_limit = 100
    print("Selected mode: Hard \n")
else:
    print("Error: Wrong difficulty selection input")
    sys.exit()

print("Start guessing!")

while True and guess_count < guess_limit:
    try:
        guess = float(input("Enter your guess: "))
        guess_count += 1

        if guess > random_number and guess <= upper_limit and guess >= bottom_limit:
            print("Lower⬇︎")
        elif guess < random_number and guess <= upper_limit and guess >= bottom_limit:
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
        if guess > upper_limit:
            print(
                f"Error: Guess was above the limit of {bottom_limit}-{upper_limit}")
            guess_count -= 1
        if guess < bottom_limit:
            print(
                f"Error: Guess was under the limit of {bottom_limit}-{upper_limit}")

    except ValueError:
        print("Error: Please enter a valid number.")
