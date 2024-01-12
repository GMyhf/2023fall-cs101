# CS101 Cheat_Sheet_Edition_3

2023.12.26 compiled by 23工院 武昱达

改正了欧拉筛；

加入了排列组合、阶乘、笛卡尔积等内容

# **一、语法糖**和常用函数

## Part 1

```python
"""语法糖和常用函数"""
print(bin(9)) #bin函数返回二进制，形式为0b1001
dict.items()#同时调用key和value
print(round(3.123456789,5)# 3.12346
print("{:.2f}".format(3.146)) # 3.15
a,b=b,a
dict.get(key,default=None) # 其中，my_dict是要操作的字典，key是要查找的键，default是可选参数，表示当指定的键不存在时要返回的默认值
ord() # 字符转ASCII
chr() # ASCII转字符
for index,value in enumerate([a,b,c]): # 每个循环体里把索引和值分别赋给index和value。如第一次循环中index=0,value="a" 
```

## Part 2

```python
# 二进制转十进制
binary_str = "1010"
decimal_num = int(binary_str, 2) # 第一个参数是字符串类型的某进制数，第二个参数是他的进制，最终转化为整数
print(decimal_num)  # 输出 10
```

## Part 3 字符串格式化

```python
# %格式化语法：
"%[(name)][flags][width][.precison]type" % 待格式化数据
参数：
format()是python的一个内置函数，其使用频率不高，语法和str.format()大同小异，可以结合lambda函数使用或在其它一些特定情况下使用。 左对齐，正数无符号，负数加负号;
    3) 空格: 右对齐(默认的对齐方式)，正数前加空格，负数前加负号;
    4) 0: 右对齐，以0填充，正数无符号，负数加负号，并将符号放置在0最左侧;
(4) width: 占位宽度, 若指定宽度小于原数据长度则按原长度数据输出;
(5) .precison: 小数点后保留位数；在字符串中则表示截取/字符串切片;
type:
(1) s: string, 字符串;
(2) d: decimal integer, 十进制数;
(3) i: integer, 用法同%d;
(4) u: unsigned integer, 无符号十进制数;
(5) f: float, 浮点数(默认保留小数点后6位);
(6) F: Float, 浮点数(默认保留小数点后6位);
(7) e: exponent, 将数字表示为科学计数法(小写e, 默认保留小数点后6位);
(8) E: Exponent, 将数字表示为科学计数法(大写E, 默认保留小数点后6位);
(9) o: octal, 八进制数(即0-7);
(10) x: hexdecimal, 十六进制数(即0-9a-f);
(11) X: Hexdecimal, 十六进进制数(0-9A-F);
(12) g: general format, 通用格式，详见如下...;
(13) G: General format, 通用格式，详见如下...;
(14) %c: character, 将十进制数转换为所对应的unicode值;
(15) %r: representation, 调用__repr__魔法方法输出;
(16) %%: 转义%，输出百分号。

# str.format( )语法：
"{[index][:[[fill]align][sign][#][0][width][grouping_option][.precision][type]]}".format()
(1) index: 待格式化字符的索引或键，若占位符数量和参数数量不一致时必须指定索引;
(2) fill: 填充字符，可为任意字符;
(3) align: 对齐方式(常配合width使用)，可选:
 # 和Excel中输入文本和数字的默认对齐方式一致
    1) <: 左对齐(字符串默认对齐方式);
    2) >: 右对齐(数字默认对齐方式);
    3) ^: 居中对齐;
    4) =: 内容右对齐，将符号(+或-)放置在填充字符的左侧，仅对数字类型有效;
(4) sign: 有无符号，可选：
    1) +: 正数加正号，负数加负号；
    2) -: 正数不变，负数加负号(默认)；
    3) 空格: 正数加空格，负数加负号；
(5) #:  
       a. 对于整数，在输出值分别添加响应的0b, 0o, 0x前缀;
       b. 对于浮点数和复数, 在输出值保留小数点符号;
       c. 在g/G模式下，保留末尾的0；
(6) 0: 若未设置对齐方式，在width前加一个0将为数字类型启用感知正负号的零填充，等同于设置fill为0, align为"=";
(7) width: 字段总宽度(十进制整数), 所有前缀，分隔符和其它格式化字符之和;  
(8) grouping_option: 设置分组(分隔):
       1) ",": 使用逗号作为千位分隔符;
       2) "_": 使用_作为分隔符:
          a. 对于十进制数, 使用_作为千位分隔符;
          b. 对于b, o, x/X，使用_每4位数插入一个下划线；
(9) .precision(十进制数):  
       a. 整数型不允许设置precison, 如果设置即被转换为浮点数;
       b. 浮点型表示小数点"后"显示多少位小数位数;
       c. 以g或G格式化表示在小数点"前后"共显示多少个数位;
       d. 字符型表示截取多少个字符；
(10) {{或}}: 转义{或}，当需要输出{或}的使用使用;
(11) type: 详见如下...
```

