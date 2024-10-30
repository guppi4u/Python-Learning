# Program for matching last word in sentence with look adhead zero assertion ("?"."$")


import re


def main():

    text = "You could get a devloper job. E.g. in robotics. Maybe. Or web Development."

    result = re.findall(r"\s+(\w+)\.(?=\s+|$)", text)

    print(result)


main()
