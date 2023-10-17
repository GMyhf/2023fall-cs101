# Todo: 2023/10/17 Tuesday 贪心和矩阵

2023年10月份，主要是掌握矩阵、贪心题目，最好能涉及到简单的DP题目。

==内容较多，但是不会拖堂，到时间就下课。==

**Sortings**: 可以按照greedy来理解，因为都有不同的优化策略

​	bubble sort, insert, selection sort, merge sort, quicksort

**Regular expression**: 

​	04015: 邮箱验证，24834:通配符匹配，58A. Chat room。不做要求，会了可以用。

​	LeetCode 65. 有效数字，https://leetcode.cn/problems/valid-number/description/

​	Regulex 正则表达式在线测试工具，https://regex101.com

**Greedy**: 

​	01017:装箱问题，25353:排队，12559: 最大最小整数 v0.3。					加点题目。。

​	==two pointers通常是greedy？==，例如：CF1364A. A. XXXXX

​	==二分查找通常也是greedy？感觉所有题目都是搜索/遍历，考虑优化的都是贪心？==

**程序生成测试数据**: 

​	26971:分发糖果，26976:摆动序列。这两个题目也是 greedy

​	CF1868A. Fill in the Matrix, tags: constructive algorithms （If there are multiple solutions, you may output any of them. 多解的题目需要spj来处理，special judge）

**Matrices**: 

​	保护圈，for loop中 range 中使用 min、max 避免越界

​	02659:Bomb Game，04133:垃圾炸弹。								加些简单题目。。。

**DP的影子**：

​	优化问题除了使用时间复杂度更低的算法（如：线性筛/欧拉筛），还可以用DP。

​	CF230B. T-primes，02810: 完美立方。 from functools import lru_cache; lru_cache(maxsize = None) 

​	==greedy题目都可以用dp来完成？==



## Sortings



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231015120308973.png" alt="image-20231015120308973" style="zoom: 50%;" />



https://stackoverflow.com/questions/47238823/why-selection-sort-is-not-greedy

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231015120427880.png" alt="image-20231015120427880" style="zoom:50%;" />



## Regular expression

### 04015: 邮箱验证

题目给的要求是\[\^@\.]，也就是说正常字段只需要不是“@”和“.”即可。以前遇到的要求是：正常字段只能是大小写字母或“-”，所以也试了试[\w-]。虽然regulation需要前后match，也就是说前面加一个“^”，后面加一个“$”， 但 是.match函数本身就是从头开始检索的，所以“^”可以删去。

```python
# https://www.tutorialspoint.com/python/python_reg_expressions.htm
# https://www.geeksforgeeks.org/python-regex/

import re
while True:
    try:
        s = input()
        reg = r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$'
        print('YES' if re.match(reg, s) else 'NO')
    except EOFError:
        break
```



```python
# https://www.tutorialspoint.com/python/python_reg_expressions.htm
# https://www.geeksforgeeks.org/python-regex/
import re  
while True: 
    try:
        s = input()
        reg   = r'[^@\.]+(\.[^@\.]+)*@[^@\.]+(\.[^@\.]+)+$'
        print('YES' if re.match(reg, s) else 'NO')
    except EOFError:
        break
```



### 24834:通配符匹配

```python
#23n2300017735(夏天明BrightSummer)
import re

for i in range(int(input())):
    s, p = input(), input().replace("?", ".{1}").replace("*", ".*") + "$"
    print("yes" if re.match(p, s) else "no")
```



### 58A. Chat room

```python
import re
s = input()
r = re.search('h.*e.*l.*l.*o', s)
print(['YES', 'NO'][r==None])
```



### LeetCode 65. 有效数字

https://leetcode.cn/problems/valid-number/description/

https://leetcode.cn/problems/valid-number/solutions/564188/you-xiao-shu-zi-by-leetcode-solution-298l/

这个正则表达式 pattern 用于判断一个字符串是否是有效数字。下面我来详细解释一下其中的各个部分：

- `^` 表示匹配字符串的开始位置。
- `[-+]?` 表示一个可选的符号字符，可以是正号 `+` 或负号 `-`。
- `(\d+(\.\d*)?|\.\d+)` 表示有效数字的主要部分，可以分成三种情况：
  - `\d+(\.\d*)?` 表示至少一位数字，后面可选的小数部分，小数部分可以没有或有多个小数位。
  - `|` 表示或的关系。
  - `.\d+` 表示以点 `.` 开始，后面至少一位数字的小数形式。
- `([eE][-+]?\d+)?` 表示指数部分，也是一个可选项，可以是 `e` 或 `E` 开头，后面可选的符号字符，以及至少一位数字。
- `$` 表示匹配字符串的结束位置。

综合起来，整个正则表达式可以解释为：

- 首先可以匹配一个可选的符号字符。
- 接下来是有效数字的主要部分，可以是整数或小数形式。
- 最后是可选的指数部分。

因此，该正则表达式可以匹配符合有效数字要求的字符串。在 Python 中使用 `re.match` 方法进行匹配时，如果匹配成功，说明字符串是一个有效数字，返回 `True`；否则，返回 `None`，表示不是一个有效数字。

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        import re 
        pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
        
        ans = re.match(pattern, s) 
        if ans is not None:
            return True
        else:
            return False
```





## Greedy

### 01017:装箱问题

直接用总数把bcdef占的位置都减掉就可以了，思路就清晰起来了。**运用列表，避免多个 if else。

```python
import math
rest = [0,5,3,1]

