
# creating python regex101 

import re

def finding_regex_in_text():

    text="hello world , hello world again"

    match_text = "hello"

    match= re.findall(match_text,text)

    print(match)


# function call
print(finding_regex_in_text())



