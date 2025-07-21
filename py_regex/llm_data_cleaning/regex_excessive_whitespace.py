# removing Excessive Whitespace

import re
def remove_whitespaces():
    sample_text = "  This   has  many   spaces.  "

    clean_text=re.sub(r"\s+"," ",sample_text).strip() 

    print(f'Cleaned text : {clean_text}')
   



# function call 

remove_whitespaces()


    
    