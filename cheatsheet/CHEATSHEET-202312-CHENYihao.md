# CHEAT SHEET

## 宇宙安全声明

```python
from functools import lru_cache 
@lru_cache(maxsize = 128) +函数

import sys
sys.setrecursionlimit(1 << 30)

import sys
input == sys.stdin.readline
+加快读取速度

import heapq  # 堆
import itertools  # 非必要不要用这个，容易TLE
from collections import deque  # 双向队列 popleft()
import re  # 处理去吧
？*+{7}{2, }{2, 6}(ab)+|[abc]+###abc aabbcc\[^0-9]
\d\D\w\W\s\S\b\B.\.^$
from collections import defaultdict  # 一个默认有返回值的dict，有时很好用
defaultdict(int)  # values为int类
```

```python
# 素数可以可用于3个因子，可以用于一些奇怪要求的题目
# 完全平方数的因子是奇数个，其他是偶数个
# 欧拉筛
import math
n = int(1e5)
ans = [False]*(n+1)
ans[1] = True
ans_list = []
for i in range(2,int(math.sqrt(n+1)+1)):
  if not ans[i]:
    for j in range(i**2,n+1,i):
      ans[j]= True
for i in range(2,n+1):
  if not ans[i]:
    ans_list.append(i)
print(ans_list)
```

```python
print("%.2f" % (a/b))  #四舍五入算法
print(','.join(map(str, ans)))  #插入“，”
print(str(5).zfill(10))  #补足0
print(f'{a:5d}')
```

```python
def check(x):
    num, s = 1, 0
    for i in range(n):
        if s + expenditure[i] > x:
            s = expenditure[i]  # 装不了了
            num += 1  # 新开一个月
        else:
            s += expenditure[i]  # 向月里加天
    return [False, True][num > m]


def isvalid(former,row,col):
    for i in range(row):  # 肯定不共行，判断是否共列或共对角线
        if former[i] == col or abs(i-row) == abs(former[i]-col):
            return False
    return True


if 0 <= px <= w + 1 and 0 <= py <= h + 1 and (i, px, py) not in vis and matrix[py][px] != "X":
# 对于某个状态的时间，我们可以取模后作为 visited[x][y][time] 的第三个变量
```

```python
###MergeSort
def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    Mid = len(lists)//2
    Left_lists = MergeSort(lists[:Mid])
    Right_lists = MergeSort(lists[Mid:])
    return Merge(Left_lists,Right_lists)

def Merge(Left,Right):
    Sortedlist = []
    i,j = 0,0
    while i < len(Left) and j < len(Right):
        if Left[i]+Right[j] <= Right[j]+Left[i]:
            Sortedlist.append(Left[i])
            i += 1
        else:
            Sortedlist.append(Right[j])
            j += 1
    Sortedlist += Left[i:]
    Sortedlist += Right[j:]
    return Sortedlist
```

## 模拟类

#### 1883D. In Love 更新列表

```python
import sys
import heapq
from collections import defaultdict  # 这是一个特殊的dict，不存在的索引也不报错，而且可以返回一个初始值

input == sys.stdin.readline  # 提速-1

minH = []
maxH = []

ldict = defaultdict(int)  # 这里索引不存在时，返回的就是0，提速-2
rdict = defaultdict(int)  # 这里索引不存在时，返回的就是0，提速-3

n = int(input())

for _ in range(n):
    op, l, r = map(str, input().strip().split())
    l, r = int(l), int(r)
    if op == "+":
        ldict[l] += 1
        rdict[r] += 1
        heapq.heappush(maxH, -l)  # 提速-4
        heapq.heappush(minH, r)  # 维护maxH， minH，提速-5
    else:
        ldict[l] -= 1
        rdict[r] -= 1  # 维护maxH， minH 
    '''
    使用 while 循环，将最大堆 maxH 和最小堆 minH 中出现次数为 0 的边界移除。
    # 由于每次比的是最大最小项，故需要判断的是第一个出现次数非0的最大最小项
    通过比较堆顶元素的出现次数，如果出现次数为 0，则通过 heappop 方法将其从堆中移除。
    '''
    while len(maxH) > 0 >= ldict[-maxH[0]]:  # 0是maxH（存的是负数）中最大一项
        heapq.heappop(maxH)
    while len(minH) > 0 >= rdict[minH[0]]:  
        heapq.heappop(minH)
    '''
    判断堆 maxH 和 minH 是否非空，并且最小堆 minH 的堆顶元素是否小于
    最大堆 maxH 的堆顶元素的相反数。
    '''
    if len(maxH) > 0 and len(minH) > 0 and minH[0] < -maxH[0]:
        print("Yes")
    else:
        print("No")

# 左一定小于右，若有题中要求的结构，则有右小于左边，为什么不用最小的右边比较最大的左边呢？（反问）
# 同时要记得dict会减到0，及时删除0项
# 为什么不只保留最大值，最小值呢？因为如果被删除了就得找次小值，和次大值
# heap的好处，就是时刻维护一个最大值，但heap改变了索引，索引变得无序
# 但这里不需要考虑每组数据的位置，因为它删除的时候就告诉你位置，所以可以用字典来访问


```

#### 01922: Ride to School

反正最后和最快的一起到

```python
import math
while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    f = True
    for _ in range(n):
        v, t = map(int, input().split())
        if t < 0:
            continue
        if f:
            ans = (4.5/v) * 3600 + t
            f = False
        tmp = (4.5/v) * 3600 + t
        ans = min(ans,tmp)
    print(math.ceil(ans))  # 向上取整
```

