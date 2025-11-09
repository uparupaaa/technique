mse, rmse
```
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_pred, squared=False)
rmse = mean_squared_error(y_true, y_pred, squared=True)
```

LabelEncoder
```
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df[col] = le.fit_transform(df[col])
```

OrdinalEncoder
```
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(
    handle_unknown="use_encoded_value", unknown_value=3,
    max_categories=3, encoded_missing_value=4)
max_categories: consider frequency
```

train_test_split
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```





