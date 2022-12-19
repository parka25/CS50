while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        new_x = int(x)
        new_y = int(y)
        percent = int((new_x/new_y)*100)
    except (ValueError, ZeroDivisionError):
        pass
    if percent == 100:
        percent = "F"
    if percent == 0:
        percent = "E"
    print("percent: ", percent)
