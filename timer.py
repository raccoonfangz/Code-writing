import time
import os

os.system('cls' if os.name == 'nt' else 'clear')


def get_duration():
    ask = input("Enter duration (mm:ss or minutes): ")
    try:
        if ':' in ask:
            mins, secs = ask.split(':')
            return int(mins) * 60 + int(secs)
        else:
            return int(ask) * 60
    except ValueError:
        print("Invalid input. Try again.")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        return get_duration()


def countdown(total_time):
    current_time = total_time
    while current_time > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(progress_bar(current_time, total_time,
              current_time), end='', flush=True)
        time.sleep(1)
        current_time -= 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(progress_bar(0, total_time, 0))
    print("Done!")


def progress_bar(current, total, current_time, bar_length=20):
    filled_length = int(bar_length * (total - current) / total)
    bar = '■' * filled_length + '-' * (bar_length - filled_length)
    mins_left = int(current // 60)
    secs_left = int(current % 60)
    percent = (100 * (total_time - current_time) / total_time)
    return f"{mins_left:02d}:{secs_left:02d} left\n\n[{bar}] {percent:.1f}% done!"


total_time = get_duration()
countdown(total_time)
