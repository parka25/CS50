import sys
import csv


def main():
    output = []
    check_for_line_arguement()
    try:
        with open(sys.argv[1], "r") as csvfile:
            read = csv.DictReader(csvfile)
            for row in read:
                split_name = row["name"].split(",")
                output.append(
                    {'first': split_name[1], 'last': split_name[0], 'house': row["house"]})

    except FileNotFoundError:
        sys.exit("File cannot be found")
    with open('after.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        for row in output:
            writer.writerow(
                {'first': row["first"], 'last': row["last"], 'house': row["house"]})


def check_for_line_arguement():
    # check if the line contains just enough arguement, only 2
    if len(sys.argv) < 3:
        print("too few arguements")
        sys.exit()
    if len(sys.argv) > 3:
        print("too many arguements")
        sys.exit()
    if sys.argv[1].endswith(".csv") == False:
        print("Not a csv file")
        sys.exit()


if __name__ == "__main__":
    main()
