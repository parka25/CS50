import inflect
import sys
p = inflect.engine()
names = []
while True:
    try:
        name = input("Name:")
        names.append(name)
        adieu_list = p.join(names)
    except EOFError:
        print()
        break
print("Adieu, adieu to ", adieu_list)
