import pandas as pd
import numpy as np

# Generate 10 evenly spaced numbers between -5 and 5
x = np.linspace(-5, 5, 10)

# Compute the y values by squaring the x values
y = x**4

# Create a DataFrame with the x and y values
df = pd.DataFrame({'x': x, 'y': y})

# Write the DataFrame to a CSV file
df.to_csv('data.csv', index=False)