**Python知识点总结** 

**竺佳诺**

```python
## 1. 除法是否使用地板除得到整数？（否则 4/2=2.0）    ##2. 是否有缩进错误？
## 3. 用于调试的print是否删去？					 ##4. 非一般情况的边界情况是否考虑？
## 5. 递归中return的位置是否准确？（缩进问题,逻辑问题）## 6. 贪心是否最优？有无更优解？
## 7. 正难则反（参考 #蒋子轩 23工院# 乌鸦坐飞机）		## 8. 审题是否准确？ 是否漏掉了输出？（参考）
```

常用解题步骤/技巧/算法，在codeforces.com中记为Tag，功能是帮助用户找到一类特定的问题。下面是一些常见的标记及其解释：

1) dp (Dynamic Programming): 这是一种算法设计策略，主要用于需要考虑预计结果和当前情境的复杂问题；它将问题分解为更小的子问题，并存储这些子问题的解，以避免重复计算。
2) greedy: 贪婪算法是一种寻找工作最优解的算法，它总是选取当前状态下最好的选项，不考虑结果对未来的影响。
3) math: 这个标签用于那些需要一定数学知识来解答的问题，如概率、组合数学、数论或几何等。
4) ds (Data Structures): 对于需要使用到数据结构（例如数组、链表、队列、栈、哈希表、树、图等）的题目，会使用这个标签。
5) graphs: 这个标签用于图论相关的题目，如最短路径、最小生成树、网络流等问题。
6) sortings：这个标签用于涉及各种排序方法（比如冒泡排序，选择排序，插入排序，快速排序等）的题目。
7) binary search: 对于涉及到二分查找的题目，会使用这个标签。
8) constructive algorithms: 这个标签用于那些需要构造性地找出解的问题，即不仅要找出一个解，还需要构造出解的策略或过程。
9) strings: 这个标签用于字符串相关的课题，如字符串匹配、操作等。
10) combinatorics: 组合数学问题，主要涉及到计数，排列，组合等问题。
11) number theory：可能涉及到一些主题。质数与因数：题目可能要求找到一个数的所有因数，判断一个数是否为质数，或者计算一个区间内的质数数量等。
    最大公约数与最小公倍数：题目可能要求计算两个数的最大公约数（GCD）或最小公倍数（LCM），或者需要利用最大公约数解决其他问题。
    同余与模运算：题目可能要求计算整数除以一个模数的余数，或者判断两个数是否是同余的，也可能涉及到欧拉定理、费马小定理等相关知识。
    数字运算：题目可能涉及到对整数进行各种运算，比如数字和、数字位数之和、数字重排等。
    整数序列：题目可能涉及到寻找某种规律的整数序列，比如斐波那契数列、卡塔兰数列等。
12) two pointers: 双指针法通常用于解决一些需要通过对数组或链表进行两个位置的遍历、对比或查找的问题。例如，在一个有序数组中查找两个数之和等于给定目标值的问题，可以使用两个指针从数组的两端向中间靠拢进行查找。这样可以减少不必要的遍历和比较。



基本语句

```python
#//整除 %取余 /除法
a1=round(a,2)#四舍五入到小数点后两位
x="{:.2f}".format(h)#保留两位小数

while True:
    try:
        a,b=input().split()
    except EOFError:#如果没有输入了
        break#跳出循环

import math
s=math.ceil(a)#ceil向上取整，floor向下取整
print(math.gcd(6,10,12))#最大公因数
print(math.lcm(4,3,7))#最小公约数

# 二进制转十进制
binary_str = "1010"
decimal_num = int(binary_str, 2) # 第一个参数是字符串类型的某进制数，第二个参数是他的进制，最终转化为整数10

ord()#把字符变为ASCII
chr()#把ASCII变为字符

import calendar
print(calendar.isleap(2020)) # True，闰年判断

from itertools import combinations#permuations类似，但考虑元素顺序
s=list(map(int,input().split()))
for i in range (1,len(s)+1):#i为元素个数
    for x in combinations (s,i):
        print(x)
   
import bisect
m= [1,3,5,6,6,6,6,7,9]#列表，升序！
insert_position = bisect.bisect_left(m, 6)# 使用 bisect_left 查找插入位置，3
right_position = bisect.bisect_right(m, 6)#使用 bisect_right 查找右侧位置，7
bisect.insort_left(m, 4)#插入值，[1, 3, 4, 5, 6, 6, 6, 6, 7, 9]
```

