
import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("Day12/mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    # this will groupby the dataframe by Gender
    gp = df.groupby(by='Gender')

    # this will print type of  groups
    print(type(gp))
    print(gp.ngroups)
    print(gp.groups)

    # this will print group keys for df
    print(gp.groups.keys())
    # display max 200 records
    pd.set_option("display.max_rows", 200)
    print(gp.get_group('Female'))
    print(gp.get_group('Male'))


main()
