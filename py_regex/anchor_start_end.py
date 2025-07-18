
# prpgram for anchor tag (^)- beginning and ($)- ending 

import re
def anchor_beginning():

    sample = "hello world\nworld hello"

    match = re.search("^hello",sample) # Only matches 'hello' at the start of the string

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match')

def anchor_end():

    sample = "hello world\nworld hello"

    match = re.search("hello$",sample) # Only matches 'hello' at the end of the string

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match')


# function call 
anchor_beginning()
print()
print("*****************")
print()
anchor_end()