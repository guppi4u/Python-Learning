
# program for grouping ()

import re 

def grouping_set_one():
    text = "apple orange banana"
    pattern = r"(apple|banana)" # Matches "apple" or "banana"
    match = re.findall(pattern, text)

    if match:
        print('Match found!!!')
        print(match)
    else:
        print('No match')
   


def grouping_set_two():
    text = "Name: John Doe, Age: 30"
    pattern = r"Name: (\w+ \w+), Age: (\d+)" # Captures name and age
    match = re.search(pattern, text)
    if match:
        print(f"Name: {match.group(1)}, Age: {match.group(2)}")
    else:
        print ('No match !!!')
    

#function call 

grouping_set_one()

print()

print ("******************")

print()

grouping_set_two()