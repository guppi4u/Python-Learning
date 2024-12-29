# program for pandas sorting

import pandas as pd


def main():

    # this will read mallcust csv file and index it to col 0
    df = pd.read_csv("Day12/mall_customers.csv", index_col=0)

    # renaming table name as per our convinience
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    # limiting display row to max 10
    pd.set_option("display.max_rows", 10)

    # sorting values  by Gender , Age
    df.sort_values(by=['Gender', 'Age'], inplace=True, axis=0, ascending=False)

    print(df)


main()
