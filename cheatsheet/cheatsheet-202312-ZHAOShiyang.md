# CS101 备忘录Cheatsheet 



Updated 1805 GMT+8 Dec 27, 2023



2023/12/27 compiled by 赵时阳-数院23



***I leave no trace of wings in the air, but I am glad I have had my flight.***

## 一、一些时间复杂度

1. Lists

```python
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Index         | l[i]         | O(1)	     |
Store         | l[i] = 0     | O(1)	     |
Length        | len(l)       | O(1)	     |
Append        | l.append(5)  | O(1)	     | mostly: ICS-46 covers details
Pop	          | l.pop()      | O(1)	     | same as l.pop(-1), popping at end
Clear         | l.clear()    | O(1)	     | similar to l = []

Slice         | l[a:b]       | O(b-a)	     | l[1:5]:O(l)/l[:]:O(len(l)-0)=O(N)
Extend        | l.extend(...)| O(len(...))   | depends only on len of extension
Construction  | list(...)    | O(len(...))   | depends on length of ... iterable

check ==, !=  | l1 == l2     | O(N)          |
Insert        | l[a:b] = ... | O(N)	     | 
Delete        | del l[i]     | O(N)	     | depends on i; O(N) in worst case
Containment   | x in/not in l| O(N)	     | linearly searches list 
Copy          | l.copy()     | O(N)	     | Same as l[:] which is O(N)
Remove        | l.remove(...)| O(N)	     | 
Pop	      	  | l.pop(i)     | O(N)	     | O(N-i): l.pop(0):O(N) (see above)
Extreme value | min(l)/max(l)| O(N)	     | linearly searches list for value
Reverse	      | l.reverse()  | O(N)	     |
Iteration     | for v in l:  | O(N)          | Worst: no return/break in loop

Sort          | l.sort()     | O(N Log N)    | key/reverse mostly doesn't change
Multiply      | k*l          | O(k N)        | 5*l is O(N): len(l)*l is O(N**2)
```

2. Sets

```python
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Length        | len(s)       | O(1)	     |
Add           | s.add(5)     | O(1)	     |
Containment   | x in/not in s| O(1)	     | compare to list/tuple - O(N)
Remove        | s.remove(..) | O(1)	     | compare to list/tuple - O(N)
Discard       | s.discard(..)| O(1)	     | 
Pop           | s.pop()      | O(1)	     | popped value "randomly" selected
Clear         | s.clear()    | O(1)	     | similar to s = set()

Construction  | set(...)     | O(len(...))   | depends on length of ... iterable
check ==, !=  | s != t       | O(len(s))     | same as len(t); False in O(1) if
      	      	     	       		       the lengths are different
<=/<          | s <= t       | O(len(s))     | issubset
>=/>          | s >= t       | O(len(t))     | issuperset s <= t == t >= s
Union         | s | t        | O(len(s)+len(t))
Intersection  | s & t        | O(len(s)+len(t))
Difference    | s - t        | O(len(s)+len(t))
Symmetric Diff| s ^ t        | O(len(s)+len(t))

Iteration     | for v in s:  | O(N)          | Worst: no return/break in loop
Copy          | s.copy()     | O(N)	     |
```

3. Dictionaries: dict and defaultdict

```python
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Index         | d[k]         | O(1)	     |
Store         | d[k] = v     | O(1)	     |
Length        | len(d)       | O(1)	     |
Delete        | del d[k]     | O(1)	     |
get/setdefault| d.get(k)     | O(1)	     |
Pop           | d.pop(k)     | O(1)	     | 
Pop item      | d.popitem()  | O(1)	     | popped item "randomly" selected
Clear         | d.clear()    | O(1)	     | similar to s = {} or = dict()
View          | d.keys()     | O(1)	     | same for d.values()

Construction  | dict(...)    | O(len(...))   | depends # (key,value) 2-tuples

Iteration     | for k in d:  | O(N)          | all forms: keys, values, items
	      	      	       		     | Worst: no return/break in loop
```



