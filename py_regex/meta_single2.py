
import re 


def meta_single_char_set():
    sample = "HelloWorldIntheWorld1234"

    match = re.search('Hello[Wlrdo]',sample)


    if match:
        print('Match found')
        print(match)

    else:
        print('No match found')



meta_single_char_set()