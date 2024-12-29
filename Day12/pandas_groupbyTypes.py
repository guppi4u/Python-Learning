import pandas as pd


def main():
    df = pd.read_csv("Day12/mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    gp = df.groupby('Gender')

    # types of type of dataframe
    print(type(gp))

    # from df getting group of Male column and printing type
    male_dataframe = gp.get_group('Male')
    print(type(male_dataframe))

    # from df getting group of Income column and printing type
    male_income_series = male_dataframe['Income']
    print(type(male_income_series))

    grouped_income_series = gp['Income']
    print(type(grouped_income_series))


main()
