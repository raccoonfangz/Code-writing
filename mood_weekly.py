print("Please type in your weekly mood score (1-10)")


def get_mood_input(day):
    try:
        value = float(input(f"{day}: "))
        if value < 1 or value > 10:  # Ensure the value is between 1 and 10
            print("Error: Mood score must be between 1 and 10.")
            exit()
        return value
    except ValueError:
        print("Error: Given value is not a number.")
        exit()


# Get mood scores for each day
Monday = get_mood_input("Monday")
Tuesday = get_mood_input("Tuesday")
Wednesday = get_mood_input("Wednesday")
Thursday = get_mood_input("Thursday")
Friday = get_mood_input("Friday")
Saturday = get_mood_input("Saturday")
Sunday = get_mood_input("Sunday")

week_mood = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

average_mood = sum(week_mood) / len(week_mood)

print("Weekly average mood score:", round(average_mood, 1))
