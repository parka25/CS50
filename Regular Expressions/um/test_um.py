from um import count


def main():
    check_error()


def check_error():
    assert count("um,um,um,um") == 3
    assert count("andrew, um, park") == 1
    assert count("andrew, um, park, um, seongmin") == 2


if __name__ == "__main__":
    main()
