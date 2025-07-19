
# re.split()-Splits the string by occurrences of the pattern.
# re.split(pattern, string, maxsplit=0, flags=0)

import re

def str_split():

    sample_txt = "one,two;three-four"
    pattern = r"[,;-]"

    match = re.split(pattern,sample_txt)


    if match:
        print('Match found!!!')
        print(match)
        print()
    else:
        print('No match found')


# function call 
str_split()

