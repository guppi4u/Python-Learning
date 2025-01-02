# program for LinearRegression

import pandas as pd
import matplotlib.pyplot as plt


def main():

    # reading data from weigts.csv and setting index_col to 0 and using space '\s' as seperator
    df = pd.read_csv("Day13/weights.csv", index_col=0, sep='\s+')

    # creates/ initialize new figure(graph)
    fig = plt.figure()

    # creates a subplot
    ax = fig.add_subplot()
    # adds title
    fig.suptitle("Weight vs Time")
    # setting lables for graphs
    ax.set_xlabel("Date")
    ax.set_ylabel("Weight(Kg)")

    # plot grpah between index(date) and weight
    ax.plot(df.index, df['weight'])

    # display graph
    plt.show()


main()
