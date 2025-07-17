
# prg for meta char in regex 

import re

def meta_char_match():

    sample = "foo123bar"

    match = re.search("[0-9][0-9][0-9]",sample)

    if match:
        print("String match found")
        print(match)

    else:
        print("No match found!!!")


#fucntion call 

meta_char_match()

