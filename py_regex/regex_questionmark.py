
# \? matches a literal question mark.

import re

def regex_questionmark():
    sample = "What? Really!"

    match=re.search("What\?",sample)

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match')

#function call 
regex_questionmark()