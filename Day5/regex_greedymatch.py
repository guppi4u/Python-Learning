# Program to demo different kind of regex match

import re


def main():
    text = "zigzag"

    # "*" operator here is greedy match
    result = re.match("z.*g", text)

    print("No match" if result is None else f"Match :{result.group()}")

    print("*****************************************************************")
    # "?" operator here is minimilistic match
    result = re.match("z.*?g", text)

    print("No match" if result is None else f"Match :{result.group()}")

    print("*****************************************************************")

    #  with just .*
    result = re.match("z.*", text)

    print("No match" if result is None else f"Match :{result.group()}")

    print("*****************************************************************")

    result = re.match("z.*?", text)

    print("No match" if result is None else f"Match :{result.group()}")

    print("*****************************************************************")

    result = re.match("z.*$", text)

    print("No match" if result is None else f"Match :{result.group()}")

    print("*****************************************************************")


main()
