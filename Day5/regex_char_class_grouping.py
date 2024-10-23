# Program for  regex character classes grouping


import re


def main():
    result = re.match(r"([a-z][a-z\.\-]+)@(\w+)\.(\w+)",
                      'helloworld@python.com')

    print(result)

    # grouping -this is done by using '()'

    name, domain, suffix = result.groups()

    print(name, domain, suffix)


main()
