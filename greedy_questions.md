# 贪心题目

Updated 2247 GMT+8 Dec 25, 2023



2023 fall, Complied by Hongfei Yan



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231226134858027.png" alt="image-20231226134858027" style="zoom:50%;" />



## 01017: 装箱问题

greedy, http://cs101.openjudge.cn/practice/01017

一个工厂制造的产品形状都是长方体，它们的高度都是h，长和宽都相等，一共有六个型号，他们的长宽分别为1\*1, 2\*2, 3\*3, 4\*4, 5\*5, 6\*6。这些产品通常使用一个 6\*6*h 的长方体包裹包装然后邮寄给客户。因为邮费很贵，所以工厂要想方设法的减小每个订单运送时的包裹数量。他们很需要有一个好的程序帮他们解决这个问题从而节省费用。现在这个程序由你来设计。

**输入**：输入文件包括几行，每一行代表一个订单。每个订单里的一行包括六个整数，中间用空格隔开，分别为1*1至6*6这六种产品的数量。输入文件将以6个0组成的一行结尾。

**输出**：除了输入的最后一行6个0以外，输入文件里每一行对应着输出文件的一行，每一行输出一个整数代表对应的订单所需的最小包裹数。

解题思路：4\*4, 5\*5, 6\*6这三种的处理方式较简单，就是每一个箱子至多只能有其中1个，根据他们的数量添加箱子，再用2\*2和1\*1填补。1\*1, 2\*2, 3\*3这些就需要额外分情况讨论，若有剩余的3\*3,每4个3\*3可以填满一个箱子，剩下的3\*3用2\*2和1\*1填补装箱。剩余的2\*2，每9个可以填满一个箱子，剩下的与1\*1一起装箱。最后每36个1\*1可以填满一个箱子，剩下的为一箱子。

样例输入

```
0 0 4 0 0 1 
7 5 1 0 0 0 
0 0 0 0 0 0 
```

样例输出

```
2 
1 
```

来源：Central Europe 1996



**直接用总数把bcdef占的位置都减掉就可以了，思路就清晰起来了。**运用列表，避免多个 if else。

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



## 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110

圣诞节来临了，在城市A中圣诞老人准备分发糖果，现在有多箱不同的糖果，每箱糖果有自己的价值和重量，每箱糖果都可以拆分成任意散装组合带走。圣诞老人的驯鹿最多只能承受一定重量的糖果，请问圣诞老人最多能带走多大价值的糖果。

**输入**

第一行由两个部分组成，分别为糖果箱数正整数n(1 <= n <= 100)，驯鹿能承受的最大重量正整数w（0 < w < 10000），两个数用空格隔开。其余n行每行对应一箱糖果，由两部分组成，分别为一箱糖果的价值正整数v和重量正整数w，中间用空格隔开。

**输出**

输出圣诞老人能带走的糖果的最大总价值，保留1位小数。输出为一行，以换行符结束。

样例输入

```
4 15
100 4
412 8
266 7
591 2
```

样例输出

```
1193.0
```



解题思路：计算平均值降序取，注意每箱糖果都可以拆分成任意散装组合带走。

```python
# 2300012302	张惠雯	生命科学学院
n, w = map(int, input().split())
candies = []

for _ in range(n):
    p, q = map(int, input().split())
    for _ in range(q):
        candies.append(p / q)

candies.sort(reverse=True)

'''
Degenerate slice indices are handled gracefully: an index that is too large 
is replaced by the string size, an upper bound smaller than the lower bound 
returns an empty string." e.g.:
    
w = [1,2,3]; sum(w[:6])
Out: 6
'''
value = sum(candies[:w])

print("{:.1f}".format(value))
```



## 18211: 军备竞赛

greedy/two pointers, http://cs101.openjudge.cn/practice/18211

鸣人是木叶村的村长，最近在跟敌国进行军备竞赛，他手边有N份武器设计图，每张设计图有制作成本（大于等于零）且最多使用一次，可以选择花钱制作或是以同样的价钱卖给敌国，同时任意时刻敌国的武器不能比我国更多，鸣人的目标是在不负债的前提下武器种类比敌国越多越好。

**输入**

