# calculate the values and anser below questions

import numpy as np
import re

data1 = """
            Water   Coffee   Tea (Litres)
Week1       50      60      45
Week2       100     150     180
Week3       70      50      45
Week4       45      20      15
"""

data2 = """
            Price per Liter
Water       0.2
Coffee      0.4
Tea         0.3
"""

"""
1. How much of each beverage was drunk in total?
2. How much liquid in total was consumed per week?
3. How much money was spent on beverages in each week?
4. How much money was spent in total on beverages?
"""


def dataloding(data):

    # initialzing empty list
    result = []

    # splitting the data using new line char
    for line in data.split("\n"):

        # extracting data from Water , Coffee , Tea and removing others (i,e 1,2,3)
        matches = re.findall(r'\s+([\d\.]+)', line)

        if len(matches) > 0:
            result.append(matches)

        print(matches)

    return result


def main():
    m1 = dataloding(data1)
    m2 = dataloding(data2)

    # putting m1 and m2 to numpy array
    a1 = np.array(m1, dtype=float)
    a2 = np.array(m2, dtype=float)


# 1. How much of each beverage was drunk in total?
    print(a1.sum(axis=0))
    print(a2.sum(axis=0))

    print("**********************************")
# 2. How much liquid in total was consumed per week?
    print(a1.sum(axis=1))
    print(a2.sum(axis=1))
    print("**********************************")

# 3. How much money was spent on beverages in each week?

    # multiplying matrices with matmul function
    print(np.matmul(a1, a2))

    print("**********************************")

# 4. How much money was spent in total on beverages?
    print(np.matmul(a1, a2).sum())


main()
