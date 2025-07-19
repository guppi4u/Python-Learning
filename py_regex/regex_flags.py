
"""
Flags modify the behavior of the regex.

    re.IGNORECASE or re.I: Performs case-insensitive matching.

    re.MULTILINE or re.M: Makes ^ and $ match the start/end of each line, not just the start/end of the string.

    re.DOTALL or re.S: Makes the . special character match any character, including a newline.

"""

import re 

# # Case-sensitive (default)
def regex_str_without_flags():

    sample_txt = "Hello world\nhello PYTHON"
    pattern = "hello"

    match= re.findall(pattern,sample_txt)

    if match:
        print('Found match!!!')
        print(match)

    else:
        print('No match')


# # Case-Insensitive 
def regex_str_with_flags():

    sample_txt = "Hello world\nhello PYTHON"
    pattern = "hello"

    match= re.findall(pattern,sample_txt,re.IGNORECASE)

    if match:
        print('Found match!!!')
        print(match)

    else:
        print('No match')


# # Ignores multiline
def regex_str_with_multiline_flags():

    sample_txt = "Demo 1\nDemo 2\nDemo 3"
    pattern = r"^Demo"

    match= re.findall(pattern,sample_txt,re.MULTILINE)

    if match:
        print('Found match!!!')
        print(match)

    else:
        print('No match')


# function call 

regex_str_without_flags()

print()

print ("***********************")

regex_str_with_flags()

print()

print ("***********************")

regex_str_with_multiline_flags()


