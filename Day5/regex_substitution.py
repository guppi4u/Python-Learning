# Program for regular expression substitution


import re


def main():

    text = "Hello Jack , how are you Jack"

    result = re.sub("Jack", "Jill", text)

    print(result)


main()
