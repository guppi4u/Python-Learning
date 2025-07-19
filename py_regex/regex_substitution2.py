


# Replace multiple spaces with a single space

import re

def str_replacement():

    sample_txt = "This   has    too  many spaces."

    pattern =r"\s+"
    match = re.sub(pattern, " ",sample_txt)

    if match:
        print('Match found!!!')
        print(match)
        print()
        print(match.strip()) # .strip() removes leading/trailing spaces
    else:
        print('No match found')


#function call 

str_replacement()