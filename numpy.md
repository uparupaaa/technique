create random data
```
np.random.choice(a, b, replace=True, p=[1, 1, ...)
a: list or integer(if 10, create 0-9 integer)
b: size
replace: same element can appear multiple times or not
p: weight
```

create np.array
```
np.array(list)
np.full((a, b), c, dtype=float) => a*b array, value=c
```

serch indices of non_zero values
```
 idx = np.nonzero(list)
list: [0, 2, 0, 5, 0] -> output: array([1, 3])
```

transpose list
```
np.transpose(list)
```
 
create random dataset
```
X = np.random.randn(100, 5)   # 100 samples, 5 features
y = np.random.randint(0, 2, 100)  # 0 or 1
```