## 二、一些数据操作

1. defaultdict

```python
from collections import defaultdict
dic=defalutdict(func)
#这里的func可以为int（默认为1），list，set，也可以自己定义工厂函数
```

2. heapq（本身是用list作为载体实现的）

```python
import heapq
1. heapq.heappush(heap, item)#将值 item 插入到堆中，保持堆的排序。
2. heapq.heappop(heap)#弹出并返回 heap 的最小元素，且保持堆的排序。如果堆为空，则会引发
IndexError 。
3. heapq.heappushpop(heap, item)#将 item 插入堆中，并弹出并返回之前的最小元素。该操作比分别调用 heappush() 和 heappop() 要快。
4. heapq.heapreplace(heap, item)#弹出并返回 heap 的最小元素，并将 item 插入堆中。该操作比heappop() 后跟 heappush() 要快。
5. heapq.heapify(x)#将列表 x 转换为合法的堆，在线性时间内，重新排列列表中的元素。
6. heapq.nlargest(n, iterable[, key])#返回 iterable 中 n 个最大元素的列表，使用 key 函数进行排序。
7. heapq.nsmallest(n, iterable[, key])#返回 iterable 中 n 个最小元素的列表，使用 key 函数进行排序。
```

如果本身是heapq只需要一直用以上函数即可保持堆结构，否则要调用5

相应懒删除/懒更新（或者另开一个字典存放未更新的值）（这种往往用于只考察该heap中最小值，不过heapq好像就是用来干这个的）

```python
#每次要删除x时out[x]+=1
from heapq import heappop,heappush
while ls:
    x = heappop(ls)
    if not out[x]:
        new_min = x
        heappush(ls,x) #不需要弹出的，记得压回去
        break
    out[x]-=1
```

3. deque

```python
from collections import deque
d=deque()#可用len(deque),和list,str一样可以用iterable.count(x)计数x出现次数复杂度O(n)
d.pop()'右弹出'		d.popleft()'左弹出'
d.append()'右添加'		d.appendleft()'左添加'
d.extend()'右扩展'		d.extendleft()'左扩展'
d.rotate()#将双向队列向右旋转 n 步。n 为正，右侧的元素会移动到左侧；n 为负,相反。
```

4. Queue（先进先出队列FIFO）

```python
from queue import Queue
q=Queue()#不能用len
q.qsize()		q.empty()#空返回True
q.put()			q.get()
```

5. LifoQueue（后进先出队列LIFO，栈）PriorityQueue（优先队列）

```python
from queue import LifoQueue/PriorityQueue
q=LifoQueue()/PriorityQueue#操作与Queue相同，只是后进入的会被先弹出
```



## 三、一些记不住的小操作

1. 排序sort加lambda

```python
list.sort(key=lambda x: x[i])#也可以用dic[x，或者不用lambda,直接def函数也可
```

2. 列表倒序 `list[::-1]`
3. 大小写切换&删空格
```python
str.upper()		str.lower()		str.title()
str.rstrip()	str.lstrip()	str.strip()
```
4. python字典别滥用，可能数据奇怪会导致降重（出问题换list试试）
5. 进制：2进制`bin()`输出0b...，八进制`oct()`输出0o...，十六进制`hex()`输出0x...，`int(str,base)`可以把字符串按照指定进制转为十进制默认base=10
6. lru_cache

```python
from functools import lru_cache
@lru_cache(maxsize=128)#tle了加大，mle了减小
def func():
```

7. 扩栈(莫名其妙都可以用，不局限于RE)

```python
import sys
sys.setrecursionlimit(1<<30)
```

8. tuple比list好
9. 用真值表好过in得多
10. 数据预处理
11. 直接退出程序

```python
import sys
sys.exit()
```

12. 学区房

```python
(10,90) (20,180) (30,270)的接受方式（并对括号内求和）
pairs = [i[1:-1] for i in input().split()]#split开并脱掉()
distances = [ sum(map(int,i.split(','))) for i in pairs]#split(',')
```

