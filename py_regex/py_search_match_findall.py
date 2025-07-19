
# program for 'search()- accross the string, match()- at the beginning of string 
#  findall()-returns nonoverlapping matches

import re

def search_str():

    sample_txt = "Third match, Second match, First match"

    pattern ="Third"

    match = re.search(pattern,sample_txt)

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match found')

def match_str():

    sample_txt = "Third match, Second match, First match"

    pattern ="Second"

    match = re.match(pattern,sample_txt) # this will return str not match

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match found')

def findall_str():

    sample_txt = "Third match, Second match, First match"

    pattern ="match"

    match = re.findall(pattern,sample_txt) # this will return non overlapping match

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match found')


# function call 
search_str()
print()
print("****************")
match_str()
print()
print("****************")
findall_str()