import pandas as pd
import random

# Generate random data for the CSV
num_records = 500  # Number of customers

# Generate random data for airline customers
data = {
    'id': [i for i in range(1, num_records + 1)],
    'gender': [random.choice(['Male', 'Female']) for _ in range(num_records)],
    'age': [random.randint(18, 80) for _ in range(num_records)],
    # Number of flight hours per year
    'flight_hours': [random.randint(10, 200) for _ in range(num_records)],
    # Spending in dollars
    'annual_spending': [random.randint(500, 25000) for _ in range(num_records)],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('airline_customers.csv', index=False)

print("CSV file 'airline_customers.csv' generated successfully!")
