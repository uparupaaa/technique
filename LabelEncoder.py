from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Example data
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'blue']
})

# Initialize encoder
le = LabelEncoder()

# Fit and transform
df['color_encoded'] = le.fit_transform(df['color'])

print(df)
