import random
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def lockpicking_game():
    global game_state
    clear()
    code = [random.randint(1, 9) for _ in range(3)]
    hints = []
    squares = [1, 2]
    random.shuffle(squares)

    # hints
    for i in squares[:2]:
        if random.choice([True, False]):
            if code[i] % 2 == 0:
                hints.append(f"Digit {i+1} is even.")
            else:
                hints.append(f"Digit {i+1} is odd.")
        else:
            actual = code[i]
            if actual == 1:
                # Can't go lower
                upper = random.randint(2, 9)
                hints.append(f"Digit {i+1} is lower than {upper}.")
            elif actual == 9:
                # Can't go higher
                lower = random.randint(1, 8)
                hints.append(f"Digit {i+1} is higher than {lower}.")
            else:
                if random.choice([True, False]):
                    upper = random.randint(actual + 1, 9)
                    hints.append(f"Digit {i+1} is lower than {upper}.")
                else:
                    lower = random.randint(1, actual - 1)
                    hints.append(f"Digit {i+1} is higher than {lower}.")

    attempts = 5
    initial_attempts = attempts

    combination = [f"[{code[0]}]", "[*]", "[*]"]
    # ui
    while attempts > 0:
        clear()
        print(
            "Guess the combination! Each [*] has a hidden number between 1-9\n")

        # Show current known state on top
        print('Current attempt:', "".join(combination))

        print("\nHints:")
        for hint in hints:
            print("- " + hint)
        print(f"\nAttempts left: {attempts}")

        guess = input("\nEnter your guess (e.g. 123): ").strip()

        if len(guess) != 3 or not guess.isdigit():
            clear()
            print("Invalid format.")
            time.sleep(1)
            continue

        guess_digits = [int(e) for e in guess]

        for i in range(1, 3):
            if guess_digits[i] == code[i]:
                combination[i] = f"[{code[i]}]"
            else:
                combination[i] = "[*]"

        if guess_digits == code:
            if attempts == initial_attempts:
                clear()
                print(
                    "Unlocked! You picked the lock successfully on the first try!")
                time.sleep(2.5)
                return
            else:
                clear()
                print("Unlocked! You picked the lock successfully.")
                time.sleep(2.5)
                return
        else:
            attempts -= 1
            if attempts == 0:
                clear()
                print(
                    f"Failed! The correct code was {code[0]} {code[1]} {code[2]}")
                time.sleep(2)
                return
            else:
                time.sleep(1)


while True:
    lockpicking_game()
