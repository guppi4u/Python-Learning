# Program to match regex with character class with [] brackets


import re


def main():
    result = re.match(r'[a-z/d]', 'abcd123')
    print(result)
    print()
    print(result.string)
    print()


main()
