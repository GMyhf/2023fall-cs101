# 每日选做



Updated 1940 GMT+8 Dec 28, 2023

2023 fall, Complied by 邓锦文 23级 物理学院



闫老师，这是我的每日选做，里面有OJ和CF的一些题目，发给您，如果有需要的你使用就好。



### 2023.11.15

#### 1、最短的愉悦旋律长度

http://cs101.openjudge.cn/routine/27103/

这道题最开始真是一点思路没有...后面在同学的帮助下才算明白——首先，要找的是**存在的**一个最短序列的长度。

这就说明了我们要找的是只要有，就可以，对于其他的，无需考虑。

**那么，怎么样才能知道存在这么一个序列呢？**

考虑**倒序**。

我们不断地扫到所有种类数字（无序，举个例子，找到了两部分所有数字都有的，那么长度为2的子序列就全部都在里面了），扫完一次加个1。这样相当于进行了分块，由于子序列是按照顺序来的，那么显然，分块之后剩下的那部分中就一定有没有出现的数字了，我们的目的也就达到了。

代码：

```python
N,M = map(int,input().split())
lst = list(map(int,input().split()))
count = 0
judge = set()
for i in range(N):
    judge.add(lst[i])
    if len(judge) == M:
        judge = set()
        count += 1
print(count+1)
```



#### 2、矩阵换行求边缘和

http://cs101.openjudge.cn/routine/20731/

比较基础。

代码：

```python
m,n = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(m)]
x,y = map(int,input().split())
matrix[x-1],matrix[y-1] = matrix[y-1],matrix[x-1]
num = sum(matrix[0]) + sum(matrix[-1])
for i in range(1,m-1):
    num += matrix[i][0] + matrix[i][-1]
print(num)
```



#### 3、河中跳房子

http://cs101.openjudge.cn/routine/08210/

这道题使用二分的思想，说实话最开始我确实没什么思路。之后也去看了题解，得到了这样的想法：设出来最短跳跃距离（这里就已经有一点特殊之处了，那就是设出来未知量认为已知，然后去带。这可以说是二分法的精髓所在），去计算要拿掉的岩石数量，再和M去比较。那么不断地比较最后就可以得到正确答案了，真的挺巧妙的。

代码：

```python
L,N,M = map(int,input().split())
D_lst = [0]+[int(input()) for _ in range(N)]+[L]
low,high = 0,L
answer = -1
while high-low > 1e-6:
    distance = (low + high)//2
    count = 0
    num = 0
    for d in D_lst[1:]:
        if d-num < distance:
            count += 1
        else:
            num = d
    if count <= M:
        low = distance + 1
        answer = distance
    elif count > M:
        high = distance
print(answer)
```





### 2023.11.16

#### 1、红蓝玫瑰

http://cs101.openjudge.cn/routine/25573/

哇...这个题当时确实没有想明白怎么使用dp欸。知道看到题解之后才发现——我的天，分成全变红和全变蓝就可以？！

那之后就很简单了...

代码：

```python
rose_lst = list(input())
n = len(rose_lst)
dp_R = [0]*(n+1)
dp_B = [0]*(n+1)
for k in range(1,n+1):
    if rose_lst[k-1] == "R":
        dp_B[k] = min(dp_B[k-1] + 1,dp_R[k-1] + 1)
        dp_R[k] = min(dp_B[k-1] + 1,dp_R[k-1])
    else:
        dp_B[k] = min(dp_B[k-1],dp_R[k-1] + 1)
        dp_R[k] = min(dp_B[k-1] + 1,dp_R[k-1] + 1)
print(min(dp_B[-1]+1,dp_R[-1]))
```



#### 2、Fence Repair

http://cs101.openjudge.cn/routine/05333/

这道题说可以应用Huffman树来解决，所以我去查了一下，发现Huffman树有将最小值存储进入根部的特点（不知道理解的对不对）。这确实启发了我，我们可以反过来想，将木板合并，那么不断地选取最短的两个木板就可以了。

代码：

```python
import heapq
N = int(input())
my_heapq = [int(input()) for _ in range(N)]
heapq.heapify(my_heapq)
cost = 0
while len(my_heapq) > 1:
    num_1 = heapq.heappop(my_heapq)
    num_2 = heapq.heappop(my_heapq)
    cost += num_1+num_2
    my_heapq.append(num_1+num_2)
print(cost)
```



#### 3、砝码称重

http://cs101.openjudge.cn/routine/04141/

...没想到啊，这是个dfs。确实没太见过，所以还是记一下思路和技巧。

P.S:递归函数的使用很巧妙，值得学习。

代码：

```python
weights = [1,2,3,5,10,20]
def dfs(num,w):
    if num == 6:
        if w != 0:
            w_set.add(w)
        return
    for i in range(w_lst[num]+1):
        dfs(num+1,w+i*weights[num])

w_lst = list(map(int,input().split()))
w_set = set()
dfs(0,0)
print(f'Total={len(w_set)}')
```



#### 4、方程求解

http://cs101.openjudge.cn/routine/04140/

标准的二分法求解方程，无需多言。

代码：

```python
low = 0
high = 10
while high - low > 1e-10:
    x = (low+high)/2
    g = x ** 3 - 5 * (x ** 2) + 10 * x - 80
    if g > 0:
        high = x
    elif g < 0:
        low = x
print(f'{x:.9f}')
```



#### 5、不定方程求解

http://cs101.openjudge.cn/routine/04139/

较为基础的遍历，无需多言。

代码：

```python
a,b,c = map(int,input().split())
x = 0
y = 0
count = 0
while True:
    y = (c-a*x)/b
    if y < 0:
        break
    if y - int(y) == 0:
        count += 1
    x += 1
print(count)
```



#### 6、最小新整数

http://cs101.openjudge.cn/routine/04137/

这道题又给我狠狠地上了一课...简单捋一下思路：1、左边的数字比右边的大就要删除；2、删除的话索引会变化，最后要的是严格递增序列。搞清楚这两点，就没有什么问题了。

代码：

```python
t = int(input())
result = []
for _ in range(t):
    n,k = map(int,input().split())
    lst = list(str(n))
    count = 0
    x = 0
    while x < len(lst)-1:
        if int(lst[x]) > int(lst[x+1]):
            count += 1
            lst.pop(x)
            x = max(0,x-1)
        else:
            x += 1
        if count == k:
            break
    if count < k:
        m = len(lst)
        lst = lst[:m-k+count]
    num = "".join(lst)
    result.append(num)
for letter in result:
    print(letter)
```



#### 7、矩形分割

http://cs101.openjudge.cn/routine/04136/

这道题的数据强度有点离谱啊。思路是简单的，就是计算相应的面积，然后比较就好了，主要是简化代码需要费一番功夫。

代码：

```python
R = int(input())
N = int(input())
lst = [0]*(R+1)
for _ in range(N):
    L,T,W,H = map(int,input().split())
    for x in range(W):
        lst[L+x] += H
total = sum(lst)
count = 0
answer = 0
min_num = total
for k in range(1,R+1):
    count += lst[k-1]
    num = 2*count - total
    if 0 <= num <= min_num:
        answer = k
        min_num = num
print(answer)
```



#### 8、月度开销

http://cs101.openjudge.cn/routine/04135/

又是二分+贪心！好离谱...只能说对于这种题目一定要注意陷入死循环的可能情况并预防。

代码：

```python
N,M = map(int,input().split())
lst = [int(input()) for _ in range(N)]
low = 0
high = sum(lst)
while low < high:
    x = (low+high)//2
    count,total,k = 0,0,0
    judge = False
    while k < N:
        if x < lst[k]:
            low = x+1
            judge = True
            break
        else:
            total += lst[k]
            if x < total:
                count += 1
                total = 0
            elif x == total:
                count += 1
                k += 1
                total = 0
            else:
                k += 1
    if not judge:
        if count < M:
            high = x
        else:
            low = x+1
print(low)
```





### 2023.11.17

#### 1、查找最接近的元素

http://cs101.openjudge.cn/routine/04134/

这个题真的...没想到会做这么久！

其实就是一个简单的二分查找，但是对于条件的简化和处理真的太重要了！！！

现在还是对于条件说一下吧：1、low如果为n，那么就直接return lst[low-1]；2、如果low为0，直接return lst[low]；3、要对于low还是low-1处的元素更接近做判断。

代码：

```python
def find(lst,x):
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] == x:
            return lst[mid]
        elif lst[mid] < x:
            low = mid+1
        else:
            high = mid-1
    if low < n and (low == 0 or abs(lst[low]-x) < abs(lst[low-1]-x)):
        return lst[low]
    else:
        return lst[low-1]

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
result = []
for _ in range(m):
    a = int(input())
    answer = find(lst,a)
    result.append(answer)
for letter in result:
    print(letter)
```





### 2023.11.18

#### 1、垃圾炸弹

http://cs101.openjudge.cn/routine/04133/

比较简单的矩阵问题，就老老实实写，然后比较就可以了。

代码：

```python
d = int(input())
n = int(input())
lst = [[0]*1025 for _ in range(1025)]
for _ in range(n):
    x,y,i = map(int,input().split())
    for p in range(max(0,x-d),min(1025,x+d+1)):
        for q in range(max(0,y-d),min(1025,y+d+1)):
            lst[p][q] += i
count,max_num = 0,0
for a in range(1025):
    for b in range(1025):
        if lst[a][b] > max_num:
            max_num = lst[a][b]
            count = 1
        elif lst[a][b] == max_num:
            count += 1
print(count,max_num)
```



#### 2、Charm Bracelet

http://cs101.openjudge.cn/routine/04131/

这道题跟小偷背包一模一样，结果用原来的代码不行，真的离谱。之后看群里面的消息才知道，原来这种时候可以尝试使用pypy，最后也是拿pypy过的...

代码：

```python
N,M = map(int,input().split())
dp = [0]*(M+1)
lst = [map(int,input().split()) for _ in range(N)]
for i in range(1,N+1):
    w,v = lst[i-1]
    for j in range(M,w-1,-1):
        dp[j] = max(dp[j],dp[j-w]+v)
print(dp[M])
```





### 2023.11.19

今天摆烂...



### 2023.11.20

#### 1、单词序列

http://cs101.openjudge.cn/routine/04128/

终于做出来了一道BFS的题目了！开心！

代码：

```python
from collections import deque

def find(start,end,lst):
    my_dict = set(lst)
    queue = deque([(start,1)])
    while queue:
        word,length = queue.popleft()
        if word == end:
            return length
        for i in range(len(word)):
            for j in range(26):
                char = list("abcdefghijklmnopqrstuvwxyz")
                new_word = word[:i] + char[j] + word[i + 1:]
                if new_word in my_dict:
                    my_dict.remove(new_word)
                    queue.append((new_word, length + 1))
                elif new_word == end:
                    return length + 1
    return 0

start,end = input().split()
lst = input().split()
result = find(start,end,lst)
print(result)
```



#### 2、变换的迷宫

http://cs101.openjudge.cn/routine/04129/

这道题做了一个下午，太离谱了！

总结起来，一方面需要注意石头的周期性变化从而定下访问相应状态的限制，另一方面需要注意对于内存的限制。

代码：

```python
from collections import deque

def find(R,C,K,maze):
    x,y,m,n = 0,0,0,0
    judge = 0
    for i in range(R):
        for j in range(C):
            if maze[i][j] == "S":
                x,y = i,j
                judge += 1
                if judge == 2:break
            elif maze[i][j] == "E":
                m,n = i,j
                judge += 1
                if judge == 2:break
    row_nums = [-1,0,1,0]
    col_nums = [0,1,0,-1]
    queue = deque([(x,y,0)])
    visited = [[[True]*K for _ in range(C)] for _ in range(R)]
    while queue:
        node = queue.popleft()
        time = node[2] + 1
        for k in range(4):
            row = node[0] + row_nums[k]
            col = node[1] + col_nums[k]
            if row == m and col == n: return time
            if 0 <= row < R and 0 <= col < C:
                if (((maze[row][col] == "." or maze[row][col] == "S") and visited[row][col][time % K])
                        or (maze[row][col] == "#" and visited[row][col][time % K] and time % K == 0)):
                    visited[row][col][time % K] = False
                    queue.append((row,col,time))
    return "Oop!"

T = int(input())
for _ in range(T):
    R,C,K = map(int,input().split())
    maze = [list(input()) for _ in range(R)]
    answer = find(R,C,K,maze)
    print(answer)
```





### 2023.11.22

这里先说一句，那些BFS/DFS是真的做不来啊...





### 2023.11.23

#### 1、两球之间的磁力

http://cs101.openjudge.cn/routine/27122/

显然就是贪心+二分，但是我居然因为最开始的一处写错了而导致改了好久...

代码：

```python
def judge(a):
    count,left = 1,nums[0]
    for k in range(1,n):
        if nums[k] - left >= a:
            count += 1
            left = nums[k]
    return count >= m

n,m = map(int,input().split())
nums = sorted(list(map(int,input().split())))
low = 0
high = nums[-1] - nums[0]
ans = 0
while low <= high:
    x = (low+high)//2
    if judge(x):
        ans = x
        low = x+1
    else:
        high = x-1
print(ans)
```



#### 2、最大上升子序列

http://cs101.openjudge.cn/routine/02757/

这道题确实没想到...很巧妙的方法啊，双重循环不断修正来得到想要的值。

代码：

```python
N = int(input())
nums = list(map(int,input().split()))
dp = [1]*N
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+1,dp[i])
print(max(dp))
```



然后，这里再做了一道最大上升子序列和的题目（http://cs101.openjudge.cn/practice/03532/），作为补充，确实都很有意思。

代码：

```python
N = int(input())
nums = list(map(int,input().split()))
dp = [0]*N
for i in range(N):
    dp[i] = nums[i]
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+nums[i],dp[i])
print(max(dp))
```



#### 3、简单的整数划分问题

https://cs101.openjudge.cn/routine/04117/

这道题对于动态规划考的挺难，但是想明白就很简单了。主要在于要知道怎么对于划分方案进行分解。

还有一点，注意题目的说明，应该使用 try&except 结构。

代码：

```python
while True:
    try:
        N = int(input())
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        for k in range(1, N + 1):
            dp[k][1], dp[1][k] = 1, 1
        for m in range(N + 1):
            dp[0][m] = 1
        for i in range(2, N + 1):
            for j in range(2, N + 1):
                if i < j:
                    dp[i][j] = dp[i][i]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - j][j]
        print(dp[N][N])
    except EOFError:
        break
```



#### 4、复杂的整数划分问题

http://cs101.openjudge.cn/routine/04119/

很有意思啊...感觉这么一道题对于动态规划的考察已经很深了。

代码：

```python
def divide(N,K):
    dp = [[0]*(N+1) for _ in range(N+1)]
    for x in range(1,N+1):
        dp[x][1] = 1
    for i in range(2,N+1):
        for j in range(2,N+1):
            if i >= j:
                dp[i][j] = dp[i-j][j] + dp[i-1][j-1]
    return dp[N][K]

def divide_dif(N):
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i < j:
                dp[i][j] = dp[i][i]
            elif i == j:
                dp[i][j] = dp[i][j-1] + 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-j][j-1]
    return dp[N][N]

def divide_odd(N):
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            if j % 2 == 0:
                dp[i][j] = dp[i][j-1]
            else:
                if i < j:
                    dp[i][j] = dp[i][i]
                elif i == j:
                    dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-j][j]
    return dp[N][N]

while True:
    try:
        N, K = map(int, input().split())
        print(divide(N, K))
        print(divide_dif(N))
        print(divide_odd(N))
    except EOFError:
        break
```



