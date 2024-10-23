import pandas as pd
import random

# Data structure based on the screenshot and df.info() output
data = {
    'Days': list(range(1, 101)),  # Days from 1 to 100
    'Outlook': random.choices(['Sunny', 'Cloudy', 'Rainy'], k=100),
    'Temprature': random.choices(['Cold', 'Warm', 'Mild'], k=100),
    'Routine': random.choices(['Indoor', 'Outdoor'], k=100),
    'Wear Jacket?': random.choices(['Yes', 'No'], k=100)
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first few rows
print(df.head())

# Optionally save to CSV for further use
df.to_csv('tree_synthetic.csv', index=False)
