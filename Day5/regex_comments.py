# Program for regex comments


import re


def main():

    text = '<div id="123">Hello</div>'

    result = re.match(
        r"""
         
        <div\s+        # Match opening tag
        id="(\w+)"     # Match id attribute
        >              # End of opening tag
        ([^<>]+)       # Match contents of tag
        </div>         # Closing div tag    

        """,
        text, re.VERBOSE)

    id, content = result.groups()

    print(id, content)


main()