第一行为起始整数经费p,并且0≤p。且要求任何时刻p不能小于0.
第二行为n个整数，以空格分隔，并且0≤每个整数。代表每张设计图的制作成本，同时也是卖价，最多用一次(无法又制作又卖).

**输出**

一个整数，代表武器种类最多比敌国多多少.

样例输入

```
Sample1 Input:
10
20 30 40

Sample1 Output:
0

解释: 10元不足以制作20元的武器，所以为0，也不能先卖50元的，不能让敌国武器比木叶多

Sample2 Input:
10
15 5

Sample2 Output:
1

解释: 10元可以制作5元的武器，木叶的武器比对手多一件
```

样例输出

```
Sample3 Input:
40
20 80 60 40

Sample3 Output:
2

解释: 先制作20元的武器，再贩卖80元的武器，这时经费为100，再制作40、60的武器，木叶的武器比对手多二件
```

来源：cs101-2018



思路：类似二分双指针left, right，有钱就买（制作），没钱就卖。感谢2020fall-cs101 汤建浩，指正 cnt<0情况。

```python
p = int(input())
n = [int(x) for x in input().split()]
n.sort()

cnt = 0
left = 0
right = len(n) - 1

while left<=right:
    if n[left]<=p:
        cnt += 1
        p -= n[left]
        left += 1
    else:
        if right==left:
            break
        
        p += n[right]
        cnt -= 1
        if cnt<0:
            cnt=0
            break

        right -= 1

print(cnt)
```



## 19948: 因材施教

greedy, http://cs101.openjudge.cn/practice/19948

有一所魔法高校招入一批学生，为了贯彻因材施教的理念，学校打算根据他们的魔法等级进行分班教育。在确定班级数目的情况下，班级内学生的差异要尽可能的小，也就是各个班级内学生的魔法等级要尽可能的接近。
例如：现在有(n = 7)位学生，他们的魔法等级分别为(r = [2, 7, 9, 9, 16, 28, 45])，我们要将他们分配到(m = 3)个班级，如果按照([2, 7], [9, 9], [16, 28, 45])的方式分班，则他们的总体差异为(d = (7 - 2) + (9 - 9) + (45 - 16) = 34)。

**输入**

第一行为两个整数:学生人数n和班级数目m，1 <= m <= n <= 10^5。
第二行为n个整数：每位学生的魔法等级ri，1 <= ri <= 10^9。

**输出**

一个整数：学生的最小总体差异d。

样例输入

```
Sample1 Input
7 3
2 7 9 9 16 28 45

Sample1 Output
14

解释：最小总体差异的分班方式为([2, 7, 9, 9, 16], [28], [45])
```

样例输出

```
Sample2 Input
15 9
90 73 116 47 400 212 401 244 13 372 248 56 194 482 177

Sample2 Output
65

解释：最小总体差异的分班方式为([13], [47, 56, 73, 90], [116], [177, 194], [212], [244, 248], [372], [400, 401], [482])
```

来源：cs101 2019 Final Exam



思路：本质就是去掉m-1个最大的差值。先升序排序魔法等级，再按照差值逆序排。

```python
n,m = map(int,input().split())
r = [int(x) for x in input().split()]
r.sort()
rd = []
for i in range(len(r)-1):
    rd.append(r[i+1] - r[i])

rd.sort(reverse=True)
d = sum(rd)

for i in rd:
    d -= i
    m -= 1
    if m==1:
        break

print(d)
```





## 16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

寒假马上就要到了，龙傲天同学获得了从第0天开始到第60天结束为期61天超长寒假，他想要尽可能丰富自己的寒假生活。
现提供若干个活动的起止时间，请计算龙同学这个寒假至多可以参加多少个活动？注意所参加的活动不能有任何时间上的重叠，在第x天结束的活动和在第x天开始的活动不可同时选择。

**输入**

第一行为整数n，代表接下来输入的活动个数(n < 10000)
紧接着的n行，每一行都有两个整数，第一个整数代表活动的开始时间，第二个整数代表全结束时间

**输出**

输出至多参加的活动个数

样例输入

```
5
0 0
1 1
2 2
3 3
4 4
```

样例输出

```
5
```

来源：cs10117 Final Exam