```python
import math
def isPerfectSquare(num):#完全平方数
    if num < 0:
        return False
    sqrt_num = math.isqrt(num)
    return sqrt_num * sqrt_num == num

#质数#思路1
def prime_num(n):
    if n<2:
        return(False)
    if n==2:
        return(True)
    if n%2==0 or n%3==0:
        return(False)
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i=i+6
    return True
#思路2：埃氏筛
max_num=int(math.sqrt(10**12))
prime=set()
is_prime=[True]*(max_num + 1)
is_prime[0]=is_prime[1]=False
for i in range(2, int(math.sqrt(max_num)) + 1):
    if is_prime[i]==True:
        for j in range(i*i, max_num + 1, i):
            is_prime[j]=False#质数的倍数（>=2倍）不是质数
for i in range(max_num + 1):
    if is_prime[i]==True:
        prime.add(i)
#欧拉筛
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
```

循环结构

```python
for i in range(1,n):#从1到n-1
for i in range(n,1,-1):#从n到2
for i in range(1,10,2):#从1到10，间隔2，不包括10，即13579
for i in range(n):#从0到n-1，循环n次
for char in s:#遍历字符串的每个字符
while(True):#死循环
#for else结构/while else结构：如果break不执行else，正常循环完才执行else
```

输入与输出

```python
n=int(input())#注意有时候别忘了int，Input默认是str
n,m=map(int,input().split())
print(n)#默认end=换行
print(n,end=" ")#输出的间隔为空格
print("Cube = {}, Triple = ({},{},{})".format(a, b, c, d))#a,b,c,d的值填进｛｝
```

字符串string

```python
s=input()#string
s1=s.upper()#upper全部大写，lower全部小写
s.find("@.")!=-1#找得到
p = s.find("@");#从左到右首次出现的索引
q = s.find(".", p+1);#从p+1开始找
str1=str1.replace(str1[0],str2[0],1)#1为replace的次数
x=len(s)#字符串长度
p=s[0]#字符串第一个字符
q=s[-1]#字符串最后一个字符
if s1>s2: #按照字典序比较string的大小
s1=s[1:4]#对列表进行切片操作，得到子列表（索引1-3）
si=index(30)#获取元素“30”的索引值，索引值从0开始
s1="123";s2="456"
print(s1+s2)#123456，字符串相加即合并
```

列表list

```python
lista=[]; n=list(map(int,input().split('+')))
lista.append(a)#添加元素
lista.sort()#永久性排序，从小到大
lista.reverse()#倒序，或者直接lista.sort(reverse=True)
sortedlista=sorted(lista)#暂时性排序，list本身不改变
ans = "".join(lista)#用join合并列表
```

集合set 字典dic{key: value}

```python
a=set()
a.add(1)#添加元素
if s in a:#判断是否在集合内
dic={}
dic={k:dic[k] for k in sorted(dic,reverse=True)}
```

矩阵matrix

```python
n,m=map(int,input().split())#rows,columns
#全0矩阵建立，加保护圈，防止index out of range（方法1）
matrix=[[0]*(m+2) for _ in range(n+2)
#矩阵输入，对matrix加保护圈
matrix=[]
matrix.append([0 for x in range(m+2)])
for _ in range(n):
    matrix.append([0] +[int(_) for _ in input().split()] + [0])  
matrix.append( [0 for _ in range(m+2)] )       
#方法2：使用max和min防止index out of range
for j in range(max(0,r-d),min(a,r+d+1)):
        for l in range(max(0,s-d),min(b,s+d+1)):
            matrix[j][l]+=t
```

堆heap

