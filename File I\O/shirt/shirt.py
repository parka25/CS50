import sys
from os.path import splitext
from PIL import Image, ImageOps


def main():
    check_for_line_arguement()
    try:
        person = Image.open(sys.argv[1])
    except FileNotFoundError:
        print("The file is not found")
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(person, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])


def check_for_line_arguement():
    # check if the line contains just enough arguement, only 2
    if len(sys.argv) < 3:
        print("too few arguements")
        sys.exit()
    if len(sys.argv) > 3:
        print("too many arguements")
        sys.exit()
    if sys.argv[1].endswith(".jpg") == False:
        print("Not a jpg file")
        sys.exit()


if __name__ == "__main__":
    main()