#### 5、开餐馆

http://cs101.openjudge.cn/routine/04118/

这道题就是一个简单的动态规划（亏我当时还没看出来...），对于对应餐馆的利润进行遍历就好。其实说起来，动态规划能否应用在于“无后效性”，那么我们怎么用就在于如何理解对应题目的无后效性。

代码：

```python
T = int(input())
result = []
for _ in range(T):
    n,k = map(int,input().split())
    locations = list(map(int,input().split()))
    profits = list(map(int,input().split()))
    dp = [0]*n
    dp[0] = profits[0]
    for i in range(1,n):
        dp[i] = max(dp[i-1],profits[i])
        for j in range(i):
            if locations[i] - locations[j] > k:
                dp[i] = max(dp[i],dp[j] + profits[i])
    result.append(dp[-1])
for letter in result:
    print(letter)
```



#### 6、最大公约数

http://cs101.openjudge.cn/routine/03248/

用欧几里得算法就可以轻松解决。

代码：

```python
def find(a,b):
    while b:
        a,b = b,a%b
    return a

while True:
    try:
        n,m = map(int,input().split())
        a,b = max(n,m),min(n,m)
        print(find(a,b))
    except EOFError:
        break
```





### 2023.11.24

#### 1、新数字三角形

http://cs101.openjudge.cn/routine/03263/

这道题看错题目了，找的是最大数而不是最大和。

代码：

```python
while True:
    N = int(input())
    if N == 0:
        break
    nums = [list(map(int,input().split())) for _ in range(N)]
    R,C = map(int,input().split())
    new_nums = []
    for i in range(N-R+1):
        new_nums.append(nums[R+i-1][C-1:C+i])
    max_num = 0
    for row in new_nums:
        for num in row:
            max_num = max(max_num,num)
    print(max_num)
```



#### 2、分解因数

http://cs101.openjudge.cn/routine/02749/

这道题，使用了递归的方法。感觉对于数学的考察比较注重，下面进行一点说明：

对于一个数n，我们想要找到它的所有乘法分解方式。根据题意及示例，我们可以发现，所有的乘法方式都是由质数乘法方式组合而成。但是从质数中挑选而组成合数从而构造乘法方式是复杂而且易错的，所以我们反其道而行之，对于这个数进行分解，同时规定从定义的x开始向上遍历，这也就避免了反向（如10*4）的重复情况。

代码：

```python
def recursion(n,x):
    if n == 1:
        return 1
    count = 0
    for k in range(x,n+1):
        if n % k == 0:
            count += recursion(n//k,k)
    return count

n = int(input())
for _ in range(n):
    print(recursion(int(input()),2))
```



#### 3、螃蟹采蘑菇

http://cs101.openjudge.cn/routine/25572/

这道题是一道典型的bfs（dfs还没学会呜呜呜...），主要是return yes的时候需要注意啊，也有要求的。

代码：

```python
 from collections import deque

def bfs(matrix,n):
    a, b, x1, y1, x2, y2, judge = -1, -1, -1, -1, -1, -1, 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 9:
                a, b = i, j
                judge += 1
                if judge == 3:
                    break
            if matrix[i][j] == 5:
                if x1 >= 0:
                    x2,y2 = i,j
                else:
                    x1,y1 = i,j
                judge += 1
                if judge == 3:
                    break

    if x1 == x2:
        check = True
        x,y = x1,min(y1,y2)
    else:
        check = False
        x,y = min(x1,x2),y1

    if check:
        queue = deque([(x, y)])
        row_nums = [-1, 0, 1, 0]
        col_nums = [0, 1, 0, -1]
        visited = [[True] * n for _ in range(n)]
        while queue:
            node = queue.popleft()
            for k in range(4):
                row = node[0] + row_nums[k]
                col = node[1] + col_nums[k]
                if 0 <= row < n and 0 <= col < n and 0 <= col + 1 < n:
                    if visited[row][col] and matrix[row][col] != 1 and matrix[row][col + 1] != 1:
                        if (row == a and col == b) or (row == a and col + 1 == b): return "yes"
                        queue.append((row, col))
                        visited[row][col] = False
        return "no"
    else:
        queue = deque([(x, y)])
        row_nums = [-1, 0, 1, 0]
        col_nums = [0, 1, 0, -1]
        visited = [[True] * n for _ in range(n)]
        while queue:
            node = queue.popleft()
            for k in range(4):
                row = node[0] + row_nums[k]
                col = node[1] + col_nums[k]
                if 0 <= row < n and 0 <= col < n and 0 <= row + 1 < n:
                    if visited[row][col] and matrix[row][col] != 1 and matrix[row + 1][col] != 1:
                        if (row == a and col == b) or (row + 1 == a and col == b): return "yes"
                        queue.append((row, col))
                        visited[row][col] = False
        return "no"

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
print(bfs(matrix,n))
```



#### 4、Coins

http://cs101.openjudge.cn/routine/01742/

这道题的数据有点离谱啊……我先是把多重背包散开，分别当成一个来算，结果显然TLE；之后用二进制优化，把n个分成1、2、4...这样的进行运算，但是自己写的确实慢了很多，基本无差别；最后查看题解，发现不应该只是把数量分成1、2、4...那种的，而应该用m表示为一个二进制数，全是0和1，再进行位运算，这样最后就可以通过数1来得到答案了，非常的巧妙。

代码：

```python
import math

while True:
    n,m = map(int,input().split())
    if n == m == 0:break
    lst = list(map(int,input().split()))
    w = (1 << (m+1)) - 1
    result = 1
    for k in range(n):
        num = lst[k+n]+1
        limit = int(math.log(num,2))
        rest = num - (1 << limit)
        for j in range(limit):
            result = (result | (result << (lst[k]*(1 << j)))) & w
        if rest:
            result = (result | (result << (lst[k]*rest))) & w
    print(bin(result).count("1")-1)
```





### 2023.11.26

#### 1、完美的爱

http://cs101.openjudge.cn/routine/27141/

利用前缀和的思想，就可以进行筛选和计算了，但是为什么我想了这么久啊……

代码：

```python
n = int(input())
lst = list(map(int,input().split()))
nums = []
for l in lst:
    nums.append(l-520)
my_dict = {0:-1}
max_len = 0
count = 0
for i in range(n):
    count += nums[i]
    if count in my_dict.keys():
        max_len = max(max_len,i-my_dict[count])
    else:
        my_dict[count] = i
print(max_len*520)
```



#### 2、Divisibility by Eight 加强版

http://cs101.openjudge.cn/routine/27150/

这道题很精彩！这里的动态规划思想确实没想到，设前$$i$$个元素删去或不删某些元素得到的数字模$$8$$是否余$$j$$，由此，我们就得到了状态转移方程：
$$
dp[i][j]=dp[i-1][j],dp[i][(10*j+nums[i])mod8]=dp[i-1][j]
$$
这里$$dp[i][j]$$指的是前$$i$$个数组成的数，删去某些数字或不删之后模$$8$$能否得到$$j$$。显然，$$dp[i][0]$$为$$True$$时，就说明存在这样的数了。由于需要打出相应的数字，我们使用$$prev$$数组进行数字的记录，看要不要把相应数字往数组里面放，最后取出来并打印就可以了。

然而，这道题不仅限于此，对于数据结构的要求是很高的，同时测试数据也有点问题（比如说，664和64），我不得不在最后确定$$ans$$之前加一个判定系统，从而得到最短的答案，当然，对于题目来说，这个限制是不必要的。

代码：

```python
nums = [int(k) for k in list(input())]
n = len(nums)
dp = [False]*8
prev = [""]*8
ans = 0
judge = False

for i in range(n):
    temp_dp = [False]*8
    temp_prev = [""]*8
    current_mod = nums[i] % 8
    temp_dp[current_mod] = True
    temp_prev[current_mod] = str(nums[i])

    for j in range(8):
        if dp[j]:
            new_mod = (10 * j + nums[i]) % 8
            if not temp_dp[j]:
                temp_dp[j] = True
                temp_prev[j] = prev[j]
            if not temp_dp[new_mod]:
                temp_dp[new_mod] = True
                temp_prev[new_mod] = prev[j] + str(nums[i])

        if temp_dp[0]:
            temp_ans = temp_prev[0]
            m = len(temp_ans)
            for q in range(m):
                if int(temp_ans[q:]) % 8 == 0:
                    ans = temp_ans[q:]
            judge = True
            break

    if judge:
        break

    dp = temp_dp
    prev = temp_prev

if judge:
    print("YES")
    print(ans)
else:
    print("NO")

```





### 2023.11.27

#### 1、书架

http://cs101.openjudge.cn/routine/03406/

做多了动态规划看什么都是动态规划，结果就MLE了。注意：背包是由一个最大承重，也就是限制，但是这道题是要超过限制，有本质的区别（虽然用动规也还是可以做的）。

代码：

```python
N,B = map(int,input().split())
H_lst = [int(input()) for _ in range(N)]
H_lst.sort(reverse=True)
k,h = 0,0
while h < B:
    h += H_lst[k]
    k += 1
print(k)
```



#### 2、算24

http://cs101.openjudge.cn/routine/02787/

这道题主要考察递归，同时给我提了个醒，递归函数调用的时候很容易出现数据方面的问题从而导致错误，所以在本题中我们应该建立一个新的列表来存储新的数，否则就会出现错误。为了以后不出现这样的情况，我觉得干脆点，直接每次做题的时候都添一个临时变量，不算麻烦而且可以防止出错。

代码：

```python
while True:
    nums = list(map(int, input().split()))
    if nums == [0, 0, 0, 0]:
        break
    def cal(nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) <= 1e-6
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num1, num2 = nums[i], nums[j]
                remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
                if cal(remaining + [num1 + num2]) or cal(remaining + [abs(num1 - num2)]) or cal(remaining + [num1 * num2]):
                    return True
                if num2 != 0 and cal(remaining + [num1 / num2]):
                    return True
                if num1 != 0 and cal(remaining + [num2 / num1]):
                    return True
        return False
    if cal(nums):
        print("YES")
    else:
        print("NO")

```





### 2023.11.29

#### 1、假币问题

http://cs101.openjudge.cn/routine/02692/

挺简单的一道题，就是brute force，但是我的代码写的太长了……（或许是半夜的缘故）

代码：

```python
n = int(input())
for _ in range(n):
    test_1 = input().split()
    test_2 = input().split()
    test_3 = input().split()
    Alphabet = "ABCDEFGHIJKL"
    for letter in Alphabet:
        weight = 0
        judge = False
        check = True
        for letter_1 in test_1[0]:
            if letter_1 == letter:
                if test_1[2] == "up":
                    weight = 1
                    judge = True
                elif test_1[2] == "down":
                    weight = -1
                    judge = True
                check = False
                break
        for letter_1 in test_1[1]:
            if letter_1 == letter:
                if test_1[2] == "up":
                    weight = -1
                    judge = True
                elif test_1[2] == "down":
                    weight = 1
                    judge = True
                check = False
                break
        for letter_2 in test_2[0]:
            if check:
                if letter_2 == letter:
                    if test_2[2] == "up":
                        weight = 1
                        judge = True
                    elif test_2[2] == "down":
                        weight = -1
                        judge = True
                    check = False
                    break
            if letter_2 == letter:
                if weight == 1:
                    if test_2[2] != "up":
                        judge = False
                elif weight == -1:
                    if test_2[2] != "down":
                        judge = False
                else:
                    if test_2[2] != "even":
                        judge = False
                break
        for letter_2 in test_2[1]:
            if check:
                if letter_2 == letter:
                    if test_2[2] == "up":
                        weight = -1
                        judge = True
                    elif test_2[2] == "down":
                        weight = 1
                        judge = True
                    check = False
                    break
            if letter_2 == letter:
                if weight == 1:
                    if test_2[2] != "up":
                        judge = False
                elif weight == -1:
                    if test_2[2] != "down":
                        judge = False
                else:
                    if test_2[2] != "even":
                        judge = False
                break
        for letter_3 in test_3[0]:
            if check:
                if letter_3 == letter:
                    if test_3[2] == "up":
                        weight = 1
                        judge = True
                    elif test_3[2] == "down":
                        weight = -1
                        judge = True
                    check = False
                    break
            if letter_3 == letter:
                if weight == 1:
                    if test_3[2] != "up":
                        judge = False
                elif weight == -1:
                    if test_3[2] != "down":
                        judge = False
                else:
                    if test_3[2] != "even":
                        judge = False
                break
        for letter_3 in test_3[1]:
            if check:
                if letter_3 == letter:
                    if test_3[2] == "up":
                        weight = -1
                        judge = True
                    elif test_3[2] == "down":
                        weight = 1
                        judge = True
                    check = False
                    break
            if letter_3 == letter:
                if weight == 1:
                    if test_3[2] != "up":
                        judge = False
                elif weight == -1:
                    if test_3[2] != "down":
                        judge = False
                else:
                    if test_3[2] != "even":
                        judge = False
                break
        if judge:
            if weight == 1:
                print(f'{letter} is the counterfeit coin and it is heavy.')
            elif weight == -1:
                print(f'{letter} is the counterfeit coin and it is light.')
            break
```





### 2023.11.30

#### 1、合唱队形

http://cs101.openjudge.cn/routine/02711/

哇，真是学什么做什么的时候都会想着用那个东西……这道题用递归是会超时的，无语。这里放一下超时代码，说不定之后看到就知道怎么剪枝了：

```python
def left(lst,H):
    if len(lst) == 1:
        if lst[0] < H:
            return 1
        else:
            return 0
    if lst[-1] < H:
        return max(left(lst[:-1],lst[-1])+1,left(lst[:-1],H))
    else:
        return left(lst[:-1],H)

def right(lst,H):
    if len(lst) == 1:
        if lst[0] < H:
            return 1
        else:
            return 0
    if lst[0] < H:
        return max(right(lst[1:],lst[0])+1,right(lst[1:],H))
    else:
        return right(lst[:-1],H)

N = int(input())
h_lst = list(map(int,input().split()))
ans = max(right(h_lst[1:],h_lst[0])+1,left(h_lst[:-1],h_lst[-1])+1)
for k in range(1,N-1):
    ans = max(ans,left(h_lst[:k],h_lst[k])+right(h_lst[k+1:],h_lst[k])+1)
print(N-ans)
```



现在言归正传，我们应该使用动态规划，因为这显然是一个极值问题，意识到这一点之后就很好做了。

P.S：这道题用贪心+二分也很好做，而且时间复杂度更小。

代码：

```python
N = int(input())
h_lst = list(map(int,input().split()))
h_lst_2 = h_lst[::-1]
left = [1 for _ in range(N)]
right = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if h_lst[i] > h_lst[j]:
            left[i] = max(left[i],left[j]+1)
        if h_lst_2[i] > h_lst_2[j]:
            right[i] = max(right[i],right[j]+1)
ans = max(left[-1],right[-1])
for k in range(1,N-1):
    ans = max(ans,left[k]+right[N-k-1]-1)
print(N-ans)
```



#### 2、最大子矩阵

http://cs101.openjudge.cn/routine/02766/

这道题需要使用kadane算法，其实就是计算前缀和，然后就可以从二维到一维了。数据的接收也很有意思，让我学到了更多的东西，同时，这里的子矩阵要求是连续的，这一点必须注意。

代码：

