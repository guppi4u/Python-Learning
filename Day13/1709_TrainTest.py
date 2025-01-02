import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

# Your code using train_test_split here


def main():
    df = pd.read_csv("Day13/weights.csv", index_col=0, sep='\s+')

    # create ticks from 0 to lenght with step size 7
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

    # setting X, Y to date and weight respectively
    x = np.arange(len(df.index))
    y = df['weight']

    # this will take traning data and test date , traning data is 0.7 which means 70% of data is traning and rest 30% is test
    (x_train, x_test, y_train, y_test) = train_test_split(
        x, y, shuffle=False, train_size=0.7)

    print(len(x_train)/len(x_test))
    print(len(y_train)/len(y_test))

    ax.plot(x, y)
    plt.show()


main()