#### 02692: 假币问题 一些简单的判断

```python
for _ in range(int(input())):
    L = [[],[],[]]
    for i in range(3):
        L[i] = input().split()
    for f in 'ABCDEFGHIJKL':
        if all((f in i[0] and i[2]=='up') or (f in i[1] and i[2]=='down') 
               or ( f not in i[0] + i[1] and i[2]=='even') for i in L):
            print("{} is the counterfeit coin and it is {}.".format(f,'heavy'))
            break
        if all((f in i[0] and i[2]=='down') or (f in i[1] and i[2]=='up') 
               or (f not in i[0]+i[1] and i[2]=='even') for i in L):
            print("{} is the counterfeit coin and it is {}.".format(f,'light'))
            break
```

#### 02746: 约瑟夫问题 queue排队枪毙

```python
from collections import deque
while True:
    n, m = map(int, input().split())
    if {n,m} == {0}:
        break
    monkey = deque(i for i in range(1, n+1))
    index = 0
    while len(monkey) != 1:
        temp = monkey.popleft()
        index += 1
        if index == m:
            index = 0
            continue
        monkey.append(temp) 
    print(monkey[0])
```

#### 23806：三数之和 第二遍的x既是中间的过程量也是最后一个遍历量

```python
"""
集合（set）可以自动去除重复的三元组，而查找的时间复杂度仍为O(1)，
并且空间复杂度也不会超过O(n)。
"""
def threeSum(nums):
    nums.sort()
    res = set()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        d = {}
        for x in nums[i + 1:]:
            if x not in d:
                d[-nums[i] - x] = 1
            else:
                res.add((nums[i], -nums[i] - x, x))
    return len(res)

n = list(map(int, input().split()))
print(threeSum(n))
```

#### 19948：英才施教——去掉最大的n个差值

#### 18182：打怪兽  —— 模拟

#### 买股票

#### *buy*\[*i*][*j*]=max{*buy*\[*i*−1][*j*],*sell*\[*i*−1][*j*]−*price*[*i*]}

#### *sell*\[*i*][*j*]=max{*sell*\[*i*−1][*j*],*buy*\[*i*−1][*j*−1]+*price*[*i*]}

由于在所有的 n 天结束后，手上不持有股票对应的最大利润一定是严格由于手上持有股票对应的最大利润的，然而完成的交易数并不是越多越好（例如数组 prices\textit{prices}prices 单调递减，我们不进行任何交易才是最优的），因此最终的答案即为 sell\[n−1][0..k]中的最大值

#### 1065：Wooden Sticks —— 也是个模拟，先sort依次去除，同一个长度就依次去除满足题意的棍子，并改变存值，记得加visited弱删除。再从头遍历。

#### 25566：CPU —— 大写入优先，小计算优先，因为计算累计的时间是一定的

写可以并行，优先选择写文件时间较长的进程，以减少总的等待时间。计算不能并行，ans1 += l\[i][0] 时间较短的进程应该尽早执行，以便尽快释放CPU资源。按照写文件时间（x[1]）降序排列，如果写文件时间相同，则按照计算时间（x[0]）升序排列。l.sort(key=lambda x: (-x[1], x[0]))

```python
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
l.sort(key=lambda x: (-x[1], x[0]))
ans1 = ans2 = 0
for i in range(n):
    ans1 += l[i][0]
    ans2 = max(ans2, ans1+l[i][1])  # 模拟，比较这时上一次写入结束时间和这次计算加写入时间
print(ans2）
```

#### 04144: 畜栏保留问题

greedy，模拟，每只奶牛不得不挤奶

```python
import heapq
num = 1
n = int(input())
cows = []
number = [0]*n  # 记录每一只牛所在的畜栏
for i in range(n):
    cows.append(list(map(int, input().split())))
for i in range(n):
    cows[i].append(i)  # 为每只牛添加编号后再排序

cows.sort(key=lambda x: x[0]) # 先按开始时间排序
column = []  # 创建列表【畜栏】
heapq.heappush(column, [cows[0][1], 0]) # 初始时只有一个元素，即为第一只牛的结束时间
number[cows[0][2]] = 1  # 第一只牛默认在第一个畜栏

for i in range(1, len(cows)):  # 对之后的每只牛遍历
    k = heapq.heappop(column)
    if k[0] < cows[i][0]: # 最早结束的已经结束，新的牛可使用该畜栏
        heapq.heappush(column, [cows[i][1], k[1]])
        number[cows[i][2]] = k[1]+1
    else:
        heapq.heappush(column, k)
        heapq.heappush(column, [cows[i][1], num])
        num += 1
        number[cows[i][2]] = num

print(len(column))  # 【畜栏】的长度即为畜栏数量
for i in number:
    print(i)
```

#### 1163B2. Cat Party (Hard Edition)

```python
#使用一个数组 f 来记录每种颜色出现的次数，使用另一个数组 cnt 来统计每个次数的颜色数量。
#通过迭代颜色列表，并根据不同的条件判断，计算并更新最长的连续天数 ans。

n = int(input())
colors = list(map(int, input().split()))

N = 10**5 + 10
ans = 0
mx = 0
f = [0] * N
cnt = [0] * N

for i in range(1, n + 1):
    color = colors[i - 1]
    cnt[f[color]] -= 1
    f[color] += 1
    cnt[f[color]] += 1
    mx = max(mx, f[color])
    ok = False
    if cnt[1] == i:  # every color has occurrence of 1
        ok = True
    elif cnt[i] == 1:  # only one color has the maximum occurrence and the occurrence is i
        ok = True
    elif cnt[1] == 1 and cnt[mx] * mx == i - 1:  # one color has occurrence of 1 and other colors have the same occurrence
        ok = True
    elif cnt[mx - 1] * (mx - 1) == i - mx and cnt[mx] == 1:  # one color has the occurrence 1 more than any other color
        ok = True
    if ok:
        ans = i
print(ans)
```

