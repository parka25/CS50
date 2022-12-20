import csv
import sys
from tabulate import tabulate


def main():
    check_for_line_arguement()
    table = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            read = csv.reader(csvfile)
            for r in read:
                table.append(r)
    except FileNotFoundError:
        sys.exit("File cannot be found")
    print(tabulate(table, tablefmt="grid"))


def check_for_line_arguement():
    # check if the line contains just enough arguement, only 2
    if len(sys.argv) < 2:
        print("too few arguements")
        sys.exit()
    if len(sys.argv) > 2:
        print("too many arguements")
        sys.exit()
# check if the file written is a .py file
    if sys.argv[1].endswith(".csv") == False:
        print("Not a csv file")
        sys.exit()


if __name__ == "__main__":
    main()
