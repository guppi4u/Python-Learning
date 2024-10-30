# Program to print nospace and no digits


import re

text = r"""
“Monty! Where are you?”

A pale green-furred boy quickly stuffed his tattered copy of The Great Pickle Mystery into his apron pocket.

“Coming sir!” He scooted into the kitchen where Snort, a patchy, red and grey-furred warthog-like creature, was ladling a glop of steaming green stuff into a wooden bowl.

Snort is the boss here at the Gristling Inn, a twelve room bed and breakfast at the end of a dark forest road.

“Here I am!” said Monty. “Sorry. I was about to stack the...”

“Never mind what you were about to do! Get this GreenGravy up to Ms. Sourbaum in room number five. Snip snap!”

"""


def main():

    # casting it to set to remove duplicate
    notSpaceSet = set(re.findall(r"\S", text))
    print(notSpaceSet)
    print()
    notAlphanumericSet = set(re.findall(r"\W", text))
    print(notAlphanumericSet)


main()