#### 04117:简单的整数划分问题（判断边界条件）

```python
def fun(n,m):
    if n == 1 or m == 1:
        return 1
    if n < m:
        return fun(n,n)
    if n == m:
        return fun(n,n-1) + 1
    if n > m:
        return fun(n-m,m) + fun(n,m-1)
while True:
    try:
        n = int(input())
    except EOFError:
        break

    print(fun(n,n))
```

#### 25561:2022决战双十一

```python
import math
n, m = map(int, input().split())
things = [[False for _ in range(m)] for _ in range(n)] ### [[False, False], [False, False]]
sale = [[] for _ in range(m)]
car = [0 for _ in range(m)]
#print(things)
#print(sale)

for i in range(n):
    temp = list(map(str, input().split()))
    for j in temp:
        store, price = map(int, j.split(':'))
        things[i][store-1] = price
#print(things)

for i in range(m):
    temp = list(map(str, input().split()))
    for j in temp:
        goal, temp_discount = map(int, j.split('-'))
        sale[i].append([goal, temp_discount])
#print(sale)

def discount(car):
    max_discount = 0
    for i_ in range(m):
        max_discount_temp = 0
        for j_ in sale[i_]:
            if car[i_] >= j_[0]:
                max_discount_temp = max(max_discount_temp,j_[1])
        max_discount += max_discount_temp
    return max_discount

minium = math.inf
def search(i, temp, things, sale):
    global minium
    if i == n:
        overall_discount = (temp//300)*50
        shop_discount = discount(car)
        minium = min(minium, temp-overall_discount-shop_discount)
    else:
        for j in range(m):
            if things[i][j]:
                car[j] += things[i][j]
                search(i+1, temp+things[i][j], things, sale)
                car[j] -= things[i][j]
search(0, 0, things, sale)
print(minium)
```

## 背包类

#### 输入模块

```python
Space,stuffNum = map(int,input().split())
worth, occupy = [0], [0]
for i in range(stuffNum):
    current_worth, current_occupy = map(int, input().split())
    worth.append(current_worth)
    occupy.append(current_occupy)
# print(worth)
```

#### 采药一维版

```python
dp = [0 for j in range(Space+1)]

for i in range(1, stuffNum+1):
    for j in range(Space,occupy[i]-1,-1):  # 反向
        if j >= occupy[i]:
            dp[j] = max(dp[j], dp[j-occupy[i]]+worth[i])
print(dp[Space])
```

#### 采药二维版

```python
dp = [[0 for j in range(T+1)] for i in range(M+1)]

for i in range(1, M+1):
    for j in range(1, T+1): 
        if j < cost[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]]+w[i])
print(dp[M][T])
```

#### 完全背包

```python
dp = [0 for j in range(Space+1)]

for i in range(1, stuffNum+1):
    for j in range(1,Space+1):
        if j % occupy[i] == 0:
            dp[j] = max(dp[j], dp[j-occupy[i]] + worth[i])
            print(dp)
print(dp[Space])
```

#### 多重背包(NBA)

```python
# 多重背包中的最优解问题
n = int(input())
if n % 50 != 0:
    print('Fail')
    exit()
n //= 50
nums = list(map(int, input().split()))
price = [1, 2, 5, 10, 20, 50, 100]
dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(7):
#for i in range(6, -1, -1):
    cur_price = price[i]
    cur_num = nums[i]
    k = 1
    while cur_num > 0:  #二进制分组优化，时间缩短了将近两个数量级。
      									#相同物品避免重复工作，「二进制分组」提高效率。
        use_num = min(cur_num, k)
        cur_num -= use_num
        for j in range(n, cur_price * use_num - 1, -1):
            dp[j] = min(dp[j], dp[j - cur_price * use_num] + use_num)
        k *= 2
if dp[-1] == float('inf'):
    print('Fail')
else:
    print(dp[-1])  # dp中包含了所有可能
```

## 双指针类（二分查找）

```python
import bisect
sorted_list = [1,3,5,7,9]  # [(0)1, (1)3, (2)5, (3)7, (4)9] 
position = bisect.bisect_left(sorted_list, 6)
print(position)  # 输出:3，因为6应该插入到位置3，才能保持列表的升序顺序

bisect.insort_left(sorted_list, 6)
print(sorted_list)  # 输出:[1, 3, 5, 6, 7, 9]，6被插入到适当的位置以保持升序顺序

sorted_list=(1,3,5,7,7,7,9) 
print(bisect.bisect_left(sorted_list,7)) 
print(bisect.bisect_right(sorted_list,7))  # 输出:3 6
```

#### 18211: 军备竞赛

类似二分双指针left, right，有钱就买（制作），没钱就卖。感谢2020fall-cs101 汤建浩，指正 cnt<0情况

#### 08210:河中跳房子

