
# creaitng prgms for matches any  Ex:- 'a','b' ....'z' single char "[]"

import re

def meta_charset():
    sample = " foobarqux"

    match = re.search('ba[artz]',sample)

    if match:
        print('Found match !!!')
        print(match)

    else:
        print('No match')


#function call 

meta_charset()