# regex matching multiple chatracters


import re


def main():
    text = "drooooo1"

    result = re.match("dr.*", text)

    if result is None:
        print("No match")

    else:
        print(result.group())


main()
