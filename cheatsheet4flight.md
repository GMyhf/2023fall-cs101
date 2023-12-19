# Cheatsheet for Book My Flight

Updated 1441 GMT+8 Dec 19, 2023

2023fall Hongfei Yan



# dictionary

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



# str

在**字典顺序**中，每个元素的位置是根据它们在字典或词典中的排序来确定的。排序规则通常是按照字符的ASCII码进行比较。

对于数字字符串来说，数字字符的ASCII码是按照从小到大的顺序排列的。因此，在按字典顺序排序时，数字字符串中的数字尽量小的将被放在前面。

举个例子，考虑以下字符串列表：["4", "2", "10", "1", "3"]。按照字典顺序排序后的结果会是：["1", "10", "2", "3", "4"]。

需要注意的是，对于整数类型的数字排序时，会按照数值的大小进行比较，而不是按照它们的ASCII码。例如，整数列表[4, 2, 10, 1, 3]按照字典顺序排序后的结果会是：[1, 2, 3, 4, 10]。

```python
b =  ["4", "2", "10", "1", "3"]
print(sorted(b))
# ['1', '10', '2', '3', '4']

a =  [4, 2, 10, 1, 3]
print(sorted(a))
# [1, 2, 3, 4, 10]

```



> dir(str)
>
> help(str.upper)

upper(self, /)
    Return a copy of the string converted to uppercase.

lower(self, /)

replace(self, old, new, count=-1, /)
    Return a copy with all occurrences of substring old replaced by new.

zfill(self, width, /)
    Pad a numeric string with zeros on the left, to fill a field of the given width.

split(self, /, sep=None, maxsplit=-1)
    Return a list of the substrings in the string, using sep as the separator string.

find(...)
    S.find(sub[, start[, end]]) -> int

> Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation.
>
> Return -1 on failure.

strip(self, chars=None, /)
    Return a copy of the string with leading and trailing whitespace removed.

count(...)
    S.count(sub[, start[, end]]) -> int



chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

ord(c, /)
    Return the Unicode code point for a one-character string.





from functools import lru_cache

@lru_cache(maxsize=None)



import sys
sys.setrecursionlimit(1<<30)



product(*iterables, repeat=1) --> product object
 |  
 |  Cartesian product of input iterables.  Equivalent to nested for-loops.
 |  
 |  For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
 |  The leftmost iterators are in the outermost for-loop, so the output tuples
 |  cycle in a manner similar to an odometer (with the rightmost element changing
 |  on every iteration).
 |  
 |  To compute the product of an iterable with itself, specify the number
 |  of repetitions with the optional repeat keyword argument. For example,
 |  product(A, repeat=4) means the same as product(A, A, A, A).
 |  
 |  product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
 |  product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...



02811: 熄灯问题

from itertools import product

product(range(2), repeat=6) --> (0, 0, 0, 0, 0, 0) (0, 0, 0, 0, 0, 1) (0, 0, 0, 0, 1, 0) (0, 0, 0, 0, 1, 1)...



```python
# 要按照指定长度生成字符串 'abcd' 的全排列
from itertools import permutations

string = 'abcd'
length = 3

result = list(permutations(string, length))
for perm in result:
    print(''.join(perm))
```



# math

math.sqrt

math.ceil

math.floor

math.log2

math.log10

math.gcd



04036:计算系数

```python
import math
a, b, k, n, m = map(int, input().split());
print((pow(a, n, 10007) * pow(b, m, 10007) * math.comb(k, m)) % 10007)
```