# **二、工具**

## 1. **素数筛**

写法1（欧拉筛）：

```python
def Euler_sieve(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    primes[0]=primes[1]=False
    return primes
print(Euler_sieve(20))
# [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False]
```

写法2（埃氏筛）：

```python
# 胡睿诚 23数院 
# 埃氏筛 基本够用
N=20
primes = []
is_prime = [True]*N
is_prime[0] = False;is_prime[1] = False
for i in range(1,N):
    if is_prime[i]:
        primes.append(i)
        for k in range(2*i,N,i): #用素数去筛掉它的倍数
            is_prime[k] = False
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19]
```

写法3（欧拉筛）：

```python
# 胡睿诚 23数院 
N=20
primes = []
is_prime = [True]*N
is_prime[0] = False;is_prime[1] = False
for i in range(2,N):
    if is_prime[i]:
        primes.append(i)
    for p in primes: #筛掉每个数的素数倍
        if p*i >= N:
            break
        is_prime[p*i] = False
        if i % p == 0: #这样能保证每个数都被它的最小素因数筛掉！
            break
print(primes)
# [2, 3, 5, 7, 11, 13, 17, 19]
```



## 2. 简单题可以多循环（提醒）

例：完美立方

```python
x=int(input())
cube=[i**3 for i in range(x+1)]
for a in range(3,x+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if cube[a] ==cube[b]+cube[c]+cube[d]:
                    print("Cube = "+str(a)+", Triple = ("+str(b)+","+str(c)+","+str(d)+")")

#以下是第二种优化方案
n=int(input())
import math
for a in range(2,n+1):
    for b in range(2,int(math.pow(a**3/3,1/3))+1):
        for c in range(b,int(math.pow(a**3/2,1/3))+1):
            for d in range(c,a):
                if a**3==b**3+c**3+d**3:
                    print('Cube = '+str(a)+', Triple = ('+str(b)+','+str(c)+','+str(d)+')')
```

## 3. 拓展包

### （1） math

```python
import math
print(math.ceil(1.5)) # 2
print(math.floor(1.5)) # 1
print(math.pow(2,3)) # 8.0
print(math.pow(2,2.5)) # 5.656854249492381
print(9999999>math.inf) # False
print(math.sqrt(4)) # 2.0
print(math.log(100,10)) # 2.0  math.log(x,base) 以base为底，x的对数
print(math.comb(5,3)) # 组合数，C53
print(math.factorial(5)) # 5！
```

### （2） lru_cache

```python
# 需要注意的是，使用@lru_cache装饰器时，应注意以下几点：
# 1.被缓存的函数的参数必须是可哈希的，这意味着参数中不能包含可变数据类型，如列表或字典。
# 2.缓存的大小会影响性能，需要根据实际情况来确定合适的大小或者使用默认值。
# 3.由于缓存中存储了计算结果，可能导致内存占用过大，需谨慎使用。
# 4.可以是多参数的。
```

### （3）bisect（二分查找）

```python
import bisect
sorted_list = [1,3,5,7,9] #[(0)1, (1)3, (2)5, (3)7, (4)9]
position = bisect.bisect_left(sorted_list, 6)
print(position)  # 输出：3，因为6应该插入到位置3，才能保持列表的升序顺序

bisect.insort_left(sorted_list, 6)
print(sorted_list)  # 输出：[1, 3, 5, 6, 7, 9]，6被插入到适当的位置以保持升序顺序

sorted_list=(1,3,5,7,7,7,9)
print(bisect.bisect_left(sorted_list,7))
print(bisect.bisect_right(sorted_list,7))
# 输出：3 6
```

### （4）年份calendar包

```python
import calendar
print(calendar.isleap(2020)) # True 判断闰年
```

### （5）heapq 优先队列

```python
import heapq # 优先队列可以实现以log复杂度拿出最小（大）元素
lst=[1,2,3]
heapq.heapify(lst) # 将lst优先队列化
heapq.heappop(lst) # 从队列中弹出树顶元素（默认最小，相反数调转）
heapq.heappush(lst,element) # 把元素压入堆中
```

