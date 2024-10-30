# Program for regular expression substitution with alternatives


import re


def main():

    text = "Hello Jack , Hello Jill , how are you both doing?"

    result = re.sub(r"Hello (Jack|Jill)", r" Hi \1", text)

    print(result)


main()
