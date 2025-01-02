import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    df = pd.read_csv("Day13/weights.csv", index_col=0, sep='\s+')

    major_ticks = range(0, len(df.index), 7)
    labels = [df.index[x] for x in major_ticks]

    fig = plt.figure(figsize=(16, 9))
    ax = fig.add_subplot()
    ax.set_xticks(ticks=major_ticks, labels=labels,
                  rotation='vertical', minor=False)
    ax.set_xticks(ticks=range(len(df.index)), minor=True)
    ax.tick_params(axis='x', which='major', labelsize=10)
    ax.tick_params(axis='x', which='minor', labelsize=4)
    fig.suptitle("Weight vs Time")
    ax.grid()
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight(Kg)")

    # assiginig x as np arange and setting to len of df.index
    x = np.arange(len(df.index))
    # defining equation of stright line (y=mx+b)
    y = -0.1 * x + 93

    ax.plot(df.index, df['weight'])
    ax.plot(x, y)
    plt.show()


main()
