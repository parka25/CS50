from datetime import date, timedelta
import inflect
import sys

inflect = inflect.engine()


def main():
    birthday = input("Date of Birth: ")
    minutes = sub_date(birthday)
    print(convert_totext(minutes))
    print(convert_totext("notthingness"))


def sub_date(birth):
    # ask for the input of date until a valid date is given
    try:
        birth_date = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")
    else:
        # take a date today using date function
        today = date.today()
        # check for the number of birth_date
        sub = today - birth_date
        total = sub.total_seconds() / 60

    return round(total)


def convert_totext(num):
    return f"{inflect.number_to_words(num, andword='')} minutes"


if __name__ == "__main__":
    main()
