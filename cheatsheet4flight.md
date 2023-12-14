# Cheatsheet for Book My Flight

Updated 1018 GMT+8 Dec 14, 2023

2023fall Hongfei Yan





Python Dictionary get() Method

return the value for the given key if present in the dictionary. If not, then it will return None (if get() is used with only one argument).

```python
d = {1: '001', 2: '010', 3: '011'}
# since 4 is not in keys, it'll print "False"
print(d.get(4, "False"))
```



Defaultdict provides a default value for the key that does not exists.

```python
from collections import defaultdict

d = defaultdict(int) 
L = [1, 2, 3, 4, 2, 4, 1, 2] 
for i in L:  
    # The default value is 0 
    d[i] += 1
print(d); print(d[7])
```



```python
from collections import defaultdict

d = defaultdict(list)

for i in range(5):
    for j in range(3):  # 追加多个项的循环
        d[i].append(i + j)

print(d)
#Output: defaultdict(<class 'list'>, {0: [0, 1, 2], 1: [1, 2, 3], 2: [2, 3, 4], 3: [3, 4, 5], 4: [4, 5, 6]})
```

