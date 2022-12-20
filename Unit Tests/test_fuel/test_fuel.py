from new_fuel import convert, gauge


def check_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("0/2") == 0
    assert convert("2/2") == 100


def check_gauge():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(33) == "33%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
