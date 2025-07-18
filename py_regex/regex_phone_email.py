
# program to extract phone num and email id from text 

import re

def extract_phone():
    sample = "Phone: 123-456-7890 Email: test@example.com"

    pattern = r"\d{3}-\d{3}-\d{4}" # Matches a phone number pattern

    match = re.search(pattern,sample)

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match')


def extract_email():
    sample = "Phone: 123-456-7890 Email: test@example.com"

    pattern = r"\w+@\w+\.\w+" # Matches a basic email pattern

    match = re.search(pattern,sample) 

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match')


# function call 

extract_phone()
print()
print("*****************")
print()
extract_email()


