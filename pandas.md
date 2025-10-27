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