```python
import heapq#导入模块
a = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(a)#将列表转化为堆
x = heapq.heappop(a)#从堆中获取最小值（或最大值）并删除
heapq.heappush(a, 7)#向堆中插入元素
x = a[0]#获取堆中最小值（或最大值）但不删除
```

贪心greedy：局部最优能导致全局最优。

冒泡排序

```python
#最大最小整数
n = int(input())
nums = input().split()
for i in range(n - 1):
	for j in range(i+1, n):
		if nums[i] + nums[j] < nums[j] + nums[i]:
			nums[i], nums[j] = nums[j], nums[i]
ans = "".join(nums)
nums.reverse()
print(ans + " " + "".join(nums))
```

双指针

田忌赛马

- if：如果田忌当前最慢的马能赢过国王最慢的马，田忌积分加1（因为赢了），同时两队的最慢马都移到下一个。
- elif：如果田忌当前最快的马能赢过国王最快的马，田忌积分加1，并且两队的最快马都移到前一个。
- else：
- **如果上面两种情况都不满足，田忌将用最慢的马去挑战王的最快的马。**(田忌输了或者平了)
- **如果田忌的马慢于国王的马，田忌积分减1（因为输了）。**
- 然后田忌最慢的马和国王最快的马都会被排除出下一轮比赛

```python
while True:
    n = int(input())
    if n==0:
        break
    *Tian, = map(int, input().split()); *King, = map(int, input().split())
    Tian.sort(); King.sort()
    lTian = 0; rTian = n - 1#初始化两队马的指针，lTian和lKing指向最慢的马
    lKing = 0; rKing = n - 1#rTian和rKing指向最快的马。
    ans = 0
    while lTian <= rTian:#开始一个循环，当田忌还有马没比赛时继续。
        if Tian[lTian] > King[lKing]:
            ans += 1;lTian += 1;lKing += 1
        elif Tian[rTian] > King[rKing]:
            ans += 1;rTian -= 1;rKing -= 1
        else:
            if Tian[lTian] < King[rKing]:
                ans -= 1
            lTian += 1;rKing -= 1
    print(ans*200)
```

寻找离目标数最近的两数之和

```python
t=int(input())
s=list(map(int,input().split()))#2 <= len(s) <= 100000
s.sort()
gap=abs(t-s[0]-s[1]); ans=s[0]+s[1]
l=0; r=len(s)-1#最小和最大，双指针
while l<r:
    total=s[l]+s[r]
    if total==t:
        ans=total
        break
    if abs(total-t)<gap:
        ans=total
        gap=abs(total-t)
    if abs(total-t)==gap:
        ans=min(ans,total)#如果存在多个解，则输出数值较小的那个。   
    if total>t:
        r-=1
    else:
        l+=1
print(ans)
```

军备竞赛

```python
#任意时刻敌国的武器不能比我国更多，且不负债，p>=0
#只看数目：便宜的用来自己制作，贵的卖给敌国
p=int(input())#财富总和
cost=list(map(int,input().split()))#武器设计或者卖出的价格
cost.sort()
l=0; r=len(cost)-1; own=0; sell=0
if p>=cost[l]:#如果一个都制作不起，就别制作也别卖
    while l<=r:
        if p>=cost[l]:
            p-=cost[l]#如果有钱，优先制作最便宜的
            l+=1; own+=1
        elif own>sell:
            if l==r:#如果遍历到最后一个武器，没法制作，就别卖了
                break
            p+=cost[r]#次之，如果武器多，卖最贵的
            r-=1; sell+=1
print(own-sell)
```



#### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110

1. 注意读题，可以拆散糖果
2. 不可以sort ratio后在循环中用ratio是否相等来获取value和weight，若样本中有多组数据ratio相等，存在重复读取的情况

```python
n,wmax=map(int,input().split())
vmax=0
ratio=[]
for i in range(n):
    v,w=map(int,input().split())
    for j in range(w):
        ratio.append(v/w)
ratio.sort()
ratio.reverse()
i=0
while i<len(ratio) and i<wmax:
    vmax+=ratio[i]
    i+=1
print(f"{vmax:.1f}")
```

