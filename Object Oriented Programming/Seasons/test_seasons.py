from seasons import sub_date, convert_totext


def main():
    check_sub_date()
    check_convert_totext()


def check_sub_date():
    assert sub_date("20002") == "Invalid date"
    assert sub_date("2006-02-25") == 8847360
    assert sub_date("January 1, 2022") == "Invalid date"
    assert sub_date("") == "Invalid date"


def check_convert_totext():
    assert convert_totext(1) == "one minutes"
    assert convert_totext(
        525600) == "five hundred twenty-five thousand, six hundread minutes"
    assert convert_totext("hello") == "zero minutes"


main()
