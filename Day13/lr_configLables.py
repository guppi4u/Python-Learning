# configuring lables and improving readability of graph

import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("Day13/weights.csv", index_col=0, sep='\s+')

    # Ticks are the values used to show specific points on the coordinate axis
    major_ticks = range(0, len(df.index), 7)

    # putting lables for index-X and looping over major_ticks
    labels = [df.index[x] for x in major_ticks]

    # initilizing figure size
    fig = plt.figure(figsize=(16, 9))

    # adding graph
    ax = fig.add_subplot()

    # setting axis for xticks, setting lables as lables and ticks to rotate vertically and minor tick is false
    ax.set_xticks(ticks=major_ticks, labels=labels,
                  rotation='vertical', minor=False)

    ax.set_xticks(ticks=range(len(df.index)), minor=True)

    # this will set tick_param as major for lable 10 and minor for lable 4
    ax.tick_params(axis='x', which='major', labelsize=10)
    ax.tick_params(axis='x', which='minor', labelsize=4)
    # setting title
    fig.suptitle("Weight vs Time")
    # configuring grid lines for graph
    ax.grid()
    # setting lables
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight(Kg)")
    # plotting graphs with (x,y)
    ax.plot(df.index, df['weight'])
    # display graph
    plt.show()


main()
