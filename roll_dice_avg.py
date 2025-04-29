import random

results = []

times = input("How many times would you like to roll the dice?")


if times.isdigit() and int(times) >= 1:
    times = int(times)  # Convert input to an integer
    for _ in range(times):
        roll = random.randint(1, 6)  # Generate a random dice roll
        print(f"You rolled: {roll}")
        results.append(roll)  # Append the roll to the results list
else:
    print("Wrong input. Enter a valid number.")

# Print all rolls
print("All rolls:", results)

# Calculate and print the average if there are results
if results:
    average = sum(results) / len(results)  # Calculate the average
    print("Average:", round(average, 2))  # Round to 2 decimal places
else:
    print("No rolls to calculate avg.")
