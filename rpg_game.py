#VERY ROUGH BETA, IDEA ONLY, DON'T KNOW IF I WILL EVER UPDATE THIS




import random
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#-------------------------------------------------------
opponent_list = {
    "Zombie": {
        "Health": 25,
        "XP": 10,
    },
    "Goblin": {
        "Health": 15,
        "XP": 8,
    }
}

inventory_items = {
    "wooden sword": {
        "Attack": random.randint(3, 11)
    },

    "wooden spear": {
        "Attack": random.randint(5, 8)
    }
}

# -------------------PVP--------------------------


def random_opponent():
    return random.choice(list(opponent_list.keys()))


def attack(opponent_name, opponent):
    player_attack = inventory_items["wooden sword"]["Attack"]

    opponent["Health"] -= player_attack

    print(

        f"You attacked the {opponent_name} and dealt {player_attack} damage!")
    if opponent["Health"] > 0:
        print(f"{opponent_name}'s remaining health: {opponent['Health']}")
    else:
        clear()
        print(f"You defeated the {opponent_name}!")
        print(f"You gained {opponent['XP']} XP!")
        return True
    return False


def combat_mechanic():
    opponent_name = random_opponent()
    opponent_template = opponent_list[opponent_name]
    opponent = opponent_template.copy()

    clear()
    print(f"A {opponent_name} appeared!")
    time.sleep(0.7)

    while opponent["Health"] > 0:
        print("\nMake your choice: \n1. Attack \n2. Defend\n3. Flee")

        choice = input("Enter your choice: ")

        if choice == "1":  # Attack
            if attack(opponent_name, opponent):  # If the opponent is defeated
                break
        elif choice == "2":  # Defend
            print("You chose to defend!")
            time.sleep(1)
        elif choice == "3":  # Flee
            print("You fled the battle!")
            break
        else:  # Invalid input
            print("Invalid choice. Try again.")
            time.sleep(1)

# ^-------------------PVP--------------------------^


def inventory():
    print("Inventory:")
    for item, stats in inventory_items.items():
        print(f"- {item.title()}: {stats}")


# Main menu
while True:
    clear()
    print("Type a command: \n- 'inventory'\n- 'sim'\n- 'exit'")
    command = input("> ").lower()

    if command == "inventory":
        clear()
        inventory()
        input("\nPress Enter to return...")
    elif command == "sim":
        clear()
        combat_mechanic()
        input("\nPress Enter to return to main menu...")
    elif command == "exit":
        break
    else:
        print("Unknown command.")
        time.sleep(1)
