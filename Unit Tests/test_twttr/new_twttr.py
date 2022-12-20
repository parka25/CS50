def main():
    word = input("Input: ")
    new_word = shorten(word)
    print("Output: ", new_word)


def shorten(word):
    word_v = ""
    for l in word:
        if not l.lower() in ["a", "e", "i", "o", "u"]:
            word_v += l
    return word_v


if __name__ == "__main__":
    main()
