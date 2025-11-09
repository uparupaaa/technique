overwrite data
```
df.loc[select rows, select columns] = x
df.loc[df['Age'].isnull(), 'Age'] = x
```

replace by dict(a -> dict[a])
```
df = df[col].map(dict)
df = df[col].replace(dict)
df = df[col].apply(lambda x: dict.get(x, np.nan))
```

copy
```
df_copy = df.copy(deep=True)
```

rename columns
```
df = df.rename(columns={'A': 'col1', 'B': 'col2'})
```

select data which dtype is float
```
float_cols = df.select_dtypes(include=['float'])
```

merge
```
merged = pd.merge(df1, df2, on='id', how='inner', suffix=('_left', '_right'))
how
  inner: keep only matcing rows(default)
  left: keep all rows from left dataframe
  right: keep all rows from right dataframe
  outer: keep all rows from both dataframes

merged = df1.join(df2, on='key')

merged = pd.concat([df1, df2, ...], axis=1)
if axis=0, concat direction is 
```

append row
```
new_row = pd.DataFrame([4, 5, 6], columns=['a', 'b', 'c'])
X = pd.concat([X, new_row], ignore_index=True)
```

create dataframe
```
row = 2D list or a value
df = pd.DataFrame(row, index=range(100), columns=cols)
```





