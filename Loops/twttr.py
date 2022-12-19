prompt = input("Input: ")
print("Output: ")
for l in prompt:
    if not l in ["a", "e", "i", "o", "u"]:
        print(l, end="")
print()