### （6）Counter包

```python
from collections import Counter 
# O(n)
# 创建一个待统计的列表
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# 使用Counter统计元素出现次数
counter_result = Counter(data) # 返回一个字典类型的东西
# 输出统计结果
print(counter_result) # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(counter_result["apple"]) # 3
```

### （7）default_dict

defaultdict是Python中collections模块中的一种数据结构，它是一种特殊的字典，可以为字典的值提供默认值。当你使用一个不存在的键访问字典时，defaultdict会自动为该键创建一个默认值，而不会引发KeyError异常。

defaultdict的优势在于它能够简化代码逻辑，特别是在处理字典中的值为可迭代对象的情况下。通过设置一个默认的数据类型，它使得我们不需要在访问字典中不存在的键时手动创建默认值，从而减少了代码的复杂性。

使用defaultdict时，首先需要导入collections模块，然后通过指定一个默认工厂函数来创建一个defaultdict对象。一般来说，这个工厂函数可以是int、list、set等Python的内置数据类型或者自定义函数。

```python
from collections import defaultdict
# 创建一个defaultdict，值的默认工厂函数为int，表示默认值为0
char_count = defaultdict(int)
# 统计字符出现次数
input_string = "hello"
for char in input_string:
    char_count[char] += 1
print(char_count)  # 输出 defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})）
```

## (8) itertools包 (排列组合等)

```python
import itertools
my_list = ['a', 'b', 'c']
permutation_list1 = list(itertools.permutations(my_list))
permutation_list2 = list(itertools.permutations(my_list, 2))
combination_list = list(itertools.combinations(my_list, 2))
bit_combinations = list(itertools.product([0, 1], repeat=4)) #repeat=n：在笛卡尔积的所有结果中任取n个合并

print(permutation_list1)
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
print(permutation_list2)
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
print(combination_list)
# [('a', 'b'), ('a', 'c'), ('b', 'c')]
print(bit_combinations)
# [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]
```

## 4.ASCII表

![image-20231227232511477](C:\Users\86181\AppData\Roaming\Typora\typora-user-images\image-20231227232511477.png)

## 5. 判断完全平方数

```python
import math
def isPerfectSquare(num):
    if num < 0:
        return False
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num
print(isPerfectSquare(97)) # False
```



# 三、递归与DFS（常用模版）

由于是按照个人习惯写的，可能与标准模板差异比较大。

## **1. 八皇后的回溯算法：**

```python
# 王铭健，工学院 2300011118
sol_list = []


def dfs(n, path="", row=0, columns_selected=[], diag1=set(), diag2=set()):
    if row == n:
        sol_list.append(path)
        return
    for col in range(n):
        if col not in columns_selected and col-row not in diag1 and col+row not in diag2:
            dfs(n, path+str(col+1), row+1, columns_selected+[col], diag1|{col-row}, diag2|{col+row})


dfs(8)
n = int(input())
result = []
for i in range(n):
    b = int(input())
    result.append(sol_list[b - 1])
for j in result:
    print(j)

```

## **2. 最大通域面积（DFS）**

```python
def dfs(matrix,x,y,visited):
    #如果越界，或接触边界，或接触已经标记的点，立刻终止递归并返回0
    if (x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0])
            or matrix[x][y]!="W" or visited[x][y]):
        return 0
    visited[x][y]=True
    area=1
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        area += dfs(matrix, x + dx, y + dy, visited)
    return area
def max_adj_area(matrix):
    rows,cols=len(matrix),len(matrix[0])
    # visited 辅助空间
    visited=[[False for _ in range(cols)] for _ in range(rows)]
    max_area=0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]=="W" and not visited[row][col]:
                area=dfs(matrix,row,col,visited)
                max_area=max(max_area,area)
    return max_area
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    matrix_1=[input() for _ in range(N)]
    print(max_adj_area(matrix_1))
```

## 3. 迷宫路径（DFS）

```python
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(maze,x,y):
    global cnt
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if maze[nx][ny]=='e':
            cnt+=1
            continue

        if maze[nx][ny]==0:
            maze[x][y]=1
            dfs(maze,nx,ny)
            maze[x][y]=0
    return
n,m=map(int,input().split())
maze=[[-1]*(m+2)]
for _ in range(n):
    temp=[-1]+list(map(int,input().split()))+[-1]
    maze.append(temp)
maze.append([-1]*(m+2))
maze[1][1]="s"
maze[n][m]="e"
cnt=0
dfs(maze,1,1)
print(cnt)
```