```python
L, n, m = map(int, input().split())
rock = [0]
for i in range(n):
    rock.append(int(input()))
rock.append(L)


def check(x):
    num = 0
    now = 0
    for i in range(1, n + 2):
        if rock[i] - now < x:  # 可去石头+1
            num += 1
        else:
            now = rock[i]  # 下一个石头

    return [False, True][num > m]


# lo, hi = 起点, 终点
lo, hi = 0, L + 1
ans = -1
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:  # 返回False，有可能是num==m
        ans = mid  # 如果num==m, mid就是答案
        lo = mid + 1

# print(lo-1)
print(ans)
```

#### 04135: 月度开销

在所给的N天开销中寻找连续M天的最小和，即为最大月度开销的最小值。

与 `OJ08210：河中跳房子`  一样都是二分+贪心判断，但注意这道题目是最大值求最小。

参考 bisect 源码的二分查找写法，两个题目的代码均进行了规整。
因为其中涉及到 num==m 的情况，有点复杂。二者思路一样，细节有点不一样。

```python
n, m = map(int, input().split())
expenditure = []
for _ in range(n):
    expenditure.append(int(input()))


def check(x):
    num, s = 1, 0
    for i in range(n):
        if s + expenditure[i] > x:
            s = expenditure[i]  # 装不了了
            num += 1  # 新开一个月
        else:
            s += expenditure[i]  # 向月里加天

    return [False, True][num > m]


lo = max(expenditure)
hi = sum(expenditure) + 1  # 绝对大值
ans = 1
while lo < hi:
####二分思路####
# print(lo)
print(ans)
```

## BFS

#### 走山路

```python
from heapq import heappop, heappush

### BFS ###
def bfs(x1, y1):
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 移动方向
    q = [(0, x1, y1)]  # 初始化堆
    v = set()  # 走过的路径
    while q:
        t, x, y = heappop(q)  # 省略建堆
        v.add((x, y))
        ### 终止条件 ###
        if x == x2 and y == y2:
            return t
        ### 移动方向 ###
        for dx, dy in dir:
        		# 这里把（x,y)因为的所有情况走完，因为是算高度差，所以一步走到已经是最优路径。
            nx, ny = x+dx, y+dy
            ### can——visit ###
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#' and (nx, ny) not in v:  # can_visit()模版，if不能则不返回堆
                nt = t + abs(int(matrix[nx][ny])-int(matrix[x][y]))  # 根据题意加上相对高度差
                heappush(q, (nt, nx, ny))  # bfs压入堆（每次处理优先处理当前最优解，但还是贪心）
    return 'NO'


### 主程序 ###
m, n, p = map(int, input().split())
matrix = [list(input().split()) for _ in range(m)]

for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    ### 预给终止条件 ###
    if matrix[x1][y1] == '#' or matrix[x2][y2] == '#':
        print('NO')
        continue
    print(bfs(x1, y1))
```

#### 螃蟹采蘑菇

```python
from collections import deque
n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
a = []
### search part ###
for i in range(n):
    for j in range(n):
        if mat[i][j] == 5:
            a.append([i,j])
### 方块 ###
lx = a[1][0] - a[0][0]
ly = a[1][1] - a[0][1]
### 方块移动 ###
dire = [[-1,0],[0,1],[1,0],[0,-1]]
### visited ###
v = [[0] * n for i in range(n)]

### bfs ###
def bfs(x,y):
  	### 打表 ###
    v[x][y] = 1
    ### 路径 ###
    queue = deque([(x,y)])
    ### 遍历路径 ###
    while queue:
        x, y = queue.popleft()
        ### 终止条件 ###
        if (mat[x][y] == 9 and mat[x + lx][y + ly] != 1) or (mat[x][y] != 1 and mat[x + lx][y + ly] == 9):
            return 'yes'
        ### 移动 ###
        for i in range(4):
            dx = x + dire[i][0]
            dy = y + dire[i][1]
            ### can_visited ###
            if 0 <= dx < row and 0 <= dy < col and 0 <= dx + lx < row and 0 <= dy + ly < col and v[dx][dy] == 0 and mat[dx + lx][dy + ly] != 1 and mat[dx][dy] != 1:
                queue.append([dx,dy])
                v[dx][dy] = 1
    return "no"

print(bfs(a[0][0],a[0][1]))
```

#### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129

你现在身处一个R*C 的迷宫中，你的位置用"S" 表示，迷宫的出口用"E" 表示。

迷宫中有一些石头，用"#" 表示，还有一些可以随意走动的区域，用"." 表示。

```python
arr2 = lambda m,n : [ [' ' for j in range(n)] for i in range(m) ]
arr3 = lambda m,n,l : [ [ [False for k in range(l)] for j in range(n)] for i in range(m) ]

N = 100
K = 10

class Node:
    def __init__(self, r=0, c=0, t=0):
        self.row = r
        self.col = c
        self.time = t
        
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(int(input())):
    maze = arr2(N, N)       # 注意不同数据组之间的初始化
    vis = arr3(N, N, K)
    q = []
    r,c,k = map(int, input().split())
    for i in range(r):
        maze[i][:c] = list(input())

    tr = tc = cnt = 0;
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                q.append(Node(i, j))
                vis[i][j][0] = True
                cnt += 1
                if cnt == 2: break
            elif maze[i][j] == 'E':
                tr = i
                tc = j
                cnt += 1
                if cnt == 2: break
            
    while(len(q)):
        t = q[0] # t : Node
        if t.row == tr and t.col == tc: break
        q.pop(0)
        for i in range(4):
            nrow = t.row + dr[i]
            ncol = t.col + dc[i]

            if nrow < 0 or nrow >= r or ncol < 0 or ncol >= c:
                 continue
                    
            # 剪枝很容易能知道，由于每过k单位时间，石头就会消失一次，那么当我们站在某点 (x,y) 时，
            # 时间为 t+k 和  t  时，它们之后行走面临的情境是完全一样的，那就意味着，
            # 对于某个状态的时间，我们可以取模后作为 visited[x][y][time] 的第三个变量，
            # 如果取模后的值代入发现已经访问过，那说明之前已经有更优越的情况出现过，不必再继续搜索了. 
            if vis[nrow][ncol][(t.time + 1) % k]:
                 continue
             
            # 时间是K 的倍数时，迷宫中的石头就会消失
            if (t.time + 1) % k and maze[nrow][ncol] == '#': 
                 continue;
            vis[nrow][ncol][(t.time + 1) % k] = True
            q.append(Node(nrow, ncol, t.time + 1))

    if len(q) == 0:
        print("Oop!")
    else:
        print(q[0].time)
```