13. 矩阵太大导致mle

```python
import array
arr=array.array(typecode,iterable(可以没有))#当作正常list用就行
#typecode:'b'--int,-128~127,'B'--int,0~255;'h','H'类似上述大小65536,'i','I'大小65536**2;'f'单精度浮点,'d'双精度浮点
```

14. 取小数和format

```python
#格式化输出：
print("Name: {}, Age: {}".format(name, age))#或者
print(f"Name: {name}, Age: {age}")
#小数：
print('{:.2f}'.format(num))
print(f"{num:.2f}")
print(round(num,2))
#可能会在1.345舍入到1.34，这是需要使用decimal
from decimal import Decimal,ROUND_HALF_UP
print(Decimal('1.345').quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))#1.35
#也可用floor(x*(10**n)+5)/(10**n)其中n为位数
```

15. count，find，index

```python
iterable.count(value)
str.find(sub)#抛出-1
list.index(x)#抛出ValueError
```

16. try&except

```python
try:	blabla
except:		blabla#error可以为ValueError,IndexError,KeyError,ZeroDivisionError(或许可以用来判RE是因为什么？试了一下确实可行)
except ValueError:		blabla
```

17. bisect

```python
import bisect
bisect.bisect_left(a,x)		bisect.bisect_right(a,x)#从左/右边看插入位置O(logn)
bisect.insort_left(a,x)		bisect.insort_right(a,x)#从左/右边看插入O(n)
```

18. deepcopy

```python
from copy import deepcopy
a=deepcopy(b)
```

19. math

```python
import math
math.pi		math.e
math.sqrt(isqrt带取整)		math.pow(x,y)=x**y		math.log(x,base)
math.floor()		math.ceil()		math.factorial()#阶乘
math.gcd(*integers)		math.lcm(*integers)		math.comb(n,k)#Cnk
math.dist(p,q)#p,q为两个大小相同数组，计算欧氏距离
math.prod(iterable,start)#计算iterable所有数乘积在start上
math.isclose(a,b)#浮点数避免a==b可以a-b==0或者用这个判断
```

20. ord&chr

```python
ord()把字符变为ASCII		chr()把ASCII变为字符
```

21. print调试用完记得注释，记得看清楚输出格式（参见Maya Calendar）
22. Counter

```python
from collections import Counter
c=Counter(iterable)#返回一个类似于字典的东西
c.update(另一个Counter)	c.most_common(k)#返回次数最多的k个成Counter相同的按出现顺序
```

23. calendar

```python
import calendar
calendar.isleap(year)#返回T，F判断闰年
```

24. 反复计算高次幂可能超时，不妨打表存下来调用会更快
25. zip

```python
a=zip(lst1,lst2,lst3...)#将这些合成一个列表，每一个元素为对应拼成的元组
```

26. 生成笛卡尔积（防止套一堆for）

```python
from itertools import product
a=[...]		b=[...]		...
res=list(product(a,b,...))#生成一个列表，内部元素为元组
```

27. dfs注意起始点和终点纠缠（重合）等特殊情况（WA自己构造数据检验）

28. infinite（注意可能不为零操作下默认值，所以要注意加特判防止输出inf）

```python
float('inf')		float('-inf')
```

29. 两个东西时分别开列表、字典维护，注意可以多用一些数据来标记维护这样可能降低时间复杂度
30. 逆向思维(尤其是greedy)

31. 拼接列表，注意list里面元素应当是str

```python
str.join(list)
```

32. 前缀和打表来实现任意段的和
33. (-1)//2=-1这是用来注意看到马走日不要随意取中点
34. min，max对于空列表不起作用
35. 给定的数据精度float（eg. 网线主管那样告诉每个数都是两位小数）可以直接将其转化为int解决，防止python浮点数发癫
36. 注意不要让代码变量名重复，可能会莫名WA
37. float这种东西少作运算
38. permutations&combinations

```python
from itertools import permutations,combinations
a=permutations(list)#生成list的全排列（每个以元组形式存在）
b=combinations(list,k)#生成list的k元组合（无序）（每个以元组形式存在）
```

