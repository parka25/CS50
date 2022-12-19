input = input("What is the answer to life, the Universe, and Everything? ")
if input.strip() == "42":
    print("Yes")
elif input.lower().strip() == "forty-two":
    print("Yes")
elif input.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")