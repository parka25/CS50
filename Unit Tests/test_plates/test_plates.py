from new_plates import is_valid


def check_correct():
    assert ("C") == False
    assert ("CDFD777") == False
    assert ("CS50") == True
    assert ("DFR6R4") == False
    assert ("!?. ") == False
    assert ("CR777") == True
    assert ("APDP09") == True
