from numb3rs import validate


def main():
    check_correct()


def check_correct():
    assert validate("244.244.244.244") == False
    assert validate("1.1.1.1") == True
    assert validate("1.1.1.") == False
    assert validate("1") == False
    assert validate("9999.255.255.255") == False
    assert validate("0.255.255.255.255") == False


main()