2020fall-cs101-苏荣薰，Greedy解题思路：只要按照结束时间排序，然后参加第一个活动，接下来的活动能参加就参加。因为这样的话不会使结果更坏，能参加尽量多的活动。假设最优解并不包括第一个结束的活动，那么最优解中第一个活动必然可以替换成第一个结束的活动，选择参加第一个结束的活动不会使结果更坏。

解题思路：随时间减少，可参加的活动数量也减少，因此应当以结束时间排序（如果选最先开始的，最短时间的活动都会出现问题）。排序后第一个活动一定能参加，使用贪心算法，选择开始时间晚于上一次结束时间的事件，次数加 1。

Greedy

```python
n = int(input())
m = [[int(x) for x in input().split()] for i in range(n)]
for i in range(n):
    m[i][0], m[i][1] = m[i][1], m[i][0]
m.sort()
y = 1
a = m[0][0]
for i in range(n-1):
    if m[i+1][1]>a:
        y += 1
        a = m[i+1][0]
print(y)
```

Greedy

```python
n = int(input())
s = [[int(x) for x in input().split()] for _ in range(n)]
s.sort(key = lambda x:x[1])

m = s[0][1]
a = 1
for i in range(1,n):
    if s[i][0] > m:
        a += 1
        m = s[i][1]

print(a)
```



## 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

Assume the coasting is an infinite straight line. Land is in one side of coasting, sea in the other. Each small island is a point locating in the sea side. And any radar installation, locating on the coasting, can only cover d distance, so an island in the sea can be covered by a radius installation, if the distance between them is at most d.

We use Cartesian coordinate system, defining the coasting is the x-axis. The sea side is above x-axis, and the land side below. Given the position of each island in the sea, and given the distance of the coverage of the radar installation, your task is to write a program to find the minimal number of radar installations to cover all the islands. Note that the position of an island is represented by its x-y coordinates.
![image-20231021115237439](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231021115237439.png)
Figure A Sample Input of Radar Installations

**输入**

The input consists of several test cases. The first line of each case contains two integers n (1<=n<=1000) and d, where n is the number of islands in the sea and d is the distance of coverage of the radar installation. This is followed by n lines each containing two integers representing the coordinate of the position of each island. Then a blank line follows to separate the cases.

The input is terminated by a line containing pair of zeros

**输出**

For each test case output one line consisting of the test case number followed by the minimal number of radar installations needed. "-1" installation means no solution for that case.

样例输入

```
3 2
1 2
-3 1
2 1

1 2
0 2

0 0
```

样例输出

```
Case 1: 2
Case 2: 1
```

来源: Beijing 2002



```python
rr=0
while True:
    n,d=map(int,input().split())
    if n==d==0:
        break
    else:
        rr+=1
        empty=[]
        for i in range(n):
            x,y=map(int,input().split())
            if d>=y:
                #empty.append([x+(d**2-y**2)**0.5,x-(d**2-y**2)**0.5])
                empty.append([x-(d**2-y**2)**0.5,x+(d**2-y**2)**0.5])
        input()
        if len(empty)<n:
            print("Case {}: -1".format(rr))
        elif d<0:
            print("Case {}: -1".format(rr))
        else:
            empty.sort(reverse=True)
            #number=n
            number = len(empty)
            c = empty[0][0]
            for j in range(1,n):
                #if empty[j][0]>=empty[j-1][1]:
                if c > empty[j][1]:
                    c = empty[j][0]
                else:
                   number-=1

            print("Case {}: {} ".format(rr,number))
```



## 04144: 畜栏保留问题

greedy, http://cs101.openjudge.cn/practice/04144/

农场有N头牛，每头牛会在一个特定的时间区间[A, B]（包括A和B）在畜栏里挤奶，且一个畜栏里同时只能有一头牛在挤奶。现在农场主希望知道最少几个畜栏能满足上述要求，并要求给出每头牛被安排的方案。对于多种可行方案，主要输出一种即可。

**输入**

输入的第一行包含一个整数N(1 ≤ N ≤ 50, 000)，表示有N牛头；接下来N行每行包含两个数，分别表示这头牛的挤奶时间\[Ai, Bi](1 ≤ A≤ B ≤ 1, 000, 000)。

**输出**

输出的第一行包含一个整数，表示最少需要的畜栏数；接下来N行，第i+1行描述了第i头牛所被分配的畜栏编号（从1开始）。