```python
def kadane(nums):
    max_num = float('-inf')
    count = 0
    for num in nums:
        count = max(num,count+num)
        max_num = max(max_num,count)
    return max_num

N = int(input())
nums = []
while len(nums) < N**2:
    nums.extend(input().split())
matrix = [list(map(int,nums[i*N:(i+1)*N])) for i in range(N)]
for i in range(1,N):
    for j in range(N):
        matrix[i][j] += matrix[i-1][j]
answer = float('-inf')
for p in range(N):
    for q in range(p,N):
        temp = [0 for _ in range(N)]
        for i in range(N):
            temp_sum = matrix[q][i]
            if p > 0:
                temp_sum -= matrix[p-1][i]
            temp[i] = temp_sum
        answer = max(answer,kadane(temp))
print(answer)
```



#### 3、登山

http://cs101.openjudge.cn/routine/02995/

跟“合唱队形”不能说非常相似，只能说一模一样……

代码：

```python
def cal(nums):
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return dp[-1]

n = int(input())
nums = list(map(int,input().split()))
ans = max(cal(nums),cal(nums[::-1]))
for k in range(1,n):
    ans = max(ans,cal(nums[:k+1])+cal(nums[k:][::-1])-1)
print(ans)
```



#### 4、海贼王之伟大航路

http://cs101.openjudge.cn/routine/04124/

我的天，这道题简直了……先是正常做，然后得到了漂亮的TLE，之后也有尝试用最短时间与当前时间比较从而剪枝，证明没什么卵用。最后通过查阅网上资料知道了可以用二进制实现更强的剪枝，策略是：如果到达一个地点之前所经过的地点是相同的且用时更长，那么就可以直接去掉，如$$1->2->3->4->5$$、$$1->3->4->2->5$$、$$1->4->2->3->5$$，它们就可以进行比较，从而达到非常好的剪枝效果。

代码：

```python
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
visited[0] = 1
ans = float('inf')
dp = [[float('inf') for _ in range(1 << n)] for _ in range(n)]
def dfs(x,state,t,num):
    global ans
    if num == n-1 and x != n-1:
        t += matrix[x][-1]
        ans = min(ans,t)
        return
    for i in range(1,n-1):
        if not visited[i]:
            tp = 1 << i
            new_state = state | tp
            if x == 0:
                dp[i][new_state] = matrix[x][i]
                visited[i] = 1
                dfs(i,new_state,t+matrix[x][i],num+1)
                visited[i] = 0
            else:
                if dp[x][state] + matrix[x][i] < dp[i][new_state]:
                    dp[i][new_state] = dp[x][state] + matrix[x][i]
                    visited[i] = 1
                    dfs(i,new_state,t+matrix[x][i],num+1)
                    visited[i] = 0
dfs(0,1,0,1)
print(ans)
```



#### 5、DNA

http://cs101.openjudge.cn/routine/04126/

这道题在做了处理之后就是一道和海贼王基本一致的题目，而我们这里使用二进制储存之前的结果从而进行记忆化搜索，与前面的方法有共同之处，值得多加体会。

代码：

```python
def match(a, b):
    l, r = 0, 0
    n = min(len(a), len(b))
    for k in range(1, n + 1):
        if b[-k:] == a[:k]:
            r = k
        if a[-k:] == b[:k]:
            l = k
    return l, r

def dfs(current, visited, matrix, memo):
    if visited == (1 << len(matrix)) - 1:
        return 0
    if memo[current][visited] != -1:
        return memo[current][visited]
    ans = float('inf')
    for i in range(len(matrix)):
        if not visited & (1 << i):
            new_len = len(strings[i]) - matrix[current][i]
            ans = min(ans, dfs(i, visited | (1 << i), matrix, memo) + new_len)
    memo[current][visited] = ans
    return ans

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    lst = [input() for _ in range(N)]
    strings = [s for s in lst if not any(s != other and s in other for other in lst)]
    n = len(strings)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            l,r = match(strings[i],strings[j])
            matrix[i][j],matrix[j][i] = l,r
    memo = [[-1] * (1 << n) for _ in range(n)]
    ans = float('inf')
    for i in range(n):
        ans = min(ans, dfs(i, 1 << i, matrix, memo) + len(strings[i]))
    print(ans)
```





### 2023.12.1

#### 1、显示器

http://cs101.openjudge.cn/routine/02746/

一道蛮简单的语法题，需要注意的地方在于数字和数字之间有空列，每一组之间有空行。

代码：

```python
while True:
    s,n = input().split()
    if s == n == "0":break
    m = int(s)
    a,b,c,d,e = ' '*(m+2),' '+'-'*m+' ','|'+' '*(m+1),' '*(m+1)+'|','|'+' '*m+'|'
    mydict = {
        '0':[b]+[e]*m+[a]+[e]*m+[b],
        '1':[a]+[d]*m+[a]+[d]*m+[a],
        '2':[b]+[d]*m+[b]+[c]*m+[b],
        '3':[b]+[d]*m+[b]+[d]*m+[b],
        '4':[a]+[e]*m+[b]+[d]*m+[a],
        '5':[b]+[c]*m+[b]+[d]*m+[b],
        '6':[b]+[c]*m+[b]+[e]*m+[b],
        '7':[b]+[d]*m+[a]+[d]*m+[a],
        '8':[b]+[e]*m+[b]+[e]*m+[b],
        '9':[b]+[e]*m+[b]+[d]*m+[b]
    }
    for x in range(2*m+3):
        letter = []
        for num in n:
            letter.append(mydict[num][x])
        print(' '.join(letter))
    print()
```



#### 2、Jumping Cows

http://cs101.openjudge.cn/routine/02181/

这道题使用动态规划，同时应该注意数据结构，从而进行时间上的优化。

代码：

```python
p = int(input())
nums = [int(input()) for _ in range(p)]
up,down = [0 for _ in range(p)],[0 for _ in range(p)]
up[0] = nums[0]
max_up,max_down = nums[0],0
for k in range(1,p):
    up[k] = max_down + nums[k]
    down[k] = max_up - nums[k]
    max_up = max(up[k],max_up)
    max_down = max(down[k],max_down)
print(max(up+down))
```



#### 3、统计单词数

http://cs101.openjudge.cn/routine/04030/

这道题目的题意容易使人混淆，从而出错，同时对于$$find()$$等函数的理解还有待加强。

代码：

```python
word = ' ' + input().lower() + ' '
essay = ' ' + input().lower() + ' '
ans = essay.find(word)
if ans >= 0:print(essay.split().count(word[1:-1]),ans)
else:print(-1)
```



#### 4、寻找离目标数最接近的两数之和

http://cs101.openjudge.cn/routine/18156/

典型的双指针……可以我最开始没想到，以后一定要能够迅速地反应过来！！！

代码：

```python
def find(t,nums):
    left,right = 0,len(nums)-1
    ans = float('inf')
    while left < right:
        current_sum = nums[left] + nums[right]
        current_diff = abs(current_sum - t)
        if current_diff < abs(t - ans):
            ans = current_sum
        elif current_diff == abs(t - ans):
            ans = min(ans,current_sum)
        if current_sum == t:
            return ans
        elif current_sum < t:
            left += 1
        else:
            right -= 1
    return ans

t = int(input())
nums = sorted(list(map(int,input().split())))
print(find(t,nums))
```





### 2023.12.2

#### 1、括号匹配问题

http://cs101.openjudge.cn/routine/03704/

简单的字符匹配问题，我记得好像还可以用正则表达式，啥时候再学习一下。

代码：

```python
while True:
    try:
        string = list(input())
        marked_lst = [0 for _ in range(len(string))]
        for k in range(len(string)):
            if string[k] == '(':
                marked_lst[k] = -1
            elif string[k] == ')':
                marked_lst[k] = 1
        for i in range(len(marked_lst)):
            if marked_lst[i] == 1:
                for j in range(i-1,-1,-1):
                    if marked_lst[j] == -1:
                        marked_lst[i] , marked_lst[j] = 0,0
                        break
        print_lst = [' ' for _ in range(len(marked_lst))]
        for x in range(len(marked_lst)):
            if marked_lst[x] == -1:
                print_lst[x] = '$'
            elif marked_lst[x] == 1:
                print_lst[x] = '?'
        print(''.join(string))
        print(''.join(print_lst))
    except EOFError:
        break
```



#### 2、最短前缀

http://cs101.openjudge.cn/routine/02797/

这道题还是简单的语法运用，但是我对于边界条件 $$or$$ 极限情况的处理还有待加强。

代码：

```python
string = []
while True:
    try:
        string.append(input())
    except EOFError:
        break
for word in string:
    for k in range(1,len(word)+1):
        if all(word[:k] != char[:k] for char in string if char != word):
            print(word,word[:k])
            break
        if k == len(word):
            print(word,word)
```





### 2023.12.3

#### 1、抓住那头牛

http://cs101.openjudge.cn/routine/04001/

使用动态规划并小小地分类一下，一遍过，开心！

代码：

```python
N,K = map(int,input().split())
if N >= K:
    print(N-K)
else:
    dp = [0 for _ in range(K+1)]
    for i in range(N+1):
        dp[i] = N-i
    for k in range(N+1,K+1):
        if k % 2 == 0:
            dp[k] = min(dp[k-1]+1,dp[k//2]+1)
        else:
            dp[k] = min(dp[k-1]+1,dp[(k-1)//2]+2,dp[(k+1)//2]+2)
    print(dp[K])
```



#### 2、拼写检查

http://cs101.openjudge.cn/routine/01035/

不知道为什么老是超时，搞得我都怀疑自己是不是应该用动态规划了……最后终于还是正常地AC了。

代码：

```python
def check(word,letter):
    n,m = len(word),len(letter)
    if n == m+1 or n == m:
        for k in range(n):
            if word[:k] + word[k+1:] == letter or word[:k] + word[k+1:] == letter[:k] + letter[k+1:]:
                return 1
    elif n == m-1:
        for k in range(m):
            if letter[:k] + letter[k+1:] == word:
                return 1
    return 0

dictionary = []
while True:
    word = input()
    if word == '#':break
    dictionary.append(word)
while True:
    letter = input()
    if letter == '#':break
    if letter in dictionary:
        print(f'{letter} is correct')
    else:
        temp = []
        for word in dictionary:
            if check(word,letter):
                temp.append(word)
        ans = ' '.join(temp)
        print(f'{letter}: {ans}')
```





### 2023.12.4

#### 1、木材加工

http://cs101.openjudge.cn/routine/02774/

又一个贪心+二分，感觉自己对于二分之后输出的结果应该用哪一个值还是有些困惑。

代码：

```python
n,k = map(int,input().split())
woods = [int(input()) for _ in range(n)]
total = sum(woods)
if total < k:
    print(0)
else:
    left,right = 1,total//k
    while left <= right:
        mid = (left+right)//2
        count = 0
        for p in range(n):
            count += woods[p]//mid
        if count >= k:
            left = mid + 1
        else:
            right = mid - 1
    print(right)
```



#### 2、选课

http://cs101.openjudge.cn/routine/02996/

实际上就是排列的一个现实场景，也对于我的知识体系有了进一步的巩固。

代码：

```python
def next_permutation(nums)->None:
    i = len(nums)-2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i],nums[j] = nums[j],nums[i]
    nums[i+1:] = nums[i+1:][::-1]

n = int(input())
m = int(input())
nums = list(map(int,input().split()))
for _ in range(m):
    next_permutation(nums)
print(*nums)
```



#### 3、股票（greedy）

http://cs101.openjudge.cn/routine/16529/

比较简单的贪心题目吧……用类似动态规划的思想去递推就可以得出答案了。

代码：

```python
n = int(input())
p_lst = list(map(float,input().split()))
perm = 1
max_num = p_lst[-1]
for k in range(n-1,-1,-1):
    max_num = max(max_num,p_lst[k])
    perm = max(perm,max_num/p_lst[k])
ans = 100*perm
print(f'{ans:.2f}')
```





### 2023.12.5

#### 1、熄灯问题

http://cs101.openjudge.cn/routine/02811/

这道题……深浅拷贝确实要注意，在我们对于第一排进行了操作之后，应该进行深拷贝，而不是直接将进行操作，**原因在于我们进行的操作没有办法进行恢复（回溯）**，因为$$matrix、new-matrix$$为全局变量。这非常值得注意。

代码：

```python
import copy
matrix = [list(map(int,input().split())) for _ in range(5)]
def operate(matrix,x,y)->None:
    matrix[x][y] = abs(matrix[x][y]-1)
    row_nums = [-1,0,1,0]
    col_nums = [0,-1,0,1]
    for k in range(4):
        nx = x + row_nums[k]
        ny = y + col_nums[k]
        if 0 <= nx < 5 and 0 <= ny < 6:
            matrix[nx][ny] = abs(matrix[nx][ny]-1)

new_matrix = [[0 for _ in range(6)] for _ in range(5)]
for a in range(2):
    new_matrix[0][0] = a
    for b in range(2):
        new_matrix[0][1] = b
        for c in range(2):
            new_matrix[0][2] = c
            for d in range(2):
                new_matrix[0][3] = d
                for e in range(2):
                    new_matrix[0][4] = e
                    for f in range(2):
                        new_matrix[0][5] = f

                        A = copy.deepcopy(matrix)
                        B = copy.deepcopy(new_matrix)
                        for p in range(6):
                            if B[0][p] == 1:
                                operate(A,0,p)
                        for k in range(1,5):
                            for q in range(6):
                                if A[k-1][q] == 1:
                                    B[k][q] = 1
                                    operate(A,k,q)
                        if A[4] == [0]*6:
                            for row in B:
                                print(' '.join(map(str,row)))
```





### 2023.12.6

#### 1、Saving Tang Monk

http://cs101.openjudge.cn/routine/04130/

这道题……做了足足半个多月，最后在闫老师的帮助下才算是勉强AC，我们来看看怎么个事。 

**首先**，使用**优先队列**。这里尤其需要注意，我觉得以后需要用这种东西的时候就直接用$$queue$$中的$$PriorityQueue$$算了，不用什么堆*（因为python中的是小根堆）*，这样更好一些。同时，为了不把优先级更高的排前面，我们这里定义了结构体$$Node$$（这里是为了便于引用），并定义函数$$lt$$，这里表示的意思是$$less$$ $$than$$（也有函数$$le$$，表示的意思为$$less$$ $$than$$ $$or$$ $$equal$$ $$to$$），以后都可以多使用试试。

**然后**，就是剪枝（不剪枝的思路应该是很好想的）。这里用了记忆化搜索，我们用一个表记录到达某一个位置身上有多少钥匙时所用时间，如果后面计算的比原来要小，那就接着算并更新数值，否则就不用计算了。这很关键，直接降低了大量的时间。

$$P.S:$$ 使用位运算记录杀了哪些对应的蛇也很有技巧性。

代码：

