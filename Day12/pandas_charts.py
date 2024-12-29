# this will print pandas charts

import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.DataFrame([[111, 222, 300], [27, 38, 49], [50, 32, 37]],
                      columns=['cow', 'goat', 'sheep'],
                      index=['grass', 'grain', 'hay'])

    print(df)
    print()
    for func in ['min', 'max', 'std', 'var', 'mean', 'sum']:
        f = getattr(df, func)
        print(func.title())
        print(f(axis=0))
        print()
    # this is graph size
    fig = plt.figure(figsize=(16, 9))
    # title of grpah
    fig.suptitle("Animal Feed")
    # iterating over columns
    for i, animal in enumerate(df.columns):
        # adding subplot
        ax = fig.add_subplot(1, 3, i+1)
        ax.set_title(animal.title())
        # print pie chart
        ax.pie(df.iloc[:, i], autopct='%.1f %%', labels=df.columns)

    plt.show()


main()
