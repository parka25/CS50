import sys


def main():
    check_for_line_arguement()
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
        print(lines)
    except:
        sys.exit("File cannot be found")


def check_for_line_arguement():
    # check if the line contains just enough arguement, only 2
    if len(sys.argv) < 2:
        print("too few arguements")
        sys.exit()
    if len(sys.argv) > 2:
        print("too many arguements")
        sys.exit()
# check if the file written is a .py file
    if sys.argv[1].endswith(".py") == False:
        print("Not a python file")
        sys.exit()


if __name__ == "__main__":
    main()