39. 用带key的sort排序时对于相同的key是按照原来顺序排放的，因此如果需要应该再加参数



## 四、一些代码

1. 埃氏筛

```python
def SieveOfEratosthenes(n, prime): 
    p = 2
    while (p * p <= n):# If prime[p] is not changed, then it is a prime 
    	if (prime[p] == True):# Update all multiples of p 
        	for i in range(p * 2, n+1, p): 
            	prime[i] = False
    	p += 1
```

2. 欧拉筛

```python
def euler(r):
    prime = [0 for i in range(r+1)]
    common = []
    for i in range(2, r+1):
        if prime[i] == 0:
            common.append(i)
        for j in common:
            if i*j > r:
                break
            prime[i*j] = 1
            if i % j == 0:
                break
    return prime 
```

3. kmp

```python
def constructLPS(pat):#构建lps
    m=len(pat)
    lps=[0]*m
    le=0
    i=1
    while i<m:
        if pat[i]==pat[le]:
            le+=1
            lps[i]=le
            i+=1
        elif le!=0:
            le=lps[le-1]
        else:
            lps[i]=0
            i+=1
    return lps
def search(pat,txt):#匹配并返回下标集（第一个数为下标）
    ind=[]
    m=len(pat)
    n=len(txt)
    lps=constructLPS(pat)
    i=0
    j=0
    while (n-i) >=(m-j):
        if pat[j]==txt[i]:
            i+=1
            j+=1
        if j==m:
            ind.append(i-m)
            j=lps[j-1]
        elif i<n and pat[j]!=txt[i]:
            if j==0:
                i+=1
            else:
                j=lps[j-1]
    return ind
```

4. 树状数组

```python
def lowbit(x):
    return x & -x
def update(trarr,n,i,val):#i的下标是1,...,n范围
    i+=1
    while i<=n:
        trarr[i]+=val
        i=i+lowbit(i)
def getsum(trarr,t):#前t个数求和
    t+=1
    s=0
    while t>0:
        s+=trarr[t]
        t-=lowbit(t)
    return s
```

5. 线段树

```python
#tree=[0]*(2*n)
def build(tree,arr,n):
    for i in range(n):
        tree[n+i]=arr[i]
    for i in range(n-1,0,-1):
        tree[i]=tree[i<<1]+tree[i<<1|1]
def update(tree,n,i,val):#i的范围是0,...,n-1
    i+=n
    tree[i]+=val
    while i>1:
        tree[i>>1]=tree[i]+tree[i^1]
        i>>=1
def query(tree,l,r,n):#0,...,n-1下标中的[l,r)的和
    res=0
    l+=n
    r+=n
    while l<r:
        if (l&1):
            res+=tree[l]
            l+=1
        if (r&1):
            r-=1
            res+=tree[r]
        l>>=1
        r>>=1
    return res
```



## 五、一些模板

1. 分发糖果，一种贪心，左边过一次之后再用右边过一次修正

```python
n=int(input())
ra=list(map(int,input().split()))
can=[1]*n
for i in range(1,n):
    if ra[i]>ra[i-1]:
        can[i]=can[i-1]+1
sta=1
#print(can)
res=can[-1]
for i in range(n-2,-1,-1):
    if ra[i]>ra[i+1]:
        sta+=1
    else:
        sta=1
    res+=max(can[i],sta)
print(res)
```

2. 二分法

```python
#求根问题（保证r-l<精度值）
def f(x):
    a=x**3-5*x**2+10*x-80
    return a
def mids(left,right,i):
    mid=(left+right)/2
    i+=1
    #print(i,mid)
    if i>500:
        return mid
    elif f(left)*f(mid)<0:
        return mids(left,mid,i)
    else:
        return mids(mid,right,i)
a=mids(0,10,1)
a="{:.9f}".format(a)
print(a)
```

```python
#排序可以直接用bisect
```

