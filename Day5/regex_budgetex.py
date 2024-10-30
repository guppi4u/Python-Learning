# Program for creating budget exercise

import re
from collections import defaultdict

data = '''
Day                 Electricity           Coffee         Cleaning

Monday                 330                  10               50
Tuesday                220                  12               40 
Wednesday              130                  14               80

'''


def main():

    # creating 2 data structures ,one for storing day total and another for commodity

    category = defaultdict(float)
    days = defaultdict(float)

    # spliting on new line ('n)

    lines = re.split("\n", data)

    # initialzing header to None
    header = None

    # looping over the lines

    for line in lines:
        # skipping any blank line and continue
        if re.search(r"^\s*$", line):
            continue

        # splitting line with wide spaces using greedy match
        fields = re.split(r"\s+", line)

        # traversing the loop and if header is encountered, dont do anything ,continue

        if header is None:
            header = fields
            continue

        print(fields)

        # for calculating day total , first we need to remove day field in the list , this is done my pop()

        day = fields.pop(0)

        # now looping accros fields with enumerator and i for categories
        for i, field in enumerate(fields):
            for i in range(len(header) - 1):
                heading = header[i+1]  # Ensure i + 1 is within bounds

            # checking if field is not empty or just whitespaces with split()
            if field.strip():
                # taking day as key and casting filed values to float
                days[day] += (float(field))

                # calculating categories
                category[heading] += float(field)

    print(header)

    print(days)
    print(category)


main()
