
# Correlation in pandas dataframe - Correlation will be between two entities and values will be between 0 and 1


import pandas as pd
import numpy as np


def main():

    # reading mall customer csv
    df = pd.read_csv("Day12/mall_customers.csv", index_col=0)

    # changing column names as per requirment
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    print(df)

    # Select only numeric columns for correlation calculation
    numeric_df = df.select_dtypes(include=['number'])

    # correlation
    corr = numeric_df.corr()
    np.fill_diagonal(corr.values, 0)

    print(corr)


main()