#### 545D. Queue

greedy, implementation, sortings, 1300

https://codeforces.com/problemset/problem/545/D

最开始直接sort了一下，WA，后来用1-10试了一下，发现了问题，灵光一现

如果在从小到大的时间排序中有人disappointed了，直接把他放在队尾，这个人仍然是不满意，但是减小后续人排队的时间

```python
# Compiled by RubyZhu
#545D. Queue
n=int(input())
t=list(map(int,input().split()))#disappointed time
t.sort()
time=0;happy=0
for i in range(n):
    if time<=t[i]:
        happy+=1
    else:
        t[i]=0#if disappointed, move to end
    time+=t[i]
print(happy)
```

#### 1793C. Dora and Search

constructive algorithms, data structures, two pointers, 1200, 

https://codeforces.com/problemset/problem/1793/C

双指针对撞！

```python
#两端的数不是max也不是min
t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    maxa=n
    mina=1
    i=0
    j=n-1
    while j-i>2:
        if a[i]!=mina and a[i]!=maxa:
            if a[j]!=mina and a[j]!=maxa:
                ans.append(str(i+1)+" "+str(j+1))
                break
        if a[i]==mina:
            mina+=1
            i+=1                
        if a[i]==maxa:
            maxa-=1
            i+=1
        if a[j]==mina:
            mina+=1
            j-=1
        if a[j]==maxa:
            maxa-=1
            j-=1   
    if j-i<=2:
        ans.append(-1)
for i in range(t):
    print(ans[i])
```

**动态规划dp **：核⼼是数学归纳法。即对于⼀个已经证明归纳的问题，可以 通过已知的前 n 项，在约束条件下，求出未知的第 n+1 项。 

最大上升子序列

输出最大上升子序列的和

序列(1, 7, 3, 5, 9, 4, 8)，它的⼀些上升⼦序列，如(1, 7), (3, 4, 8) 等等。这些⼦序列中最⻓的⻓度是4，s是⼦序列(1, 3, 5, 8).

```python
n=int(input())
b = [int(x) for x in input().split()]
dp = [0]*n
#从第i个数开始逐次递推
#主要思路就是记录把每个数作为序列最后1位时的序列和，取 max。
#即，以每项为末项的最大上升子序列和
for i in range(n):
    dp[i] = b[i]
    for j in range(i):#考虑第 i个数的情况时，再从第1到i-1个数开始逐个检验
        if b[j]<b[i]:#如果第 i个数大于前 i个数中的第 j个数
            dp[i] = max(dp[j]+b[i], dp[i])#那么将前 j个数的最大上升子序列和再加上第 i个数
print(max(dp))
```

最大公共子序列

子序列需要严格上升，输出最大公共子序列长度

```python
while True:
    try:
        a, b = input().split()
    except EOFError:#如果没有输入了
        break#跳出循环
    alen = len(a)
    blen = len(b)
    dp = [[0]*(blen+1) for i in range(alen+1)]
    for i in range(1, alen+1):
        for j in range(1, blen+1):
            if a[i-1]==b[j-1]:#如果a的第i-1个元素和b的第j-1个元素相等，
                dp[i][j] = dp[i-1][j-1] + 1#则最长公共子序列的长度在前一个索引位置的长度基础上加1。
            else:#如果a的第i-1个元素和b的第j-1个元素不相等
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])#最长公共子序列的长度取自上方或左方的最大值
    print(dp[alen][blen])
```

登山

