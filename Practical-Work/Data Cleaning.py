import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values, duplicates, and outliers
data = {
'ID': [1, 2, 3, 4, 5, 2, 6],
'Date': ['2022-01-01', '2022-02-15', '2022-03-20', '2022-04-10', '2022-05-05', '2022-02-15', '2022-06-30'],
'Sales': [1000, 1500, np.nan, 2000, 1800, 1500, 2500]
}
df = pd.DataFrame(data)

# Handling missing values
df.dropna(inplace=True)
#df.fillna(df.mean(), inplace=True) # Uncomment to replace missing values with mean

# Correcting data formats
df['Date'] = pd.to_datetime(df['Date'])

# Dealing with duplicates
df.drop_duplicates(subset=['ID'], keep='first', inplace=True)

# Handling outliers (use appropriate method)

print(df) 