```
from pathlib import PATH
p = Path('/Users/you/Documents/example.txt')
print(p.name)  #example.txt
print(p.parent)  #/Users/you/Documents
print(p.exists())  #True or False
````

```
import os
p = Path('/Users/you/Documents/example.txt')
print(os.path.basename(p))  #example.txt
print(os.path.dirname(p))  #/Users/you/Documents
print(os.path.exists(p))  #True or False
```

