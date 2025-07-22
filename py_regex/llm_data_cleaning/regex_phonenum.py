
# program to extract phone num from given string 

import re 

def extract_phonenum():
    sample_txt = "Call us at (123) 456-7890 or 987.654.3210."

    pattern_regex=r"\(?(\{d3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})"
    orginal_pattern_regex =r"\(?(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})"

    clean_txt=re.sub(orginal_pattern_regex,r"\1-\2-\3",sample_txt)

    print(clean_txt)


# function call 

extract_phonenum()