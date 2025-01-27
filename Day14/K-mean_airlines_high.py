'''
Steps:
1. Define what constitutes "high" values: You can decide the threshold for "high" spending and flying hours based on the data, such as using the mean, median, or a specific percentile (e.g., top 10% of values).
2. Filter data: Identify the rows that meet the criteria for "high" values.
3. Annotate points: Use ax.text() to display labels at those points.

'''


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def plot(df):
    fig = plt.figure(figsize=(16, 9))  # Creates a figure with specific size
    ax = fig.add_subplot()  # Adds a subplot (the area where the plot will appear)

    # Scatter plot with points colored by cluster
    scatter = ax.scatter(df['AnnualSpending'], df['FlyingHours'],
                         c=df['cluster'], cmap='plasma')

    ax.set_xlabel('Annual Spending')  # Label the x-axis as 'AnnualSpending'
    ax.set_ylabel('Flying Hours')  # Label the y-axis as 'FlyingHours'

    # Label high annual spending and flying hours points
    # You can adjust the thresholds based on your data or use percentiles.
    high_spending_threshold = df['AnnualSpending'].quantile(
        0.9)  # Top 10% for Annual Spending
    high_flying_hours_threshold = df['FlyingHours'].quantile(
        0.9)  # Top 10% for Flying Hours

    high_points = df[(df['AnnualSpending'] > high_spending_threshold) &
                     (df['FlyingHours'] > high_flying_hours_threshold)]

    for i, row in high_points.iterrows():
        ax.text(row['AnnualSpending'], row['FlyingHours'], 'High',
                fontsize=12, color='red', ha='center', va='center')

    plt.show()  # Show the plot on the screen


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
