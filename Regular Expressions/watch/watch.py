import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url = re.search(
            r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$", s)
        if url:
            split_url = url.groups()
            return "https://youtu.be/" + split_url
        # return"okay"
    # else:
        # return("not valid, try another url")


if __name__ == "__main__":
    main()