#### 接雨水

```python
m,n=map(int,input().split())
heightMap = [list(map(int, input().split())) for _ in range(m)]



def trapRainWater():
    m, n = len(heightMap), len(heightMap[0])
    maxHeight = max(max(row) for row in heightMap)
    water = [[maxHeight for _ in range(n)] for _ in range(m)]
    dirs = [-1, 0, 1, 0, -1]

    qu = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                if water[i][j] > heightMap[i][j]:
                    water[i][j] = heightMap[i][j]
                    qu.append([i, j])

    while len(qu) > 0:
        [x, y] = qu.pop(0)
        for i in range(4):
            nx, ny = x + dirs[i], y + dirs[i + 1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if water[x][y] < water[nx][ny] and water[nx][ny] > heightMap[nx][ny]:
                water[nx][ny] = max(water[x][y], heightMap[nx][ny])
                qu.append([nx, ny])

    ans = 0
    for i in range(m):
        for j in range(n):
            ans = ans + water[i][j] - heightMap[i][j]
    return ans



print(trapRainWater())
```

## DFS

#### 01011：Sticks

```python
#基本的思路就是枚举所有可能的棍子长度。对于假定的长度，看看能否将全部木棒都用完，拼成若干根棍子。因希望棍子尽可能短，枚举棍子长度的时候，就应该从小到大枚举。这实际上也就是对搜索顺序的选择。枚举的范围则是从最长的那根木棒的长度，到木棒长度和的一半。如果都不成功，那就把所有木棒拼成一根棍子。
# 枚举时，不必每个长度都试，对于不是木棒长度和的因子的长度可以直接否定，无须尝试。这是本题中最容易想到，也最强的剪枝。
N = L = 0   
used = []
length = []

def Dfs(R, M):
    if R==0 and M==0:
        return True
    if M==0:
        M = L
    
    for i in range(N):
        if used[i]==False and length[i] <= M:
            if i > 0:
                if used[i-1]==False and length[i]==length[i-1]:
                    continue	# 不要在同一个位置多次尝试相同长度的木棒，剪枝1
            
            used[i] = True
            if (Dfs(R - 1, M - length[i])):
                return True  # 一步登天
            else:
                used[i] = False 
                
                # 不能仅仅通过替换最后一根木棒来达到目的，剪枝3   
                # 替换第一个根棍子是没有用的，因为就算现在不用，也总会用到这根木棍，剪枝2
                if length[i]==M or M==L:
                    return False

    return False

while True:
    N = int(input())
    if N==0:
        break

    length = [int(x) for x in input().split()]
    length.sort(reverse = True)				# 排序是为了从长到短拿木棒进行尝试
       
    totalLen = sum(length)
    
    for L in range(length[0], totalLen//2 + 1):
        if totalLen % L:
            continue		# 不是木棒长度和的因子的长度，直接否定
        
        used = [False]*65
        if Dfs(N, L):
            print(L)
            break

    else:
        print(totalLen)
```

#### 04123: 马走日

```python
maxn = 10;
sx = [-2,-1,1,2, 2, 1,-1,-2]
sy = [ 1, 2,2,1,-1,-2,-2,-1]

ans = 0;
 
def Dfs(dep: int, x: int, y: int):
    #是否已经全部走完
    if n*m == dep:
        global ans
        ans += 1
        return
    
    #对于每个可以走的点
    for r in range(8):
        s = x + sx[r]
        t = y + sy[r]
        if chess[s][t]==False and 0<=s<n and 0<=t<m :
            chess[s][t]=True
            Dfs(dep+1, s, t)
            chess[s][t] = False; #回溯
 

for _ in range(int(input())):
    n,m,x,y = map(int, input().split())
    chess = [[False]*maxn for _ in range(maxn)]  #False表示没有走过
    ans = 0
    chess[x][y] = True
    Dfs(1, x, y)
    print(ans)
```

## DP

斐波那契数列f(n) = f(n-1) + f(n-2)