## 4. I'm glad that I've had my flight——回溯

![image-20231228000127909](C:\Users\86181\AppData\Roaming\Typora\typora-user-images\image-20231228000127909.png)

# 四、dp问题

## **1. 斐波那契数列的简单dp（手动）**

```python
def Fplus(x):
    if x<=2:
        return 1
    else:
        if dp[x]!=-1:
            return dp[x]
        else:
            return Fplus(x-1)+Fplus(x-2)

lst_res=[]
for i in range(int(input())):
    n=int(input())
    dp=[-1 for _ in range(n+1)]
    temp=Fplus(n)
    lst_res.append(temp)
for i in lst_res:
    print(i)
```

## 2. 斐波那契数列的lru-cache_dp

```python
from functools import lru_cache
@lru_cache(maxsize=20)
def F(x):
    if x<=2:
        return 1
    else:
        return F(x-1)+F(x-2)
print(F(30))
```

## 3.最长上升子序列

令 dp[i]表示以 A[i]结尾的最长上升子序列长度(和最大连续子序列和问题一样,以 A[i]结尾是强制的要求)。这样对 A[i]来说就会有两种可能:
① 如果存在 A[i]之前的元素 $A[j] (j<i)$，使得 $A[j]<A[i]\ 且\ dp[j]+1> dp[i]$  (即把 A[i]跟在以 A[i]结尾的 LIS 后面时能比当前以 A[i]结尾的 LIS 长度更长)，那么就把 A[i]跟在以 A[i]结尾的LIS 后面，形成一条更长的上升子序列 (令 $dp[i]= dp[j]+1$)。 

② 如果 A[i]之前的元素都比 A[i]大，那么 A[i]就只好自己形成一条 LIS，但是长度为1，即这个子序列里面只有一个 A[i]。
最后以 A[i]结尾的 LIS 长度就是①②中能形成的最大长度。

由此可以写出状态转移方程:

$dp[i]= max(1,dp[i]+1), (j=1,2,...,i-1 \ \&\& \ A[j] < A[i])$

上面的状态转移方程中隐含了边界: $dp[i]=1 \ (1≤i≤n)$。显然 dp[i]只与小于i的j有关,因此只要让i从小到大遍历即可求出整个 dp 数组。由于 dp[i]表示的是以 A[i]结尾的LIS 长度，因此从整个 dp 数组中找出最大的那个才是要寻求的整个序列的 LIS 长度，整体复杂度为$O(n^2)$.

```python
n = int(input())
*b, = map(int, input().split())
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if b[j] < b[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# bisect写法
import bisect
n = int(input())
*lis, = map(int, input().split())
dp = [1e9]*n
for i in lis:
    dp[bisect.bisect_left(dp, i)] = i
print(bisect.bisect_left(dp, 1e8))
```

bisect用法，Maintain lists in sorted order, https://pymotw.com/2/bisect/

此处用bisect的想法是保证有序的情况下，在dp代表的子序列中不断用列表后面更小的值替代原来列表前面更大的值，如果出现一个比前面所有值都大的值则最长子序列长度+1。



最大上升子序列和与此题类似，只是转移方程为 dp[i] = max(dp[j]+a[i], dp[i])

## 4. 小偷背包（采药）

```python
# 动态规划之背包问题（算法图解书中例⼦实现）

# 1 二维数组
n, b = map(int, input().split())
price = [0] + [int(i) for i in input().split()]
weight = [0] + [int(i) for i in input().split()]
bag = [[0] * (b+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, b+1):
        if weight[i] <= j:
            bag[i][j] = max(price[i] + bag[i-1][j-weight[i]], bag[i-1][j])
        else:
            bag[i][j] = bag[i-1][j]
print(bag[-1][-1])

# 2 一维数组优化版
# 压缩矩阵/滚动数组 ⽅法
N,B = map(int, input().split())
*p, = map(int, input().split())
*w, = map(int, input().split())
dp=[0]*(B+1)
for i in range(N):
    for j in range(B, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j-w[i]]+p[i])
print(dp[-1])

#完全背包问题（必须装满）：二维数组中初值除dp[0][0] = 0 外其余均为无穷小 -float("inf") 即方案不合法
```

# 五、BFS

## 1. 寻宝 BFS