while True:
    a,b,c,d,e,f = map(int,input().split())
    if a + b + c + d + e + f == 0:
        break
    boxes = d + e + f           #装4*4, 5*5, 6*6
    boxes += math.ceil(c/4)     #填3*3
    spaceforb = 5*d + rest[c%4] #能和4*4 3*3 一起放的2*2
    if b > spaceforb:
    	boxes += math.ceil((b - spaceforb)/9)
    spacefora = boxes*36 - (36*f + 25*e + 16*d + 9*c + 4*b)     #和其他箱子一起的填的1*1
    
    if a > spacefora:
        boxes += math.ceil((a - spacefora)/36)
    print(boxes)
```



### 25353:排队

```python
N, D = map(int, input().split())
height = [0]*N
check = [False]*N
for i in range(N):
    height[i] = int(input())

height_new = []
while False in check:
    i, l = 0, len(height)
    buffer = []
    while i < l:
        if check[i]:
            i += 1
            continue
        if len(buffer) == 0:
            buffer.append(height[i])
            maxh = height[i]
            minh = height[i]
            check[i] = True
            continue

        maxh = max(height[i], maxh)
        minh = min(height[i], minh)
        if maxh-height[i] <= D and height[i]-minh <= D:
            buffer.append(height[i])
            check[i] = True
        i += 1
    buffer.sort()
    height_new.extend(buffer)

print(*height_new, sep='\n')
```



### 12559: 最大最小整数 v0.3

greedy/strings/sortings, http://cs101.openjudge.cn/practice/12559

思路：先拼接出最小值：即字典序最小；要保证每一个小的字符串，左移到合适位置，需要两两比较（刚好是冒泡排序）。这个题目是个不容易的，字符串处理题目。

求minimum时，对相邻两strA[k]与A[k+1]，比较A[k]+A[k+1]与A[k+1]+A[k]的大小，若A[k+1]+A[k]大，颠倒A[k]与A[k+1]；最多交换len(A)-1次。求maximum时，颠倒求minimum时的有序序列即可。使用冒泡排序，循环(n-1)次。

把这些数当成字符串处理，然后采用类似冒泡排序的做法排出大小。

```python
n = int(input())
nums = input().split()
for i in range(n - 1):
    for j in range(i+1, n):
        #print(i,j)
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

ans = "".join(nums)
nums.reverse()
print(ans + " " + "".join(nums))
```





### CF1364A. A. XXXXX

https://codeforces.com/problemset/problem/1364/A



## 程序生成测试数据

### 26971:分发糖果



```python
import random
import time

random.seed(0)

for epoch in range(20):
    n = random.randint(10 + epoch * 2, 900 + 200 * (epoch // 2) ** 2)
    nums = [random.randint(0, 800 + 200 * (epoch // 2) ** 2 ) for _ in range(n)]
    inlines = [f'{n}\n'] + [' '.join([str(num) for num in nums]) + '\n']
    
    with open(f'data/{epoch}.in', 'w') as f:
        f.writelines(inlines)

    def candy(ratings):
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
    
        right = ret = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)
    
        return ret

    #input()
    #*nums, = map(int, input().split())
    start = time.time()
    ans = candy(nums)
    end = time.time() - start

    print(f"[{epoch}] {end:.3f}sec")
    print(ans)

    with open(f'data/{epoch}.out', 'w') as f:
        f.writelines([str(ans) + '\n'])
```



### 26976:摆动序列

```python
import random
import time

random.seed(0)

for epoch in range(20):
    n = random.randint(1, min(1000, 10 + epoch*50))
    nums = [random.randint(0, 1000 ) for _ in range(n)]
    inlines = [f'{n}\n'] + [' '.join([str(num) for num in nums]) + '\n']

    with open(f'data/{epoch}.in', 'w') as f:
        f.writelines(inlines)

    def wiggleMaxLength(nums):
        n = len(nums)
        if n < 2:
            return n
        
        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff
        
        return ret
    

    #input()
    #*nums, = map(int, input().split())
    start = time.time()
    ans = wiggleMaxLength(nums)
    end = time.time() - start
    
    print(f"[{epoch}] {end:.3f}sec")
    print(ans)
    
    with open(f'data/{epoch}.out', 'w') as f:
        f.writelines([str(ans) + '\n'])
```



![image-20231015123114430](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231015123114430.png)



## Matrices

保护圈，range中min、max



### 02659:Bomb Game



### 04133:垃圾炸弹，



## DP的影子

### CF230B

​	求解素数的三种方法，包括：试除法（trial division）、埃氏筛（Sieve of Eratosthenes）、欧拉筛（Sieve of Euler，线性法），https://blog.dotcpp.com/a/69737

@lru_cache(maxsize = None) 



除余法，pypy3可以AC 230B。lru_cache 如果屏蔽了，超时。

![image-20231015122106014](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231015122106014.png)

```python
import math
from functools import lru_cache 

@lru_cache(maxsize = None) 
def prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

input()

*a, = map(int, input().split())
ans = []
for i in a:
    if i == 1:
        ans.append('NO')
        continue
    tmp = int(math.sqrt(i))
    if tmp**2 != i:
        ans.append('NO')
        continue
    
    if prime(tmp):
        ans.append('YES')
    else:
        ans.append('NO')

print('\n'.join(ans))
```



### 02810: 完美立方

1）lru_cache 有作用，时间接近先算好的方法。完美立方，http://cs101.openjudge.cn/practice/02810/  2）今天课件里面用lru_cache的程序没有写对，因为它对函数的参数起缓存作用，所以作用的函数一定要有参数。

![image-20231015122235199](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231015122235199.png)