```python
from queue import PriorityQueue

class Node:
    def __init__(self,x,y,time,keys,snake):
        self.x = x
        self.y = y
        self.time = time
        self.keys = keys
        self.snake = snake
    def __lt__(self, other):
        return self.time < other.time

def bfs(maze,n,m):
    a,b,count = 0,0,0
    marked_lst = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'K':
                a,b = i,j
            if maze[i][j] == 'S':
                marked_lst[i][j] = count
                count += 1

    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    memo = [[[float('inf')]*(m+1) for _ in range(n)] for _ in range(n)]
    queue = PriorityQueue()
    queue.put(Node(a,b,0,0,0))
    memo[a][b][0] = 0
    while not queue.empty():
        node = queue.get()
        for k in range(4):
            nx = node.x + row_nums[k]
            ny = node.y + col_nums[k]
            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] == '#':
                    continue
                elif maze[nx][ny] == 'S':
                    if (node.snake >> marked_lst[nx][ny]) & 1:
                        if node.time + 1 < memo[nx][ny][node.keys]:
                            memo[nx][ny][node.keys] = node.time + 1
                            queue.put(Node(nx,ny,node.time+1,node.keys,node.snake))
                    else:
                        if node.time + 2 < memo[nx][ny][node.keys]:
                            memo[nx][ny][node.keys] = node.time + 2
                            queue.put(Node(nx,ny,node.time+2,node.keys,
                                           node.snake | (1 << marked_lst[nx][ny])))
                elif maze[nx][ny].isdigit():
                    if int(maze[nx][ny]) == node.keys + 1:
                        if node.time + 1 < memo[nx][ny][node.keys+1]:
                            memo[nx][ny][node.keys+1] = node.time + 1
                            queue.put(Node(nx,ny,node.time+1,node.keys+1,node.snake))
                    else:
                        if node.time + 1 < memo[nx][ny][node.keys]:
                            memo[nx][ny][node.keys] = node.time + 1
                            queue.put(Node(nx,ny,node.time+1,node.keys,node.snake))
                elif maze[nx][ny] == 'T' and node.keys == m:
                    return node.time + 1
                else:
                    if node.time + 1 < memo[nx][ny][node.keys]:
                        memo[nx][ny][node.keys] = node.time + 1
                        queue.put(Node(nx,ny,node.time+1,node.keys,node.snake))
    return 'impossible'

result = []
while True:
    n,m = map(int,input().split())
    if n == m == 0:break
    maze = [list(input()) for _ in range(n)]
    ans = bfs(maze,n,m)
    result.append(ans)
for letter in result:
    print(letter)
```



#### 2、硬币

http://cs101.openjudge.cn/routine/04120/

这道题又是一道之前尝试过的陈年老题……大概思路是：先使用多重背包的计算方式得到相应金额的表示方法数，之后我们利用递归函数$$recursion(a,b)$$表示在不使用$$b$$时表示$$a$$的方法数量，如果$$a$$的表示一定需要$$b$$，那么显然，函数为0，由此我们就可以进行判断了。

$$P.S:$$开头两行很重要，需要非常注意。

代码：

```python
import sys
sys.setrecursionlimit(1 << 30)

n,x = map(int,input().split())
nums = list(map(int,input().split()))
dp = [0]*10001
dp[0] = 1
for i in range(1,n+1):
    for j in range(10000,nums[i-1]-1,-1):
        dp[j] = max(dp[j],dp[j-nums[i-1]]+dp[j])

def recursion(a,b):
    if a < b:
        return dp[a]
    else:
        return dp[a]-recursion(a-b,b)

count = 0
result = []
for k in range(n):
    if recursion(x,nums[k]) == 0:
        count += 1
        result.append(nums[k])
print(count)
print(" ".join(map(str, result)))
```



#### 3、Sticks

http://cs101.openjudge.cn/routine/01011/

一道$$dfs$$题目，剪枝有几部分：1、没必要尝试已经知道不行的相同长度木棍；2、如果这个木棍之后的那些木棍不行，那么就可以根据这根木棍长度是否满足一定条件来判断能否拼成；3、不是总长度的因子的，**一定不行，这是最强的剪枝**。

$$P.S:$$ 借着这道题的机会，还学到了$$for...else...$$的结构。

代码：

```python
n = l = 0
used,nums = [],[]

def dfs(r,m):
    if r == m == 0:
        return True
    if m == 0:
        m = l
    for k in range(n):
        if used[k] and nums[k] <= m:
            if k > 0:
                if used[k-1] and nums[k] == nums[k-1]:
                    continue
            used[k] = False
            if dfs(r-1,m-nums[k]):
                return True
            else:
                used[k] = True
                if nums[k] == m or m == l:
                    return False
    return False

while True:
    n = int(input())
    if n == 0:
        break
    nums = list(map(int,input().split()))
    total = sum(nums)
    nums.sort(reverse=True)
    for l in range(nums[0],total//2 + 1):
        if total % l:
            continue
        used = [True for _ in range(n)]
        if dfs(n,l):
            print(l)
            break
    else:
        print(total)
```



#### 4、洋葱

http://cs101.openjudge.cn/routine/25570/

这道题比较水，属于矩阵操作中的一种。

代码：

```python
def cal(matrix,n):
    total = sum(matrix[0]) + sum(matrix[-1])
    for k in range(1,n-1):
        total += matrix[k][0]+matrix[k][-1]
    return total

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
ans = 0
while n > 0:
    if n == 1:
        ans = max(ans,matrix[0][0])
    else:
        ans = max(ans,cal(matrix,n))
        matrix = [matrix[p][1:n-1] for p in range(1,n-1)]
    n -= 2
print(ans)
```



#### 5、加密的称赞 v0.2

http://cs101.openjudge.cn/routine/21462/

这道题有用到旋转矩阵的相关知识，总体还是比较简单的。

代码：

```python
n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
row_nums,col_nums = [1,0,-1,0],[0,1,0,-1]
k = 0
word = ''
x,y = 0,0
while True:
    if matrix[x][y] == 0:
        break
    word += chr(matrix[x][y])
    matrix[x][y] = 0
    nx = x + row_nums[k]
    ny = y + col_nums[k]
    if (not 0 <= nx < n) or (not 0 <= ny < n) or matrix[nx][ny] == 0:
        k = (k+1) % 4
        nx = x + row_nums[k]
        ny = y + col_nums[k]
    x,y = nx,ny
print(word)
```





### 2023.12.7

#### 1、寻宝

http://cs101.openjudge.cn/routine/19930/

……开头就是宝的情况怎么能不考虑？！

代码：

```python
from collections import deque

class Node:
    def __init__(self,x=0,y=0,time=0):
        self.x = x
        self.y = y
        self.time = time

def bfs(maze,m,n):
    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    queue = deque()
    queue.append(Node(0,0,0))
    while queue:
        node = queue.popleft()
        if maze[node.x][node.y] == 1:
            return node.time
        for k in range(4):
            nx = node.x + row_nums[k]
            ny = node.y + col_nums[k]
            if 0 <= nx < m and 0 <= ny < n:
                if maze[nx][ny] == 2:
                    continue
                elif maze[nx][ny] == 1:
                    return node.time + 1
                else:
                    queue.append(Node(nx,ny,node.time+1))
                    maze[nx][ny] = 2
    return "NO"

m,n = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(m)]
ans = bfs(maze,m,n)
print(ans)
```



#### 2、滑雪

http://cs101.openjudge.cn/routine/01088/

终于做到这道题目了，就是显然的记忆化搜索，使用一个数组来记录能滑多远，再加上一个dfs就没啥毛病。

代码：

```python
r,c = map(int,input().split())
maze = [[float('inf') for _ in range(c+2)]]
for _ in range(r):
    maze.append([float('inf')] + list(map(int,input().split())) + [float('inf')])
maze += [[float('inf') for _ in range(c+2)]]
memo = [[0 for _ in range(c+2)] for _ in range(r+2)]
row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]

def dfs(x,y):
    if memo[x][y] > 0:
        return memo[x][y]
    for k in range(4):
        nx = x + row_nums[k]
        ny = y + col_nums[k]
        if maze[nx][ny] < maze[x][y]:
            memo[x][y] = max(memo[x][y],dfs(nx,ny)+1)
    return memo[x][y]

ans = 0
for i in range(1,r+1):
    for j in range(1,c+1):
        ans = max(ans,dfs(i,j))
print(ans+1)
```



#### 3、2022决战双十一

http://cs101.openjudge.cn/routine/25561/

这么久终于做了这道题啊……其实还是蛮简单的，数据不大而且用dfs也优化不了多少，我使用了模拟，进行判断（相当于就是暴力穷举），最后比较得到最小值。

代码：

```python
n,m = map(int,input().split())
prices,pref,shops = [],[],[]
judge_lst = [0 for _ in range(n)]
ans = 1e10
for i in range(n):
    prices.append({})
    shops.append([])
    temp = input().split()
    for temp_num in temp:
        sem,value = map(int,temp_num.split(':'))
        prices[i][sem-1] = value
        shops[-1].append(sem-1)
for j in range(m):
    pref.append([])
    temp = input().split()
    for comb in temp:
        a,b = map(int,comb.split('-'))
        pref[-1].append((a,b))
while judge_lst[0] < len(shops[0]):
    temp_lst = [0 for _ in range(m)]
    for k in range(n):
        temp_lst[shops[k][judge_lst[k]]] += prices[k][shops[k][judge_lst[k]]]
    delta = sum(temp_lst)//300 * 50
    for i in range(m):
        money = 0
        for x,y in pref[i]:
            if temp_lst[i] >= x:
                money = max(money,y)
        delta += money
    ans = min(ans,sum(temp_lst)-delta)
    judge_lst[-1] += 1
    for p in range(n-1,0,-1):
        if judge_lst[p] == len(shops[p]):
            judge_lst[p] = 0
            judge_lst[p-1] += 1
print(ans)
```





### 2023.12.8

#### 1、马走日

http://cs101.openjudge.cn/routine/04123/

回溯啊……回溯！一定要记得在运行完下一个递归之后，要把原来的标记改回来。

代码：

```python
maze = []
n,m = 0,0
row_nums,col_nums = [-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]
ans = 0
def dfs(num,x,y):
    global ans
    if num == n*m:
        ans += 1
        return
    for k in range(8):
        nx = x + row_nums[k]
        ny = y + col_nums[k]
        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny]:
                maze[nx][ny] = False
                dfs(num+1,nx,ny)
                maze[nx][ny] = True

t = int(input())
for _ in range(t):
    n,m,x,y = map(int,input().split())
    maze = [[True for _ in range(m)] for _ in range(n)]
    maze[x][y] = False
    ans = 0
    dfs(1,x,y)
    print(ans)
```



#### 2、切割回文

http://cs101.openjudge.cn/routine/04122/

这道题目使用动态规划，递推方程为：
$$
dp[i]=\begin{cases}
0,如果前i个字符组成的前缀为回文串\\
dp[i]=dp[j]+1，如果j+1到i为回文串(j为1到i-1中的数)
\end{cases}
$$
需要注意的是前$$i$$个字符组成的前缀本身就是回文串的情况可以直接放到第一个循环内进行判断，从而减少时间的耗费。

代码：

```python
t = int(input())
for _ in range(t):
    word = list(input())
    n = len(word)
    dp = [k for k in range(n)]
    for i in range(n):
        if word[:i + 1] == word[:i + 1][::-1]:
            dp[i] = 0
            continue
        for j in range(i):
            if word[j+1:i+1] == word[j+1:i+1][::-1]:
                dp[i] = min(dp[i],dp[j]+1)
    print(dp[-1])
```



#### 3、股票买卖

http://cs101.openjudge.cn/routine/04121/

这又是一道动态规划，需要算两次，感觉与分发糖果比较类似，分别从左到右和从右到左进行计算，不断更新就可以了。但我还是觉得自己对于这种题目的敏感性不够，可能还是需要多加练习。

代码：

```python
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    lst_1 = [0 for _ in range(n+1)]
    lst_2 = [0 for _ in range(n+1)]

    max_num = 0
    minn = nums[0]
    for i in range(1,n+1):
        minn = min(minn,nums[i-1])
        lst_1[i] = max(lst_1[i-1],nums[i-1]-minn)
    maxn = nums[-1]
    for j in range(n-1,-1,-1):
        maxn = max(maxn,nums[j])
        lst_2[j] = max(lst_2[j+1],maxn - nums[j])
        max_num = max(max_num,lst_1[j]+lst_2[j])
    print(max_num)
```



#### 4、拯救行动

http://cs101.openjudge.cn/routine/04116/

说实话，做了Saving Tang Monk之后做这种题，真的就没啥毛病了嘿嘿……

代码：

```python
from queue import PriorityQueue

class Node:
    def __init__(self,x=0,y=0,time=0,snake=0):
        self.x = x
        self.y = y
        self.time = time
        self.snake = snake
    def __lt__(self, other):
        return self.time < other.time

def bfs(maze,n,m):
    memo = [[float('inf') for _ in range(m)] for _ in range(n)]
    marked_lst = [[0 for _ in range(m)] for _ in range(n)]
    x,y,count = 0,0,0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'r':
                x,y = i,j
            if maze[i][j] == 'x':
                marked_lst[i][j] = count
                count += 1

    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    queue = PriorityQueue()
    queue.put(Node(x,y,0,0))
    while not queue.empty():
        node = queue.get()
        for k in range(4):
            nx = node.x + row_nums[k]
            ny = node.y + col_nums[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '#':
                    continue
                elif maze[nx][ny] == 'x':
                    if (node.snake >> marked_lst[nx][ny]) & 1:
                        if node.time + 1 < memo[nx][ny]:
                            memo[nx][ny] = node.time + 1
                            queue.put(Node(nx,ny,node.time+1,node.snake))
                    else:
                        if node.time + 2 < memo[nx][ny]:
                            memo[nx][ny] = node.time + 2
                            queue.put(Node(nx,ny,node.time+2,node.snake | (1 << marked_lst[nx][ny])))
                elif maze[nx][ny] == 'a':
                    return node.time + 1
                else:
                    if node.time + 1 < memo[nx][ny]:
                        memo[nx][ny] = node.time + 1
                        queue.put(Node(nx, ny, node.time+1, node.snake))
    return 'Impossible'

s = int(input())
for _ in range(s):
    n,m = map(int,input().split())
    maze = [list(input()) for _ in range(n)]
    ans = bfs(maze,n,m)
    print(ans)
```



#### 5、鸣人和佐助

http://cs101.openjudge.cn/routine/04115/

说实话，做了Saving Tang Monk之后真就像打通了任督二脉一样，bfs都是要么正常写，要么直接写结构体，用优先队列，基本上这两种方法挨个用就都可以做了。

代码：

```python
from queue import PriorityQueue

class Node:
    def __init__(self,x,y,time,snake,chakra):
        self.x = x
        self.y = y
        self.time = time
        self.snake = snake
        self.chakra = chakra
    def __lt__(self, other):
        return self.time < other.time

def bfs(maze,n,m,t):
    memo = [[[float('inf') for _ in range(t+1)] for _ in range(m)] for _ in range(n)]
    marked_lst = [[0 for _ in range(m)] for _ in range(n)]
    x,y,count = 0,0,0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '@':
                x,y = i,j
            if maze[i][j] == '#':
                marked_lst[i][j] = count
                count += 1

    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    queue = PriorityQueue()
    queue.put(Node(x,y,0,0,t))
    memo[x][y][t] = 0
    while not queue.empty():
        node = queue.get()
        for k in range(4):
            nx = node.x + row_nums[k]
            ny = node.y + col_nums[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '#':
                    if (node.snake >> marked_lst[nx][ny]) & 1:
                        if node.time + 1 < memo[nx][ny][node.chakra]:
                            memo[nx][ny][node.chakra] = node.time + 1
                            queue.put(Node(nx,ny,node.time+1,node.snake,node.chakra))
                    else:
                        if node.chakra == 0:
                            continue
                        else:
                            if node.time + 1 < memo[nx][ny][node.chakra - 1]:
                                memo[nx][ny][node.chakra - 1] = node.time + 1
                                queue.put(Node(nx,ny,node.time+1,
                                               node.snake | (1 << marked_lst[nx][ny]),node.chakra-1))
                elif maze[nx][ny] == '+':
                    return node.time + 1
                else:
                    if node.time + 1 < memo[nx][ny][node.chakra]:
                        memo[nx][ny][node.chakra] = node.time + 1
                        queue.put(Node(nx, ny, node.time + 1, node.snake, node.chakra))
    return -1

n,m,t = map(int,input().split())
maze = [list(input()) for _ in range(n)]
ans = bfs(maze,n,m,t)
print(ans)
```



