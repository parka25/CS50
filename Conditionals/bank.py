input = input("Greeting: ")
input2 = input.lower().strip()

if "hello" in input2:
    print("you get $0")
elif "h" == input2[0]:
    print("you get $20")
else:
    print("you get $100")