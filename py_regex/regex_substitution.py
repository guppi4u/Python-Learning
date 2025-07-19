
# program for string substitution 
# re.sub() -It replaces occurrences of a pattern with a specified replacement string.
# re.sub(pattern, replacement, string, count=0, flags=0)

import re

def str_substitution():
    sample_txt = "Hello 123 World 456"

    pattern =r"\d+" # this will remove all digits from sample_txt

    match =re.sub(pattern,"",sample_txt)

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match found')


# function call 

str_substitution()
