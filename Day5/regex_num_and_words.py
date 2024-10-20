# Program to match words and numbers in sentence using regex

'''
\w: matches alphanumeric characters 
+: matches one or more ,as many a possible 
\s : matches space 
\d: matches digits 
\r :raw string 

'''

import re


def main():

    text = "The tempreture is 40."

    # single word in the string
    result = re.match("\w", text)

    print("No match" if result is None else f"'{result.group()}'")

    print("****************************************************")

    # three words in the string
    result = re.match("\w\w\w", text)

    print("No match" if result is None else f"'{result.group()}'")

    print("****************************************************")

    # three words in the string
    result = re.match(r"\w+", text)

    print("No match" if result is None else f"'{result.group()}'")

    print("****************************************************")

    # space in the string
    result = re.match(r"\w+\s", text)

    print("No match" if result is None else f"'{result.group()}'")

    print("****************************************************")

    # word after space
    result = re.match(r"\w+\s\w+\s\w+\s\d\d\.", text)

    print("No match" if result is None else f"'{result.group()}'")

    print("****************************************************")


main()
