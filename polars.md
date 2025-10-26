reading
```
df = pl.read_csv(path)
```

information(info() function doesn't exist in polars)
```
train.shape
train.columns
train.dtypes
train.null_count()

train.describe  # count, null count, mean, std, min, max, etc
```

delete missing values
```
df = df.drop_nulls() # delete columns
df = df.filter(pl.col(col).is_not_null()) # delete rows
```

count unique values
```
n_unique = df.select(pl.col(col).n_unique())
```

convert dtype from str to int
```
df = df.with_columns(
    pl.col(col).cast(pl.Int64, strict=False) for col, dtype in zip(df.columns, df.dtypes) if dtype==pl.String
)
# ignore missing values by strict=False
```

convert x to missing values
```
df = df.fill_null(x)
```

show data
```
df.head(10)
df.tail(10)
```

overwrite data
```
df = df.with_columns(
    pl.when(pl.col('Age').is_null())
      .then(pl.lit(df['Age'].mean()))
      .otherwise(pl.col('Age'))
      .round()
      .alias('Age'),

    pl.when(pl.col('Embarked').is_null())
      .then(pl.lit(df['Embarked'].mode()[0]))
      .otherwise(pl.col('Embarked'))
      .alias('Embarked')
)
```

replace by dict(a -> dict[a])
```
df = df.with_columns(
    pl.col('Color).replace(dict).alias('Color')
)
```



















