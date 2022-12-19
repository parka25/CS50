import random


def main():
    level = get_level()
    score = check_answer(level)
    print("Score: ", score)


def get_level():
    # Prompts the user for a level, n. If the
    # user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


def round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == (x + y):
                return True
            else:
                count_tries = count_tries + 1
                print("EEE")
        except:
            count_tries = count_tries + 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False


def check_answer(level):
    questions = 1
    point = 0
    while questions <= 10:
        x, y = generate_integer(level)
        user_answer = round(x, y)
        if user_answer == True:
            point = point + 1
        questions = questions + 1
    return point


if __name__ == "__main__":
    main()
