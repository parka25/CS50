prompt = input("camelCase: ")
print("snake_case: ")
for c in prompt:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end="")
print("")