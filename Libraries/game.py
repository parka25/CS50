import random
while True:
    try:
        level = int(input("Level: "))
        if level == int(level):
            rand = random.randint(0, level)
            break
    except (ValueError):
        pass
while True:
    try:
        guess = int(input("Guess: "))
        if guess > rand:
            print("Too Large!")
        elif guess < rand:
            print("Too Small")
        elif guess == rand:
            break
    except (ValueError):
        pass
print("Just About Right!")
