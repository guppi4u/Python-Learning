
import re

def meta_match():

    sample2 = "foo456bar"

    sample3 = "atob123alwaysmatch"


    match2 =re.search('[0-9][0-9][0-9]',sample2)

    if match2:
        print('Match found')
        print(match2)
        print()
    else:
        print('No match found')

    match3 =re.search('[0-9][0-9][0-9]',sample3)

    if match3:
        print('Match found')
        print(match3)
        print()
    else:
        print('No match found')



#function call 
meta_match()