样例输入

```
5
1 10
2 4
3 6
5 8
4 7
```

样例输出

```
4
1
2
3
2
4
```

来源: http://poj.org/problem?id=3190



```python
# 时间调度问题
# cows元素：（start, end, index，）
import heapq
max_num = 1
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
        heapq.heappush(column, [cows[i][1], max_num])
        max_num += 1
        number[cows[i][2]] = max_num

print(len(column))  # 【畜栏】的长度即为畜栏数量
for i in number:
    print(i)
```



## 18164: 剪绳子

greedy/huffman, http://cs101.openjudge.cn/practice/18164/

思路： 剪绳子，实际上是 Huffman编码/树，https://zhuanlan.zhihu.com/p/42238580

```python
# OJ18164
import sys
try: fin = open('test.in','r').readline
except: fin = sys.stdin.readline

n = int(fin())
import heapq
a = list(map(int, fin().split()))
heapq.heapify(a)
ans = 0
for i in range(n-1):
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    z = x + y
    heapq.heappush(a, z)
    ans += z
print(ans)
```



## 01065: Wooden Sticks

greedy, http://cs101.openjudge.cn/practice/01065/

There is a pile of n wooden sticks. The length and weight of each stick are known in advance. The sticks are to be processed by a woodworking machine in one by one fashion. It needs some time, called setup time, for the machine to prepare processing a stick. The setup times are associated with cleaning operations and changing tools and shapes in the machine. The setup times of the woodworking machine are given as follows: 
(a) The setup time for the first wooden stick is 1 minute. 
(b) Right after processing a stick of length l and weight w , the machine will need no setup time for a stick of length l' and weight w' if l <= l' and w <= w'. Otherwise, it will need 1 minute for setup. 
You are to find the minimum setup time to process a given pile of n wooden sticks. For example, if you have five sticks whose pairs of length and weight are ( 9 , 4 ) , ( 2 , 5 ) , ( 1 , 2 ) , ( 5 , 3 ) , and ( 4 , 1 ) , then the minimum setup time should be 2 minutes since there is a sequence of pairs ( 4 , 1 ) , ( 5 , 3 ) , ( 9 , 4 ) , ( 1 , 2 ) , ( 2 , 5 ) . 

输入

The input consists of T test cases. The number of test cases (T) is given in the first line of the input file. Each test case consists of two lines: The first line has an integer n , 1 <= n <= 5000 , that represents the number of wooden sticks in the test case, and the second line contains 2n positive integers l1 , w1 , l2 , w2 ,..., ln , wn , each of magnitude at most 10000 , where li and wi are the length and weight of the i th wooden stick, respectively. The 2n integers are delimited by one or more spaces. 

输出

The output should contain the minimum setup time in minutes, one per line. 

样例输入

```
3 
5 
4 9 5 2 2 1 3 5 1 4 
3 
2 2 1 1 2 2 
3 
1 3 2 2 3 1 
```

样例输出

```
2
1
3
```

来源: Taejon 2001



```python
def min_setup_time(sticks):
    n = len(sticks)
    check = [0]*n
    setup_time = 0
    while (0 in check):
        #print(check)
        #print(sticks)
        i = 0
        for j in range(n):
            if check[j] == 0:
                i = j
                break
        current = sticks[i]
        check[i] = 1
        setup_time += 1
        i += 1
        while  i < n:
            if  check[i]==0 and current[0]<=sticks[i][0] and  current[1]<= sticks[i][1]:
                check[i] = 1
                current = sticks[i]
            
            i +=1

    return setup_time


T = int(input())  
for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    sticks = [(data[i], data[i + 1]) for i in range(0, 2 * n, 2)]
    sticks.sort()
    print(min_setup_time(sticks)) 
```



```python
#dilworth和最长单调子序列
# 答案就是对l排序后求w的最长严格递减子序列（用Dilworth's theorem不难证明），
# 最长严格递减子序列有经典的nlogn的算法
# （https://en.wikipedia.org/wiki/Longest_increasing_subsequence）。
#一般有一样的都不是大问题，因为可以把(3,5) (3,6) 直接看作(3.1, 5) (3.2, 6)

import bisect

def doit():
    n = int(input())
    data = list(map(int, input().split()))
    sticks = [(data[i], data[i + 1]) for i in range(0, 2 * n, 2)]
    sticks.sort()
    f = [sticks[i][1] for i in range(n)]
    f.reverse()
    stk = []

    for i in range(n):
        t = bisect.bisect_left(stk, f[i])
        if t == len(stk):
            stk.append(f[i])
        else:
            stk[t] = f[i]

    print(len(stk))

T = int(input())
for _ in range(T):
    doit()
```



