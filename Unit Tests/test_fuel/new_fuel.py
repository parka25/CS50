def main():
    fraction = input("Fraction: ")
    fraction_done = convert(fraction)
    percent_output = gauge(fraction_done)
    print(percent_output)


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            new_x = int(x)
            new_y = int(y)
            f = new_x/new_y
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage == 100:
        return "F"
    if percentage == 0:
        return "E"
    else:
        return ("percent: ", percentage)


if __name__ == "__main__":
    main()
