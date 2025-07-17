
# checking for truthy value with if condtion 

import re 

def match_pattern():

    # creating sample srtring
    sample_string ="foo123bar"
    
    # searching '123' in etire sample string 
    match =re.search('123',sample_string)
    
    if match:
        print("String match !!!")
    else:
        print("No match found !!!")


# function call 
match_pattern()