```python
n=int(input())#景点数
h=[int(x) for x in input().split()]#每个景点的海拔
dp=[1]*n
rdp=[1]*n
#每次所浏览景点的编号都要大于前一个浏览景点的编号
#说明整个过程为上升子序列
#不连续浏览海拔相同的两个景点，并且一旦开始下山，就不再向上走了
for i in range(n):#上坡
    for j in range(i+1,n):
        if h[i]<h[j]:
            dp[j]=max(dp[j],dp[i]+1)
h.reverse()
for i in range(n):#下坡
    for j in range(i+1,n):
        if h[i]<h[j]:
            rdp[j]=max(rdp[j],rdp[i]+1)
ans=[0]*n
for i in range(n):
    ans[i]=dp[i]+rdp[n-1-i]-1#最大高度的景点算了两次
print(max(ans))
"""
u = 0  # 初始化变量u为0
zip_dp = zip(dp, list(reversed(rdp)))  # 使用zip()函数将dp和rdp中对应位置的元素组合，存储在zip_dp中
*u, = map(lambda x: x[0]+x[1], zip_dp)  # 使用map()函数对zip_dp中的每个元组进行(x[0]+x[1])的操作，将结果存储在u中
print(max(u) - 1)  # 打印u中的最大值减去1"""
```

小青蛙跳荷叶

```python
n=int(input())#荷叶数
#小青蛙可以从岸边每次跳1、2个荷叶
#即，n拆成1*x+2*y的组合有多少个
dp=[0]*(n+2)
dp[1]=1;dp[2]=2
if n>2:
    for i in range(3,n+1):    
        dp[i]=dp[i-1]+dp[i-2]
        #跳到i：从i-1跳一下，i-2跳一下
        #从i-2到i-1会和i-1的重复
print(dp[n])
```

Cut Ribbon

```python
n,a,b,c=map(int,input().split())
#剪完n后片段长度必须为a,b,c，且片段数最大
#求片段数
dp=[0]+[-4000]*4000
for i in range(1,n+1):
    dp[i]=max(dp[i-a],dp[i-b],dp[i-c])+1
print(dp[n])
```

Ilya and Queries

```python
#
s=input()
dp=[0];num=0;answer=[]
m=int(input())
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        num+=1
    dp.append(num)
for i in range(m):
    l,r=map(int,input().split())
    answer.append(dp[r-1]-dp[l-1])
for i in range(m):
    print(answer[i])
#print('\n'.join(answer))
```

Sereja and Suffixes

```python
#
n,m=map(int,input().split())
a=list(map(int,input().split()))
dp=[0]*(n-1)+[1]
num=set()
num.add(a[n-1])
for i in range(n-2,-1,-1):
    if a[i] in num:
        dp[i]=dp[i+1]
    else:
        dp[i]=dp[i+1]+1
    num.add(a[i])
for i in range(m):
    l=int(input())
    print(dp[l-1])
#data structures
n, m = map(int,input().split())
a = list(map(int, input().split()))
adic = {}
for i in range(n):
    if a[i] in adic:
        adic[a[i]] += 1
    else:
        adic[a[i]] = 1
 
ans = [0]*n
for i in range(n):
    if a[i] in adic:
        if adic[a[i]] == 1:
            adic.pop(a[i])
            ans[i] += 1
        else:
            adic[a[i]] -= 1
    ans[i] += len(adic)
 
for i in range(m):
    print(ans[int(input()) - 1])
```

Boredom

```python
n=int(input())
a=[0]*100001
for i in map(int,input().split()):
    a[i]+=1
dp=[0]*100001
for i in range(100001):
    dp[i]=max(dp[i-1],dp[i-2]+a[i]*i)
print(max(dp))
```

采药

```python
dp=[-1]*(T+1)
dp[0]=0
for _ in range(m):
    t,v=map(int,input().split())
    for i in range(T,t-1,-1):
        if dp[i-t]!=-1:
            dp[i]=max(dp[i],dp[i-t]+v)
print(max(dp))

T, M = map(int, input().split())
dp = [ [0] + [0]*T for _ in range(M+1)]
t = [0]
v = [0]
for i in range(M):
    ti, vi = map(int, input().split())
    t.append(ti)
    v.append(vi)
for i in range(1, M+1): # 外层循环（行）药草M
    for j in range(0, T+1): # 内层循环（列）时间T
        if j >= t[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-t[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[M][T])
```



**深度优先搜索 dfs**

晶矿个数：连起来的r或b

