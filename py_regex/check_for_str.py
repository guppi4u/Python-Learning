
# checking for pattern match

import re


def check_for_str():

    sample = "The rain in the anything after this should match Spain"

    """
    ^ - match beginning of string 
    . - A meta char matches any single character except newline

    * - Matches zero or more repetitions

    $ - Anchors a match at the end of a string
    """

    searching = re.search("^The.*Spain$", sample)

    if searching:
        print("Found match")
    else:
        print("No match found")


# function call

check_for_str()
