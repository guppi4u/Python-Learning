# Program with regex findall()


import re


def main():

    test = """

     1. Apple 
     2. Orange 
     3. Cherries
     4. Strawberries
    

     """

    result = re.findall(r"(\d+)\.\s+(\w+)", test)

    print(result)


main()
