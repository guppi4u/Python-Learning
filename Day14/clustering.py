# creating clustering and graph for mall customer database

import pandas as pd
import matplotlib.pyplot as plt


def plot(df):

    # defining plot figure size
    figure = plt.figure(figsize=(16, 9))
    # adding figure to subplot
    ax = figure.add_subplot()
    # creating scatter plot
    ax.scatter(df['income'], df['spending'])
    # defining x,y lable
    ax.set_xlabel("Income")
    ax.set_ylabel("Spending")
    # showing plot
    plt.show()


def main():
    # reading csv
    df = pd.read_csv("Day14/mall_customers.csv")
    # setting column names

    df.columns = ['id', 'gender', 'age', 'income',
                  'spending']  # Give meaningful column names
    plot(df)


main()