```python
dire = [[-1,0], [1,0], [0,-1], [0,1]]
def dfs(x, y, c):
    m[x][y] = '#'
    for i in range(len(dire)):
        tx = x + dire[i][0]
        ty = y + dire[i][1]
        if m[tx][ty] == c:
            dfs(tx, ty, c)
for _ in range(int(input())):
    n = int(input())
    m = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(1, n+1):
        m[i][1:-1] = input()
    r = 0 ; b=0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if m[i][j] == 'r':
                dfs(i, j, 'r')
                r += 1
            if m[i][j] == 'b':
                dfs(i,j,'b')
                b += 1
    print(r, b)
```

马走日：是否能遍布棋盘

```python
maxn = 10;ans = 0
sx = [-2,-1,1,2, 2, 1,-1,-2];sy = [ 1, 2,2,1,-1,-2,-2,-1]
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

**广度优先搜索 bfs**

寻宝

```python
# 苏王捷 23工院# 武昱达注：用heapq替代了双向队列，用入堆模拟入队，用pop模拟出队。
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



```python
#螺旋矩阵
n = int(input())
s = [[401]*(n+2)]
mx = s + [[401] + [0]*n + [401] for _ in range(n)] + s
dirL = [[0,1], [1,0], [0,-1], [-1,0]]
row = 1
col = 1
N = 0
drow, dcol = dirL[0]
for j in range(1, n*n+1):
    mx[row][col] = j
    if mx[row+drow][col+dcol]:
        N += 1
        drow, dcol = dirL[N%4]
    row += drow
    col += dcol
for i in range(1, n+1):
    print(' '.join(map(str, mx[i][1:-1])))
    
```

```python

# 乌鸦坐飞机
n, k = map(int, input().split())
inp = list(map(int, input().split()))
a = n*2 # 12 / 78 这种两个连着的位置的数⽬，易知12必须来⾃同⼀窝，78也必须来⾃同⼀窝
b = n # 3456 Z这种4个连着的位置的数⽬，易知3456必须来⾃同⼀窝
# 考虑到相邻的位置要坐来⾃同⼀窝的乌鸦，⾸先分配4连b代表剩余未分配的4连座数⽬
for i in range(k):
    x = inp[i]//4 # x代表第i窝乌鸦的数⽬是4的多少倍
    y = min(x,b) # y代表第i窝乌鸦还能分配出去的4连座数⽬
    b -= y # b代表把第i窝分配到4连座之后，还剩下未分配的4连座数⽬
    inp[i] -= (y*4) # 第i窝乌鸦的数⽬减掉已分配4连座的乌鸦数⽬
# 由于4连座不能拆成两个2连座，先当成⼀个2连座
# a是剩余未分配的2连座数⽬
a += b
for i in range(k):
    x = inp[i]//2 # x代表第i窝乌鸦的中未分配的数⽬是2的多少倍
    y = min(x,a) # y代表第i窝乌鸦还能分配出去的2连座数⽬
    a -= y # a代表把第i窝分配到2连座之后，还剩下未分配的2连座数⽬
    inp[i] -= (y*2) # 第i窝乌鸦的数⽬减掉已分配2连座的乌鸦数⽬
# sum(inp)是剩余未分配的乌鸦总数，若能分配开应该是0
# b是剩余的4连座，由于之前把b当成2连座加⼊a分配了，此时b剩下两个座位，但是只能坐⼀只来⾃不同窝的乌鸦
# a是剩余的2连座，只能坐⼀只来⾃不同窝的乌鸦
# a + b是剩余未分配的座位数，也就是能坐下的乌鸦数⽬，这⾥答案的写法只考虑了此时⼀只乌鸦分配到⼀个空的2连座或者⼀个已经有两个⼈的4连座上，所以是sum(inp) <= (a+b)
# 若⻜机座位太少，可能每窝乌鸦都剩下好多只，必然有a = b = 0，此时也是不满⾜条件的
if sum(inp) <= (a+b):
    print ("YES")
else:
    print ("NO")
```