Sumset dp[i] = dp[i-2] + dp[i//2]

多重背包dp[j] = min(dp[j], dp[j - cur_price * use_num] + use_num)

一维背包dp[j] = max(dp[j], dp[j-occupy[i]]+worth[i])（反向）

完全背包dp[j] = max(dp[j], dp[j-occupy[i]] + worth[i])（正向）

jumpcow

```python
# 2300010763	胡睿诚	数学科学学院
P = int(input())
potions = []
for i in range(P):
    potions.append((int(input())))
result = 0
sign = 1
for i in range(P-1):
    if (potions[i + 1] - potions[i]) * sign < 0:
        result += sign * potions[i]
        sign = -sign
if sign == 1:
    result += potions[P-1]
print(result)

###
def sgn(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    elif x < 0:
        return -1


n = int(input())
nums = list(map(int,input().split()))
delta = [sgn(nums[i+1]-nums[i]) for i in range(n-1)]

result = 1
sign = 0
for i in range(n-1):
    if delta[i] * sign < 0 or (sign == 0 and delta[i] != 0):
        result += 1
        sign = delta[i]
print(result)
```



#### 02757: 最长上升子序列

```python
N = int(input())
nums=list(map(int,input().split()))  # 输入一组序列
length=len(nums)
# print(n)
 
dp=[1]*(length+1)
 
for i in range(length):
    for j in range(0,i):
        if nums[i]>nums[j]:
                    # 状态：dp[i] 表示以 nums[i] 结尾的「上升子序列」的长度
                    # 当nums[i]前面存在小于nums[i]的nums[j],
                    # 则暂存在dp[j]+1就是当前nums[i]的最长增长子序列的长度
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))  # 用函数max直接找到dp数组的最大值，无需再遍历了
```

#### 02806:公共子序列

```python
while True:
    try:
        X, Y = input().split()
        a = len(X)
        b = len(Y)
        dp = [[0 for j in range(b+1)] for i in range(a+1)]
        for i in range(1, a+1):  # 1-a的自然数列表
            for j in range(1, b+1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1  # 这是递进程序
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 这是回溯程序
        print(dp[a][b])
    except EOFError:
        break
```

#### 红蓝玫瑰

```python
r=list(input())
n=len(r)
R=[0]*n
B=[0]*n
if r[0]=="R":R[0]=0;B[0]=1
else:R[0]=1;B[0]=0
for i in range(n-1):
    if r[i+1]=="R":
        R[i+1]=R[i]
        B[i+1]=min(R[i],B[i])+1
    else:
        R[i+1]=min(R[i],B[i])+1
        B[i+1]=B[i]
print(R[-1])
```

#### N皇后

```python
def isvalid(former,row,col):
    for i in range(row):  # 肯定不共行，判断是否共列或共对角线
        if former[i] == col or abs(i-row) == abs(former[i]-col):
            return False
    return True

def queen(former=[],row=0):
    if row == n:  # 结果储存
        result.append(former[:])
        return
    for col in range(n):
        if isvalid(former,row,col):
          former.append(col)  # 压入
          queen(former,row+1)  # 状态转移方程
          former.pop()  # 回溯

n = int(input())
result = []
queen()
if result:
    for _ in result:
    	print(*_)
else:
    print("NO ANSWER")
```

#### 16528: 充实的寒假生活

dp解法，“最大上升子序列和”思路。dp前，数据预处理，如果开始时间一样，保留结束时间最早的活动。因为至少可以参加一个活动，所以dp初始化为1.

```python
n = int(input())
act = [None]*61
for _ in range(n):
    s,e = map(int, input().split())
    if act[s]==None:
        act[s] = e
    elif act[s] > e:
        act[s] = e

dp = [1]*61
for i in range(61):
    if act[i]!=None:
        for j in range(i):
            if act[j]!=None and act[j]<i:
                dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
```

#### 滑雪，最长递减序列

```python
r, c = map(int, input().split())
node = []       # height of each element
node.append( [100001 for _ in range(c+2)] )  # 加保护圈
for _ in range(r):
    node.append([100001] +[int(_) for _ in input().split()] + [100001])
    
node.append( [100001 for _ in range(c+2)] )

dp = [[0]*(c+2) for _ in range(r+2)]
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

def dfs(i,j):
    if dp[i][j]>0:
        return dp[i][j]
    
    for k in range(4):       
        if node[i+dx[k]][j+dy[k]] < node[i][j]:
            dp[i][j] = max( dp[i][j], dfs(i+dx[k], j+dy[k])+1 )

    return dp[i][j]

ans = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        ans = max( ans, dfs(i,j) )

print(ans+1)
```



## 字符串处理

#### 02694: 波兰表达式

recursion/strings

```python
calculatelist=[]
pos=-1

def Exp():
    global pos
    pos+=1
    chr=calculatelist[pos]
    if chr=='+' :
        return Exp()+Exp()
    elif chr=='-' :
        return Exp()-Exp()
    elif chr=='*' :
        return Exp()*Exp()
    elif chr=='/' :
        return Exp()/Exp()
    else:
        return float(chr)
def main():
    global calculatelist
    calculatelist=list(input().split())
    result=Exp()
    print("{:.6f}".format(result))
    
if __name__=='__main__' :
    main()
```

#### 27314: 一键换词

只替换单独的word

```python
import re
raw = input().lower()
old, new = input().lower().split()
text = re.sub(r'(?<=\b)' + old + r'(?=\b)', new, raw)
print(". ".join(s.capitalize() for s in text.split(". ")))
```

"."可代表｜\n外所有东西{1}代表位数，“*”代表任意长度

```python
#23n2300017735(夏天明BrightSummer)
import re

for i in range(int(input())):
    s, p = input(), input().replace("?", ".{1}").replace("*", ".*") + "$"
    print("yes" if re.match(p, s) else "no")
```


#### 生日快乐

核心是第七行，用 get 和空格来针对同一键对应多个值。（可能说得不准确，但意思是那样）。

```python
n = int(input())
info = {}
for i in range(n):
    id, m, d = map(str, input().split())
    m = int(m)
    d = int(d)
    info[(m,d)] = info.get((m,d),'') + ' ' + id 
a = list(info.items())
a.sort()
for i,j in a:
    m,d = i
    if len(j.split()) > 1:
        print(str(m) + ' ' + str(d) + j)
```

#### 梅森数

```python
# 23数院 胡睿诚
from math import log10, ceil
M = 10**500
MAXP = 3100000

p = int(input())
print(int(p*log10(2)) + 1)
#print(ceil(p*0.3010299956639812))

a = [2]
for _ in range(len(bin(MAXP)) - 2):
    a.append((a[-1]**2) % M)

s = 1
i = 0
for j in reversed(bin(p)[2:]):  # bin()前两位时0b
    if j == '1':
        s = (s*a[i]) % M
    i += 1

ans = list(str(s-1))
l = len(ans)
if l < 500:
    ans = ['0']*(500-l)+ans
for i in range(0, 500, 50):
    print(''.join(ans[i:i+50]))
```

#### 12757：阿尔法星人翻译官

```python
###sgn###
sign = 1
if tokens[0]=="negative":
    sign = -1
    del tokens[0]

total = 0
tmp = 0
for i in tokens:
    if i in ("thousand", "million"):
        total += tmp*dic[i]
        tmp = 0
        continue
    if i == "hundred":  # 遇到一个位数表达时x100
        tmp *= dic[i]
    else:
        tmp += dic[i]
        
print( sign * (total + tmp) )
```

#### 01008：Maya Calendar

```python
n = int(input())
listdate = []
MouthDict = 打表
MouthDict2 = 打表
for i in range(n):
    NumberOfTheDay,Month,year = map(str,input().split())
    sum = int(NumberOfTheDay.replace(".",'')) + int(MouthDict[Month])*20 + int(year)*365
    Year2 = sum//260
    Month2 = MouthDict2[sum%20]
    Number = sum%13+1
    newdate = f'{Number} {Month2} {Year2}'
    listdate.append(newdate)
print(n)
for i in listdate:
    print(i)
```

## 矩阵

#### 02659: Bomb Game（加权搜索）（和俄罗斯世界杯同理）

```python
A,B,K = map(int,input().split())
martix = []
less = 0
most = 0
poss = 0
for create in range(A):
    martix.append([0]*B)
for round in range(K):
    R,S,P,T = map(int,input().split())
    if T == 1:
        for i in range(max(0,R-1-P//2),min(A,R+P//2)):
            for j in range(max(0,S-1-P//2),min(B,S+P//2)):
                martix[i][j] += 1  # 给每个点加权
    else:
        for i in range(max(0,R-1-P//2),min(A,R+P//2)):
            for j in range(max(0,S-1-P//2),min(B,S+P//2)):
                martix[i][j] -= 1  # 给每个点减权
for row in martix:
    less = max(row)
    most = max(less,most)
for row in martix:
    poss += row.count(most)
print(poss)
```

#### 02802: 小游戏

dfs, bfs, 思路：最初没想到要记录线段数量，发现问题后，采用了swj大佬的做法，以后应该还会用到

```python
# 基于 23 工学院 苏王捷
import heapq

num1 = 1
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    print(f"Board #{num1}:")
    matrix = [[" "] * (w + 2)] + [[" "] + list(input()) + [" "] for _ in range(h)] + [[" "] * (w + 2)]
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num2 = 1
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            break
        queue, flag = [], False
        vis = set()
        heapq.heappush(queue, (0, x1, y1, -1))   ##初始情况-1下，线段数+1，i代表方向
        matrix[y2][x2] = " "
        vis.add((-1, x1, y1))
        while queue:
            step, x, y, dirs = heapq.heappop(queue)
            if x == x2 and y == y2:
                flag = True
                break
            for i, (dx, dy) in enumerate(dir):
                px, py = x + dx, y + dy
                if 0 <= px <= w + 1 and 0 <= py <= h + 1 and (i, px, py) not in vis and matrix[py][px] != "X":
                    vis.add((i, px, py))
                    heapq.heappush(queue, (step + (dirs != i), px, py, i))  #trick:变加上1
        if flag:
            print(f"Pair {num2}: {step} segments.")
        else:
            print(f"Pair {num2}: impossible.")
        matrix[y2][x2] = "X"
        num2 += 1
    print()
    num1 += 1

```



## 数据预处理

#### 01328: Radar Installation

greedy

数据都建好了，但最后雷达的建立范围有点没搞清楚，逆序排列，这里每个pos都是局部最小值。从后往前推，如果最小值比前一个的最大值大的话，那就再建一个站，如果前一个的最大值大于最小值的话， 那就应该建在后一个的最小值到前一个最大值的范围内。又已知这里的最小值就是局部的最小值，那么把雷达建在最小值处就是最优解

```python
            pos.append([float(a-(d**2-b**2)**0.5),float(a+(d**2-b**2)**0.5)])
    input()
    if len(pos) < n:
        print(f'Case {turn}: -1')
    else:
        pos.sort(reverse=True)   #<<<这里排序很重要
        number = len(pos)
        c = pos[0][0]
        for j in range(1,n):
            if c > pos[j][1]:
                c = pos[j][0]
            else:
                number -= 1
        print(f'Case {turn}: {number}')

```

#### 只因线段覆盖

```python
### 线段全覆盖 ###
N = int(input())
a = list(map(int,input().split()))
intervals = [(max(0,i-a[i]),min(N-1,i+a[i])) for i in range(N)]
intervals.sort()  <<< # 这里可能需要反转思考

ans = 0
right = 0
temp = -1
index = 0
while index < N and right < N:
    while index < N and intervals[index][0] <= right:
        temp = max(temp,intervals[index][1])
        index += 1
    right = temp + 1
    ans += 1

print(ans)
```



```python
### 线段最大覆盖 ###
def generate_intervals(x, width, m):
    temp = []
    for start in range(max(0, x-width+1), min(m, x+1)):
        end = start+width
        if end <= m:
            temp.append((start, end))
    return temp

n, m = map(int, input().split())
plans = [tuple(map(int, input().split())) for _ in range(n)]
intervals = []
for x, width in plans:
    intervals.extend(generate_intervals(x, width, m))
intervals.sort(key=lambda x: (x[1], x[0]))
cnt = 0
last_end = 0
for start, end in intervals:
    if start >= last_end:
        last_end = end
        cnt += 1
print(cnt)
```

## 搜索（遍历，dfs，bfs

#### re 统计单词数

```python
import re
re.sub(pattern, repl, string, count=0, flags=0)  # 替换
print("yes" if re.match(p, s) else "no")  #匹配

word = input().lower()
article = input().lower()

a = re.findall(r'\b'+word+r'\b', article)
cnt = len(a)
if cnt == 0:
    print(-1)
else:
    aa  = re.search(r'\b'+word+r'\b', article)
    print(cnt, aa.start())
```

#### 最大连通域

```python
temp = 0
def search(i,j):
    global temp
    temp += 1
    matrix[i][j] = "."
    for p in dfs:
        if matrix[i+p[0]][j+p[1]] == "W":
            search(i+p[0],j+p[1])

dfs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
T = int(input())
for _ in range(T):
    maxium = 0
    N,M = map(int,input().split())
    matrix = [["."]*(M+2)]
    for i in range(N):
        matrix.append(["."]+list(input())+["."])
    matrix.append(["."]*(M+2))
    #print(matrix)
    for i in range(1,N+1):
        for j in range(1,M+1):
            if matrix[i][j] == "W":
                temp = 0
                search(i,j)
                maxium = max(maxium,temp)
    print(maxium)
```

#### 算n点

recursion

```python
#gpt
'''
在这个优化的代码中，我们使用了递归和剪枝策略。首先按照题目的要求，输入的4个数字保持不变，
不进行排序。在每一次运算中，我们首先尝试加法和乘法，因为它们的运算结果更少受到数字大小的影响。
然后，我们根据数字的大小关系尝试减法和除法，只进行必要的组合运算，避免重复运算。

值得注意的是，这种优化策略可以减少冗余计算，但对于某些输入情况仍需要遍历所有可能的组合。
因此，在最坏情况下仍然可能需要较长的计算时间。
'''

def find(nums):
    if len(nums) == 1:
        return abs(nums[0] - 24) <= 0.000001  # <<<<<<<<<<<修改项
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            a = nums[i]
            b = nums[j]
            remaining_nums = []
            for k in range(len(nums)):
                if k != i and k != j:
                    remaining_nums.append(nums[k])
            if find(remaining_nums + [a + b]) or find(remaining_nums + [a * b]):
                return True
            if a > b and find(remaining_nums + [a - b]):
                return True
            if b > a and find(remaining_nums + [b - a]):
                return True
            if b != 0 and find(remaining_nums + [a / b]):
                return True
            if a != 0 and find(remaining_nums + [b / a]):
                return True
    return False
n = int(input())
card = list(map(int,input().split()))
print("YES" if find(card) else "NO")
```

## 熄灯枚举

#### 02811: 熄灯问题

brute force, deep copy

```python
import itertools
from copy import deepcopy
from itertools import product
matrix = [[0]*8]
for _ in range(5):
    matrix.append([0] + list(map(int, input().split())) + [0])
matrix.append([0]*8)
dx = [0, 0, 0, 1]
dy = [-1, 0, 1, 0]

for i in itertools.product([0, 1], repeat=6):
    ans = []
    temp_matrix = deepcopy(matrix)
    first_line = list(i)
    ans.append(first_line)
    for j in range(6):
        if first_line[j] == 1:
            for k in range(4):
                temp_matrix[1+dx[k]][j+1+dy[k]] = abs(temp_matrix[1+dx[k]][j+1+dy[k]] - 1)
    ans.append(temp_matrix[1][1:7])
    for _ in range(4):
        for j in range(6):
            if ans[-1][j] == 1:
                for k in range(4):
                    temp_matrix[len(ans) + dx[k]][j + 1 + dy[k]] = abs(temp_matrix[len(ans) + dx[k]][j + 1 + dy[k]] - 1)
        ans.append(temp_matrix[len(ans)][1:7])
    if ans[-1] == [0,0,0,0,0,0]:
        for j in range(5):
            print(" ".join(map(str, ans[j])))
        break
```

## 数据结构

#### 排队 分层排队

```python
N, D = map(int, input().split())
height = []
check = []
for i in range(N):
    height.append(int(input()))
    check.append(False)
height_new = []

while True:
    if not(False in check):
        break
    try:
        i, l = 0, len(height)
        temp = []
        while i < l:
            if(check[i]):
                i += 1
                continue
            if not temp:
                temp = [height[i]]
                maxh = height[i]
                minh = height[i]
                check[i] = True
                continue
            if(height[i] < minh):
                minh = height[i]
            if(height[i] > maxh):
                maxh = height[i]
            if maxh - height[i] <= D and height[i] - minh <= D:
                temp.append(height[i])
                check[i] = True
            i += 1
        temp.sort()
        height_new.append(temp)
    except IndexError:
        break

for i in height_new:
    for j in i:
        print(j)
```
