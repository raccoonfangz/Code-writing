import random
import os
import time

COIN_BALANCE = 0


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_winning_numbers():
    return random.sample(range(1, 9), 3)  # 3 winning numbers from 1 to 9


def generate_scratch_numbers():
    return random.sample(range(1, 9), 6)  # 6 numbers on the scratch card


def display_card(scratched, revealed):
    for i in range(6):
        if scratched[i]:
            print(f"[{revealed[i]:2}]", end=' ')
        else:
            print("[  ]", end=' ')
    print()


def scratcher():
    global COIN_BALANCE
    winning = generate_winning_numbers()
    scratch_numbers = generate_scratch_numbers()
    scratched = [False] * 6
    revealed = [None] * 6
    print(f"Winning Numbers: {sorted(winning)}\n")

    total_scratched = 0

    while total_scratched < 6:
        clear()
        print("=== SCRATCHER MINI-GAME ===")
        print(f"Winning Numbers: {sorted(winning)}\n")
        print("Your Card:")
        display_card(scratched, revealed)
        try:
            choice = int(input("\nScratch a slot (1-6): "))
            if 1 <= choice <= 6:
                idx = choice - 1
                if scratched[idx]:
                    print("\nThat slot is already scratched.")
                    time.sleep(1)
                else:
                    scratched[idx] = True
                    revealed[idx] = scratch_numbers[idx]
                    total_scratched += 1
            else:
                print("\nChoose a number between 1 and 6.")
                time.sleep(1)
        except ValueError:
            clear()
            print("Invalid input. Use digits 1–6 only.")
            time.sleep(1)

        print()
    clear()
    print("All numbers scratched!")
    print("\nYour Numbers:", revealed)
    matches = [n for n in revealed if n in winning]
    print("Matching Numbers:", matches)
    payout = 10 * len(matches)
    COIN_BALANCE += payout
    print(f"Total Matches: {len(matches)}",
          f"\n\n- YOU WIN {payout}c! (10c per match)" if len(matches) > 0 else "- No luck this time.")

    print(f"\nYour current coin balance: {COIN_BALANCE}c")
    input("\n\nPress enter to continue")


while True:
    scratcher()
