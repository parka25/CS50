from working import convert, convert_time


def main():
    check_answer()


def check_answer():
    assert convert("9:00AM to 5:00PM") == True
    assert convert("9 AM to 5 PM") == True
    assert convert("9 AM to 5:30PM") == True
    assert convert("9 to 5") == False
