
import pandas as pd


def main():
    df = pd.read_csv('Day12/exercises.csv', sep=r'\s*,\s*',
                     engine='python', index_col=0)

    print(df.at['Wed', 'Pushups'])
    print(df.iat[3, 0])


main()
