'''
This program is a simple example of using KMeans clustering to group customers based on their Annual income and FlyingHours patterns, and then visualizing the results with a scatter plot. 
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def plot(df):
    fig = plt.figure(figsize=(16, 9))  # Creates a figure with specific size
    ax = fig.add_subplot()  # Adds a subplot (the area where the plot will appear)
    # Scatter plot with points colored by cluster
    ax.scatter(df['AnnualSpending'], df['FlyingHours'],
               c=df['cluster'], cmap='plasma')
    ax.set_xlabel('Annual Spending')  # Label the x-axis as 'AnnualSpending'
    ax.set_ylabel('Flying Hours')  # Label the y-axis as 'FlyingHours'
    plt.show()  # Show the plot on the scree


def cluster(df, n):
    # Select the 'AnnualSpending' and 'FlyingHours' columns for clustering
    X = df[['AnnualSpending', 'FlyingHours']]

    # Handle missing values by removing rows with missing data
    X = X.dropna()

    # Create a KMeans model to group the data into 'n' clusters
    model = KMeans(n_clusters=n)
    model.fit(X)  # Fit the model to the data (this does the clustering)

    # Assign the cluster labels back to the original dataframe
    df['cluster'] = model.labels_


def main():
    df = pd.read_csv('Day14/airline_customers.csv')

    # Check the column names in the dataset and adjust them if needed
    print(df.columns)  # This will help identify the correct column names

    # Assign meaningful column names if needed
    df.columns = ['id', 'gender', 'age', 'FlyingHours', 'AnnualSpending']

    cluster(df, 5)  # Perform clustering with 5 clusters
    plot(df)  # Create the scatter plot


main()
