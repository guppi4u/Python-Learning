# Program for regex ignore case

import re


def main():
    text = "Hello Bob"

    # matching regular expression with ignorecase flag
    print(re.match(r".*bob", text, re.IGNORECASE))

    print(re.sub(r"bob", "Zoe", text, flags=re.IGNORECASE))


main()
