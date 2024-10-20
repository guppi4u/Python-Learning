# Program for regular expression

import re


def main():
    demoText = "dog"

    result = re.match("dog", demoText)
    print(result)
    print(result is not None)


main()