```python
#最大值的最小值（反之亦然），河中跳房子，其实暗藏贪心，就是在检验t是不是解的时候
l,n,m=map(int,input().split())
ps=[]
for i in range(n):
    ps.append(int(input()))
def bis(t):
    global ps,m,n
    pos=0
    num=0
    for i in range(n):
        if ps[i]-pos<t:
            num+=1
        else:
            pos=ps[i]
    if l-pos<t:
        num+=1
    #print(num)
    if num>m:
        return 1
    else: 
        return 0
le=0
ri=2*l
while le<ri:
    #print(le,ri)
    mid=(le+ri)//2
    if not bis(mid):
        le=mid+1
    else:
        ri=mid
print(le-1)
#重新总结：本题是针对于有限m步操作下所能实现的min的max，（m越大结果越大）做法是取一个[l,r]潜在结果的闭区间，然后对于mid验证，这里注意验证有两种结果操作大于m步，这是不可行的，因此mid不可用，而结果就必然小于m，就让r=mid-1，若是小于等于m步，则有可能可行，故l=mid，但当最后让l==r时，需要不进入死循环，故应当mid=(l+r+1)//2，这样完成闭环（即mid应偏向于不取mid的那个）
#原来的想法则是用二分找到了最小的不符合要求的解，因此减一
#还有一种就是l=mid+1,r=mid-1,最后答案l-1
```

```python
#求数列平衡点，求极值均可以使用
```

```python
#或者一系列具有某种单调性质的结果（给定精度），注意结果是整数不一定意味着要mid=//2，有可能只是精度为整数，这是直接mid=/2，最后取四舍五入
```

3. 背包dp

```python
#0-1背包的memory简化
f[i][l]=max(f[i-1][l],f[i-1][l-w[i]]+v[i])#这要二维数组i为进行到第i个物品，l为最大容量
for i in range(1, n + 1):#这时只需要一维，l为最大容量，通过反复更新维护
    for l in range(W, w[i] - 1, -1):#必须这样逆序，要让每个f只被更新一次
        f[l] = max(f[l], f[l - w[i]] + v[i])
```

```python
#完全背包（每件物品可以选择任意次）
f[i][l]=max(f[i-1][l],f[i][l-w[i]]+v[i])#这要二维数组i为进行到第i个物品，l为最大容量
for i in range(1, n + 1):#这时只需要一维，l为最大容量，通过反复更新维护
    for l in range(0, W - w[i] + 1):#此时要正序，根本原因是可以多次选择
        f[l + w[i]] = max(f[l] + v[i], f[l + w[i]])
```

```python
#多重背包（物品选择指定次）
#朴素想法转化为0-1背包，可能超时，因此考察二进制拆分（先尽力拆为1，2，4，8...)
import math
k=int(math.log(x,2))
    for i in range(k+2):
        if x>=2**i:
            x-=2**i
            coi.append(y*(2**i))
        else:
            coi.append(x*y)
            break
```

4. bfs

```python
#最初的版本，用deque且原地修改（其实不好，比较麻烦最好用vis列表或数组），连通块
from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y):
    global mat
    tg=deque([(x,y)])
    while tg:
        po=tg.popleft()
        mat[po[0]][po[1]]=0
        for ii in range(4):
            nx=po[0]+dx[ii]
            ny=po[1]+dy[ii]
            if mat[nx][ny]:
                tg.append((nx,ny))
n,m=map(int,input().split())
mat=[]
mat.append([0]*(m+2))
for i in range(n):
    mat.append([0]+list(map(int,input().split()))+[0])
mat.append([0]*(m+2))
num=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if mat[i][j]:
            bfs(i,j)
            num+=1
print(num)
```

