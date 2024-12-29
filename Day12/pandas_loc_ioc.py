
import pandas as pd


def main():
    df = pd.read_csv('Day12/exercises.csv', sep=r'\s*,\s*',
                     engine='python', index_col=0)

    print(df)

    print("*************")

    # this will print coloum range from mon to fri with step 2
    print(df.loc['Mon':'Fri':2])

    print("*************")

    # this will print specific coloum
    print(df.loc['Mon':'Fri', 'Pullups':'Pushups'])

    print("*************")

    # this will print specific coloum based on intger values
    print(df.iloc[3:6, :2])


main()
