
'''
This program is a simple example of using KMeans clustering to group customers based on their income and spending patterns, and then visualizing the results with a scatter plot. 
'''


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def plot(df):
    fig = plt.figure(figsize=(16, 9))  # Creates a figure with specific size
    ax = fig.add_subplot()  # Adds a subplot (the area where the plot will appear)
    # Scatter plot with points colored by cluster
    ax.scatter(df['income'], df['spending'], c=df['cluster'], cmap='plasma')
    ax.set_xlabel('Income')  # Label the x-axis as 'Income'
    ax.set_ylabel('Spending')  # Label the y-axis as 'Spending'
    plt.show()  # Show the plot on the screen


def cluster(df, n):
    # Select the 'income' and 'spending' columns for clustering
    X = df[['income', 'spending']]
    # Create a KMeans model to group the data into 'n' clusters
    model = KMeans(n_clusters=n)
    model.fit(X)  # Fit the model to the data (this does the clustering)
    df['cluster'] = model.labels_  # Add the cluster labels to the DataFrame


def main():
    df = pd.read_csv('Day14/mall_customers.csv')
    df.columns = ['id', 'gender', 'age', 'income',
                  'spending']  # Give meaningful column names

    cluster(df, 5)  # Perform clustering with 5 clusters
    plot(df)  # Create the scatter plot


main()