```python
#迷宫最短路径的BFS写法
# 苏王捷 23工院
# 武昱达注：用heapq替代了双向队列，用入堆模拟入队，用pop模拟出队。

import heapq
def bfs(x,y,matrix):
    # 定义步空间
    dx,dy=[1,0,-1,0],[0,1,0,-1]
    # 定义队列（heapq实现）和visited辅助空间
    queue,visited=[],set()
    heapq.heappush(queue,[0,x,y])
    visited.add((x,y))
    # while queue 队列非空则继续
    while queue:
        # 拆解当前访问坐标
        step,x,y=heapq.heappop(queue)
        # 当前访问元素的退出条件
        if matrix[x][y]==1:
            return step
        # 访问当前元素的比邻元素
        for i in range(4):
            # 取每种可能的下一步
            nx,ny=x+dx[i],y+dy[i]
            # 若不是障碍物且未经访问则入队
            if matrix[nx][ny]!=2 and (nx,ny) not in visited:
                heapq.heappush(queue,[step+1,nx,ny])
                visited.add((nx,ny))
    # 最终返回结果
    return "NO"

m,n=map(int,input().split())
matrix=[[2]*(n+2)]
for _ in range(m):
    matrix.append([2]+list(map(int,input().split()))+[2])
matrix.append([2]*(n+2))
print(bfs(1,1,matrix))
```

## 2.走山路BFS（带权最短路径）

用heapq解决。一定记得出队时再打标记！

```python
# 王铭健，工学院 2300011118
from heapq import heappush, heappop
m, n, p = map(int, input().split())
matrix = []
for i in range(m):
    matrix.append(list(input().split()))
start = []
end = []
for j in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    start.append((x1, y1))
    end.append((x2, y2))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def judge(x, y, in_queue):
    if 0 <= x < m and 0 <= y < n:
        return matrix[x][y] != "#" and not in_queue[x][y]
    return False


def bfs(x1, y1, x2, y2):
    in_queue = [[0] * n for _ in range(m)]
    in_queue[x1][y1] = 1
    queue = [(0, x1, y1)]
    while queue:
        front = heappop(queue)
        cost = front[0]
        xi = front[1]
        yi = front[2]
        in_queue[xi][yi] = 1
        if xi == x2 and yi == y2:
            return cost
        for i in range(4):
            tx = xi + dx[i]
            ty = yi + dy[i]
            if judge(tx, ty, in_queue):
                heappush(queue, (cost+abs(int(matrix[xi][yi]) - int(matrix[tx][ty])), tx, ty))
    return "NO"


result = []
for k in range(p):
    if matrix[start[k][0]][start[k][1]] == '#'\
       or matrix[end[k][0]][end[k][1]] == '#':
        result.append("NO")
    else:
        result.append(bfs(start[k][0], start[k][1], end[k][0], end[k][1]))
for t in result:
    print(t)
```

# 六、双指针

## 1.接雨水

![image-20231228135934854](C:\Users\86181\AppData\Roaming\Typora\typora-user-images\image-20231228135934854.png)

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        
        return ans
```

# 七、 逃生指南

## 1. 除法是否使用地板除得到整数？（否则 4/2=2.0）

## 2. 是否有缩进错误？

## 3. 用于调试的print是否删去？

## 4. 非一般情况的边界情况是否考虑？

## 5. 递归中return的位置是否准确？（缩进问题,逻辑问题）

## 6. 贪心是否最优？有无更优解？

## 7. 正难则反（参考 #蒋子轩 23工院# 乌鸦坐飞机）

## 8. 审题是否准确？ 是否漏掉了输出？（参考）

## 9.是否考虑了可能出现的空集情况或者只含一个元素的情况？

## 10.TLE时，是否可以减少循环次数？MLE时，是否可以压缩空间（减少数组的维数）？

## 11.四舍六入五双

精确n位数字或保留n位小数，采用如下的规则(以保留n位小数为例)：

a. 四舍: 保留n位小数，若第n+1位≤4, 则舍去;

b. 六入: 保留n位小数，若第n+1位≥6, 则第n位进1；

c. 五双: 保留n位小数，若第n+1位=5, 若 如果第n+1位后面没有任何数字, 则第n位数字为偶数就舍去n+1位，第n位数字为奇数则进1;

如果第n+1位后还存在不为0的任何数字，则第n位数字无论是奇数还是偶数都进1。

print("{:.2f}".format(1.125))需要保留两位小数(n=2)，则观察小数点后第二位数字2的后一位(n+1位)。第n+1为5，且5后没有其它数字，第n位2为偶数，所以直接舍去，故最后的结果为1.12。

****







