from new_bank import value


def check_right_value():
    assert value("Hello") == 0
    assert value("Hello Andrew") == 0
    assert value("hello Andrew") == 0
    assert value("hello andrew") == 0
    assert value("h") == 20
    assert value("hi") == 20
    assert value("hippo") == 20
    assert value("----") == 100
    assert value("Greeting") == 100
