# Program for  regex character class not

import re


def main():

    tag = '<div id="123">Hello</div>'

    result = re.match(r"[<][^>]+>([^<>]+)</[^>]+>", tag)

    print(result)

    # this will print 1st group
    content = result.group(1)
    print(content)


main()