# 其他问题



## 12559: 最大最小整数 v0.3

greedy/strings/sortings, http://cs101.openjudge.cn/practice/12559



假设有n个正整数，将它们连成一片，将会组成一个新的大整数。现需要求出，能组成的最大最小整数。

比如，有4个正整数，23，9，182，79，连成的最大整数是97923182，最小的整数是18223799。

**输入**

第一行包含一个整数n，1<=n<=1000。
第二行包含n个正整数，相邻正整数间以空格隔开。

**输出**

输出为一行，为这n个正整数能组成的最大的多位整数和最小的多位整数，中间用空格隔开。

样例输入

```
Sample1 in:
4
23 9 182 79

Sample1 out:
97923182 18223799
```

样例输出

```
Sample2 in:
2
11 113

Sample2 out:
11311 11113
```

提示

位数不同但前几位相同的时候。例如： 898 8987，大整数是898+8987，而不是8987+898。

来源：cs10116 final exam



思路：先拼接出最小值：即字典序最小；要保证每一个小的字符串，左移到合适位置，需要两两比较（刚好是冒泡排序）。这个题目是个不容易的，字符串处理题目。

求minimum时，对相邻两strA[k]与A[k+1]，比较A[k]+A[k+1]与A[k+1]+A[k]的大小，若A[k+1]+A[k]大，颠倒A[k]与A[k+1]；最多交换len(A)-1次。求maximum时，颠倒求minimum时的有序序列即可。使用冒泡排序，循环(n-1)次。

把这些数当成字符串处理，然后采用类似冒泡排序的做法排出大小。

```python
# O(n^2)
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



## 19961: 最大点数(外太空2048)

http://cs101.openjudge.cn/practice/19961/

2048是一款不用念诗能够实现时间跳跃的小游戏（参考https://2048game.com），只需玩5分钟，就可以跳到两小时后的世界。J同学在进行了上百次时间穿越后，得到灵感设计了一款新游戏，规则如下。
接近原2048规则（重力作用）中移动方块和增加点数的方法不变，棋盘从4*4变成m*n型，开始时棋盘上即摆放了一些不同点数的方块，但每次移动后不会生成新的方块。在有限的操作次数（往上/下/左/右方向上移动一次记为一次操作）内，得到更高点数（即所有方块中点数最高者）。

Note: 我们的2048，是在外太空玩的，不符合重力作用，规则如下图。
![img](http://media.openjudge.cn/images/upload/1576719539.png)

**输入**

第一行：整数m与n（2 <= m, n <= 10）,最大操作次数p（1 <= p <= 6）。空格分隔。
之后m行：空格分隔的n个整数，代表每一格上方块的点数（2, 4, 8, 16, ..., 1024）。若为0，则表示此格没有方块。这m行输入保证不全为0（即不会输入空棋盘）。

**输出**

一个整数，代表p次操作内能得到的最高点数。

样例输入

```
Sample1 Input:
4 4 2
2 4 512 16
2 128 16 16
2 8 256 0
2 512 256 2

Sample1 Output:
1024

解释：第一步，向下移动，变成
0 4 0 0
0 128 512 0
4 8 16 32
4 512 512 2
第二步，向左移动，将第4行两个512拼合得到1024。


Sample2 Input:
2 4 2
2 2 4 4
0 0 8 2

Sample2 Output:
16
# 一步2 2 4 4 -> 4 4 4 -> 8 4，得0 0 8 4，第二步向下就有16。
```

样例输出

```
Sample3 Input:
2 3 6
2 4 4
32 16 8

Sample3 Output:
64

# 第一步，向右移动，第二步，向下移动，第三步，向左移动，第四步，向左移动。
后两步无论怎样移动最大值都是64。

Sample4 Input:
4 3 5
32 256 128
256 128 64
32 64 128
256 128 256

