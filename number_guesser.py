import random


difficulty = input(
    "Select your difficulty: \n1. Easy (1-10) \n2. Medium (1-50)\n3. Hard (1-100)\n")

if difficulty == 1 or 'easy':
    random_number = random.randint(1, 10)
elif difficulty == 2 or 'medium':
    random_number = random.randint(1, 50)
elif difficulty == 3 or "hard":
    random_number = random.randint(1, 100)
else:
    print("Error: Wrong difficulty selection input")
    exit()


print("Start guessing 1-10")

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