#### 6、宠物小精灵之收服

http://cs101.openjudge.cn/routine/04102/

这道题好巧妙啊……设置一个$$dp$$数组，定义为收服 $$i$$ 个宠物，剩余体力为 $$j $$ 时，小智手中的精灵球数量。之后进行遍历，注意，在每次加入数组的时候就进行遍历，从而不断地更新数组。

代码：

```python
n,m,k = map(int,input().split())
dp = [[-1 for _ in range(m+1)] for _ in range(k+1)]
dp[0][m] = n
for i in range(1,k+1):
    v,w = map(int,input().split())
    for j in range(m+1):
        for p in range(i,0,-1):
            if j + w <= m and dp[p-1][j+w] != -1:
                dp[p][j] = max(dp[p][j],dp[p-1][j+w]-v)
def ans():
    for x in range(k,-1,-1):
        for y in range(m,-1,-1):
            if dp[x][y] != -1:
                return [str(x),str(y)]
print(' '.join(ans()))
```



#### 7、子串

http://cs101.openjudge.cn/routine/04018/

这道题就是从最开始进行比对，然后进行判断就好了（为什么我写动态规划没对啊，可能是太晚了吧……）。

代码：

```python
def check(s,t):
    judge = False
    for letter in s:
        judge = False
        while t:
            check_letter = t.pop(0)
            if check_letter == letter:
                judge = True
                break
    if judge:
        return 'Yes'
    else:
        return 'No'

while True:
    try:
        word_1,word_2 = input().split()
        s,t = list(word_1),list(word_2)
        print(check(s,t))
    except EOFError:
        break
```



#### 8、拼点游戏

http://cs101.openjudge.cn/routine/04005/

典型的田忌赛马，懒得再写了，就直接拿之前的改了……

代码：

```python
import copy
while True:
    n = int(input())
    if n == 0:break
    lst_2 = sorted(list(map(int,input().split())))
    lst_1 = sorted(list(map(int,input().split())))
    lt_1 = copy.deepcopy(lst_2)
    lt_2 = copy.deepcopy(lst_1)
    ans = 0
    other_ans = 0
    for _ in range(n):
        if lst_1[-1] > lst_2[-1]:
            ans += 1
            lst_1.remove(lst_1[-1]),lst_2.remove(lst_2[-1])
        else:
            if lst_1[0] > lst_2[0]:
                ans += 1
                lst_1.remove(lst_1[0]), lst_2.remove(lst_2[0])
            else:
                if lst_1[0] < lst_2[-1]:
                    ans -= 1
                    lst_1.remove(lst_1[0]),lst_2.remove(lst_2[-1])
    for _ in range(n):
        if lt_1[-1] > lt_2[-1]:
            other_ans += 1
            lt_1.remove(lt_1[-1]),lt_2.remove(lt_2[-1])
        else:
            if lt_1[0] > lt_2[0]:
                other_ans += 1
                lt_1.remove(lt_1[0]), lt_2.remove(lt_2[0])
            else:
                if lt_1[0] < lt_2[-1]:
                    other_ans -= 1
                    lt_1.remove(lt_1[0]),lt_2.remove(lt_2[-1])
    print(ans+2*n,2*n-other_ans)
```





### 2023.12.9

#### 1、麦森数

http://cs101.openjudge.cn/routine/02706/

这道题没明白，而且也只能用pypy过……后面一定要把它搞明白！！！

代码：

```python
import math

mid = [0] * 1002
base = [0] * 1002
ans = [0] * 1002
def qpower():
    global mid, ans, base
    mid = [0] * 1002
    for i in range(1, 501):
        for j in range(1, 501):
            mid[i+j-1] += ans[i]*base[j]
    for i in range(1, 501):
        mid[i+1] += mid[i] // 10
        mid[i] %= 10
    ans = mid[:]

def grow():
    global mid, base
    mid = [0] * 1002
    for i in range(1, 501):
        for j in range(1, 501):
            mid[i+j-1] += base[i] * base[j]
    for i in range(1, 501):
        mid[i+1] += mid[i] // 10
        mid[i] %= 10
    base = mid[:]

p = int(input())
print(int(math.log10(2)*p+1))
ans[1] = 1
base[1] = 2

while p > 0:
    if p & 1:
        qpower()
    grow()
    p >>= 1

sum = 0
ans[1] -= 1

for i in range(500, 0, -1):
    print(ans[i], end='')
    sum += 1
    if sum % 50 == 0:
        print()
```



#### 2、Red and Black

http://cs101.openjudge.cn/routine/03866/

还是那句话，现在做的bfs题目与Saving Tang Monk相比，简直就小巫见大巫。

代码：

```python
from collections import deque

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y

ans = 0
def bfs(maze,n,m):
    global ans
    x,y = 0,0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '@':
                x,y = i,j

    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    queue = deque()
    queue.append(Node(x,y))
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    ans = 1
    while queue:
        node = queue.popleft()
        for k in range(4):
            nx = node.x + row_nums[k]
            ny = node.y + col_nums[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '.' and not visited[nx][ny]:
                    ans += 1
                    visited[nx][ny] = True
                    queue.append(Node(nx,ny))
    return ans

while True:
    m,n = map(int,input().split())
    if n == m == 0:
        break
    maze = [list(input()) for _ in range(n)]
    print(bfs(maze,n,m))
```



#### 3、移动路线

http://cs101.openjudge.cn/routine/03717/

这道题成功地揭露了我高中数学已经忘了不少的事实……有两种做法，一种直接用排列组合，一种用dfs，这里都展示出来。

代码：

排列组合：

```python
import math
m,n = map(int,input().split())
print(math.comb(m+n-2,m-1))
```

dfs：

```python
n,m = map(int,input().split())
row_nums,col_nums = [0,1],[1,0]
def dfs(x,y):
    ans = 0
    if x == n-1 and y == m-1:
        return 1
    for k in range(2):
        nx = x + row_nums[k]
        ny = y + col_nums[k]
        if 0 <= nx < n and 0 <= ny < m:
            ans += dfs(nx,ny)
    return ans
print(dfs(0,0))
```



#### 4、电池的寿命

http://cs101.openjudge.cn/routine/03468/

这道题就是简单的贪心，这里一定要注意到电池是随便拆的，不要想复杂了。

代码：

```python
while True:
    try:
        n = int(input())
        nums = list(map(int,input().split()))
        nums.sort()
        total = sum(nums[:n-1])
        if nums[-1] > total:
            print(f'{total:.1f}')
        else:
            print(f'{(total+nums[-1])/2:.1f}')
    except EOFError:
        break
```



#### 5、4 Values whose Sum is 0

http://cs101.openjudge.cn/routine/03441/

4个数里面分别找2个组对，然后进行判断和计数就可以了，主要问题在于内存的优化，由于使用了defaultdict，所以可以不进行条件判断就能往里面添加键值对，但这也会导致访问无关的元素时内存增加，从而MLE，因此还是要进行条件判断，即便这会增加运行时间。

```python
from collections import defaultdict
n = int(input())
A,B,C,D = [],[],[],[]
for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

my_dict = defaultdict(int)
for a in A:
    for b in B:
        my_dict[a+b] += 1
ans = 0
for c in C:
    for d in D:
        if -c-d in my_dict:
            ans += my_dict[-c-d]
print(ans)
```





### 2023.12.10

#### 1、全排列

http://cs101.openjudge.cn/routine/02748/

这道题直接使用 $$itertools$$ 中的 $$permutations$$，就可以非常轻松地解决。

代码：

```python
from itertools import permutations
sentence = list(input())
n = len(sentence)
perm_result = list(permutations(range(n)))
for perm in perm_result:
    ans = ''
    for num in perm:
        ans += sentence[num]
    print(ans)
```



#### 2、二叉树

http://cs101.openjudge.cn/routine/02756/

主要需要理解二叉树中各个数字的关系，理解之后就非常好写了。

代码：

```python
x,y = map(int,input().split())
while x != y:
    if x > y:
        x = x//2
    else:
        y = y//2
print(x)
```



#### 3、拦截导弹

http://cs101.openjudge.cn/routine/02945/

挺简单的一道动态规划，但是可能做的还是有点久。

代码：

```python
n = int(input())
nums = list(map(int,input().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if nums[j] >= nums[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
```



#### 4、金银岛

http://cs101.openjudge.cn/routine/02795/

简单的贪心，没啥好说的。

代码：

```python
k = int(input())
for _ in range(k):
    w = int(input())
    s = int(input())
    lst = list(map(int,input().split()))
    nums = []
    for k in range(s):
        temp = [lst[2*k],lst[2*k+1]]
        nums.append(temp)
    nums.sort(key=lambda x:x[1]/x[0],reverse=True)
    money = 0
    for j in range(s):
        if w > nums[j][0]:
            w -= nums[j][0]
            money += nums[j][1]
        else:
            money += nums[j][1]*w/nums[j][0]
            print(f'{money:.2f}')
            break
    else:
        print(f'{money:.2f}')
```



#### 5、改卷子

http://cs101.openjudge.cn/routine/16530/

这道题就是不断地找恰好满足条件的最短字符串，但感觉边界还是不好想明白。

代码：

```python
n = int(input())
stu = [input() for _ in range(n)]
stu.sort()
word_1 = list(stu[n//2 - 1])
word_2 = list(stu[n//2])
judge = False
ans = ''
temp = ''
t,length = 0,len(word_1)
while t < length:
    for j in range(26):
        ans = temp
        ans += chr(j+65)
        if ''.join(word_1) <= ans < ''.join(word_2):
            judge = True
            break
    if judge:
        break
    temp += word_1[t]
    t += 1
print(ans)
```



#### 6、军备竞赛

http://cs101.openjudge.cn/routine/18211/

贪心+双指针，感觉也不算好想，还是要多加练习啊。

代码：

```python
w = int(input())
nums = sorted(list(map(int,input().split())))
left,right = 0,len(nums)-1
count = 0
while left <= right:
    if nums[left] <= w:
        w -= nums[left]
        count += 1
        left += 1
    else:
        if left == right:break
        w += nums[right]
        count -= 1
        right -= 1
        if count < 0:
            count = 0
            break
print(count)
```





### 2023.12.12

#### 1、小游戏

http://cs101.openjudge.cn/routine/02802/

这道题为什么用优先队列要慢呢？！

代码：

```python
from queue import PriorityQueue
class Node:
    def __init__(self,x,y,step,direct):
        self.x = x
        self.y = y
        self.step = step
        self.direct = direct
    def __lt__(self, other):
        return self.step < other.step

def bfs(maze,a,b,c,d):
    queue = PriorityQueue()
    memo = [[[float('inf') for _ in range(4)] for _ in range(w+2)] for _ in range(h+2)]
    for k in range(4):
        memo[a][b][k] = 0
    queue.put(Node(a,b,0,-1))
    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    while not queue.empty():
        node = queue.get()
        for k in range(4):
            nx = node.x + row_nums[k]
            ny = node.y + col_nums[k]
            if node.direct == -1 or node.direct == k:
                direct = k
                step = node.step
            else:
                direct = k
                step = node.step + 1
            if 0 <= nx <= h+1 and 0 <= ny <= w+1:
                if nx == c and ny == d:
                    return step+1
                if maze[nx][ny] == 'X':
                    continue
                else:
                    if step < memo[nx][ny][direct]:
                        memo[nx][ny][direct] = step
                        queue.put(Node(nx,ny,step,direct))
    return 0

board = 0
while True:
    w,h = map(int,input().split())
    if w == h == 0:
        break
    board += 1
    maze = ([[' ' for _ in range(w+2)]]+[[' ']+list(input())+[' '] for _ in range(h)]
            +[[' ' for _ in range(w+2)]])
    print(f'Board #{board}:')
    pair = 0
    while True:
        b,a,d,c = map(int,input().split())
        if a == b == c == d == 0:
            break
        pair += 1
        ans = bfs(maze,a,b,c,d)
        if ans:
            print(f'Pair {pair}: {ans} segments.')
        else:
            print(f'Pair {pair}: impossible.')
    print()
```





### 2023.12.13

#### 1、N皇后问题

http://cs101.openjudge.cn/routine/22007/

基本上和八皇后是一样的板子题，但感觉这方面写的不够熟练，还是要多加练习。

代码：

```python
temp = []
result = []
n = 0
def dfs(x):
    for k in range(n):
        judge = True
        for j in range(x):
            if k == temp[j] or x-j == abs(k-temp[j]):
                judge = False
                break
        if judge:
            temp.append(k)
            if len(temp) == n:
                result.append(' '.join(map(str,temp)))
            else:
                dfs(x+1)
            temp.pop()
n = int(input())
dfs(0)
if result:
    for letter in result:
        print(letter)
else:
    print('NO ANSWER')
```



#### 2、WERTYU

http://cs101.openjudge.cn/routine/02538/

这道题很水，但是也有考察细节的地方。

代码：

```python
while True:
    try:
        sentence = list(input())
        lst = list("`1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./")
        result = []
        for word in sentence:
            if word == ' ':
                result.append(word)
            else:
                ans = ''
                for letter in word:
                    ans += lst[lst.index(letter) - 1]
                result.append(ans)
        print(''.join(result))
    except EOFError:
        break
```



#### 3、密码

http://cs101.openjudge.cn/routine/02818/

这道题确实自己想的不够清楚，找到规律（每隔多少次哪个位置的字符就会变回初态）并得到列表，然后根据输入取模就可以大大简化从而降低时间复杂度。

代码：

```python
import copy
while True:
    n = int(input())
    if n == 0:
        break
    nums = [0] + list(map(int,input().split()))
    mod = [0 for _ in range(n+1)]
    my_index = list(range(n+1))
    for k in range(1,n+1):
        while True:
            mod[k] += 1
            my_index[k] = nums[my_index[k]]
            if my_index[k] == k:
                break
    while True:
        index = copy.deepcopy(my_index)
        lst = input()
        if lst == '0':
            print()
            break
        times,Code = lst.split(' ',1)
        t = int(times)
        code = list(Code)
        if len(code) < n:
            code += [' ' for _ in range(n-len(code))]
        for j in range(1,n+1):
            temp = t % mod[j]
            for _ in range(temp):
                index[j] = nums[index[j]]
        new_code = [' ' for _ in range(n)]
        for i in range(n):
            new_code[index[i+1]-1] = code[i]
        print(''.join(new_code))
```





### 2023.12.14

#### 1、城堡问题

http://cs101.openjudge.cn/routine/02815/

这道题一方面考察位运算，一方面考察dfs，但都比较基础。

代码：

```python
def find(num):
    ans = []
    for k in range(4):
        if not num & (1 << k):
            ans.append(k)
    return ans

s = 0
def dfs(maze,n,m,x,y):
    global s
    row_nums,col_nums = [0,-1,0,1],[-1,0,1,0]
    s += 1
    visited[x][y] = True
    for k in find(maze[x][y]):
        nx = x + row_nums[k]
        ny = y + col_nums[k]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(maze,n,m,nx,ny)

n = int(input())
m = int(input())
maze = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
count = 0
max_s = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            s = 0
            count += 1
            dfs(maze,n,m,i,j)
            max_s = max(max_s,s)
