import random
import sys


difficulty = input(
    "Select your difficulty: \n1. Easy (1-10) \n2. Medium (1-50)\n3. Hard (1-100)\n")

if difficulty == '1' or difficulty.lower() == 'easy':
    random_number = random.randint(1, 10)
    print("Selected mode: Easy \n")
elif difficulty == '2' or difficulty.lower() == 'medium':
    random_number = random.randint(1, 50)
    print("Selected mode: Medium \n")
elif difficulty == '3' or difficulty.lower() == "hard":
    random_number = random.randint(1, 100)
    print("Selected mode: Hard \n")
else:
    print("Error: Wrong difficulty selection input")
    sys.exit()


print("Start guessing!")

guess_count = 0

while True:
    try:
        guess = float(input("Enter your guess: "))
        guess_count += 1

        if guess > random_number:
            print("Lower")
        elif guess < random_number:
            print("Higher")
        else:
            print("You won :3")
            break
    except ValueError:
        print("Error: Please enter a valid number.")

print("Guess attempts:", guess_count)
