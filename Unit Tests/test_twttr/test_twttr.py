from new_twttr import shorten

# Check for any mistakes within the functions


def check_for_lower_case():
    assert shorten("answer") == "nswr"
    assert shorten("ANSWER") == "NSWR"
    assert shorten("AnsWer") == "nsWr"


def check_for_other_character():
    assert shorten("8888") == "8888"
    assert shorten("@#$%") == "@#$%"
