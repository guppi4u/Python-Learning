import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("Day12/mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    values = np.random.randint(low=0, high=100, size=100)
    print(values[values < 48])
    print(values[(values == 48) | (values == 44)])

    # this will print Gender as Female and age is 27
    print(df.loc[(df['Gender'] == 'Female') & (df['Age'] == 32)])


main()