print(count)
print(max_s)
```



#### 2、最大并发量

http://cs101.openjudge.cn/routine/25302/

一定要注意，这道题不能用区间的那种去想（暂时不知道能不能做，但确实很容易WA），用字典记录然后看就可以了。

代码：

```python
from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    time_dict = defaultdict(int)
    for _ in range(n):
        a,b = map(int,input().split())
        time_dict[a] += 1
        time_dict[b] -= 1
    ans = 0
    count = 0
    for j in sorted(time_dict):
        count += time_dict[j]
        ans = max(ans,count)
    print(ans)
```



#### 3、移动办公

http://cs101.openjudge.cn/routine/19164/

很基础的一道动态规划，但关于拷贝的问题还是要注意。

代码:

```python
t,m = map(int,input().split())
B,N = [],[]
for _ in range(t):
    a,b = map(int,input().split())
    B.append(a)
    N.append(b)
bp,np = B[0],N[0]
for k in range(1,t):
    temp_bp = max(bp,np-m) + B[k]
    temp_np = max(np,bp-m) + N[k]
    bp,np = temp_bp,temp_np
print(max(bp,np))
```



#### 4、阿尔法星人翻译官

http://cs101.openjudge.cn/routine/12757/

这道题挺正常的，主要需要注意的就是关于拷贝的问题。

代码：

```python
def change(sentence):
    num = 0
    if 'million' in sentence:
        k = sentence.index('million')
        temp = sentence[:k]
        sentence[:] = sentence[k+1:]
        temp_num = 0
        if 'hundred' in temp:
            temp_num += my_dict[temp[0]]*100
            temp[:] = temp[2:]
        for letter in temp:
            temp_num += my_dict[letter]
        num += my_dict['million']*temp_num
    if 'thousand' in sentence:
        k = sentence.index('thousand')
        temp = sentence[:k]
        sentence[:] = sentence[k+1:]
        temp_num = 0
        if 'hundred' in temp:
            temp_num += my_dict[temp[0]]*100
            temp[:] = temp[2:]
        for letter in temp:
            temp_num += my_dict[letter]
        num += my_dict['thousand']*temp_num
    if 'hundred' in sentence:
        num += my_dict[sentence[0]]*100
        sentence = sentence[2:]
    for letter in sentence:
        num += my_dict[letter]
    return num

lst = list('zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, '
           'thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, '
           'thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, '
           'thousand, million'.split(', '))
nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90,100,1000,1000000]
my_dict = dict(zip(lst,nums))
sentence = list(input().split())
num = 0
if sentence[0] == 'negative':
    sentence.pop(0)
    num = change(sentence)
    print(-num)
else:
    num = change(sentence)
    print(num)
```



#### 5、Wooden Sticks

http://cs101.openjudge.cn/routine/01065/

这道题的思路来源于群里面，其实就是排序之后求另一个元素组成的序列中的最长严格递减序列的长度。

代码：

```python
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    sticks = [[lst[2*k],lst[2*k+1]] for k in range(n)]
    sticks.sort(key=lambda x:(x[0],x[1]))
    w_lst = [temp[1] for temp in sticks]
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if w_lst[j] > w_lst[i]:
                dp[i] = max(dp[i],dp[j]+1)
    print(max(dp))
```





### 2023.12.15

#### 1、神奇的口袋

http://cs101.openjudge.cn/routine/02755/

本来想用动态规划做，结果WA（不理解为什么），于是就直接暴力穷举hhh……

代码：

```python
n = int(input())
w = [int(input()) for _ in range(n)]
count = 0
for i in range(1,1<<n):
    temp = 0
    for j in range(n):
        if i & (1<<j):
            temp += w[j]
    if temp == 40:
        count += 1
print(count)
```



#### 2、CPU调度

http://cs101.openjudge.cn/routine/25566/

这道题的策略感觉不知道咋明确证明啊……但是确实挺好写。

代码：

```python
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort(key=lambda x:(-x[1],x[0]))
ans,count = 0,0
for j in range(n):
    count += lst[j][0]
    ans = max(ans,count+lst[j][1])
print(ans)
```



#### 3、P大卷王查询系统

http://cs101.openjudge.cn/routine/21759/

这道题挺基础，没什么问题。

代码：

```python
from collections import defaultdict
n,x,y = map(int,input().split())
count_dict = defaultdict(int)
average_dict = defaultdict(int)
for _ in range(n):
    course,name,grades = input().split()
    count_dict[name] += 1
    average_dict[name] = (average_dict[name]*(count_dict[name]-1)+int(grades))/count_dict[name]
k = int(input())
for _ in range(k):
    name = input()
    if count_dict[name] >= x and average_dict[name] > y:
        print('yes')
    else:
        print('no')
```



#### 4、解梦人kk

http://cs101.openjudge.cn/routine/20121/

比较基础的题目，使用bfs的思想就可以AC。

代码：

```python
from collections import deque
def bfs(matrix,n):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    queue = deque()
    queue.append([0,0,0])
    row_nums,col_nums = [0,1,0,-1],[1,0,-1,0]
    ans = matrix[0][0]
    while queue:
        x,y,direct = queue.popleft()
        nx,ny = x+row_nums[direct],y+col_nums[direct]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            ans += matrix[nx][ny]
            queue.append([nx,ny,direct])
            visited[nx][ny] = True
        else:
            new_direct = (direct+1) % 4
            xx,yy = x+row_nums[new_direct],y+col_nums[new_direct]
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:
                ans += matrix[xx][yy]
                queue.append([xx,yy,new_direct])
                visited[xx][yy] = True
    return ans

n = int(input())
matrix = [list(input().split()) for _ in range(n)]
print(bfs(matrix,n))
```



#### 5、Running Miles

https://codeforces.com/problemset/problem/1826/D

没想到吧嘿嘿嘿……CF、洛谷上的题目也应该做。

这道题挺有意思，想明白了不难但是问题就在于怎么很快地得到AC代码。

代码：

```python
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    new_nums = nums[::-1]
    max_l,max_r = -float('inf'),-float('inf')
    left,right = [],[]
    for k in range(n):
        max_l = max(max_l,nums[k]+k)
        max_r = max(max_r,new_nums[k]-(n-1-k))
        left.append(max_l)
        right.append(max_r)
    right = right[::-1]
    ans = -float('inf')
    for p in range(1,n-1):
        ans = max(ans,nums[p]+left[p-1]+right[p+1])
    print(ans)
```



#### 6、恩尼格玛

http://cs101.openjudge.cn/routine/19960/

什么阴间玩意，读了半天没明白意思，后面查阅了一下相关资料才明白。

代码：

```python
code_1,code_2,code_3,code_4 = [[0]*6 for _ in range(4)]
for _ in range(6):
    a,b = map(int,input().split())
    code_1[a-1] = b-1
for _ in range(6):
    a,b = map(int,input().split())
    code_2[a-1] = b-1
for _ in range(6):
    a,b = map(int,input().split())
    code_3[a-1] = b-1
for _ in range(3):
    a,b = map(int,input().split())
    code_4[a-1] = b-1
    code_4[b-1] = a-1
letters = list('abcdef')
sentence = list(input())
ans = ''
for j in range(len(sentence)):
    p,q,m = j%6,(j//6)%6,(j//36)%6
    new_code_1,new_code_2,new_code_3 = [[0]*6 for _ in range(3)]
    for k in range(6):
        new_code_1[(k+p)%6] = (code_1[k]+p)%6
        new_code_2[(k+q)%6] = (code_2[k]+q)%6
        new_code_3[(k+m)%6] = (code_3[k]+m)%6
    num = letters.index(sentence[j])
    ans += letters[new_code_1.index(new_code_2.index(new_code_3.index(code_4[new_code_3[new_code_2[new_code_1[num]]]])))]
print(ans)
```





### 2023.12.16

#### 1、充实的寒假生活

http://cs101.openjudge.cn/routine/16528/

这道题就是简单的动态规划，但是不知道为什么时间这么长……

代码：

```python
n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]
nums.sort(key=lambda x:(x[0],x[1]))
dp = [[0,0] for _ in range(n+1)]
dp[0] = [0,-1]
for j in range(1,n+1):
    for k in range(j):
        if nums[j-1][0] > dp[k][1] and nums[j-1][1] <= 60:
            dp[j] = [dp[k][0]+1,nums[j-1][1]]
ans = -1
for temp in dp:
    ans = max(ans,temp[0])
print(ans)
```



#### 2、幸福的寒假生活

http://cs101.openjudge.cn/routine/23568/

这道题就是上一道题的翻版，没啥区别。

代码：

```python
n = int(input())
nums = []
for _ in range(n):
    start,end,v = input().split()
    a,b = map(int,start.split('.'))
    c,d = map(int,end.split('.'))
    s,e = (a-1)*31+b-7,(c-1)*31+d-7
    nums.append([s,e,int(v)])
nums.sort(key=lambda x:(x[0],x[1]))
dp = [[0,0] for _ in range(n+1)]
dp[0] = [0,-1]
for j in range(1,n+1):
    for k in range(j):
        if nums[j-1][0] > dp[k][1] and nums[j-1][1] <= 44:
            if nums[j-1][2]+dp[k][0] > dp[j][0]:
                dp[j] = [dp[k][0]+nums[j-1][2],nums[j-1][1]]
ans = -1
for temp in dp:
    ans = max(ans,temp[0])
print(ans)
```



#### 3、走山路

http://cs101.openjudge.cn/practice/20106/

这道题属于比较正常的bfs题目，需要注意到应该找到最小解，因此应当比较一下。

代码：

```python
from queue import PriorityQueue

class Node:
    def __init__(self,x,y,t):
        self.x = x
        self.y = y
        self.t = t
    def __lt__(self, other):
        return self.t < other.t

