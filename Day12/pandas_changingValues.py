import pandas as pd


def main():
    df = {
        'one': [1, 2, 3],
        'Two': [4, 5, 6],
        'Three': [7, 8, 9]
    }

    # printing dic as dataframe
    df = pd.DataFrame(df)
    print(df)

    print("*************")

    # multipling dataframe with 0.5
    df *= 0.5

    print(df)

    print("*************")

    # accessing data and chainging using iloc
    df.iloc[:, 1] = 5
    print(df)

    print("******")
    df.iloc[:, 2] = 0
    print(df)


main()
