import pandas as pd
import numpy as np


def main():
    df = pd.read_csv("Day12/mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    gp = df.groupby('Gender')

    print(type(gp))

    male_dataframe = gp.get_group('Male')
    print(type(male_dataframe))

    male_income_series = male_dataframe['Income']
    print(type(male_income_series))

    grouped_income_series = gp['Income']
    print(type(grouped_income_series))

    # printing agg functions mean()
    print(gp.mean())
    print()
    # printing agg functions mean() for grouped income series
    print(grouped_income_series.mean())
    print()
    print(gp.agg([np.std, np.mean, len]))
    print()
    print(grouped_income_series.agg([np.std, np.mean, len]))


main()