```python
#用到Queue且用vis数组，马走日蹩腿，确实把vis写为列表用in最好
from queue import Queue
n,m,x,y=map(int,input().split())
kk=int(input())
dx=[2,2,-2,-2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2]
ddx=[1,1,-1,-1,0,0,0,0]
ddy=[0,0,0,0,1,-1,1,-1]
che=[]
che.append(['w']*(m+4))
che.append(['w']*(m+4))
for i in range(n):
    che.append(['w','w']+[-1]*m+['w','w'])
che.append(['w']*(m+4))
che.append(['w']*(m+4))
for k in range(kk):
    xx,yy=map(int,input().split())
    che[xx+1][yy+1]='w'
vis=[]
vis.append(['w']*(m+4))
vis.append(['w']*(m+4))
for i in range(n):
    vis.append(['w','w']+[0]*m+['w','w'])
vis.append(['w']*(m+4))
vis.append(['w']*(m+4))
#print(che)
def bfs(x,y):
    global che,vis
    q=Queue()
    q.put((x+1,y+1))
    k=0
    che[x+1][y+1]=0
    vis[x+1][y+1]=1
    while not q.empty():
        w=q.qsize()
        k+=1
        for i in range(w):
            fa=q.get()
            for ii in range(8):
                nx=fa[0]+dx[ii]
                ny=fa[1]+dy[ii]
                mx=fa[0]+ddx[ii]
                my=fa[1]+ddy[ii]
                if che[nx][ny]!='w' and che[mx][my]!='w' and not vis[nx][ny]:
                    q.put((nx,ny))
                    che[nx][ny]=k
                    vis[nx][ny]=1
bfs(x,y)
#print(che)
for i in range(n):
    for j in range(m-1):
        if che[i+2][j+2]!='w':
            print(che[i+2][j+2],end=' ')
        else: print(-1,end=' ')
    if che[i+2][m+1]!='w':
        print(che[i+2][m+1])
    else: print(-1)
```

```python
#走山路的heapq，事实上应该和Dijkstra除了没有记录父节点没什么区别（应该？
#核心是所谓的出队vis其实就是Dijkstra挑出目前nonvis的最近点让他走遍就vis
#出队标记不可乱用因为本身出队vis是验尸过程，这导致了冗余计算，且heapq的pop,push速度均为logn
#因此他特殊在于是用带权的边，并且权非负（最小权值路）
import heapq
m,n,p=map(int,input().split())
mat=[]
mat.append(['#']*(n+2))
for i in range(m):
    mat.append(['#']+list(input().split())+['#'])
mat.append(['#']*(n+2))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(p):
    x1,y1,x2,y2=map(int,input().split())
    if mat[x1+1][y1+1]=='#' or mat[x2+1][y2+1]=='#':
        print('NO')
        continue
    vis=set()
    def bfs(x1,y1,x2,y2):
        que=[(0,x1,y1)]
        vis.add((x1,y1))
        while que:
            cos,x,y=heapq.heappop(que)
            vis.add((x,y))
            if x==x2 and y==y2:
                return cos
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if (nx,ny) not in vis and mat[nx][ny]!='#':
                    heapq.heappush(que,(cos+abs(int(mat[x][y])-int(mat[nx][ny])),nx,ny))
                    #vis.add((nx,ny))
        return 'NO'
    ans=bfs(x1+1,y1+1,x2+1,y2+1)
    print(ans)
```

5. dfs

好像说dfs也可以用stack即上述LifoQueue，似乎可以避免爆栈（？，但我也不会

在图搜索中似乎求最小的东西比较好用bfs，而对于求最大权值，最长步伐，所有方法总数可能还是需要全枚举得到

```python
#最初始的写法用函数递归，也是当地修改
n,m=map(int,input().split())
mat=[]
mat.append([1]*(m+2))
for i in range(n):
    mat.append([1]+list(map(int,input().split()))+[1])
mat.append([1]*(m+2))
mat[1][1]='s'
mat[n][m]='e'
dx=[1,-1,0,0]
dy=[0,0,1,-1]
num=0
#print(mat)
def dfs(mat,x,y):
    global num
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if mat[nx][ny]=='e':
            num+=1
        elif mat[nx][ny]==0:
            mat[x][y]=1
            dfs(mat,nx,ny)
            mat[x][y]=0
dfs(mat,1,1)
print(num)
```