Sample4 Output:
256

# 此局面如何移动都不会变，故最大值为256。
```

提示

在太空，没有阻力，所以都是完全非弹性碰撞。
碰撞后，尾部算起的相同的两个数字先黏结。因为在外太空没有能量损失，
黏结后，如果尾部算起还有两个数字相同，可以继续黏结。如样例2所示。

来源: cs101-2019 胡康德龙

```python
# 23 黄原明 化院
# 测试数据小，可以任人摆布？直接枚举？
from itertools import product
from copy import deepcopy
m,n,p=map(int,input().split())
board=[list(map(int,input().split())) for i in range(m)]
def turn(board,dirt):
    if dirt==2:
        changed = 0
        while True:
            c = 0
            for i in range(m):
                for j in range(n - 1, 0, -1):
                    if board[i][j] > 0 and board[i][j - 1] == 0:
                        board[i][j], board[i][j - 1] = 0, board[i][j]
                        c = 1
            changed = c
            if not c:
                break
        for i in range(m):
            for j in range(n - 1, 0, -1):
                if board[i][j] == board[i][j - 1]:
                    board[i][j - 1] *= 2
                    board[i][j] = 0
                    changed = 1
        while True:
            c = 0
            for i in range(m):
                for j in range(n - 1, 0, -1):
                    if board[i][j] > 0 and board[i][j - 1] == 0:
                        board[i][j], board[i][j - 1] = 0, board[i][j]
                        c = 1
            if not c:
                break
        return changed
    elif dirt==3:
        changed = 0
        while True:
            c = 0
            for i in range(m):
                for j in range(0,n-1):
                    if board[i][j] > 0 and board[i][j+1] == 0:
                        board[i][j], board[i][j+1] = 0, board[i][j]
                        c = 1
            changed = c
            if not c:
                break
        for i in range(m):
            for j in range(0,n-1):
                if board[i][j] == board[i][j+1]:
                    board[i][j+1] *= 2
                    board[i][j] = 0
                    changed = 1
        while True:
            c = 0
            for i in range(m):
                for j in range(0,n-1):
                    if board[i][j] > 0 and board[i][j+1] == 0:
                        board[i][j], board[i][j+1] = 0, board[i][j]
                        c = 1
            if not c:
                break
        return changed
    elif dirt==0:
        changed = 0
        while True:
            c = 0
            for i in range(m-1,0,-1):
                for j in range(n):
                    if board[i][j] > 0 and board[i-1][j] == 0:
                        board[i][j], board[i-1][j] = 0, board[i][j]
                        c = 1
            changed = c
            if not c:
                break
        for i in range(m-1,0,-1):
            for j in range(n):
                if board[i][j] == board[i-1][j]:
                    board[i-1][j] *= 2
                    board[i][j] = 0
                    changed = 1
        while True:
            c = 0
            for i in range(m-1,0,-1):
                for j in range(n):
                    if board[i][j] > 0 and board[i-1][j] == 0:
                        board[i][j], board[i-1][j] = 0, board[i][j]
                        c = 1
            if not c:
                break
        return changed
    elif dirt == 1:
        changed = 0
        while True:
            c = 0
            for i in range(0,m-1):
                for j in range(n):
                    if board[i][j] > 0 and board[i+1][j] == 0:
                        board[i][j], board[i+1][j] = 0, board[i][j]
                        c = 1
            changed = c
            if not c:
                break
        for i in range(0,m-1):
            for j in range(n):
                if board[i][j] == board[i+1][j]:
                    board[i+1][j] *= 2
                    board[i][j] = 0
                    changed = 1
        while True:
            c = 0
            for i in range(0,m-1):
                for j in range(n):
                    if board[i][j] > 0 and board[i+1][j] == 0:
                        board[i][j], board[i+1][j] = 0, board[i][j]
                        c = 1
            if not c:
                break
        return changed

#用枚举法解，这样最多4096种情况
max_=0
for i in product(range(4),repeat=p):
    mx=deepcopy(board)
    i=list(i)
    for dirt in i:
        turn(mx,dirt)
    max__=0
    for a in range(m):
        for b in range(n):
            if mx[a][b]>max__:
                max__=mx[a][b]
    if max__>max_:
        max_=max__
print(max_)
```

