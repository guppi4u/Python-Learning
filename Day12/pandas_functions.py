import pandas as pd


def main():
    df = pd.DataFrame([[11, 22, 33], [21, 34, 45], [56, 32, 30]],
                      columns=['Horse', 'Elephant', 'Giraffe'],
                      index=['grass', 'grain', 'hay'])

    print(df)
    print()
    # this will iterate through fucntions -'min', max etc
    for func in ['min', 'max', 'std', 'var', 'mean', 'sum']:
        # this will get attributes of  functions
        f = getattr(df, func)
        # this will print the function title
        print(func.title())
        # this will print col
        print(f(axis=0))
        print()


main()
