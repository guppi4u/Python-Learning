# Program to create range in string text using characters range "{}"(flower.brackets)

import re


def main():

    text = "hellojohn@testing.com"

    result = re.match("", text)

    # matching 3 char before @ symbol
    result1 = re.match(r'\w{3}@', text)

    print("No match" if result is None else "Match")
    print()
    print("No match" if result1 is None else "Match")


main()
