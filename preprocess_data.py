import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('raw_data.csv')

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Normalize numerical fields
scaler = StandardScaler()
df[['Temperature', 'Wind Speed']] = scaler.fit_transform(df[['Temperature', 'Wind Speed']])

# Save processed data
df.to_csv('processed_data.csv', index=False)
