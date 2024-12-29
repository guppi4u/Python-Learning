# Program will copy data from the clipboard and print as data frame
# Note this program required installation of pyperclip package

"""
ID  Weight  Height
1   700     1600
2   600      1550
3   1000     1800
"""

import pandas as pd


def main():

    # this will copy data from clipboard
    df = pd.read_clipboard(index_col=0)

    print(df)

    height = df['Height']
    # print type of height object
    print(type(height))
    print(height)
    print("**********")
    print(type(height.index))
    # putting height.index into list
    print(list(height.index))
    print()
    print(type(height.values))
    print(list(height.values))

    print()
    print("***************")
    # prints height mean value
    print(height.mean())


main()
