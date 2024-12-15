import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load preprocessed data
df = pd.read_csv('processed_data.csv')

# Train model
X = df[['Humidity', 'Wind Speed']]  # Example features
y = df['Temperature']
model = LinearRegression()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