```python
#gpt写的用stack的写法，备用着吧
import queue
def dfs(graph, start):
    visited = set()
    stack = queue.LifoQueue()
    stack.put(start)
    while not stack.empty():
        current_node = stack.get()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.put(neighbor)
# 图的邻接表表示
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs(graph, 'A')
```

```python
#带权的，这就是求最大的
n,m=map(int,input().split())
mat=[]
mat.append([-999]*(m+2))
for i in range(n):
    mat.append([-999]+list(map(int,input().split()))+[-999])
mat.append([-999]*(m+2))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
su=float("-inf")
#print(mat)
tempath=[(1,1)]
ultpath=[(1,1)]
def dfs(mat,x,y,tsu):
    global su,ultpath
    if x==n and y==m:
        if tsu> su:
            su=tsu
            ultpath=list(tempath)
            #print(tempath)
            #print(ultpath)
            return 0
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if mat[nx][ny]!=-999:
                tem=mat[x][y]
                mat[x][y]=-999
                tempath.append((nx,ny))
                dfs(mat,nx,ny,tsu+mat[nx][ny])
                tempath.pop()
                mat[x][y]=tem
dfs(mat,1,1,mat[1][1])
for spot in ultpath:
    print(spot[0],end=' ')
    print(spot[1])
```

```python
#dfs+lru_cache(dp)，最长路
from functools import lru_cache
r,c=map(int,input().split())
mat=[]
mat.append([10001]*(c+2))
for i in range(r):
    mat.append([10001]+list(map(int,input().split()))+[10001])
mat.append([10001]*(c+2))
dx=[1,-1,0,0]
dy=[0,0,1,-1]
#print(mat)
@lru_cache(maxsize=1024)
def dp(x,y):
    ans=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if mat[x][y]>mat[nx][ny]:
            ans=max(ans,1+dp(nx,ny))
    return ans
ans=0
for i in range(1,r+1):
    for j in range(1,c+1):
        ans=max(ans,dp(i,j))
        #print(i,j,dp(i,j))
print(ans)
```

```python
#事实上对于走迷宫这种东西dfs似乎是不如bfs因为dfs最差情况就是全枚举，所以感觉就是一个全枚举的方便写法，以下是双十一2022，需要注意的是npr(now_price)的先加后减的回溯
n,m=map(int,input().split())
pris=[]
for i in range(n):
    dic={}
    a=input().split()
    for x in a:
        d,p=map(int,x.split(':'))
        dic[d]=p
    pris.append(dic)
cous=[]
for i in range(m):
    dic={}
    a=input().split()
    for x in a:
        y,j=map(int,x.split('-'))
        dic[y]=j
        dic={k:dic[k] for k in sorted(dic,reverse=True)}
    cous.append(dic)
npr=[0]*m
ans=float("inf")
def dfs(k):
    global npr,ans
    if k==n:
        nan=sum(npr)
        nan-=(nan//300)*50
        for i in range(m):
            cou=cous[i]
            for y,j in cou.items():
                if npr[i]>=y:
                    nan-=j
                    break
        ans=min(nan,ans)
    else: 
        pri=pris[k]
        for x,p in pri.items():
            npr[x-1]+=p
            dfs(k+1)
            npr[x-1]-=p
dfs(0)
print(ans)

#至于八皇后
def valid(i,x,j,y):
    if x==y:
        return False
    elif abs(i-j)==abs(x-y):
        return False
    else:
        return True
def dfs(k):
    global st,que
    if k<8:
        for i in range(8):
            sta=True
            for j in range(k):
                if not valid(j,st[j],k,i+1):
                    sta=False
                    #print('a')
            if sta:
                st.append(i+1)
                dfs(k+1)
                st.pop()
    else:
        #print(int(''.join(map(str,st))))
        que.append(int(''.join(map(str,st))))
        #print(len(que))
        return
que=[]
for ii in range(8):
    st=[ii+1]
    dfs(1)
n=int(input())
for i in range(n):
    print(que[int(input())-1])
```