def bfs(maze,n,m,a,b,c,d):
    queue = PriorityQueue()
    queue.put(Node(a,b,0))
    if maze[a][b] == '#' or maze[c][d] == '#':
        return -1
    memo = [[float('inf') for _ in range(m)] for _ in range(n)]
    memo[a][b] = 0
    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    while not queue.empty():
        node = queue.get()
        for k in range(4):
            nx = node.x + row_nums[k]
            ny = node.y + col_nums[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == '#':
                    continue
                if node.t + abs(int(maze[nx][ny])-int(maze[node.x][node.y])) < memo[nx][ny]:
                    memo[nx][ny] = node.t + abs(int(maze[nx][ny])-int(maze[node.x][node.y]))
                    queue.put(Node(nx,ny,node.t + abs(int(maze[nx][ny])-int(maze[node.x][node.y]))))
    return memo[c][d]

n,m,p = map(int,input().split())
maze = [list(input().split()) for _ in range(n)]
for _ in range(p):
    a,b,c,d = map(int,input().split())
    ans = bfs(maze,n,m,a,b,c,d)
    if ans == float('inf') or ans == -1:
        print('NO')
    else:
        print(ans)
```



#### 4、护林员盖房子

http://cs101.openjudge.cn/routine/21577/

比较基础的矩阵二维化一维的题目，只是细节稍多（或者我的问题）。

代码：

```python
n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    for j in range(m):
        maze[i][j] += maze[i-1][j]
s = 0
for p in range(n):
    dp = maze[p]
    temp = 0
    for num in dp:
        if num == 0:
            temp += 1
        else:
            temp = 0
        s = max(s,temp*(p+1))
    if p > 0:
        for q in range(p):
            dp = [maze[p][i]-maze[q][i] for i in range(m)]
            temp = 0
            for num in dp:
                if num == 0:
                    temp += 1
                else:
                    temp = 0
                s = max(s,temp*(p-q))
print(s)
```



#### 5、今日化学论文

http://cs101.openjudge.cn/routine/20140/

这道题对于字符串的匹配确实考察的非常深入，值得多加学习。

$$P.S:$$ 搞明白这道题之后，我感觉自己能做那道双重tag里的整数了，明天一试！

代码：

```python
sentence = list(input())
stack = []
for i in range(len(sentence)):
    stack.append(sentence[i])
    if stack[-1] == ']':
        stack.pop()
        temp = []
        while stack[-1] != '[':
            temp.append(stack.pop())
        stack.pop()
        num = ''
        while temp[-1].isdigit():
            num += temp.pop()
        temp = temp*int(num)
        while temp != []:
            stack.append(temp.pop())
print(''.join(stack))
```





### 2023.12.17

#### 1、健身房

http://cs101.openjudge.cn/routine/

这道题就是简单的背包问题，但是不知道为什么我感觉没问题的代码会WA……

代码：

```python
T,n = map(int,input().split())
dp = [-float('inf') for _ in range(T+1)]
dp[0] = 0
for _ in range(n):
    t,w = map(int,input().split())
    for j in range(T,t-1,-1):
        dp[j] = max(dp[j],dp[j-t] + w)
if dp[T] > 0:
    print(dp[T])
else:
    print(-1)
```



#### 2、电影节

http://cs101.openjudge.cn/routine/16067/

做烂了的一道题……就是排序+dp。

代码：

```python
while True:
    n = int(input())
    if n == 0:break
    nums = [list(map(int,input().split())) for _ in range(n)]
    nums.sort(key=lambda x:(x[0],x[1]))
    dp = [[0,0] for _ in range(n+1)]
    for j in range(1,n+1):
        for k in range(j):
            if dp[k][1] <= nums[j-1][0] and dp[k][0]+1 > dp[j][0]:
                dp[j] = [dp[k][0]+1,nums[j-1][1]]
    print(dp[n][0])
```



#### 3、一键换词

http://cs101.openjudge.cn/routine/27314/

这道题就是相对简单的字符串处理，不算难，但是细节也还是有。

代码：

```python
sentence = list(input().split())
word,new_word = input().split()
word = word.lower()
new_word = new_word.lower()
for k in range(len(sentence)):
    check = sentence[k].lower()
    if '.' in check or ',' in check:
        if word == check[:-1]:
            sentence = sentence[:k] + [new_word+check[-1]] + sentence[k+1:]
    else:
        if word == check:
            sentence = sentence[:k] + [new_word] + sentence[k+1:]
new_sentence = []
for j in range(len(sentence)):
    temp = sentence[j].lower()
    if j == 0 or sentence[j-1][-1] == '.':
        temp = temp.title()
    new_sentence.append(temp)
print(' '.join(new_sentence))
```



#### 4、NBA门票

http://cs101.openjudge.cn/routine/20089/

这道题先用二进制优化结果还是超时，所以再用字典稍加优化勉强通过。

代码：

```python
import math
money = int(input())
nums = list(map(int,input().split()))
num_lst = [1,2,5,10,20,50,100]
dp = {0:0}
for k in range(7):
    limit = int(math.log(nums[k]+1,2))
    rest = (nums[k]-(1 << limit)+1)*num_lst[k]*50
    for p in range(limit):
        temp = (1 << p)*num_lst[k]*50
        delta = 1 << p
        if temp <= money:
            for j in range(money-temp,-1,-1):
                if j in dp:
                    if j+temp in dp:
                        dp[j + temp] = min(dp[j + temp], dp[j] + delta)
                    else:
                        dp[j + temp] = dp[j] + delta
    delta = nums[k] - (1 << limit) + 1
    if delta and rest <= money:
        for j in range(money-rest,-1,-1):
            if j in dp:
                if j+rest in dp:
                    dp[j + rest] = min(dp[j + rest], dp[j] + delta)
                else:
                    dp[j + rest] = dp[j] + delta
if money in dp:
    print(dp[money])
else:
    print('Fail')
```



#### 5、Sumsets

http://cs101.openjudge.cn/routine/02229/

太晚了，有点神志不清……导致这道题最开始都没看出来是一个简单的动态规划，拷打！

代码：

```python
n = int(input())
dp = [0] * (n + 2)
dp[1] = 1
dp[2] = 2
for i in range(3, n + 1):
    if i % 2 == 1:
        dp[i] = dp[i - 1]
    else:
        dp[i] = (dp[i - 2] + dp[i // 2]) % 1000000000
print(dp[n])
```





### 2023.12.18

#### 1、Lake Counting

http://cs101.openjudge.cn/routine/02386/

典型的dfs，注意有可能爆栈，所以应该使用sys。

代码：

```python
import sys
sys.setrecursionlimit(1<<30)
n,m = map(int,input().split())
maze = [list(input()) for _ in range(n)]
count = 0
row_nums,col_nums = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]
visited = [[False for _ in range(m)] for _ in range(n)]
def dfs(x,y):
    if maze[x][y] == 'W' and not visited[x][y]:
        visited[x][y] = True
        for k in range(8):
            nx = x + row_nums[k]
            ny = y + col_nums[k]
            if 0 <= nx < n and 0 <= ny < m:
                dfs(nx,ny)
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'W' and not visited[i][j]:
            count += 1
            dfs(i,j)
print(count)
```



#### 2、Babelfish

http://cs101.openjudge.cn/routine/02503/

基本的对于字典的运用题目。

代码：

```python
my_dict = {}
while True:
    try:
        word,new_word = input().split()
        my_dict[new_word] = word
    except ValueError:
        break
while True:
    try:
        check = input()
        if check in my_dict:
            print(my_dict[check])
        else:
            print('eh')
    except EOFError:
        break
```



#### 3、Aggressive Cows

http://cs101.openjudge.cn/routine/02456/

经典的贪心+二分，奇怪的是这次二分迅速就过了，没出什么问题。

代码：

```python
def operate(nums,l):
    limit,count = nums[0],1
    for k in range(1,n):
        if nums[k] - limit >= l:
            count += 1
            limit = nums[k]
    return count

n,c = map(int,input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
left,right = 1,nums[-1]-nums[0]
while left <= right:
    middle = (left+right)//2
    check = operate(nums,middle)
    if check >= c:
        left = middle+1
    else:
        right = middle-1
print(right)
```





### 2023.12.19

今天被作业折磨地非常离谱……





### 2023.12.20

#### 1、繁荣的步行街

http://cs101.openjudge.cn/routine/20103/

这道题纯考语文啊……

代码：

```python
n = int(input())
lst = [[-float('inf'),0]]+[list(map(int,input().split())) for _ in range(n)]+[[float('inf'),0]]
ans,end = 0,-float('inf')
for j in range(1,n+1):
    if lst[j-1][0] < lst[j][0]-lst[j][1] > end and lst[j][0]+lst[j][1] < lst[j+1][0]:
        ans += 1
        end = lst[j][0]+lst[j][1]
print(ans)
```



#### 2、Expedition

http://cs101.openjudge.cn/routine/02431/

这道题比较有意思，我最开始用dfs做超时且超内存，现在知道了，dfs只适合做数据量小的，而这道题用一个相对简单的贪心策略就可以AC了。

代码：

```python
import heapq
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)] + [[0,0]]
lst.sort(reverse=True)
l,p = map(int,input().split())
Q = []
ans,length,power = 0,l,p
for j in range(n+1):
    d = length-lst[j][0]
    while power-d < 0:
        if len(Q) == 0:
            print(-1)
            exit()
        power += -heapq.heappop(Q)
        ans += 1
    power -= d
    heapq.heappush(Q,-lst[j][1])
    length = lst[j][0]
print(ans)
```



#### 3、修理牛棚

http://cs101.openjudge.cn/practice/20974/

没想到贪心策略……不过这道题确实就是因材施教的翻版。唉，确实是我水平低了。

代码：

```python
m,s,c = map(int,input().split())
lst = sorted([int(input()) for _ in range(c)])
diff = sorted([lst[i]-lst[i-1]-1 for i in range(1,c)])
print(lst[-1] - lst[0] + 1 - sum(diff[c-m:]))
```



#### 4、Quests

https://codeforces.com/problemset/problem/1914/C

这道题的贪心策略挺简单的……但是我还是在蠢蠢地用dfs试错，唉……

代码：

```python
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a_lst = list(map(int,input().split()))
    b_lst = list(map(int,input().split()))
    a,b,ans = 0,0,0
    for j in range(min(n,k)):
        a += a_lst[j]
        b = max(b,b_lst[j])
        ans = max(ans,a+(k-1-j)*b)
    print(ans)
```



#### 5、Game With Multiset

https://codeforces.com/problemset/problem/1913/C

笑死，这道题为什么写函数就能过，直接写就不行？！

代码：

```python
from collections import defaultdict
def solve(v,d):
    for j in range(29,-1,-1):
        temp = min(v >> j,d[j])
        v -= temp << j
        if v == 0:
            return 'YES'
    else:
        return 'NO'

def operate():
    m = int(input())
    my_dict = defaultdict(int)
    for _ in range(m):
        t, v = map(int, input().split())
        if t == 1:
            my_dict[v] += 1
        else:
            print(solve(v, my_dict))
operate()
```





### 2023.12.21

#### 1、冬泳

http://cs101.openjudge.cn/routine/20100/

读题要读清楚啊……“之一”那么大两个字怎么就看不到呢？

代码：

```python
import heapq
n = int(input())
d_lst = list(map(int,input().split()))
t_lst = list(map(int,input().split()))
a_lst = list(map(int,input().split()))
t,v = [],[]
heapq.heappush(t,float('inf'))
heapq.heappush(v,0)
ans = 0
for j in range(n-1):
    if a_lst[j] < t_lst[j]:
        if a_lst[j] < t[0] or d_lst[j]/a_lst[j] > -v[0]:
            ans += 1
    heapq.heappush(t,a_lst[j])
    heapq.heappush(v,-d_lst[j]/a_lst[j])
print(ans)
```



#### 2、Palindrome

http://cs101.openjudge.cn/routine/01159/

这道题用动态规划，二维很好想，但是简化就比较困难了。需要注意到奇偶性是不断变换的，所以可以循环使用之前存的东西，从而达到优化的目的。这样滚动数组的方法非常值得注意。

代码：

```python
def solve():
    n = int(input())
    s = input()
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for j in range(n-1,-1,-1):
        for k in range(j,n):
            if s[j] == s[k]:
                dp[j%2][k] = dp[(j+1)%2][k-1]
            else:
                dp[j%2][k] = min(dp[j%2][k-1],dp[(j+1)%2][k]) + 1
    print(dp[0][n-1])
solve()
```



#### 3、环形穿梭车调度

http://cs101.openjudge.cn/routine/19929/

比较基础的一道动态规划，不过还是要注意对于边界的处理。

代码：

```python
m,n = map(int,input().split())
A = list(map(int,input().split()))
W = list(map(int,input().split()))
dp = [0 for _ in range(m+1)]
for i in range(1,m+1):
    dp[i] = W[i-1]
    for j in range(1,i):
        if A[j-1] <= A[i-1]:
            dp[i] = max(dp[j]+W[i-1],dp[i])
print(max(dp))
```



#### 4、Piggy-Bank

http://cs101.openjudge.cn/routine/01384/

这道题就是一个完全背包，注意是找最小，所以不用逆向枚举。

代码：

```python
t = int(input())
for _ in range(t):
    e,f = map(int,input().split())
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    W = f-e
    dp = [float('inf') for _ in range(W+1)]
    dp[0] = 0
    for j in range(n):
        if W >= lst[j][1]:
            for k in range(lst[j][1],W+1):
                if dp[k-lst[j][1]]+lst[j][0] < dp[k]:
                    dp[k] = min(dp[k-lst[j][1]]+lst[j][0],dp[k])
    if dp[W] == float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[W]}.')
```



#### 5、食物链

http://cs101.openjudge.cn/routine/01182/

哇塞，并查集，很有意思的理论。说起来就是不断地查询并进行路径压缩。我们把定义三个区间，一个是同类，一个是吃，一个是被吃，从而不断进行更新维护，以便于进行判断。

代码：

```python
def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

n,k = map(int,input().split())
p = [i for i in range(3*n+1)]
ans = 0
for _ in range(k):
    d,x,y = map(int,input().split())
    if x > n or y > n:
        ans += 1
        continue
    if d == 1:
        if find(x+n) == find(y) or find(y+n) == find(x):
            ans += 1
            continue
        p[find(x)] = find(y)
        p[find(x+n)] = find(y+n)
        p[find(x+2*n)] = find(y+2*n)
    else:
        if find(x) == find(y) or find(y+n) == find(x):
            ans += 1
            continue
        p[find(x+n)] = find(y)
        p[find(x+2*n)] = find(y+n)
        p[find(y+2*n)] = find(x)

print(ans)
```



#### 6、最大点数（重力作用2048）

http://cs101.openjudge.cn/routine/20052/

这道题真的……唉，不知道为什么要整这么一道题目，还分重力作用和外太空，搞得做题人还要去理解2048的规则。

代码：

```python
import copy
import sys
sys.setrecursionlimit(1 << 30)

n,m,p = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def operate(lst):
    for j in range(len(lst)-1,0,-1):
        if lst[j] == 0:
            pass
        else:
            for k in range(j-1,-1,-1):
                if lst[j] == lst[k]:
                    lst[j],lst[k] = lst[j]*2,0
                    break
                elif lst[k] == 0:
                    pass
                else:
                    break
    ans = []
    count = 0
    for p in lst:
        if p == 0:
            count += 1
        else:
            ans.append(p)
    return [0 for _ in range(count)]+ans

def slide(matrix,dir):
    temp = copy.deepcopy(matrix)
    if dir == 0:
        for k in range(n):
            new_row = operate(temp[k])
            temp[k] = new_row
    elif dir == 1:
        for k in range(m):
            temp_col = [temp[i][k] for i in range(n)]
            new_col = operate(temp_col)
            for j in range(n):
                temp[j][k] = new_col[j]
    elif dir == 2:
        for k in range(n):
            temp_row = [temp[k][i] for i in range(m-1,-1,-1)]
            new_row = operate(temp_row)
            temp[k] = new_row[::-1]
    else:
        for k in range(m):
            temp_col = [temp[i][k] for i in range(n-1,-1,-1)]
            new_col = operate(temp_col)
            for j in range(n):
                temp[j][k] = new_col[::-1][j]
    return temp

result = 0

def solve(matrix,num):
    global result
    if num == p:
        result = max(result,max(max(matrix[i]) for i in range(n)))
        return
    for q in range(4):
        solve(slide(matrix, q), num + 1)

solve(matrix,0)
print(result)
```





### 2023.12.22

#### 1、接雨水II

http://cs101.openjudge.cn/practice/27421/

一维本来挺好做，现在来个二维的，感觉不算太简单，如果使用bfs这种方法，那么对于判断条件就要想清楚，否则很可能WA。

代码：

```python
from queue import PriorityQueue
class Node:
    def __init__(self,x,y,h):
        self.x = x
        self.y = y
        self.h = h
    def __lt__(self, other):
        return self.h < other.h

def bfs(n,m,maze):
    max_h = max(max(row) for row in maze)
    memo = [[max_h for _ in range(m)] for _ in range(n)]
    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    queue = PriorityQueue()
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n-1 or j == m-1:
                if memo[i][j] > maze[i][j]:
                    memo[i][j] = maze[i][j]
                    queue.put(Node(i,j,maze[i][j]))
    while not queue.empty():
        node = queue.get()
        for k in range(4):
            nx = node.x + row_nums[k]
            ny = node.y + col_nums[k]
            if 0 <= nx < n and 0 <= ny < m:
                if memo[node.x][node.y] < memo[nx][ny] > maze[nx][ny]:
                    memo[nx][ny] = max(memo[node.x][node.y],maze[nx][ny])
                    queue.put(Node(nx,ny,memo[nx][ny]))
    return memo

n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
memo = bfs(n,m,maze)
ans = 0
for i in range(n):
    for j in range(m):
        ans += memo[i][j]-maze[i][j]
print(ans)
```



#### 2、生日蛋糕

http://cs101.openjudge.cn/routine/01190/

在蒋神的帮助下终于AC了，感觉对于dfs的理解可能还是不够，而且为什么会是两千多毫秒啊……

代码：

```python
import sys
sys.setrecursionlimit(1 << 30)
v,s,min_s = 0,0,float('inf')

def dfs(r,h,l):
    global v,s,min_s
    if v+memo[l] > n or n-v > (m-l)*(h-1)*((r-1)**2) or s + 2*(n-v)/r > min_s:
        return
    if l == m:
        if v == n:
            min_s = s
        return
    for nr in range(r-1,m-l-1,-1):
        for nh in range(h-1,m-l-1,-1):
            if l == 0:
                s += nr**2
            s += 2*nr*nh
            v += nh*(nr**2)
            dfs(nr,nh,l+1)
            if l == 0:
                s -= nr**2
            s -= 2*nr*nh
            v -= nh*(nr**2)
    return

n,m = [int(input()) for _ in range(2)]
rest = n
memo = [0 for _ in range(m+1)]
for j in range(1,m):
    rest -= j**3
    memo[-j-1] = n - rest
if rest <= 0:
    print(0)
    quit()
max_r = int((rest/m)**0.5)
max_h = int(rest/(m**2))
dfs(max_r,max_h,0)
if min_s == float('inf'):
    print(0)
else:
    print(min_s)
