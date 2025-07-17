
import re 

def match_pattern():

    # creating sample srtring
    sample_string ="foo123bar"
    
    # searching '123' in etire sample string 
    match =re.search('123',sample_string)
    print(match)


# function call 
match_pattern()

