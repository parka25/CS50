def main():
    prompt = input("what time is it? ")
    time = convert(prompt)
    if time >= 7 and time <= 8:
        print("breakfest time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours_float = float(hours)
    minutes_float = float(minutes)/60
    return hours_float + minutes_float

if __name__ == "__main__":
    main()