```





### 2023.12.23

#### 1、小兔子捡金币

http://cs101.openjudge.cn/routine/04006/

这道题主要考察对于螺旋矩阵的坐标关系的理解，因为卡了内存，所以不能直接建一个矩阵，而需要不断进行计算，感觉对于理解矩阵的帮助还是挺大的。

代码：

```python
def find(n,x,y):
    matrix = [4*i*(n-i)+1 for i in range((n+1)//2)]
    now = min(min(x,y),min(n-x+1,n-y+1)) - 1
    if x <= y:
        return matrix[now]+x+y-2*now-2
    else:
        return matrix[now+1]-x-y+2*now+2
k,n = map(int,input().split())
for _ in range(k):
    x,y = map(int,input().split())
    print(find(n,x,y))
```



#### 2、棋盘分割

http://cs101.openjudge.cn/routine/01191/

感觉很创新的一道递归啊……主要对于矩形的选取以及变量的标记很有讲究。

代码：

```python
from collections import defaultdict
def operate(n,a,b,x,y):
    if dp[(n,a,b,x,y)] > 0:
        return dp[(n,a,b,x,y)]
    if n == 1:
        temp = 0
        for i in range(a,x+1):
            for j in range(b,y+1):
                temp += maze[i][j]
        dp[(n,a,b,x,y)] = temp**2
        return temp**2
    min_num = float('inf')
    for r in range(a,x):
        min_num = min(operate(n-1,r+1,b,x,y)+operate(1,a,b,r,y),min_num)
        min_num = min(operate(n-1,a,b,r,y)+operate(1,r+1,b,x,y),min_num)
    for t in range(b,y):
        min_num = min(operate(n-1,a,t+1,x,y)+operate(1,a,b,x,t),min_num)
        min_num = min(operate(n-1,a,b,x,t)+operate(1,a,t+1,x,y),min_num)
    dp[(n,a,b,x,y)] = min_num
    return min_num

n = int(input())
maze = [list(map(int,input().split())) for _ in range(8)]
dp = defaultdict(int)
s = sum(sum(row) for row in maze)/n
ans = (operate(n,0,0,7,7)/n - s**2)**0.5
print(f'{ans:.3f}')
```



#### 3、棋盘问题

http://cs101.openjudge.cn/routine/01321/

这道题最开始感觉挺简单，不就是普通的dfs嘛……结果疯狂超时，原来有一个很有效的剪枝没想到。那就是如果从 $$r$$ 到 $$i$$

没有满足条件的，那么接下来的搜索可以跳过而不管它们。

代码：

```python
ans = 0
def dfs(r,t):
    global ans
    if t == k:
        ans += 1
        return
    if r == n:
        return
    for i in range(r,n):
        for j in range(n):
            if maze[i][j] == '#' and judge[j]:
                judge[j] = False
                dfs(i+1,t+1)
                judge[j] = True
                
while True:
    n,k = map(int,input().split())
    if n == k == -1:
        break
    maze = [list(input()) for _ in range(n)]
    judge = [True for _ in range(n)]
    ans = 0
    dfs(0,0)
    print(ans)
```



#### 4、A Knight's Journey

http://cs101.openjudge.cn/routine/02488/

本来想着用bfs做的，结果发现不太合适，索性就用dfs写了。

代码：

```python
Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
dir = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
result = ''
def dfs(x,y,t,ans):
    global result
    if result:
        return
    if t == m*n:
        result = ans
        return
    for a,b in dir:
        nx = x + a
        ny = y + b
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,t+1,ans+Alphabet[nx]+str(ny+1))
                visited[nx][ny] = False

k = int(input())
for j in range(1,k+1):
    print(f'Scenario #{j}:')
    m,n = map(int,input().split())
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    result = ''
    dfs(0,0,1,'A1')
    if result:
        print(result)
    else:
        print('impossible')
    print()
```



#### 5、Holiday Hotel

http://cs101.openjudge.cn/routine/02783/

这道题有点考阅读理解能力，需要明白只要比前面的都便宜就可以，而无需管后面的酒店价格。

代码：

```python
import heapq
while True:
    n = int(input())
    if n == 0:
        break
    lst = sorted([list(map(int,input().split())) for _ in range(n)])
    money = []
    heapq.heappush(money,lst[0][1])
    ans = 0
    for hotel in lst:
        if hotel[1] < money[0]:
            ans += 1
        heapq.heappush(money,hotel[1])
    print(ans+1)
```



#### 6、当前队列中位数

http://cs101.openjudge.cn/routine/27256/

这道题教会了我怎么使用bisect库，真的很有用。

代码：

```python
import bisect
from collections import deque
n = int(input())
my_lst = []
mark_lst = deque()
for _ in range(n):
    my_input = input()
    if my_input[0] == 'a':
        a,num = my_input.split()
        bisect.insort_left(my_lst,int(num))
        mark_lst.append(int(num))
    elif my_input[0] == 'd':
        num = mark_lst.popleft()
        my_lst.pop(bisect.bisect_left(my_lst,num))
    else:
        k = len(my_lst)
        if k % 2 == 0:
            ans = (my_lst[k//2-1]+my_lst[k//2])/2
            if ans == int(ans):
                print(int(ans))
            else:
                print(ans)
        else:
            print(my_lst[k//2])
```





### 2023.12.24

#### 1、二维数组回形遍历

http://cs101.openjudge.cn/routine/07645/

比较简单的一道螺旋矩阵题目。

代码：

```python
from collections import deque
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dir = [(0,1),(1,0),(0,-1),(-1,0)]
queue = deque()
queue.append([0,0,0])
while queue:
    x,y,k = queue.popleft()
    visited[x][y] = True
    print(matrix[x][y])
    a,b = dir[k]
    nx = x+a
    ny = y+b
    if 0 <= nx < n and 0 <= ny < m:
        if not visited[nx][ny]:
            queue.append([nx,ny,k])
        else:
            k = (k+1)%4
            p,q = dir[k]
            xx = x+p
            yy = y+q
            if 0 <= xx < n and 0 <= yy < m:
                if not visited[xx][yy]:
                    queue.append([xx,yy,k])
    else:
        k = (k + 1) % 4
        p, q = dir[k]
        xx = x + p
        yy = y + q
        if 0 <= xx < n and 0 <= yy < m:
            if not visited[xx][yy]:
                queue.append([xx, yy, k])
```



#### 2、ROADS

http://cs101.openjudge.cn/routine/01724/

比较简单的一道bfs吧，感觉确实现在做这种题目都没什么大问题了。

代码：

```python
from queue import PriorityQueue
class Node:
    def __init__(self,x,l,t):
        self.x = x
        self.l = l
        self.t = t
    def __lt__(self, other):
        return self.l <other.l
def bfs(my_dict,k,n):
    queue = PriorityQueue()
    queue.put(Node(1,0,0))
    memo = [[float('inf') for _ in range(k + 1)] for _ in range(n + 1)]
    memo[1][0] = 0
    while not queue.empty():
        node = queue.get()
        if node.x == n:
            return node.l
        for road in my_dict[node.x]:
            if node.t+road[2] <= k:
                if node.l + road[1] < memo[road[0]][node.t + road[2]]:
                    memo[road[0]][node.t + road[2]] = node.l + road[1]
                    queue.put(Node(road[0],node.l+road[1],node.t+road[2]))
    return -1

k,n,r = [int(input()) for _ in range(3)]
my_dict = {}
for j in range(1,n+1):
    my_dict[j] = []
for _ in range(r):
    s,d,l,t = map(int,input().split())
    my_dict[s].append([d,l,t])
print(bfs(my_dict,k,n))
```



#### 3、Flip Game

http://cs101.openjudge.cn/routine/01753/

熄灯问题的简单版？总体来说还是不难的，但是我没想到居然会出现 ‘Impossible’ 的情况。

代码：

```python
import copy
def operate(matrix,x,y)->None:
    matrix[x][y] = abs(matrix[x][y]-1)
    row_nums,col_nums = [-1,0,1,0],[0,-1,0,1]
    for k in range(4):
        nx = x + row_nums[k]
        ny = y + col_nums[k]
        if 0 <= nx < 4 and 0 <= ny < 4:
            matrix[nx][ny] = abs(matrix[nx][ny]-1)

def work(matrix):
    result = []
    new_matrix = [[0 for _ in range(4)] for _ in range(4)]
    for a in range(2):
        new_matrix[0][0] = a
        for b in range(2):
            new_matrix[0][1] = b
            for c in range(2):
                new_matrix[0][2] = c
                for d in range(2):
                    new_matrix[0][3] = d
                    A = copy.deepcopy(matrix)
                    B = copy.deepcopy(new_matrix)
                    for k in range(4):
                        if B[0][k]:
                            operate(A,0,k)
                    for i in range(1,4):
                        for j in range(4):
                            if A[i-1][j]:
                                B[i][j] += 1
                                operate(A,i,j)
                    if A[3] == [0]*4:
                        result.append(sum(sum(row) for row in B))
    if result:
        return min(result)
    else:
        return float('inf')

matrix = [list(input()) for _ in range(4)]
P,Q = [[0 for _ in range(4)] for _ in range(4)],[[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        if matrix[i][j] == 'w':
            P[i][j] += 1
        else:
            Q[i][j] += 1
ans = min(work(P),work(Q))
if ans == float('inf'):
    print('Impossible')
else:
    print(ans)
```





### 2023.12.25

#### 1、Erase First or Second Letter

https://codeforces.com/problemset/problem/1917/B

这道题我真的感觉想的不太清楚，感觉有点像愉悦旋律的最短长度，比较重要的一点就是我们总可以先进行 $$i$$ 次第一类操作再进行 $$j$$ 次第二类操作。

代码：

```python
for _ in range(int(input())):
    n = int(input())
    sentence = list(input())
    my_set = set()
    ans = 0
    for letter in sentence:
        my_set.add(letter)
        ans += len(my_set)
    print(ans)
```



#### 2、NBA门票价格变了

http://cs101.openjudge.cn/practice/27441/

同样的二进制优化，没什么区别。

代码：

```python
import math
n,m = map(int,input().split())
money = list(map(int,input().split()))
nums = list(map(int,input().split()))
dp = {0:0}
for k in range(m):
    limit = int(math.log(nums[k]+1,2))
    rest = (nums[k]-(1 << limit)+1)*money[k]
    for p in range(limit):
        temp = (1 << p)*money[k]
        delta = 1 << p
        if temp <= n:
            for j in range(n-temp,-1,-1):
                if j in dp:
                    if j+temp in dp:
                        dp[j+temp] = min(dp[j+temp],dp[j]+delta)
                    else:
                        dp[j+temp] = dp[j]+delta
    delta = nums[k] - (1 << limit) + 1
    if delta and rest <= n:
        for j in range(n-rest,-1,-1):
            if j in dp:
                if j+rest in dp:
                    dp[j+rest] = min(dp[j+rest],dp[j]+delta)
                else:
                    dp[j+rest] = dp[j]+delta
if n in dp:
    print(dp[n])
else:
    print('Fail')
```



#### 3、Line Trip

https://codeforces.com/problemset/problem/1901/A

非常简单的一道题目。

代码：

```python
for _ in range(int(input())):
    n,x = map(int,input().split())
    nums = [0]+list(map(int,input().split()))+[x]
    diff = [nums[i+1]-nums[i] for i in range(n+1)]
    diff[-1] = 2*diff[-1]
    print(max(diff))
```



#### 4、Chip and Ribbon

https://codeforces.com/contest/1901/problem/B

这道题最开始没想明白，现在知道了，只要右边的比左边高，那么一定需要二者之差的次数的转移，再加上最开始的就可以得到答案。

代码：

```python
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    ans = nums[0]-1
    for j in range(n-1):
        if nums[j+1] > nums[j]:
            ans += nums[j+1]-nums[j]
    print(ans)
```



#### 5、Add, Divide and Floor

https://codeforces.com/contest/1901/problem/C

这道题首先找到最大和最小，然后进行分析就可以了，注意到奇数除了之后还会有一个0.5，所以遇到奇数应该加一，偶数则不用。

代码：

```python
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    a,b = min(nums),max(nums)
    ans = 0
    result = []
    while a < b:
        if a % 2 == 0:
            a,b = a//2,b//2
            ans += 1
            result.append(0)
        else:
            a,b = (a+1)//2,(b+1)//2
            ans += 1
            result.append(1)
    if ans == 0 or ans > n:
        print(ans)
    else:
        print(ans)
        print(' '.join(map(str,result)))
```



#### 6、Yet Another Monster Fight

https://codeforces.com/contest/1901/problem/D

这道题有点类似于CF上的另一道题目——Running Miles，都是找到规律后构造新数列，然后按要求取极值。

代码：

```python
n = int(input())
nums = list(map(int,input().split()))
if n == 1:
    print(nums[0])
    quit()
positive = [nums[k]+k for k in range(n)][::-1]
opposite = [nums[k]+n-1-k for k in range(n)]
for k in range(1,n):
    positive[k] = max(positive[k-1],positive[k])
    opposite[k] = max(opposite[k-1],opposite[k])
positive.reverse()
ans = min(max(nums[0],positive[1]),max(nums[-1],opposite[n-2]))
for j in range(1,n-1):
    ans = min(ans,max(nums[j],positive[j+1],opposite[j-1]))
print(ans)
```





### 2023.12.26

#### 1、Sequence

http://cs101.openjudge.cn/routine/02313/

这道题做了好久……感觉有时候真的不能投机取巧，否则很容易出错、出问题。

代码：

```python
n = int(input())
nums = [int(input()) for _ in range(n)]
B = [0 for _ in range(n)]
B[0],B[-1] = nums[0],nums[-1]
for k in range(1,n-1):
    if B[k-1] < nums[k] > nums[k+1]:
        B[k] = max(B[k-1],nums[k+1])
    elif B[k-1] > nums[k] < nums[k+1]:
        B[k] = min(B[k-1],nums[k+1])
    else:
        B[k] = nums[k]
V = 0
for j in range(1,n):
    V += abs(B[j]-B[j-1])+abs(nums[j]-B[j])
print(V)
```





### 2023.12.27

#### 1、数学密码

http://cs101.openjudge.cn/routine/21532/

这道题就是我想复杂了……直接遍历就可以！

代码：

```python
n = int(input())
j = 6
while True:
    if n % j == 0:
        print(n//j)
        break
    j += 1
```



#### 2、垂直直方图

http://cs101.openjudge.cn/routine/01802/

这道题主要考察对于字符串的应用，比较基础。

代码：

```python
from collections import defaultdict
my_dict = defaultdict(int)
for _ in range(4):
    for letter in input():
        if letter.isalpha():
            my_dict[letter] += 1
lines = max(my_dict.values())
matrix = [[' ' for _ in range(26)] for _ in range(lines)]
Alpha_lst = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(lines):
    for j in range(26):
        if my_dict[Alpha_lst[j]]:
            matrix[i][j] = '*'
            my_dict[Alpha_lst[j]] -= 1
matrix.reverse()
for row in matrix:
    print(' '.join(row))
print(' '.join(Alpha_lst))
```



#### 3、19岁生日礼物-Birthday Gift

http://cs101.openjudge.cn/routine/07810/

比较简单的一道题目。

代码：

```python
def judge(n):
    if '19' in n or int(n) % 19 == 0:
        return 'Yes'
    return 'No'
for _ in range(int(input())):
    print(judge(input()))
```



#### 4、Post Office

http://cs101.openjudge.cn/routine/01160/

感觉很难的一道题，转移方程比较好想，但是有可能会超时，这里的代码是看了网上的说法之后给出的。

代码：

```python
v,p = map(int,input().split())
nums = list(map(int,input().split()))
dp = [[float('inf') for _ in range(400)] for _ in range(400)]
pre,suf = [0 for _ in range(400)],[0 for _ in range(400)]
w = mark = [[0 for _ in range(400)] for _ in range(400)]
for i in range(1,v+1):
    pre[i] = pre[i-1]+nums[i-1]-nums[0]
for j in range(v,0,-1):
    suf[j] = suf[j+1]+nums[-1]-nums[j-1]
for i in range(1,v+1):
    for j in range(i+1,v+1):
        if i != j:
            mid = (i+j)//2
            w[i][j] = (pre[j]-pre[mid]-(j-mid)*(nums[mid-1]-nums[0])
                       +suf[i]-suf[mid]-(mid-i)*(nums[-1]-nums[mid-1]))
for i in range(v+1):
    dp[i][i] = 0
    dp[i][1] = w[1][i]
for i in range(1,v+1):
    for j in range(min(i,p),0,-1):
        if not mark[i-1][j]:
            mark[i-1][j] = min(i-1,j-1)
        if not mark[i][j+1]:
            mark[i][j+1] = i-1
        for k in range(mark[i-1][j],mark[i][j+1]+1):
            if dp[i][j] > dp[k][j-1]+w[k+1][i]:
                dp[i][j] = dp[k][j-1]+w[k+1][i]
                mark[i][j] = k
print(dp[v][p])
```



#### 5、上机考试

http://cs101.openjudge.cn/practice/16531/

这道题感觉挺怪的，不能超过百分之四十为什么直接那么写就行？……我好像明白了！要注意索引和直接算的不同！！！

代码：

```python
m,n = map(int,input().split())
stu = [[-1]*(n+2)]+[[-1]+list(map(int,input().split()))+[-1] for _ in range(m)]+[[-1]*(n+2)]
grade = [list(map(int,input().split())) for _ in range(m*n)]
ans = 0
for i in range(1,m+1):
    for j in range(1,n+1):
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        for a,b in dir:
            if stu[i+a][j+b] != -1:
                if grade[stu[i+a][j+b]] == grade[stu[i][j]]:
                    ans += 1
                    break
num = 0
lst = sorted([sum(row) for row in grade],reverse=True)
judge = int(m*n*0.4)
for k in lst:
    if k > lst[judge]:
        num += 1
print(ans,num)
```























