# 2023fall-cs101 Notes

Updated 1041 GMT+8 Jan 24, 2024

2023 fall, Complied by Hongfei Yan



week1 课程概述 202309_ICOverview.pptx

week2 计算机文化 202309_A brief History of computer Development.pptx

week3 编程语言 计算机基础补充知识.pptx，202309_ProgramLanguage.pptx

week4 国庆节 Oct月考

week5 排序和超时 202310-17_CTP-Sorting.pptx

# 1017-Week6 贪心和矩阵 

2023年10月份，主要是掌握矩阵、贪心题目，最好能涉及到简单的DP题目。

==内容较多，但是不会拖堂，到时间就下课。==



目录：

**Sortings**: 可以按照greedy来理解，因为都有不同的优化策略

​	bubble sort, insert, selection sort, merge sort, quicksort

**Regular expression**: 不做要求，会了可以用。

​	04015: 邮箱验证，24834:通配符匹配，

​	CF58A. Chat room, https://codeforces.com/problemset/problem/58/A

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

克鲁斯卡尔算法是求连通网的最小生成树的另一种方法。与[普里姆算法](https://baike.baidu.com/item/普里姆算法/4255724?fromModule=lemma_inlink)不同，它的时间复杂度为O（eloge）（e为网中的边数），所以，适合于求边稀疏的网的最小生成树。

一个有 n 个结点的[连通图](https://baike.baidu.com/item/连通图/6460995?fromModule=lemma_inlink)的生成树是原图的极小连通子图，且包含原图中的所有 n 个结点，并且有保持图连通的最少的边。 [1] 最小生成树可以用[kruskal](https://baike.baidu.com/item/kruskal/10242089?fromModule=lemma_inlink)（克鲁斯卡尔）算法或[prim](https://baike.baidu.com/item/prim/10242166?fromModule=lemma_inlink)（普里姆）算法求出。

普里姆算法（[Prim算法](https://baike.baidu.com/item/Prim算法/10986864?fromModule=lemma_inlink)），图论中的一种算法，可在加权连通图里搜索[最小生成树](https://baike.baidu.com/item/最小生成树?fromModule=lemma_inlink)。意即由此算法搜索到的边子集所构成的树中，不但包括了连通图里的所有顶点（英语：Vertex (graph theory)），且其所有边的权值之和亦为最小。



https://stackoverflow.com/questions/47238823/why-selection-sort-is-not-greedy

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231015120427880.png" alt="image-20231015120427880" style="zoom:50%;" />



## Regular expression

正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

**正则表达式**，又称规则表达式**,**（Regular Expression，在代码中常简写为regex、regexp或RE），是一种[文本模式](https://baike.baidu.com/item/文本模式/7355156?fromModule=lemma_inlink)，包括普通字符（例如，a 到 z 之间的字母）和[特殊字符](https://baike.baidu.com/item/特殊字符/112715?fromModule=lemma_inlink)（称为"[元字符](https://baike.baidu.com/item/元字符/6062776?fromModule=lemma_inlink)"），是[计算机科学](https://baike.baidu.com/item/计算机科学/9132?fromModule=lemma_inlink)的一个概念。正则表达式使用单个[字符串](https://baike.baidu.com/item/字符串/1017763?fromModule=lemma_inlink)来描述、匹配一系列匹配某个[句法规则](https://baike.baidu.com/item/句法规则/53352483?fromModule=lemma_inlink)的字符串，通常被用来检索、替换那些符合某个模式（规则）的文本。



### 04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015

POJ 注册的时候需要用户输入邮箱，验证邮箱的规则包括：
1)有且仅有一个'@'符号
2)'@'和'.'不能出现在字符串的首和尾
3)'@'之后至少要有一个'.'，并且'@'不能和'.'直接相连
满足以上3条的字符串为合法邮箱，否则不合法，
编写程序验证输入是否合法

**输入**

输入包含若干行，每一行为一个代验证的邮箱地址，长度小于100

**输出**

每一行输入对应一行输出
如果验证合法，输出 YES
如果验证非法：输出 NO

样例输入

```
.a@b.com
pku@edu.cn
cs101@gmail.com
cs101@gmail
```

样例输出

```
NO
YES
YES
NO
```





这题目输入没有明确结束，需要套在try ...  except里面。测试时候，需要模拟输入结束，看你是window还是mac。If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.



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

[\^xyz]，匹配未包含的任意字符。例如，“[\^abc]”可以匹配“plain”中的“plin”任一字符。

$匹配输入行尾。

(pattern)，匹配pattern并获取这一匹配。所获取的匹配可以从产生的Matches集合得到。



https://regex101.com

![image-20231017131949282](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017131949282.png)



### 24834: 通配符匹配

http://cs101.openjudge.cn/practice/24834/

给定一个字符串s和一个字符模式p，请实现一个支持'?'和'*'的通配符匹配功能。

其中‘?’可以匹配任何单个字符，如‘a?c’可以成功匹配‘aac’,‘abc’等字符串，但不可匹配‘ac’,‘aaac’等字符串 。

‘\*’ 可以匹配任意长度字符串（包括空字符串）,如‘a*c’可以成功匹配‘ac’,‘abdc’,‘abc’,‘aaac’等字符串，但不可匹配‘acb’，‘cac’等字符串。

两个字符串完全匹配才算匹配成功。

**输入**

输入为一个数字n表示测试字符串与字符模式对数，换行。(n ≤ 30)
后续2n行为每组匹配的s与p，每行字符串后换行。
s 非空，只包含从 a-z 的小写字母。
p 非空，只包含从 a-z 的小写字母，以及字符 ? 和 *。
字符串s和p的长度均小于50

**输出**

每一组匹配串匹配成功输出‘yes’,否则输出‘no’。

样例输入

```
3
abc
abc
abc
a*c
abc
a??c
```

样例输出

```
yes
yes
no
```





```python
#23n2300017735(夏天明BrightSummer)
import re

for i in range(int(input())):
    s, p = input(), input().replace("?", ".{1}").replace("*", ".*") + "$"
    print("yes" if re.match(p, s) else "no")
```

.点，匹配除“\n”和"\r"之外的任何单个字符。要匹配包括“\n”和"\r"在内的任何字符，请使用像“[\s\S]”的模式。

\*，匹配前面的子表达式任意次。例如，z*能匹配“z”，也能匹配“zo”以及“zoo”。*等价于{0,}。



### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A

Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word *s*. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word *s*.

**Input**

The first and only line contains the word *s*, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

**Output**

If Vasya managed to say hello, print "YES", otherwise print "NO".

Examples

input

```
ahhellllloou
```

output

```
YES
```

input

```
hlelo
```

output

```
NO
```





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



https://stackoverflow.com/questions/43233535/explicitly-define-datatype-in-python-function 

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017141419717.png" alt="image-20231017141419717" style="zoom: 50%;" />



## Greedy

**基本思想：**
贪心算法是指从问题的初始状态出发，通过多次的贪心选择，最终得到整个问题的最优解。它是一种最接近人们日常思维的解题算法。由于贪心算法比较简单直观（贪心算法和动态规划的难度取决于具体的问题和解题的思路），因此在最优化问题中有着广泛的应用。

贪心策略通常只考虑当前局部最优的策略，最终得到全局的最优解。这是由于问题本身包含特定的性质，保证了当前局部的贪心策略可以获得最优解。1）由于贪心的局部性，因此贪心算法往往也比其他算法更加简单，易于实现。2）与此同时，一些直观的贪心策略虽然在局部是最优的，但是能否保证得到全局的最优解是贪心问题的关键。

贪心算法的应用相对来说更为灵活多样，**没有一个固定的模板或规律可循**。贪心算法的核心思想是在每一步选择中都采取当前看起来最优的选择，以期望最终能够达到全局最优解。然而，并不是所有问题都适合使用贪心算法，并且在使用贪心算法时，需要注意问题的特殊性和贪心选择的合理性。

在使用贪心算法时，通常需要满足**贪心选择性质**和**最优子结构性质**。贪心选择性质指的是在做出每一步选择时，都选择当前最优的解决方案。最优子结构性质指的是问题的最优解可以通过子问题的最优解来构造。当问题满足贪心选择性质和最优子结构性质时，贪心算法往往可以得到全局最优解。

然而，贪心算法也有其局限性。由于贪心算法的策略是局部最优，而不进行全局考虑，因此有些问题无法通过贪心算法得到最优解。在这种情况下，动态规划等其他算法思想可能更适用。



![image-20231017140409613](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017140409613.png)



•是在问题求解时，总是做出在当前看来是最好的选择，不从整体最优上考虑

•贪心算法没有固定的算法框架，关键是贪心策略的选择，贪心策略使用的前提是局部最优能导致全局最优

•常规贪心

*OJ01017：[装箱问题](http://cs101.openjudge.cn/practice/01017)

*CF1000B: [Light It Up](https://codeforces.com/problemset/problem/1000/B)

CF1221A: [2048 ](http://codeforces.com/problemset/problem/1221/A)[Game](http://codeforces.com/problemset/problem/1221/A)





### 01017:装箱问题

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

Greedy, http://cs101.openjudge.cn/practice/25353/

有 N 名同学从左到右排成一排，第 i 名同学的身高为 hi。现在张老师想改变排队的顺序，他能进行任意多次（包括0次）如下操作：

\- 如果两名同学相邻，并且他们的身高之差不超过 D，那么老师就能交换他俩的顺序。

请你帮张老师算一算，通过以上操作，字典序最小的所有同学（从左到右）身高序列是什么？

输入

第一行包含两个正整数 $N, D (1≤N≤10^5, 1≤D≤10^9)$。
接下去 N 行，每行一个正整数 hi (1<=hi<=109) 表示从左到右每名同学的身高。

输出

输出 N 行，第 i 行表示答案中第 i 名同学的身高。

样例输入

```
5 3
7
7
3
6
2
```

样例输出

```
6
7
7
2
3
```

提示

【样例解释】
一种交换位置的过程如下：
`7 7 3 6 2-> 7 7 6 3 2-> 7 7 6 2 3-> 7 6 7 2 3-> 6 7 7 2 3`

【数据范围和约定】
对于 10% 的数据，满足 N≤100；
对于另外 20% 的数据，满足 N≤5000；
对于全部数据，满足 $1≤N≤10_5, 1≤D≤10^9, 1≤h_i≤10^9$。



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017133436664.png" alt="image-20231017133436664" style="zoom: 50%;" />

从最左侧的输入高度找起，按照约束条件都找出来，加入暂存列表、排序、同时标志改为True。循环找接下来还没有入选的。

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



2020fall-cs101，黄旭

思路：这道题的关键应该是找到排序的方式，前一个数和后一个数比较，如果位数不足，就要重新从第一位开始比，所以说我就先取这个数列的最大位数，然后把每个数都扩充到相同位数进行比较，就可以了。

```python
# 虽然能AC，但实际上不对。两倍长度是正确的。
from math import ceil
input()
lt = input().split()

max_len = len(max(lt, key = lambda x:len(x)))
lt.sort(key = lambda x: tuple([int(i) for i in x]) * ceil(max_len/len(x)))
lt1 = lt[::-1]
print(''.join(lt1),''.join(lt))
```



```python
# 两倍长度是正确的。O(nlogn)
from math import ceil
input()
lt = input().split()

max_len = len(max(lt, key = lambda x:len(x)))
lt.sort(key = lambda x: x * ceil(2*max_len/len(x)))
lt1 = lt[::-1]
print(''.join(lt1),''.join(lt))
```



### CF1364A. XXXXX

https://codeforces.com/problemset/problem/1364/A

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A

Ehab loves number theory, but for some reason he hates the number 𝑥. Given an array 𝑎, find the length of its longest subarray such that the sum of its elements **isn't** divisible by 𝑥, or determine that such subarray doesn't exist.

An array 𝑎 is a subarray of an array 𝑏 if 𝑎 can be obtained from 𝑏 by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

**Input**

The first line contains an integer 𝑡 (1≤𝑡≤5) — the number of test cases you need to solve. The description of the test cases follows.

The first line of each test case contains 2 integers 𝑛 and 𝑥 (1≤𝑛≤10^5^, 1≤𝑥≤10^4^) — the number of elements in the array 𝑎 and the number that Ehab hates.

The second line contains 𝑛 space-separated integers $𝑎_1, 𝑎_2, ……, 𝑎_𝑛 (0≤𝑎_𝑖≤10^4)$ — the elements of the array 𝑎.

**Output**

For each testcase, print the length of the longest subarray whose sum isn't divisible by 𝑥. If there's no such subarray, print −1.

Example

input

```
3
3 3
1 2 3
3 4
1 2 3
2 2
0 6
```

output

```
2
3
-1
```

Note

In the first test case, the subarray \[2,3\] has sum of elements 5, which isn't divisible by 3.

In the second test case, the sum of elements of the whole array is 6, which isn't divisible by 4.

In the third test case, all subarrays have an even sum, so the answer is −1.



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017133804692.png" alt="image-20231017133804692" style="zoom:50%;" />



```python
# 查达闻
def r(i):return int(i)%b
for z in range(int(input())):
  a,b=map(int,input().split());a=list(map(r,input().split()))
  if sum(a)%b:print(len(a))
  else:
    n=1
    for i in range(len(a)):
    	if a[i]or a[~i]:print(len(a)-i-1);n=0;break
    if n:print(-1)
```



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017134301175.png" alt="image-20231017134301175" style="zoom:67%;" />



```python
def prefix_sum(nums):
    prefix = []
    total = 0
    for num in nums:
        total += num
        prefix.append(total)
    return prefix
 
def suffix_sum(nums):
    suffix = []
    total = 0
    # 首先将列表反转
    reversed_nums = nums[::-1]
    for num in reversed_nums:
        total += num
        suffix.append(total)
    # 将结果反转回来
    suffix.reverse()
    return suffix
 
 
t = int(input())
for _ in range(t):
    N, x = map(int, input().split())
    a = [int(i) for i in input().split()]
    aprefix_sum = prefix_sum(a)
    asuffix_sum = suffix_sum(a)
 
    left = 0
    right = N - 1
    if right == 0:
        if a[0] % x !=0:
            print(1)
        else:
            print(-1)
        continue
 
    leftmax = 0
    rightmax = 0
    while left != right:
        total = asuffix_sum[left]
        if total % x != 0:
            leftmax = right - left + 1
            break
        else:
            left += 1
 
    left = 0
    right = N - 1
    while left != right:
        total = aprefix_sum[right]
        if total % x != 0:
            rightmax = right - left + 1
            break
        else:
            right -= 1
    
    if leftmax == 0 and rightmax == 0:
        print(-1)
    else:
        print(max(leftmax, rightmax))
```





## 程序生成测试数据

### 26971:分发糖果

greedy, http://cs101.openjudge.cn/routine/26971/

`n` 个孩子站成一排。给你一个整数数组 `ratings` 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

- 每个孩子至少分配到 `1` 个糖果。
- 相邻两个孩子评分更高的孩子会获得更多的糖果。

请你给每个孩子分发糖果，计算并返回需要准备的 **最少糖果数目** 。

**输入**

第一行包含一个整数n。1 <= n <= 2 * 10^4
第二行包含n个整数，相邻整数间以空格隔开。0 <= ratings[i] <= 2 * 10^4

**输出**

一个整数

样例输入

```
Sample1 input:
3
1 0 2
Sample1 output:
5
```

样例输出

```
Sample2 input:
3
1 2 2
Sample2 output:
4
```

提示

tags: greedy

来源

LeetCode 135.分发糖果：https://leetcode.cn/problems/candy/





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

greedy, http://cs101.openjudge.cn/routine/26976/

如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 **摆动序列 。**第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

- 例如， 

[1, 7, 4, 9, 2, 5] 是一个 **摆动序列** ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

- 相反，

[1, 4, 7, 2, 5]

[1, 7, 4, 5, 5] 

**子序列** 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 nums ，返回 nums 中作为 **摆动序列** 的 **最长子序列的长度** 。

**输入**

第一行包含一个整数n。1 <= n <= 1000

第二行包含n个整数，相邻整数间以空格隔开。0 <= nums[i] <= 1000

**输出**

一个整数

样例输入

```
sample1 input:
6
1 7 4 9 2 5
sample1 output:
6

sample2 input:
10
1 17 5 10 13 15 10 5 16 8
sample2 output:
7
```

样例输出

```
sample3 input:
9
1 2 3 4 5 6 7 8 9
sample3 output:
2
```

提示

tags: greedy

来源

LeetCode 376. 摆动序列: https://leetcode.cn/problems/wiggle-subsequence/





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



### CF1868A. Fill in the Matrix

 tags: constructive algorithms （If there are multiple solutions, you may output any of them. 多解的题目需要spj来处理，special judge）

constructive algorithms, implementation, 1300, https://codeforces.com/problemset/problem/1868/A

There is an empty matrix 𝑀 of size 𝑛×𝑚.

Zhongkao examination is over, and Daniel would like to do some puzzle games. He is going to fill in the matrix  using permutations of length 𝑚. That is, each row of 𝑀 must be a permutation of length 𝑚†.

Define the *value* of the 𝑖-th column in 𝑀 as $𝑣𝑖=MEX(𝑀_{1,𝑖},𝑀_{2,𝑖},…,𝑀_{𝑛,𝑖})$‡. Since Daniel likes diversity, the *beauty* of 𝑀 is $𝑠=MEX(𝑣_1,𝑣_2,⋯,𝑣_𝑚)$.

You have to help Daniel fill in the matrix 𝑀 and **maximize** its beauty.

†† A permutation of length 𝑚 is an array consisting of 𝑚 distinct integers from 00 to 𝑚−1 in arbitrary order. For example, \[1,2,0,4,3] is a permutation, but \[0,1,1] is not a permutation (1 appears twice in the array), and \[0,1,3] is also not a permutation (𝑚−1=2 but there is 3 in the array).

‡‡ The MEXMEX of an array is the smallest non-negative integer that does not belong to the array. For example, MEX(2,2,1)=0 because 0 does not belong to the array, and MEX(0,3,1,2)=4 because 0, 1, 2 and 3 appear in the array, but 4 does not.

**Input**

The first line of input contains a single integer 𝑡 (1≤𝑡≤1000) — the number of test cases. The description of test cases follows.

The only line of each test case contains two integers 𝑛 and 𝑚 (1≤𝑛,𝑚≤2⋅10^5^) — the size of the matrix.

It is guaranteed that the sum of 𝑛⋅𝑚 over all test cases does not exceed 2⋅10^5^.

**Output**

For each test case, in the first line output a single integer — the maximum beauty of 𝑀.

Then output the matrix 𝑀 of size 𝑛×𝑚 — the matrix you find.

If there are multiple solutions, you may output any of them.

Example

input

Copy

```
4
4 3
1 16
6 6
2 1
```

output

Copy

```
3
1 0 2
0 2 1
1 0 2
0 2 1
2
14 7 15 4 10 0 8 6 1 2 3 5 9 11 12 13 
6
3 0 1 4 2 5 
5 2 1 0 4 3 
1 3 2 4 5 0 
4 1 3 2 5 0 
4 2 5 3 0 1 
2 4 0 5 1 3
0
0
0
```

Note

In the first test case:

- 𝑣1=MEX(1,0,1,0)=2;
- 𝑣2=MEX(0,2,0,2)=1;
- 𝑣3=MEX(2,1,2,1)=0.

Therefore, 𝑠=MEX(2,1,0)=3.

It can be shown that 33 is the maximum possible beauty of 𝑀.

In the second test case, any permutation will make 𝑠=2.

In the third test case:

- 𝑣1=MEX(3,5,1,4,4,2)=0;
- 𝑣2=MEX(0,2,3,1,2,4)=5;
- 𝑣3=MEX(1,1,2,3,5,0)=4;
- 𝑣4=MEX(4,0,4,2,3,5)=1;
- 𝑣5=MEX(2,4,5,5,0,1)=3;
- 𝑣6=MEX(5,3,0,0,1,3)=2.

Therefore, 𝑠=MEX(0,5,4,1,3,2)=6.



## Matrices

### range中使用min、max



#### 02659:Bomb Game

matrices, http://cs101.openjudge.cn/practice/02659/

Bosko and Susko are playing an interesting game on a board made of rectangular fields arranged in A rows and B columns.

When the game starts, Susko puts its virtual pillbox in one field one the board. Then Bosko selects fields on which he will throw his virtual bombs. After each bomb, Susko will tell Bosko whether his pillbox is in the range of this bomb or not.

The range of a bomb with diameter P (P is always odd), which is thrown in field (R, S), is a square area. The center of the square is in the field (R, S), and the side of the square is parallel to the sides of the board and with length P.

After some bombs have been thrown, Bosko should find out the position of Susko's pillbox. However, the position may be not unique, and your job is to help Bosko to calculate the number of possible positions.

输入

First line of input contains three integers: A, B and K, 1 <= A, B, K <=100. A represents the number of rows, B the number of columns and K the number of thrown bombs.

Each of the next K lines contains integers R, S, P and T, describing a bomb thrown in the field at R-th row and S-th column with diameter P, 1 <= R <= A, 1 <= S <= B, 1 <= P <= 99, P is odd. If the pillbox is in the range of this bomb, T equals to 1; otherwise it is 0.

输出

Output the number of possible fields, which Susko's pillbox may stay in.

样例输入

```
5 5 3
3 3 3 1
3 4 1 0
3 4 3 1
```

样例输出

```
5
```

来源

Croatia OI 2002 National – Juniors





```python
def max_count(matrix):
    maximum = max(max(row) for row in matrix)
    count = sum(row.count(maximum) for row in matrix)
    return count

def calculate_possible_positions(A, B, K, bombs):
    positions = [[0] * B for _ in range(A)]

    for (R, S, P, T) in bombs:
        for i in range(max(0, R - (P - 1) // 2), min(A, R + (P + 1) // 2)):
            for j in range(max(0, S - (P - 1) // 2), min(B, S + (P + 1) // 2)):
                if T == 1 :
                    positions[i][j] += 1
    
                elif T == 0:
                    positions[i][j] -= 1

    #for row in positions:
    #    print(row)
    return max_count(positions)

A, B, K = map(int, input().split())
bombs = []
for _ in range(K):
    R, S, P, T = map(int, input().split())
    bombs.append((R - 1, S - 1, P, T))

result = calculate_possible_positions(A, B, K, bombs)
print(result)
```



#### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

  2018年俄罗斯世界杯（2018 FIFA World Cup）开踢啦！为了方便球迷观看比赛，莫斯科街道上很多路口都放置了的直播大屏幕，但是人群散去后总会在这些路口留下一堆垃圾。为此俄罗斯政府决定动用一种最新发明——“垃圾炸弹”。这种“炸弹”利用最先进的量子物理技术，爆炸后产生的冲击波可以完全清除波及范围内的所有垃圾，并且不会产生任何其他不良影响。炸弹爆炸后冲击波是以正方形方式扩散的，炸弹威力（扩散距离）以d给出，表示可以传播d条街道。

  例如下图是一个d=1的“垃圾炸弹”爆炸后的波及范围。

![img](http://media.openjudge.cn/images/upload/1403230629.jpg)

  假设莫斯科的布局为严格的1025*1025的网格状，由于财政问题市政府只买得起一枚“垃圾炸弹”，希望你帮他们找到合适的投放地点，使得一次清除的垃圾总量最多（假设垃圾数量可以用一个非负整数表示，并且除设置大屏幕的路口以外的地点没有垃圾）。

输入

第一行给出“炸弹”威力d(1 <= d <= 50)。第二行给出一个数组n(1 <= n <= 20)表示设置了大屏幕(有垃圾)的路口数目。接下来n行每行给出三个数字x, y, i, 分别代表路口的坐标(x, y)以及垃圾数量i. 点坐标(x, y)保证是有效的（区间在0到1024之间），同一坐标只会给出一次。

输出

输出能清理垃圾最多的投放点数目，以及能够清除的垃圾总量。

样例输入

```
1
2
4 4 10
6 6 20
```

样例输出

```
1 30
```





```python
#gpt
'''
过遍历方式计算出在每个点投掷炸弹能清理的垃圾数量，并用max_point存储垃圾数量的最大值，
res存储清理垃圾数量最大时的点的数量。最后输出结果。
是一个比较经典的滑动窗口问题
'''
d = int(input())
n = int(input())
square = [[0]*1025 for _ in range(1025)]
for _ in range(n):
    x, y, k = map(int, input().split())
    #for i in range(x-d if x-d >= 0 else 0, x+d+1 if x+d <= 1024 else 1025):
      #for j in range(y-d if y-d >= 0 else 0, y+d+1 if y+d <= 1024 else 1025):
    for i in range(max(x-d, 0), min(x+d+1, 1025)):
        for j in range(max(y-d, 0), min(y+d+1, 1025)):
          square[i][j] += k

res = max_point = 0
for i in range(0, 1025):
  for j in range(0, 1025):
    if square[i][j] > max_point:
      max_point = square[i][j]
      res = 1
    elif square[i][j] == max_point:
      res += 1
print(res, max_point)
```





### 保护圈

#### 12560: 生存游戏

matrices, http://cs101.openjudge.cn/practice/12560/

有如下生存游戏的规则：

给定一个n*m(1<=n,m<=100)的数组，每个元素代表一个细胞，其初始状态为活着(1)或死去(0)。

每个细胞会与其相邻的8个邻居（除数组边缘的细胞）进行交互，并遵守如下规则：

任何一个活着的细胞如果只有小于2个活着的邻居，那它就会由于人口稀少死去。

任何一个活着的细胞如果有2个或者3个活着的邻居，就可以继续活下去。

任何一个活着的细胞如果有超过3个活着的邻居，那它就会由于人口拥挤而死去。

任何一个死去的细胞如果有恰好3个活着的邻居，那它就会由于繁殖而重新变成活着的状态。



请写一个函数用来计算所给定初始状态的细胞经过一次更新后的状态是什么。

注意：所有细胞的状态必须同时更新，不能使用更新后的状态作为其他细胞的邻居状态来进行计算。

**输入**

第一行为n和m，而后n行，每行m个元素，用空格隔开。

**输出**

n行，每行m个元素，用空格隔开。

样例输入

```
3 4
0 0 1 1
1 1 0 0
1 1 0 1
```

样例输出

```
0 1 1 0
1 0 0 1
1 1 1 0
```

来源：cs10116 final exam



![image-20231017141049409](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017141049409.png)



加保护圈，八个邻居步长用dx,dy对表示。

```python
dx = [-1, -1, -1, 0, 1, 1,  1,  0]
dy = [-1,  0,  1, 1, 1, 0, -1, -1]

def check(board, y, x):
    c = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        c += board[ny][nx]
        
    if board[y][x] and (c<2 or c>3):
        return 0
    elif board[y][x]==0 and c==3:
        return 1
    
    return board[y][x]

n, m = map(int, input().split())

board=[]
board.append( [0 for x in range(m+2)] )
for _ in range(n):
    board.append([0] +[int(_) for _ in input().split()] + [0])
    
board.append( [0 for _ in range(m+2)] )
    
# in place solver
bn = [[0]*m for y in range(n)]
for i in range(n):
    for j in range(m):
        bn[i][j] = check(board, i+1, j+1)
        
for row in bn:
    print(*row)
```



#### 508A. Pasha and Pixels

brute force, 1100, http://codeforces.com/problemset/problem/508/A

Pasha loves his phone and also putting his hair up... But the hair is now irrelevant.

Pasha has installed a new game to his phone. The goal of the game is following. There is a rectangular field consisting of *n* row with *m* pixels in each row. Initially, all the pixels are colored white. In one move, Pasha can choose any pixel and color it black. In particular, he can choose the pixel that is already black, then after the boy's move the pixel does not change, that is, it remains black. Pasha loses the game when a 2 × 2 square consisting of black pixels is formed.

Pasha has made a plan of *k* moves, according to which he will paint pixels. Each turn in his plan is represented as a pair of numbers *i* and *j*, denoting respectively the row and the column of the pixel to be colored on the current move.

Determine whether Pasha loses if he acts in accordance with his plan, and if he does, on what move the 2 × 2 square consisting of black pixels is formed.

**Input**

The first line of the input contains three integers *n*, *m*, *k* (1 ≤ *n*, *m* ≤ 1000, 1 ≤ *k* ≤ 10^5^) — the number of rows, the number of columns and the number of moves that Pasha is going to perform.

The next *k* lines contain Pasha's moves in the order he makes them. Each line contains two integers *i* and *j* (1 ≤ *i* ≤ *n*, 1 ≤ *j* ≤ *m*), representing the row number and column number of the pixel that was painted during a move.

**Output**

If Pasha loses, print the number of the move when the 2 × 2 square consisting of black pixels is formed.

If Pasha doesn't lose, that is, no 2 × 2 square consisting of black pixels is formed during the given *k* moves, print 0.

Examples

input

```
2 2 4
1 1
1 2
2 1
2 2
```

output

```
4
```

input

```
2 3 6
2 3
2 2
1 3
2 2
1 2
1 1
```

output

```
5
```

input

```
5 3 7
2 3
1 2
1 1
4 1
3 1
5 3
3 2
```

output

```
0
```



![image-20231017141240860](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017141240860.png)



练习加保护圈

```python
# http://codeforces.com/contest/508/submission/44603553
n,m,k = map(int, input().split())
mx = [(m+2)*[0] for i in range(n+2)]

# if square 2 × 2 formed from black cells appears, and 
# cell (i, j) will upper-left, upper-right, bottom-left 
# or bottom-right of this squares.

def square_check(i,j):
    if mx[i][j+1] and mx[i+1][j] and mx[i+1][j+1]:
        return True
    if mx[i][j-1] and mx[i+1][j-1] and mx[i+1][j]:
        return True
    if mx[i-1][j] and mx[i-1][j+1] and mx[i][j+1]:
        return True
    if mx[i-1][j-1] and mx[i-1][j] and mx[i][j-1]:
        return True
    return False

for i in range(k):
    x,y = map(int, input().split())
    mx[x][y] = 1
    if square_check(x,y):
        print(i+1)
        break
else:
    print(0)
```





## DP的影子

![image-20231017140455207](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017140455207.png)



“Programming” 指的是一种表格法，不是写计算机程序

•Dp应用于自问题重叠的情况，即不同的子问题具有公共的子问题

•Dp对每个子问题只求解一次，并将其解保存在一个表格中，从而无需每次求解一个子问题时都重新计算



•最优化问题（optimization problems）可以有很多可行解，每个解都有一个值，希望寻找具有最优值（最小值或最大值）的解。

•称这样的解为问题的一个最优解（an optimal solution），而不是最优解（the optimal solution），因为可能有多个解都达到最优值



•四个步骤来设计一个dp算法：

•刻画一个最优解的结构特征

•递推地定义最优解的值

•计算最优的值，通常采用自底向上的方法

•利用计算出的信息结构构造一个最优解

![image-20231017140722761](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017140722761.png)



![image-20231017140820148](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017140820148.png)



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



## Data Structure

三个常用的数据结构：stack, queue, heap



### Stack in Python

https://www.geeksforgeeks.org/stack-in-python/

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017141624213.png" alt="image-20231017141624213" style="zoom: 50%;" />



### Queue in Python

https://www.geeksforgeeks.org/queue-in-python/

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017141756212.png" alt="image-20231017141756212" style="zoom:50%;" />



### Heap queue (or heapq) in Python

https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231017141926463.png" alt="image-20231017141926463" style="zoom:50%;" />



# 1024-Week7 贪心和DP 

2023年10月份，主要是掌握矩阵、贪心题目，下旬涉及到简单的DP题目。



目录：



## Greedy 

### Greedy Algorithms

https://www.geeksforgeeks.org/greedy-algorithms/

### What is Greedy Algorithm?

> Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. So the problems where choosing locally optimal also leads to global solution are the best fit for Greedy.

For example consider the [Fractional Knapsack Problem](https://www.geeksforgeeks.org/fractional-knapsack-problem/). The local optimal strategy is to choose the item that has maximum value vs weight ratio. This strategy also leads to a globally optimal solution because we are allowed to take fractions of an item.

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/Fractional-Knapsackexample-min-1024x512.png" alt="greedy-algorithms" style="zoom:75%;" />



**Topics:**

| Introduction                        | Approximate Greedy Algorithms for NP Complete Problems |
| ----------------------------------- | ------------------------------------------------------ |
| Standard Greedy Algorithms          | Greedy for Special Cases of DP                         |
| Greedy Problems on Array            | Some Practice problems on Greedy                       |
| Greedy Problems on Operating System | Quick Links                                            |
| Greedy Problems on Graph            |                                                        |



### Standard Greedy Algorithms:

Activity Selection Problem
Job Sequencing Problem
Huffman Coding

...



CF545C: Woodcutters, dp/greedy, 1500 

https://codeforces.com/problemset/problem/545/C

04144: 畜栏保留问题

greedy, http://cs101.openjudge.cn/practice/04144/

26646: 建筑修建

greedy, http://cs101.openjudge.cn/practice/26646/

2000012515 熊江凯 元培学院，推荐题目



![image-20231024140437960](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231024140437960.png)





### Greedy for Special Cases of DP

Fractional Knapsack Problem
Minimum number of coins required



#### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110

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



26646: 建筑修建

greedy, http://cs101.openjudge.cn/practice/26646/

2000012515 熊江凯 元培学院，推荐题目



#### Minimum number of coins required

《Python数据结构与算法分析》（第2版），5.12. Dynamic Programming 


https://runestone.academy/runestone/books/published/cppds/Recursion/DynamicProgramming.html

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231024133816344.png" alt="image-20231024133816344" style="zoom:50%;" />



### Greedy Problems on Graph

Kruskal’s Minimum Spanning Tree
Prim’s Minimum Spanning Tree
Boruvka’s Minimum Spanning Tree
Dijkastra’s Shortest Path Algorithm

...



#### Kruskal’s Minimum Spanning Tree (MST) Algorithm

https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/



![image-20231019162115981](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231019162115981.png)



> 空间上可以优化，申请一个矩阵就可以。俩矩阵相乘，输入对应的三元组，可以直接相乘。因为 矩阵C的每个元素都由A的对应行中的元素与B的对应列中的元素一一相乘并求和得到，即$C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + …… +A[i][n-1]*B[n-1][j] $。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231024135214262.png" alt="image-20231024135214262" style="zoom:50%;" />



A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected, undirected graph is a spanning tree with a weight less than or equal to the weight of every other spanning tree. 

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231024134259716.png" alt="image-20231024134259716" style="zoom: 50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/2560px-Minimum_spanning_tree.svg.png" alt="undefined" style="zoom: 33%;" />



##### Introduction to Kruskal’s Algorithm:

Here we will discuss **Kruskal’s algorithm** to find the MST of a given weighted graph. 

In Kruskal’s algorithm, sort all edges of the given graph in increasing order. Then it keeps on adding new edges and nodes in the MST if the newly added edge does not form a cycle. It picks the minimum weighted edge at first and the maximum weighted edge at last. Thus we can say that it makes a locally optimal choice in each step in order to find the optimal solution. Hence this is a Greedy Algorithm.

##### How to find MST using Kruskal’s algorithm?

Below are the steps for finding MST using Kruskal’s algorithm:

1. Sort all the edges in non-decreasing order of their weight. 
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If the cycle is not formed, include this edge. Else, discard it. 
3. Repeat step#2 until there are (V-1) edges in the spanning tree.

> **Step 2** uses the [Union-Find algorithm](https://www.geeksforgeeks.org/union-find/) to detect cycles. 
>
> So we recommend reading the following post as a prerequisite. 
>
> - [Union-Find Algorithm | Set 1 (Detect Cycle in a Graph)](https://www.geeksforgeeks.org/union-find/) 
> - [Union-Find Algorithm | Set 2 (Union By Rank and Path Compression)](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/)

> Introduction to Disjoint Set (Union-Find Algorithm)
>
> https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
>
> Check "Data Structure" part.



Kruskal’s algorithm to find the minimum cost spanning tree uses the greedy approach. The Greedy Choice is to pick the smallest weight edge that does not cause a cycle in the MST constructed so far. Let us understand it with an example:

##### Illustration:

Below is the illustration of the above approach:

> ![Kruskal’s Minimum Spanning Tree Algorithm](https://raw.githubusercontent.com/GMyhf/img/main/img/UntitledDiagram92.png)
>
> 
>
> 
>
> *The graph contains 9 vertices and 14 edges. So, the minimum spanning tree formed will be having (9 – 1) = 8 edges.* 
> *After sorting:*
>
> | Weight | Source | Destination |
> | ------ | ------ | ----------- |
> | 1      | 7      | 6           |
> | 2      | 8      | 2           |
> | 2      | 6      | 5           |
> | 4      | 0      | 1           |
> | 4      | 2      | 5           |
> | 6      | 8      | 6           |
> | 7      | 2      | 3           |
> | 7      | 7      | 8           |
> | 8      | 0      | 7           |
> | 8      | 1      | 2           |
> | 9      | 3      | 4           |
> | 10     | 5      | 4           |
> | 11     | 1      | 7           |
> | 14     | 3      | 5           |
>
> Now pick all edges one by one from the sorted list of edges 
>
> **Step 1:** Pick edge 7-6. No cycle is formed, include it. 
>
> ![Add edge 7-6 in the MST](https://raw.githubusercontent.com/GMyhf/img/main/img/img1drawio.png)
>
> ​				*Add edge 7-6 in the MST*
>
> **Step 2:** Pick edge 8-2. *No cycle is formed, include it.* 
>
> ![Add edge 8-2 in the MST](https://raw.githubusercontent.com/GMyhf/img/main/img/img2drawio.png)
>
> ​				*Add edge 8-2 in the MST*
>
> **Step 3:** Pick edge 6-5. No cycle is formed, include it. 
>
> ![Add edge 6-5 in the MST](https://raw.githubusercontent.com/GMyhf/img/main/img/img3drawio.png)
>
> ​				Add edge 6-5 in the MST
>
> **Step 4: **Pick edge 0-1. No cycle is formed, include it.
>
> ![Add edge 0-1 in the MST](https://raw.githubusercontent.com/GMyhf/img/main/img/img4drawio.png)
>
> ​		Add edge 0-1 in the MST
>
> **Step 5:**Pick edge 2-5. No cycle is formed, include it.
>
> ![Add edge 0-1 in the MST](https://raw.githubusercontent.com/GMyhf/img/main/img/img5drawio.png)
>
> ​		Add edge 2-5 in the MST
>
> **Step 6:** Pick edge 8-6. Since including this edge results in the cycle, discard it. Pick edge 2-3: No cycle is formed, include it.
>
> ![Add edge 2-3 in the MST](https://raw.githubusercontent.com/GMyhf/img/main/img/img6drawio.png)
>
> ​		Add edge 2-3 in the MST
>
> **Step 7:** **Pick edge 7-8.** Since including this edge results in the cycle, discard it. Pick edge 0-7. No cycle is formed, include it.
>
> ![Add edge 0-7 in MST](https://raw.githubusercontent.com/GMyhf/img/main/img/img7drawio.png)
>
> Add edge 0-7 in MST
>
> ***\*Step 8:\**** **Pick edge 1-2.** Since including this edge results in the cycle, discard it. **Pick edge 3-4.** No cycle is formed, include it.
>
> ![Add edge 3-4 in the MST](https://raw.githubusercontent.com/GMyhf/img/main/img/img8drawio.png)
>
> dd edge 3-4 in the MST
>
> ***\*Note:\**** Since the number of edges included in the MST equals to (V – 1), so the algorithm stops here

```python
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph 


# Class to represent a graph 
class Graph: 

	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [] 

	# Function to add an edge to graph 
	def addEdge(self, u, v, w): 
		self.graph.append([u, v, w]) 

	# A utility function to find set of an element i 
	# (truly uses path compression technique) 
	def find(self, parent, i): 
		if parent[i] != i: 

			# Reassignment of node's parent 
			# to root node as 
			# path compression requires 
			parent[i] = self.find(parent, parent[i]) 
		return parent[i] 

	# A function that does union of two sets of x and y 
	# (uses union by rank) 
	def union(self, parent, rank, x, y): 

		# Attach smaller rank tree under root of 
		# high rank tree (Union by Rank) 
		if rank[x] < rank[y]: 
			parent[x] = y 
		elif rank[x] > rank[y]: 
			parent[y] = x 

		# If ranks are same, then make one as root 
		# and increment its rank by one 
		else: 
			parent[y] = x 
			rank[x] += 1

	# The main function to construct MST 
	# using Kruskal's algorithm 
	def KruskalMST(self): 

		# This will store the resultant MST 
		result = [] 

		# An index variable, used for sorted edges 
		i = 0

		# An index variable, used for result[] 
		e = 0

		# Sort all the edges in 
		# non-decreasing order of their 
		# weight 
		self.graph = sorted(self.graph, 
							key=lambda item: item[2]) 

		parent = [] 
		rank = [] 

		# Create V subsets with single elements 
		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 

		# Number of edges to be taken is less than to V-1 
		while e < self.V - 1: 

			# Pick the smallest edge and increment 
			# the index for next iteration 
			u, v, w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent, v) 

			# If including this edge doesn't 
			# cause cycle, then include it in result 
			# and increment the index of result 
			# for next edge 
			if x != y: 
				e = e + 1
				result.append([u, v, w]) 
				self.union(parent, rank, x, y) 
			# Else discard the edge 

		minimumCost = 0
		print("Edges in the constructed MST") 
		for u, v, weight in result: 
			minimumCost += weight 
			print("%d -- %d == %d" % (u, v, weight)) 
		print("Minimum Spanning Tree", minimumCost) 


# Driver code 
if __name__ == '__main__': 
	g = Graph(4) 
	g.addEdge(0, 1, 10) 
	g.addEdge(0, 2, 6) 
	g.addEdge(0, 3, 5) 
	g.addEdge(1, 3, 15) 
	g.addEdge(2, 3, 4) 

	# Function call 
	g.KruskalMST() 

# This code is contributed by Neelam Yadav 
# Improved by James Graça-Jones 

```

**Output**

```
Following are the edges in the constructed MST
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
Minimum Cost Spanning Tree: 19
```

**Time Complexity:** O(E * logE) or O(E * logV) 

- Sorting of edges takes O(E * logE) time. 
- After sorting, we iterate through all edges and apply the find-union algorithm. The find and union operations can take at most O(logV) time.
- So overall complexity is O(E * logE + E * logV) time. 
- The value of E can be at most O(V2), so O(logV) and O(logE) are the same. Therefore, the overall time complexity is O(E * logE) or O(E*logV)

**Auxiliary Space:** O(V + E), where V is the number of vertices and E is the number of edges in the graph.

This article is compiled by Aashish Barnwal and reviewed by the GeeksforGeeks team. Please write comments if you find anything incorrect, or if you want to share more information about the topic discussed above.











## Matrices: 

Todo 螺旋矩阵。先来看 constructive algorithms

​	

### CF1868A. Fill in the Matrix

constructive algorithms, implementation, https://codeforces.com/problemset/problem/1868/A



https://codeforces.com/blog/entry/116642

**Hint 1**

What is the upper bound of 𝑠 according to 𝑛 and 𝑚? Can you construct such a matrix that reaches the upper bound?

**Hint 2**

If not, can you construct a matrix which maximizes$ ∑𝑚^m_{i=1}=𝑣_𝑖$? This is of some help to get the solution.

**Solution**

On one hand, the matrix 𝑀 has 𝑛 rows, so the maxmium 𝑣𝑖does not exceed $MEX(0,1,⋯,𝑛−1)=𝑛$, and 𝑠 does not exceed 𝑛+1.

On the other hand, the matrix 𝑀 has 𝑚 columns, and there are only 𝑚 numbers in the array 𝑣, so 𝑠 must not exceed 𝑚.

Therefore, the upper bound of 𝑠 is $min(𝑛+1,𝑚)$.

How can we reach the upper bound?

If 𝑚=1, then the only possible 
$$
𝑀=
\left(
\matrix{
  0 \\
  0 \\
  \vdots \\
  0 
}
\right)
$$
 in this case, 𝑣1=1, so 𝑠 must be 0, which unfortunately cannot reach the upper bound. ~~Sadly, many participants failed on pretest 2 because of it.~~ I've added this test to examples:)

If 𝑚>1, let's construct the 𝑀 in two cases:

- **Case 1. 𝑚≥𝑛+1.**

  In this case, we can construct 𝑀 like following:


  $$
  𝑀=
  \left(
  \matrix{
    0 & 1 & ... & m-2 & m-1\\
    1 & 2 & ... & m-1 & 0\\
    2 & 3 & ... & 0 & 1\\
    \vdots & \vdots & \ddots & \vdots & \vdots\\
    n-1 & n & ... & n-3 & n-2 
  }
  \right)
  $$


  More formally, $𝑀_{𝑖,𝑗}=(𝑖+𝑗−1) \; mod \; 𝑚$.

  Note that in this case 𝑛−1<𝑚−1, so we have $𝑣_1=𝑛, 𝑣_2=𝑣_3=⋯=𝑣_{𝑚−𝑛−1}=0, 𝑣_{𝑚−𝑛}=1,𝑣_{𝑚−𝑛+1}=2,⋯,𝑣_𝑚=𝑛−1$. Then 𝑠=𝑛+1, which reaches the upper bound.

- **Case 2. 𝑚<𝑛+1.**

  In this case, we can construct 𝑀 like following:
  $$
  𝑀=
  \left(
  \matrix{
    0 & 1 & ... & m-2 & m-1\\
    1 & 2 & ... & m-1 & 0\\
    2 & 3 & ... & 0 & 1\\
    \vdots & \vdots & \ddots & \vdots & \vdots\\
    m-2 & m-1 & ... & m-4 & m-3\\
    0 & 1 & ... & m-2 & m-1\\
    0 & 1 & ... & m-2 & m-1\\
    \vdots & \vdots & \ddots & \vdots & \vdots\\
    0 & 1 & ... & m-2 & m-1
  }
  \right)
  $$

  


  More formally, for $1≤𝑗≤𝑚−1, 𝑀_{𝑖,𝑗}=(𝑖+𝑗−1) \; mod \; 𝑚, for 𝑚≤𝑗≤𝑛, 𝑀_{𝑖,𝑗}=(𝑗−1) \; mod \; 𝑚$.

  Note that 𝑚>1, and 𝑚−2≥0. Similarly to case 1 we can get $𝑠=𝑚$, which also reaches the upper bound.

Time Complexity:  O(𝑛⋅𝑚) per test case.

**Implementation**

```c++
#include <bits/stdc++.h>
#define all(s) s.begin(), s.end()
using namespace std;
using ll = long long;
using ull = unsigned long long;

const int _N = 1e5 + 5;

int T;

void solve() {
	int n, m;
	cin >> n >> m;
	if (m == 1) cout << 0 << '\n';
	else if (n > m - 1) cout << m << '\n';
	else cout << n + 1 << '\n';
	for (int i = 0; i < min(m - 1, n); i++) {
		for (int j = 0; j < m; j++) {
			cout << (j + i) % m << ' ';
		}
		cout << '\n';
	}
	if (n > m - 1) {
		for (int i = m - 1; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cout << j << ' ';
			}
			cout << '\n';
		}
	}
	return;
}

int main() {
	ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
	cin >> T;
	while (T--) {
		solve();
	}
}
```





## **Dynamic Programming**

### What is Dynamic Programming?

![image-20231024142227555](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231024142227555.png)



Recursion is an effective problem-solving technique. The key points to remember are as follows:

•All recursive algorithms must have a base case.

•A recursive algorithm must change its state and make progress toward the base case.

•A recursive algorithm must call itself (recursively).

•Recursion can take the place of iteration in some cases.

•Recursive algorithms often map very naturally to a formal expression of the problem you are trying to solve.

•Recursion is not always the answer. 

•Sometimes a recursive solution may be more computationally expensive than an dynamic programming algorithm.

​	



### OEIS



![image-20231019100416961](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231019100416961.png)



How to use OESIS (On-line Encyclopedia of Integer Sequences)

https://www.geeksforgeeks.org/how-to-use-oesis/

Last Updated : 10 Feb, 2018



We sometimes land up in a situation when various coding problems can be simplified to a mathematical formula but often finding that formula isn’t that straightforward .Here comes, OESIS for rescue. We can calculate the terms for initial indices i.e n=0,1,2,3,…….. and then may use OEIS to find the mathematical expression.

This article focuses on using [OEIS](https://oeis.org/) (On-line Encyclopedia of Integer Sequences) to solve many complex problems easily by formulating them in some sort of mathematical expression. OEIS is a massive encyclopedia where we can look for various sequences and find their mathematical expression,examples and related facts about them .

Lets try to understand using an example: You are given n balls and are supposed to make equilateral triangle as shown in the image below.Each subsequent pattern should add a new row  to the triangle.

![OESIS_GeeksforGeeks](https://raw.githubusercontent.com/GMyhf/img/main/img/TriangularNumber_.png)



Now if we see the sequence of dots being added to form triangle,

The first few numbers are `1, 3, 6, 10, 15`…

This problem is known as **triangular number** which counts the objects that can form an equilateral triangle,. The *n*th triangular number is the number of dots composing a triangle with *n* dots on a side, and is equal to the sum of the *n* natural numbers from 1 to *n*. The sequence of triangular numbers starting at the 0th triangular number, is:

0, 1, 3, 6, 10, 15 ….

Now we have got the sequence and if we search it on [OEIS](https://oeis.org/search?q=1%2C%2C3%2C6%2C10&sort=&language=&go=Search) ,we get the following result:

![o](https://raw.githubusercontent.com/GMyhf/img/main/img/TriangularNumber_1.png)
OESIS proves extremely helpful in finding the algorithm to solve the problem.OEIS records information on integer sequences of interest to both professional [mathematicians](https://en.wikipedia.org/wiki/Mathematician) and [amateurs](https://en.wikipedia.org/wiki/Recreational_mathematics), and is widely cited. As of 22 August 2015 it contains over 260,000 sequences, making it the largest database of its kind.

This article is contributed by **Siddharth Lalwani.** If you like GeeksforGeeks and would like to contribute, you can also write an article and mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above







## Data Structure

三个常用的数据结构：stack, queue, heap, disjoint set



### Introduction to Disjoint Set (Union-Find Algorithm)

https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/

#### What is a Disjoint set data structure?

> Two sets are called **disjoint sets** if they don’t have any element in common, the intersection of sets is a null set.

A data structure that stores non overlapping or disjoint subset of elements is called disjoint set data structure. The disjoint set data structure supports following operations:

- Adding new sets to the disjoint set.
- Merging disjoint sets to a single disjoint set using **Union** operation.
- Finding representative of a disjoint set using **Find** operation.
- Check if two sets are disjoint or not. 

Consider a situation with a number of persons and the following tasks to be performed on them:

- Add a **new friendship relation**, i.e. a person x becomes the friend of another person y i.e adding new element to a set.
- Find whether individual **x is a friend of individual y** (direct or indirect friend)

**Examples:** 

> We are given 10 individuals say, a, b, c, d, e, f, g, h, i, j
>
> Following are relationships to be added:
> a <-> b  
> b <-> d
> c <-> f
> c <-> i
> j <-> e
> g <-> j
>
> Given queries like whether a is a friend of d or not. We basically need to create following 4 groups and maintain a quickly accessible connection among group items:
> G1 = {a, b, d}
> G2 = {c, f, i}
> G3 = {e, g, j}
> G4 = {h}



**Find whether x and y belong to the same group or not, i.e. to find if x and y are direct/indirect friends.**

Partitioning the individuals into different sets according to the groups in which they fall. This method is known as a **Disjoint set Union** which maintains a collection of **Disjoint sets** and each set is represented by one of its members.

**To answer the above question two key points to be considered are:**

- **How to Resolve sets?** Initially, all elements belong to different sets. After working on the given relations, we select a member as a **representative**. There can be many ways to select a representative, a simple one is to select with the biggest index.
- **Check if 2 persons are in the same group?** If representatives of two individuals are the same, then they’ll become friends.



**Data Structures used are:** 

**Array:** An array of integers is called **Parent[]**. If we are dealing with **N** items, i’th element of the array represents the i’th item. More precisely, the i’th element of the Parent[] array is the parent of the i’th item. These relationships create one or more virtual trees.

**Tree:** It is a **Disjoint set**. If two elements are in the same tree, then they are in the same **Disjoint set**. The root node (or the topmost node) of each tree is called the **representative** of the set. There is always a single **unique representative** of each set. A simple rule to identify a representative is if ‘i’ is the representative of a set, then **Parent[i] = i**. If i is not the representative of his set, then it can be found by traveling up the tree until we find the representative.



#### **Operations on Disjoint Set Data Structures:**

1. Find
2. Union

##### **1. Find:**

Can be implemented by recursively traversing the parent array until we hit a node that is the parent of itself.



```python
# Finds the representative of the set
# that i is an element of

def find(i):

	# If i is the parent of itself
	if (parent[i] == i):

		# Then i is the representative of
		# this set
		return i
	else:

		# Else if i is not the parent of
		# itself, then i is not the
		# representative of his set. So we
		# recursively call Find on its parent
		return find(parent[i])

# The code is contributed by Nidhi goel

```



**Time complexity**: This approach is inefficient and can take O(n) time in worst case.



##### **2. Union:** 

It takes **two elements** as input and finds the representatives of their sets using the **Find** operation, and finally puts either one of the trees (representing the set) under the root node of the other tree.

```python
# Unites the set that includes i
# and the set that includes j

def union(parent, rank, i, j):
	# Find the representatives
	# (or the root nodes) for the set
	# that includes i
	irep = find(parent, i)
	
	# And do the same for the set
	# that includes j
	jrep = find(parent, j)
	
	# Make the parent of i’s representative
	# be j’s representative effectively
	# moving all of i’s set into j’s set)
	
	parent[irep] = jrep

```



**Optimizations (Union by Rank/Size and Path Compression):**

The efficiency depends heavily on which tree get attached to the other***\*.\**** There are 2 ways in which it can be done. First is Union by Rank, which considers height of the tree as the factor and Second is Union by Size, which considers size of the tree as the factor while attaching one tree to the other . This method along with Path Compression gives complexity of nearly constant time.



**[Path Compression](https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/) (Modifications to Find()):**

It speeds up the data structure by **compressing the height** of the trees. It can be achieved by inserting a small caching mechanism into the **Find** operation. Take a look at the code for more details:

```python
# Finds the representative of the set that i
# is an element of.


def find(i):

	# If i is the parent of itself
	if Parent[i] == i:

		# Then i is the representative 
		return i
	else:

		# Recursively find the representative.
		result = find(Parent[i])

		# We cache the result by moving i’s node 
		# directly under the representative of this
		# set
		Parent[i] = result
	
		# And then we return the result
		return result

# The code is contributed by Arushi Jindal. 

```



**Time Complexity**: O(log n) on average per call.



#### **[Union by Rank](https://www.geeksforgeeks.org/union-by-rank-and-path-compression-in-union-find-algorithm/):**

First of all, we need a new array of integers called **rank[]**. The size of this array is the same as the parent array **Parent[]**. If i is a representative of a set, **rank[i]** is the height of the tree representing the set. 
Now recall that in the Union operation, it doesn’t matter which of the two trees is moved under the other. Now what we want to do is minimize the height of the resulting tree. If we are uniting two trees (or sets), let’s call them left and right, then it all depends on the **rank of left** and the **rank of right**. 

- If the rank of **left** is less than the rank of **right**, then it’s best to move **left under right**, because that won’t change the rank of right (while moving right under left would increase the height). In the same way, if the rank of right is less than the rank of left, then we should move right under left.
- If the ranks are equal, it doesn’t matter which tree goes under the other, but the rank of the result will always be one greater than the rank of the trees.



```c++
// Unites the set that includes i and the set
// that includes j by rank

#include <bits/stdc++.h>
using namespace std;

void unionbyrank(int i, int j) {

	// Find the representatives (or the root nodes)
	// for the set that includes i
	int irep = this.find(i);

	// And do the same for the set that includes j
	int jrep = this.Find(j);

	// Elements are in same set, no need to
	// unite anything.
	if (irep == jrep)
		return;
	
	// Get the rank of i’s tree
	irank = Rank[irep],

	// Get the rank of j’s tree
	jrank = Rank[jrep];

	// If i’s rank is less than j’s rank
	if (irank < jrank) {

		// Then move i under j
		this.parent[irep] = jrep;
	}

	// Else if j’s rank is less than i’s rank
	else if (jrank < irank) {

		// Then move j under i
		this.Parent[jrep] = irep;
	}

	// Else if their ranks are the same
	else {

		// Then move i under j (doesn’t matter
		// which one goes where)
		this.Parent[irep] = jrep;

		// And increment the result tree’s
		// rank by 1
		Rank[jrep]++;
	}
}

```



#### **Union by Size:**

Again, we need a new array of integers called **size[]**. The size of this array is the same as the parent array **Parent[]**. If i is a representative of a set, **size[i]** is the number of the elements in the tree representing the set. 
Now we are uniting two trees (or sets), let’s call them left and right, then in this case it all depends on the **size of left** and the **size of right** tree (or set).

- If the size of **left** is less than the size of **right**, then it’s best to move **left under right** and increase size of right by size of left. In the same way, if the size of right is less than the size of left, then we should move right under left. and increase size of left by size of right.
- If the sizes are equal, it doesn’t matter which tree goes under the other.

```c++
// Unites the set that includes i and the set
// that includes j by size

#include <bits/stdc++.h>
using namespace std;

void unionbysize(int i, int j) {

	// Find the representatives (or the root nodes)
	// for the set that includes i
	int irep = this.find(i);

	// And do the same for the set that includes j
	int jrep = this.Find(j);

	// Elements are in same set, no need to
	// unite anything.
	if (irep == jrep)
		return;
	
	// Get the size of i’s tree
	isize = Size[irep],

	// Get the size of j’s tree
	jsize = Size[jrep];

	// If i’s size is less than j’s size
	if (isize < jsize) {

		// Then move i under j
		this.parent[irep] = jrep;
	
	// Increment j's size by i'size
		Size[jrep]+=Size[irep];
	}

	// Else if j’s rank is less than i’s rank
	else if (jsize < isize) {

		// Then move j under i
		this.Parent[jrep] = irep;
	
	// Increment i's size by j'size
		Size[irep]+=Size[jrep];
	}

	// Else if their ranks are the same
	else {

		// Then move i under j (doesn’t matter
		// which one goes where)
		this.Parent[irep] = jrep;

		// Increment j's size by i'size
		Size[jrep]+=Size[irep];
	}
}

```



**Time complexity**: O(log n) without Path Compression.



**Below is the complete implementation of disjoint set with path compression and union by rank.**

```python
# Python3 program to implement Disjoint Set Data
# Structure.

class DisjSet:
	def __init__(self, n):
		# Constructor to create and
		# initialize sets of n items
		self.rank = [1] * n
		self.parent = [i for i in range(n)]


	# Finds set of given item x
	def find(self, x):
		
		# Finds the representative of the set
		# that x is an element of
		if (self.parent[x] != x):
			
			# if x is not the parent of itself
			# Then x is not the representative of
			# its set,
			self.parent[x] = self.find(self.parent[x])
			
			# so we recursively call Find on its parent
			# and move i's node directly under the
			# representative of this set

		return self.parent[x]


	# Do union of two sets represented
	# by x and y.
	def Union(self, x, y):
		
		# Find current sets of x and y
		xset = self.find(x)
		yset = self.find(y)

		# If they are already in same set
		if xset == yset:
			return

		# Put smaller ranked item under
		# bigger ranked item if ranks are
		# different
		if self.rank[xset] < self.rank[yset]:
			self.parent[xset] = yset

		elif self.rank[xset] > self.rank[yset]:
			self.parent[yset] = xset

		# If ranks are same, then move y under
		# x (doesn't matter which one goes where)
		# and increment rank of x's tree
		else:
			self.parent[yset] = xset
			self.rank[xset] = self.rank[xset] + 1

# Driver code
obj = DisjSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)
if obj.find(4) == obj.find(0):
	print('Yes')
else:
	print('No')
if obj.find(1) == obj.find(0):
	print('Yes')
else:
	print('No')

# This code is contributed by ng24_7.

```



**Time complexity**: O(n) for creating n single item sets . The two techniques -path compression with the union by rank/size, the time complexity will reach nearly constant time. It turns out, that the final[ amortized time complexity](https://www.geeksforgeeks.org/introduction-to-amortized-analysis/) is O(α(n)), where α(n) is the inverse Ackermann function, which grows very steadily (it does not even exceed for n<10600  approximately).

**Space complexity:** O(n) because we need to store n elements in the Disjoint Set Data Structure.



### 并查集例题

#### 01182: 食物链

并查集, http://cs101.openjudge.cn/practice/01182

动物王国中有三类动物A,B,C，这三类动物的食物链构成了有趣的环形。A吃B， B吃C，C吃A。
现有N个动物，以1－N编号。每个动物都是A,B,C中的一种，但是我们并不知道它到底是哪一种。
有人用两种说法对这N个动物所构成的食物链关系进行描述：
第一种说法是"1 X Y"，表示X和Y是同类。
第二种说法是"2 X Y"，表示X吃Y。
此人对N个动物，用上述两种说法，一句接一句地说出K句话，这K句话有的是真的，有的是假的。当一句话满足下列三条之一时，这句话就是假话，否则就是真话。
1） 当前的话与前面的某些真的话冲突，就是假话；
2） 当前的话中X或Y比N大，就是假话；
3） 当前的话表示X吃X，就是假话。
你的任务是根据给定的N（1 <= N <= 50,000）和K句话（0 <= K <= 100,000），输出假话的总数。

**输入**

第一行是两个整数N和K，以一个空格分隔。
以下K行每行是三个正整数 D，X，Y，两数之间用一个空格隔开，其中D表示说法的种类。
若D=1，则表示X和Y是同类。
若D=2，则表示X吃Y。

**输出**

只有一个整数，表示假话的数目。

样例输入

```
100 7
1 101 1 
2 1 2
2 2 3 
2 3 3 
1 1 3 
2 3 1 
1 5 5
```

样例输出

```
3
```

来源: Noi 01



## 语法相关

### 浅拷贝、深拷贝

![image-20231019142454622](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231019142454622.png)



![image-20231019145259031](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231019145259031.png)



![image-20231019142517681](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231019142517681.png)



![image-20231019142544202](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231019142544202.png)



These data structures are internally represented with index arrays, which label the data, and data arrays, which contain the actual data. Now, when we try to copy these data structures we essentially copy the object’s indices and data and there are two ways to do so, namely Shallow Copy and Deep Copy. 

When a shallow copy of a object is created, it doesn’t copy the indices and the data of the original object but it simply copies the references to its indices and data. As a result of which, a change made to one is reflected in the other one. 

It refers to constructing a new collection object and then populating it with references to the child objects found in the original. The copying process does not recurse and therefore won’t create copies of the child objects themselves. 

A deep copy of a object has its own copy of index and data. It is a process in which the copying process occurs recursively. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original. In the case of deep copy, a copy of an object is copied into another object. It means that any changes made to a copy of the object do not reflect in the original object. 



#### copy in Python (Deep Copy and Shallow Copy)

https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

In [Python](https://www.geeksforgeeks.org/python-programming-language/), Assignment statements do not copy objects, they create bindings between a target and an object. When we use the **=** operator, It only creates a new variable that shares the reference of the original object. In order to create “real copies” or “clones” of these objects, we can use the copy module in [Python](https://www.geeksforgeeks.org/python-programming-language/).

**Syntax of Deep copy**

> **Syntax:** copy.deepcopy(x)

**Syntax of Shallow copy**

> **Syntax:** copy.copy(x)

**Example:**

In order to make these copies, we use the copy module. The copy() returns a shallow copy of the list, and deepcopy() returns a deep copy of the list. As you can see that both have the same value but have different IDs.

```python
import copy

# initializing list 0
li0 = [1, 2, [3, 5], 4]
print("li0 ID: ", id(li0))

li1 = li0
print("li1 ID: ", id(li1))
print('assignment: ', id(li0) == id(li1), end=',')
print(id(li0[2]) == id(li1[2]))
print()

# using copy for shallow copy
li2 = copy.copy(li0)
print("li2 ID: ", id(li2))
print('shallow_copy: ', id(li0) == id(li2), end=',')
print(id(li0[2]) == id(li2[2]))
print()

# using deepcopy for deepcopy
li3 = copy.deepcopy(li0)
print("li3 ID: ", id(li3))
print('deep_copy ',id(li0) == id(li3), end=',')
print(id(li0[2]) == id(li3[2]))
'''
Important Points: The difference between shallow and deep copying is 
only relevant for compound objects (objects that contain other objects, 
like lists or class instances):

A shallow copy constructs a new compound object and then 
(to the extent possible) inserts references into it to the objects 
found in the original.
A deep copy constructs a new compound object and then, recursively, 
inserts copies into it of the objects found in the original.
'''
```



![image-20231019151529623](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231019151529623.png)



![image-20231019153308217](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231019153308217.png)





#### 需要先申请到内存空间，才能使用

指针是内存地址，类似门牌号，要找人得到具体物理位置，门牌号里面找不到。

例如：ma=[[0]\*(m+2)]*(n+2) 只是一个指针，还没有拿到空间。

在Python中，变量 `ma` 的赋值 `[[0]*(m+2)]*(n+2)` 只是创建了一个指向空间的引用，并没有实际申请到内存空间。

需要注意的是，这种方式创建二维列表时，内层列表的元素实际上是共享的，它们指向同一块内存空间。这意味着如果你修改了其中一个内层列表的元素，会影响到其他内层列表中对应位置的元素。

如果你想创建独立的内层列表，可以使用列表推导式来实现，例如：

```
ma = [[0] * (m + 2) for _ in range(n + 2)]
```

这样每个内层列表都会有自己独立的内存空间，避免了共享元素的问题。

![image-20231021105913274](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231021105913274.png)





## Python内置函数运行速度

python内置函数执行特别快，如sort, find，即使用同样方法实现，也没有直接调用函数快。是因为内置函数都是C语言实现编译成可执行文件库了？

是的，Python内置函数在执行速度上通常会比用纯Python代码实现的相同功能更快。这是因为很多内置函数（如`sort`、`find`等）实际上是用C语言实现的，并且在Python解释器中以编译成的可执行文件库的形式存在。相比于纯Python代码，C语言的执行速度更快，这是由于C语言的底层实现更加高效。因此，当使用内置函数时，Python解释器可以直接调用这些C语言实现的函数，从而获得更快的执行速度。

另外，Python解释器本身也会对一些常用的操作进行优化，比如将循环展开、使用位运算等技巧，以提高执行效率。这些优化也可以帮助内置函数获得更好的性能。

需要注意的是，并不是所有的内置函数都是用C语言实现的，有一些内置函数的实现可能是用Python编写的。但是，Python标准库中的绝大部分内置函数都是用C实现的，因此它们通常具有很高的执行速度。



### 26999:2023找出全部子串位置

string, naive, kmp algorithm, http://cs101.openjudge.cn/practice/26999/

输入两个串 txt, pat，找出 pat 在 txt 中所有出现的位置

例如'aa'在 aaaa 里出现的位置有0,1,2

**输入**

第一行是整数n
接下来有n行，每行两个不带空格的字符串 txt, pat。0 < len(pat) <= len(txt) < 2* 10^7

**输出**

对每行，从小到大输出 pat 在 txt 中所有的出现位置。位置从0开始算
如果 pat 没出现过，输出 "no"
行末多输出空格没关系

样例输入

```
4
ababcdefgabdefab ab
aaaaaaaaa a
aaaaaaaaa aaa 
112123323 a
```

样例输出

```
0 2 9 14 
0 1 2 3 4 5 6 7 8 
0 1 2 3 4 5 6 
no
```



```python
n = int(input())
for _ in range(n):
    s1, s2 = input().split()
    positions = []
    start = 0
    while True:
        pos = s1.find(s2, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    if positions:
        for pos in positions:
            print(pos, end=" ")
        print("")
    else:
        print("no")
```



Naive pattern algorithm, Time Limit Exceeded

```python
# https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
# Naive Pattern Searching algorithm
def search(pat, txt):
    M = len(pat)
    N = len(txt)

    res = []
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
    #i = 0
    #while i < N - M + 1:
        j = 0

        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):
                #i = i+j + 1
                break
            j += 1

        if (j == M):
            res.append(str(i))
            #i += M

    return res


n = int(input())
for _ in range(n):
    txt, pat = input().split()
    ans = search(pat, txt)
    if ans:
        print(' '.join(ans))
    else:
        print('no')
```





```python
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
# KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    
    res = []

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            #print("Found pattern at index " + str(i-j))
            cur = i - j
            res.append(str(cur))

            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    return res


# Function to compute LPS array
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix

    lps[0] = 0 # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


# Driver code
# if __name__ == '__main__':
#     txt = "ABABDABACDABABCABAB"
#     pat = "ABABCABAB"
#     KMPSearch(pat, txt)
# This code is contributed by Bhavya Jain
n = int(input())
for _ in range(n):
    txt, pat = input().split()
    ans = KMPSearch(pat, txt)
    if ans:
        print(' '.join(ans))
    else:
        print('no')
```



### 01742: Coins

dp, http://cs101.openjudge.cn/routine/01742/

People in Silverland use coins.They have coins of value A1,A2,A3...An Silverland dollar.One day Tony opened his money-box and found there were some coins.He decided to buy a very nice watch in a nearby shop. He wanted to pay the exact price(without change) and he known the price would not more than m.But he didn't know the exact price of the watch.
You are to write a program which reads n,m,A1,A2,A3...An and C1,C2,C3...Cn corresponding to the number of Tony's coins of value A1,A2,A3...An then calculate how many prices(form 1 to m) Tony can pay use these coins.

**输入**

The input contains several test cases. The first line of each test case contains two integers n(1<=n<=100),m(m<=100000).The second line contains 2n integers, denoting A1,A2,A3...An,C1,C2,C3...Cn (1<=Ai<=100000,1<=Ci<=1000). The last test case is followed by two zeros.

**输出**

For each test case output the answer on a single line.

样例输入

```
3 10
1 2 4 2 1 1
2 5
1 4 2 1
0 0
```

样例输出

```
8
4
```

来源

LouTiancheng@POJ



```python
# 23n2300010763，数院胡睿诚
'''
多重背包问题 (二进制优化)
多重背包问题通常可转化成01背包问题求解。但若将每种物品的数量拆分成多个1的话，时间复杂度会很高，
从而导致TLE。所以，需要利用二进制优化思想。即:一个正整数n，可以被分解成1,2,4,...,2^(k-1),
n-2^k+1的形式。其中，k是满足n-2^k+1>0的最大整数。
例如，假设给定价值为2，数量为10的物品，依据二进制优化思想可将10分解为1+2+4+3，则原来价值为2,
数量为10的物品可等效转化为价值分别为1*2，2*2，4*2，3*2，即价值分别为2，4，8，6，数量均为1的物品。

'''
import math


def sum_2(x):
    s = 0
    while x > 0:
        s += (x & 1)
        x = x >> 1
    return s


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    ls = list(map(int, input().split()))
    w = (1 << (m + 1)) - 1                  #e.g., m=10, w=2047
    result = 1
    for i in range(n):
        number = ls[i+n] + 1                # e.g., number = 10
        limit = int(math.log(number, 2))    # limit = 3
        rest = number - (1 << limit)        # rest = 3
        for j in range(limit):
            result = (result | (result << (ls[i] * (1 << j)))) & w
        if rest > 0:
            result = (result | (result << (ls[i] * rest))) & w
    #print(sum_2(result) - 1)
    print(bin(result).count('1') - 1)
```





### Assignment #7

作业包括 greedy+matrices 5个，及1个简单dp。作业有点难，最好每天至少完成1个。





# 1031-Week8 线段树和树状数组

通常11月份前两周是各科密集期中考试时间，我们计划讲点拓展知识，月考/作业相应降低难度，便于同学均衡各科学习时间。



**本周主要内容：**

理解时间复杂度 $O(1)$ 和 $O(n)$ 权衡处理方法，有的题目 $O(n^2)$ 算法超时，需要把时间复杂度降到$O(nLogn)$才能AC。

例如：27018:康托展开，http://cs101.openjudge.cn/practice/27018/

假如有一个数组 $arr[0 ... n-1]$，需要：1）计算前 i 个元素的和。2）修改数组 $arr[i] = x$ 中指定元素的值，其中$0 \leq i \leq n-1$。
一个**简单的解决方案**是运行一个从 0 到 i-1 的循环，并计算元素的和。要更新一个值，只需执行 $arr[i] = x$。前者操作需要 $O(n)$ 时间，后者需要 $O(1)$ 时间。另一个简单的解决方案是创建一个额外的数组，并将前第 i 个元素的和存储在这个新数组的第 i 个索引处。给定范围的求和现在可以在 O(1) 时间内计算，但是更新操作现在需要 $O(n)$ 时间。如果有大量的查询（读）操作，但很少的更新（写）操作，那么这种方法可以很好地工作。

是否可以在 $O(log n)$ 时间内同时执行查询和更新操作? 一个有效的解决方案是使用**线段树 (Segment Tree)** 分别在 $O(Logn)$ 时间内执行这两个操作的。另一种解决方案是**二叉索引树（Fenwick Tree/Binary Indexed Tree）**，它的两种操作时间复杂度也是 $O(Logn)$。与线段树相比，二叉索引树需要更少的空间，更容易实现。



组合数学是对于计数问题的研究，数论就是对于整除性问题的研究，组合与数论是程序中的常见考点。题目背景知识，数学思维。

因为整数除法具有分配律的性质，单项整除可以等价于各项求和最后整除。



## 康托展开Cantor Expansion

### 源起 01833: 排列

Math, http://cs101.openjudge.cn/practice/01833

大家知道，给出正整数n，则1到n这n个数可以构成n！种排列，把这些排列按照从小到大的顺序（字典顺序）列出，如 n=3 时，列出1 2 3，1 3 2，2 1 3，2 3 1，3 1 2，3 2 1六个排列。

任务描述：
给出某个排列，求出这个排列的下k个排列，如果遇到最后一个排列，则下1排列为第1个排列，即排列1 2 3…n。
比如：n = 3，k=2 给出排列2 3 1，则它的下1个排列为3 1 2，下2个排列为3 2 1，因此答案为3 2 1。

**输入**

第一行是一个正整数m，表示测试数据的个数，下面是m组测试数据，每组测试数据第一行是2个正整数n( 1 <= n < 1024 )和k(1<=k<=64)，第二行有n个正整数，是1，2 … n的一个排列。

**输出**

对于每组输入数据，输出一行，n个数，中间用空格隔开，表示输入排列的下k个排列。

样例输入

```
3
3 1
2 3 1
3 1
3 2 1
10 2	
1 2 3 4 5 6 7 8 9 10
```

样例输出

```
3 1 2
1 2 3
1 2 3 4 5 6 7 9 8 10
```

来源

qinlu@POJ



这三个题目是相同的，tags: two pointers

01833:排列

http://cs101.openjudge.cn/practice/01833/

02996:选课

http://cs101.openjudge.cn/practice/02996/

31.下一个排列

https://leetcode.cn/problems/next-permutation/



#### 思路一：字典序

Wikipedia has a nice [article](http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order) on lexicographical order generation. It also describes an algorithm to generate the next permutation.

Quoting:

The following algorithm generates the next permutation lexicographically after a given permutation. It changes the given permutation in-place.

1. Find the highest index i such that s[i] < s[i+1]. If no such index exists, the permutation is the last permutation.
2. Find the highest index j > i such that s[j] > s[i]. Such a j must exist, since i+1 is such an index.
3. Swap s[i] with s[j].
4. Reverse the order of all of the elements after index i till the last element.

即：

1）从后往前找第一组相邻的升序数对，记录左边的位置p。
2）从后往前找第一个比p位置的数大的数，将两个数交换。
3）把p位置后所有数字逆序。

举例：

1.从数列的右边向左寻找连续递增序列, 例如对于：1,3,5,4,2，其中5-4-2即为递增序列。

2.从上述序列中找一个比它前面的数（3）大的最小数（4），并将且交换这两个数。于是1,3,5,4,2->1,4,5,3,2，此时交换后的依然是递增序列。

3.新的递增序列逆序，即：1,4,5,3,2 => 1,4,2,3,5



```python
from typing import List


def nextPermutation(nums: List[int]) -> None:
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]
    
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# =============================================================================
# n = int(input())
# m = int(input())
# arr = list(map(int, input().split()))
# for k in range(m):
#     nextPermutation(arr)
# print(*arr)
# =============================================================================

m = int(input())
for _ in range(m):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(k):
        nextPermutation(a)

    print(*a)
```



#### 思路二：康托展开

```python
# 2022fall-cs101，陈勃宇
# cantor expansion

aa = [1]
c = 1
for i in range(1,1025):
    c = c * i
    aa.append(c)

for _ in range(int(input())):
    n,k = map(int,input().split())
    *cc, = map(int,input().split())
    *bb, = range(1,n + 1)
    
    d = 0
    l = n - 1
    for j in cc:
        d = d + bb.index(j) * aa[l]
        bb.remove(j)
        l -= 1
    
    d += k
    while d >= aa[n]:
        d -= aa[n]
        
    dd = []
    *bb, = range(1,n + 1)
    for p in range(n - 1,-1,-1):
        t = d // aa[p]
        dd.append(bb[t])
        del(bb[t])
        d -= t * aa[p]
    print(*dd)
```



程序中用到了remove，pop操作，gpt提醒是否用OrderedDict能优化。

```
# 计算阶乘
aa = [1]
for i in range(1, n+1):
    aa.append(aa[-1] * i)

# 初始化 bb 和 pos（bb中每个元素的位置）
pos = [0] * (n+1)
bb = list(OrderedDict.fromkeys(range(1, n+1)))
```





### 27018: 康托展开

http://cs101.openjudge.cn/practice/27018/

总时间限制: 3000ms 单个测试点时间限制: 2000ms 内存限制: 90112kB
描述
求 1∼N 的一个给定全排列在所有 1∼N 全排列中的排名。结果对 998244353取模。

**输入**
第一行一个正整数 N。

第二行 N 个正整数，表示 1∼N 的一种全排列。
**输出**
一行一个非负整数，表示答案对 998244353 取模的值。
样例输入

```
Sample1 in:
3
2 1 3

Sample1 output:
3
```

样例输出

```
Sample2 in:
4
1 2 4 3

Sample2 output:
2
```

提示: 对于100%数据，$1≤N≤1000000$。
来源: https://www.luogu.com.cn/problem/P5367



思路：容易想到的方法是把所有排列求出来后再进行排序，但事实上有更简单高效的算法来解决这个问题，那就是康托展开。

> **康托展开**是一个全排列到一个自然数的双射，常用于构建特定哈希表时的空间压缩。 康托展开的实质是计算当前排列在所有由小到大全排列中的次序编号，因此是可逆的。即由全排列可得到其次序编号（康托展开），由次序编号可以得到对应的第几个全排列（逆康托展开）。
>
> 康托展开的**表达式为**：
>
> $X＝a_n×(n-1)!＋a_{n-1}×(n-2)!＋…＋a_i×(i-1)!＋…＋a_2×1!＋a_1×0!$
>
> 其中：X 为比当前排列小的全排列个数（X+1即为当前排列的次序编号）；n 表示全排列表达式的字符串长度；$a_i$ 表示原排列表达式中的第 i 位（由右往左数），前面（其右侧） i-1 位数有多少个数的值比它小。


例如求 5 2 3 4 1 在 {1, 2, 3, 4, 5} 生成的排列中的次序可以按如下步骤计算。
从右往左数，i 是5时候，其右侧比5小的数有1、2、3、4这4个数，所以有4×4！。
是2，比2小的数有1一个数，所以有 1×3！。
是3，比3小的数有1一个数，为1×2！。
是4，比4小的数有1一个数，为1×1！。
最后一位数右侧没有比它小的数，为 0×0！＝0。
则 4×4！＋1×3！＋1×2！＋1×1！＝105。
这个 X 只是这个排列之前的排列数，而题目要求这个排列的位置，即 5 2 3 4 1排在第 106 位。

同理，4 3 5 2 1的排列数：3×4!＋2×3!＋2×2!＋1×1!＝89，即 4 3 5 2 1 排在第90位。
因为比4小的数有3个：3、2、1；比3小的数有2个：2、1；比5小的数有2个：2、1；比2小的数有1个：1。

参考代码如下。



```python
MOD = 998244353								# Time Limit Exceeded, 内存7140KB, 时间18924ms
fac = [1]

def cantor_expand(a, n):
    ans = 0
    
    for i in range(1, n + 1):
        count = 0
        for j in range(i + 1, n + 1):
            if a[j] < a[i]:
                count += 1				# 计算有几个比他小的数
        ans = (ans + (count * fac[n - i]) % MOD) % MOD
    return ans + 1

a = [0]
N = int(input())		# 用大写N，因为spyder的debug，执行下一条指令的命令是 n/next。与变量n冲突。

for i in range(1, N + 1):
    fac.append((fac[i - 1] * i) % MOD)		# 整数除法具有分配律

*perm, = map(int, input().split())
a.extend(perm)

print(cantor_expand(a, N))
```



用C++也是超时

```c++
#include<iostream>							// Time Limit Exceeded, 内存960KB, 时间1986ms
using namespace std;

const long long MOD = 998244353;
long long fac[1000005]={1};

int cantor_expand (int a[],int n){
    int i, j, count;
    long long ans = 0 ;

    for(i = 1; i <= n; i ++){
        count = 0;
        for(j = i + 1; j <= n; j ++){
            if(a[j] < a[i]) count ++;						// 计算有几个比它小的数
        }
        ans = (ans + (count * fac[n-i]) % MOD ) % MOD;
    }
    return ans + 1;
}


int a[1000005];

int main()
{
  int N;
  //cin >> N;
  scanf("%d", &N);
  for (int i=1; i<=N; i++){
      fac[i] = (fac[i-1]*i)%MOD;
  }

  for (int i=1; i<=N; i++)
      //cin >> a[i];
      scanf("%d",&a[i]);
  cout << cantor_expand(a,N) << endl;
  return 0;
}
```



### 树状数组或线段树来优化

康托展开用 $O(n^2)$ 算法超时，需要把时间复杂度降到$O(nLogn)$。“计算有几个比他小的数”，时间复杂度由 $O(n)$ 降到 $O(Logn)$。

#### 树状数组（Binary Indexed Tree）

实现树状数组的核心部分，包括了三个重要的操作：lowbit、修改和求和。

1. lowbit函数：`lowbit(x)` 是用来计算 `x` 的二进制表示中最低位的 `1` 所对应的值。它的运算规则是利用位运算 `(x & -x)` 来获取 `x` 的最低位 `1` 所对应的值。例如，`lowbit(6)` 的结果是 `2`，因为 `6` 的二进制表示为 `110`，最低位的 `1` 所对应的值是 `2`。

2. update函数：这个函数用于修改树状数组中某个位置的值。参数 `x` 表示要修改的位置，参数 `y` 表示要增加/减少的值。函数使用一个循环将 `x` 的所有对应位置上的值都加上 `y`。具体的操作是首先将 `x` 位置上的值与 `y` 相加，然后通过 `lowbit` 函数找到 `x` 的下一个需要修改的位置，将该位置上的值也加上 `y`，然后继续找下一个位置，直到修改完所有需要修改的位置为止。这样就完成了数组的修改。

3. getsum函数：这个函数用于求解树状数组中某个范围的前缀和。参数 `x` 表示要求解前缀和的位置。函数使用一个循环将 `x` 的所有对应位置上的值累加起来，然后通过 `lowbit` 函数找到 `x` 的上一个位置（即最后一个需要累加的位置），再将该位置上的值累加起来，然后继续找上一个位置，直到累加完所有需要累加的位置为止。这样就得到了从位置 `1` 到位置 `x` 的前缀和。

这就是树状数组的核心操作，通过使用这三个函数，我们可以实现树状数组的各种功能，如求解区间和、单点修改等。

```python
n, MOD, ans = int(input()), 998244353, 1						# 内存69832KB, 时间2847ms
a, fac = list(map(int, input().split())), [1]

tree = [0] * (n + 1)

def lowbit(x):
    return x & -x

def update(x, y):
    while x <= n:
        tree[x] += y
        x += lowbit(x)

def getsum(x):
    tot = 0
    while x:
        tot += tree[x]
        x -= lowbit(x)
    return tot


for i in range(1, n):
    fac.append(fac[i-1] * i % MOD)

for i in range(1, n + 1):
    cnt = getsum(a[i-1])
    update(a[i-1], 1)
    ans = (ans + ((a[i-1] - 1 - cnt) * fac[n - i]) % MOD) % MOD
    
print(ans)
```



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231029152322373.png" alt="image-20231029152322373" style="zoom:67%;" />



#### 线段树（Segment tree）

线段树 segment tree 来计算第i位右边比该数还要小的数的个数。

```python
n, MOD, ans = int(input()), 998244353, 1					# 内存69900KB, 时间5162ms
a, fac = list(map(int, input().split())), [1]

tree = [0] * (2*n)


def build(arr):

    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = arr[i]

    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]


# function to update a tree node
def updateTreeNode(p, value):

    # set value at position p
    tree[p + n] = value
    p = p + n

    # move upward and update parents
    i = p
    while i > 1:

        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1


# function to get sum on interval [l, r)
def query(l, r):

    res = 0

    l += n
    r += n

    while l < r:

        if (l & 1):
            res += tree[l]
            l += 1

        if (r & 1):
            r -= 1
            res += tree[r]

        l >>= 1
        r >>= 1

    return res


#build([0]*n)

for i in range(1, n):
    fac.append(fac[i-1] * i % MOD)

for i in range(1, n + 1):
    cnt = query(0, a[i-1])
    updateTreeNode(a[i-1]-1, 1)
    
    ans = (ans + (a[i-1] -1 - cnt) * fac[n - i]) % MOD
    
print(ans)

```



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231029161854925.png" alt="image-20231029161854925" style="zoom: 50%;" />







## 数据结构：线段树和树状数组

线段树（Segment Tree）和树状数组（Binary Indexed Tree）的区别和联系：1）时间复杂度相同, 但是树状数组的常数优于线段树。2）树状数组的作用被线段树完全涵盖, 凡是可以使用树状数组解决的问题, 使用线段树一定可以解决, 但是线段树能够解决的问题树状数组未必能够解决。3）树状数组的代码量比线段树小很多。



Segment Tree and Its Applications

https://www.baeldung.com/cs/segment-trees#:~:text=The%20segment%20tree%20is%20a,structure%20such%20as%20an%20array.

The segment tree is a type of data structure from computational geometry. [Bentley](https://en.wikipedia.org/wiki/Bentley–Ottmann_algorithm) proposed this well-known technique in 1977. A segment tree is essentially a binary tree in whose nodes we store the information about the segments of a linear data structure such as an array.



Fenwick tree

https://en.wikipedia.org/wiki/Fenwick_tree#:~:text=A%20Fenwick%20tree%20or%20binary,in%20an%20array%20of%20values.&text=This%20structure%20was%20proposed%20by,further%20modification%20published%20in%201992.

A **Fenwick tree** or **binary indexed tree** **(BIT)** is a data structure that can efficiently update values and calculate [prefix sums](https://en.wikipedia.org/wiki/Prefix_sum) in an array of values.

This structure was proposed by Boris Ryabko in 1989 with a further modification published in 1992. It has subsequently become known under the name Fenwick tree after Peter Fenwick, who described this structure in his 1994 article.



### Segment tree | Efficient implementation

https://www.geeksforgeeks.org/segment-tree-efficient-implementation/

Let us consider the following problem to understand Segment Trees without recursion.
We have an array $arr[0 . . . n-1]$. We should be able to, 

1. Find the sum of elements from index l to r where $0 \leq l \leq r \leq n-1$
2. Change the value of a specified element of the array to a new value x. We need to do $arr[i] = x$ where $0 \leq i \leq n-1$. 

A **simple solution** is to run a loop from l to r and calculate the sum of elements in the given range. To update a value, simply do $arr[i] = x$. The first operation takes **O(n)** time and the second operation takes **O(1)** time.

**Another solution** is to create another array and store the sum from start to i at the ith index in this array. The sum of a given range can now be calculated in O(1) time, but the update operation takes O(n) time now. This works well if the number of query operations is large and there are very few updates.
What if the number of queries and updates are equal? Can we perform both the operations in O(log n) time once given the array? We can use a [Segment Tree](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/) to do both operations in O(Logn) time. We have discussed the complete implementation of segment trees in our [previous](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/) post. In this post, we will discuss the easier and yet efficient implementation of segment trees than in the previous post.
Consider the array and segment tree as shown below:  叶子是数组值，非叶是和

![img](https://media.geeksforgeeks.org/wp-content/uploads/excl.png)



You can see from the above image that the original array is at the bottom and is 0-indexed with 16 elements. The tree contains a total of 31 nodes where the leaf nodes or the elements of the original array start from node 16. So, we can easily construct a segment tree for this array using a 2*N sized array where N is the number of elements in the original array. The leaf nodes will start from index N in this array and will go up to index (2*N – 1). Therefore, the element at index i in the original array will be at index (i + N) in the segment tree array. Now to calculate the parents, we will start from the index (N – 1) and move upward. 根节点下标从1开始，For index i , the left child will be at (2 * i) and the right child will be at (2*i + 1) index. So the values at nodes at (2 * i) and (2*i + 1) are combined at i-th node to construct the tree. 
As you can see in the above figure, we can query in this tree in an interval [L,R) with left index(L) included and right (R) excluded.
We will implement all of these multiplication and addition operations using bitwise operators.
Let us have a look at the complete implementation: 

```python
# Python3 Code Addition 

# limit for array size 
N = 100000; 

# Max size of tree 
tree = [0] * (2 * N); 

# function to build the tree 
def build(arr) : 

	# insert leaf nodes in tree 
	for i in range(n) : 
		tree[n + i] = arr[i]; 
	
	# build the tree by calculating parents 
	for i in range(n - 1, 0, -1) : 
    # tree[i] = tree[2*i] + tree[2*i+1]
		tree[i] = tree[i << 1] + tree[i << 1 | 1]; 	

# function to update a tree node 
def updateTreeNode(p, value) : 
	
	# set value at position p 
	tree[p + n] = value; 
	p = p + n; 
	
	# move upward and update parents 
	i = p; 
	
	while i > 1 : 
		
		tree[i >> 1] = tree[i] + tree[i ^ 1]; 
		i >>= 1; 

# function to get sum on interval [l, r) 
def query(l, r) : 

	res = 0; 
	
	# loop to find the sum in the range 
	l += n; 
	r += n; 
	
	while l < r : 
	
		if (l & 1) : 
			res += tree[l]; 
			l += 1
	
		if (r & 1) : 
			r -= 1; 
			res += tree[r]; 
			
		l >>= 1; 
		r >>= 1
	
	return res; 

if __name__ == "__main__" : 

	a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]; 

	n = len(a); 
	
	build(a); 
	
	# print the sum in range(1,2) index-based 
	print(query(1, 3)); 
	
	# modify element at 2nd index 
	updateTreeNode(2, 1); 
	
	# print the sum in range(1,2) index-based 
	print(query(1, 3)); 

```



**Output:** 

```
5
3
```

Yes! That is all. The complete implementation of the segment tree includes the query and update functions. Let us now understand how each of the functions works: 


1. The picture makes it clear that the leaf nodes are stored at i+n, so we can clearly insert all leaf nodes directly.
2. The next step is to build the tree and it takes O(n) time. The parent always has its less index than its children, so we just process all the nodes in decreasing order, calculating the value of the parent node. If the code inside the build function to calculate parents seems confusing, then you can see this code. It is equivalent to that inside the build function. 

```python
tree[i] = tree[2*i] + tree[2*i+1]
```

 

3. Updating a value at any position is also simple and the time taken will be proportional to the height （“高度”这个概念，其实就是从下往上度量，树这种数据结构的高度是从最底层开始计数，并且计数的起点是0） of the tree. We only update values in the parents of the given node which is being changed. So to get the parent, we just go up to the parent node, which is p/2 or p>>1, for node p. p^1 turns (2\*i) to (2\*i + 1) and vice versa to get the second child of p.
4. Computing the sum also works in $O(Logn)$ time. If we work through an interval of [3,11), we need to calculate only for nodes 19,26,12, and 5 in that order.  要演示这个索引上行的求和过程，前面程序数组是12个元素，图示是16个元素，需要稍作修改。增加了print输出，便于调试。



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/202310312148391.png" alt="image-20231031214814445" style="zoom:50%;" />



The idea behind the query function is whether we should include an element in the sum or whether we should include its parent. Let’s look at the image once again for proper understanding. 

![img](https://media.geeksforgeeks.org/wp-content/uploads/excl.png)

Consider that L is the left border of an interval and R is the right border of the interval [L,R). It is clear from the image that if L is odd, then it means that it is the right child of its parent and our interval includes only L and not the parent. So we will simply include this node to sum and move to the parent of its next node by doing L = (L+1)/2. Now, if L is even, then it is the left child of its parent and the interval includes its parent also unless the right borders interfere. Similar conditions are applied to the right border also for faster computation. We will stop this iteration once the left and right borders meet.
The theoretical time complexities of both previous implementation and this implementation is the same, but practically, it is found to be much more efficient as there are no recursive calls. We simply iterate over the elements that we need. Also, this is very easy to implement.

**Time Complexities:**

- Tree Construction: O( n )
- Query in Range: O( Log n )
- Updating an element: O( Log n ).

**Auxiliary Space:** O(2*N)



#### 1364A: A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A

Ehab loves number theory, but for some reason he hates the number 𝑥. Given an array 𝑎, find the length of its longest subarray such that the sum of its elements **isn't** divisible by 𝑥, or determine that such subarray doesn't exist.

An array 𝑎 is a subarray of an array 𝑏 if 𝑎 can be obtained from 𝑏 by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

**Input**

The first line contains an integer 𝑡 (1≤𝑡≤5) — the number of test cases you need to solve. The description of the test cases follows.

The first line of each test case contains 2 integers 𝑛 and 𝑥 (1≤𝑛≤10^5^, 1≤𝑥≤10^4^) — the number of elements in the array 𝑎 and the number that Ehab hates.

The second line contains 𝑛 space-separated integers $𝑎_1, 𝑎_2, ……, 𝑎_𝑛 (0≤𝑎_𝑖≤10^4)$ — the elements of the array 𝑎.

**Output**

For each testcase, print the length of the longest subarray whose sum isn't divisible by 𝑥. If there's no such subarray, print −1.

Example

input

```
3
3 3
1 2 3
3 4
1 2 3
2 2
0 6
```

output

```
2
3
-1
```

Note

In the first test case, the subarray \[2,3\] has sum of elements 5, which isn't divisible by 3.

In the second test case, the sum of elements of the whole array is 6, which isn't divisible by 4.

In the third test case, all subarrays have an even sum, so the answer is −1.



Pypy3 可以AC。使用tree segment，时间复杂度是O(n*logn)

```python
# CF 1364A
 
# def prefix_sum(nums):
#     prefix = []
#     total = 0
#     for num in nums:
#         total += num
#         prefix.append(total)
#     return prefix
 
# def suffix_sum(nums):
#     suffix = []
#     total = 0
#     # 首先将列表反转
#     reversed_nums = nums[::-1]
#     for num in reversed_nums:
#         total += num
#         suffix.append(total)
#     # 将结果反转回来
#     suffix.reverse()
#     return suffix
 
 
t = int(input())
ans = []
for _ in range(t):
    n, x = map(int, input().split())
    a = [int(i) for i in input().split()]


# Segment tree | Efficient implementation
# https://www.geeksforgeeks.org/segment-tree-efficient-implementation/

    # Max size of tree 
    tree = [0] * (2 * n); 

    def build(arr) : 

        # insert leaf nodes in tree 
        for i in range(n) : 
            tree[n + i] = arr[i]; 
        
        # build the tree by calculating parents 
        for i in range(n - 1, 0, -1) : 
            tree[i] = tree[i << 1] + tree[i << 1 | 1]; 

    # function to update a tree node 
    def updateTreeNode(p, value) : 
        
        # set value at position p 
        tree[p + n] = value; 
        p = p + n; 
        
        # move upward and update parents 
        i = p; 
        
        while i > 1 : 
            
            tree[i >> 1] = tree[i] + tree[i ^ 1]; 
            i >>= 1; 

    # function to get sum on interval [l, r) 
    def query(l, r) : 

        res = 0; 
        
        # loop to find the sum in the range 
        l += n; 
        r += n; 
        
        while l < r : 
        
            if (l & 1) : 
                res += tree[l]; 
                l += 1
        
            if (r & 1) : 
                r -= 1; 
                res += tree[r]; 
                
            l >>= 1; 
            r >>= 1
        
        return res; 
    #aprefix_sum = prefix_sum(a)
    #asuffix_sum = suffix_sum(a)
 
    build([i%x for i in a]);
    
    left = 0
    right = n - 1
    if right == 0:
        if a[0] % x !=0:
            print(1)
        else:
            print(-1)
        continue
 
    leftmax = 0
    rightmax = 0
    while left != right:
        #total = asuffix_sum[left]
        total = query(left, right+1)
        if total % x != 0:
            leftmax = right - left + 1
            break
        else:
            left += 1
 
    left = 0
    right = n - 1
    while left != right:
        #total = aprefix_sum[right]
        total = query(left, right+1)
        if total % x != 0:
            rightmax = right - left + 1
            break
        else:
            right -= 1
    
    if leftmax == 0 and rightmax == 0:
        #print(-1)
        ans.append(-1)
    else:
        #print(max(leftmax, rightmax))
        ans.append(max(leftmax, rightmax))

print('\n'.join(map(str,ans)))
```



如果用sum求和，O(n^2)，pypy3也会在test3 超时。







#### Benifits of segment tree usage

https://www.geeksforgeeks.org/segment-tree-sum-of-given-range/

- **Range Queries:** One of the main use cases of segment trees is to perform range queries on an array in an efficient manner. The query function in the segment tree can return the ==minimum, maximum, sum, or any other aggregation== of elements within a specified range in the array in O(log n) time.

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031140857139.png" alt="image-20231031140857139" style="zoom:50%;" />



假设根节点下标从0开始，左子节点 = 2\*父节点+1，右子节点  = 2\*父节点+2

二叉树的父子节点位置关系，https://zhuanlan.zhihu.com/p/339763580

```python
class SegmentTree:
	def __init__(self, array):
		self.size = len(array)
		self.tree = [0] * (4 * self.size)
		self.build_tree(array, 0, 0, self.size - 1)

	def build_tree(self, array, tree_index, left, right):
		if left == right:
			self.tree[tree_index] = array[left]
			return
		mid = (left + right) // 2
		self.build_tree(array, 2 * tree_index + 1, left, mid)
		self.build_tree(array, 2 * tree_index + 2, mid + 1, right)
		self.tree[tree_index] = min(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

	def query(self, tree_index, left, right, query_left, query_right):
		if query_left <= left and right <= query_right:
			return self.tree[tree_index]
		mid = (left + right) // 2
		min_value = float('inf')
		if query_left <= mid:
			min_value = min(min_value, self.query(2 * tree_index + 1, left, mid, query_left, query_right))
		if query_right > mid:
			min_value = min(min_value, self.query(2 * tree_index + 2, mid + 1, right, query_left, query_right))
		return min_value

	def query_range(self, left, right):
		return self.query(0, 0, self.size - 1, left, right)


if __name__ == '__main__':
	array = [1, 3, 2, 5, 4, 6]
	st = SegmentTree(array)
	print(st.query_range(1, 5)) # 2

```

如果要返回区间最大值，只需要修改第14、20、22、24行程序为求最大相应代码

```python
        #self.tree[tree_index] = min(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])
        self.tree[tree_index] = max(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])
...
				#min_value = float('inf')
        min_value = -float('inf')
        if query_left <= mid:
            #min_value = min(min_value, self.query(2 * tree_index + 1, left, mid, query_left, query_right))
            min_value = max(min_value, self.query(2 * tree_index + 1, left, mid, query_left, query_right))
        if query_right > mid:
            #min_value = min(min_value, self.query(2 * tree_index + 2, mid + 1, right, query_left, query_right))
            min_value = max(min_value, self.query(2 * tree_index + 2, mid + 1, right, query_left, query_right))
        return min_value
   ....
   print(st.query_range(1, 5)) # 6   
      
```

如果要返回区间 求和，只需要修改第14、20、22、24行程序为求和代码。



### 树状数组

树状数组或二叉索引树（英语：Binary Indexed Tree），又以其发明者命名为Fenwick树，最早由Peter M. Fenwick于1994年以A New Data Structure for Cumulative Frequency Tables为题发表。其初衷是解决数据压缩里的累积频率（Cumulative Frequency）的计算问题，现多用于高效计算数列的前缀和， 区间和。



#### Binary Indexed Tree or Fenwick Tree

https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/

Let us consider the following problem to understand Binary Indexed Tree.
We have an array $arr[0 . . . n-1]$. We would like to 
**1** Compute the sum of the first i elements. 
**2** Modify the value of a specified element of the array arr[i] = x where $0 \leq i \leq n-1$.
A **simple solution** is to run a loop from 0 to i-1 and calculate the sum of the elements. To update a value, simply do arr[i] = x. The first operation takes O(n) time and the second operation takes O(1) time. Another simple solution is to create an extra array and store the sum of the first i-th elements at the i-th index in this new array. The sum of a given range can now be calculated in O(1) time, but the update operation takes O(n) time now. This works well if there are a large number of query operations but a very few number of update operations.
**Could we perform both the query and update operations in O(log n) time?** 
One efficient solution is to use [Segment Tree](https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/) that performs both operations in O(Logn) time.
An alternative solution is Binary Indexed Tree, which also achieves O(Logn) time complexity for both operations. Compared with Segment Tree, Binary Indexed Tree requires less space and is easier to implement.

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141452788.png" alt="image-20231031141452788" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141531597.png" alt="image-20231031141531597" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141548736.png" alt="image-20231031141548736" style="zoom:50%;" />

**Representation** 
Binary Indexed Tree is represented as an array. Let the array be BITree[]. Each node of the Binary Indexed Tree stores the sum of some elements of the input array. The size of the Binary Indexed Tree is equal to the size of the input array, denoted as n. In the code below, we use a size of n+1 for ease of implementation.

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141831067.png" alt="image-20231031141831067" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031141629059.png" alt="image-20231031141629059" style="zoom:50%;" />




**Construction** 
We initialize all the values in BITree[] as 0. Then we call update() for all the indexes, the update() operation is discussed below.
**Operations** 


> ***getSum(x): Returns the sum of the sub-array arr[0,…,x]*** 
> // Returns the sum of the sub-array arr[0,…,x] using BITree[0..n], which is constructed from arr[0..n-1] 
>
> 1) Initialize the output sum as 0, the current index as x+1. 
> 2) Do following while the current index is greater than 0. 
>
> …a) Add BITree[index] to sum 
> …b) Go to the parent of BITree[index]. The parent can be obtained by removing 
> the last set bit from the current index, i.e., index = index – (index & (-index)) 
>
> 3) Return sum.

 

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/BITSum.png" alt="BITSum" style="zoom: 67%;" />



getsum(7)

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031142037881.png" alt="image-20231031142037881" style="zoom:50%;" />

getsum(8)

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031142146355.png" alt="image-20231031142146355" style="zoom:50%;" />



**整数的二进制表示常用的方式之一是使用补码**

补码是一种表示有符号整数的方法，它将负数的二进制表示转换为正数的二进制表示。补码的优势在于可以使用相同的算术运算规则来处理正数和负数，而不需要特殊的操作。

在补码表示中，最高位用于表示符号位，0表示正数，1表示负数。其他位表示数值部分。

具体将一个整数转换为补码的步骤如下：

1. 如果整数是正数，则补码等于二进制表示本身。
2. 如果整数是负数，则需要先将其绝对值转换为二进制，然后取反，最后加1。

例如，假设要将-5转换为补码：

1. 5的二进制表示为00000101。

2. 将其取反得到11111010。

3. 加1得到11111011，这就是-5的补码表示。

   

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031142210011.png" alt="image-20231031142210011" style="zoom:50%;" />



The diagram above provides an example of how getSum() is working. Here are some important observations.
BITree[0] is a dummy node. 
BITree[y] is the parent of BITree[x], if and only if y can be obtained by removing the last set bit from the binary representation of x, that is y = x – (x & (-x)).
The child node BITree[x] of the node BITree[y] stores the sum of the elements between y(inclusive) and x(exclusive): arr[y,…,x). 


> ***update(x, val): Updates the Binary Indexed Tree (BIT) by performing arr[index] += val*** 
> // Note that the update(x, val) operation will not change arr[]. It only makes changes to BITree[] 
>
> 1) Initialize the current index as x+1. 
> 2) Do the following while the current index is smaller than or equal to n. 
>
> …a) Add the val to BITree[index] 
> …b) Go to next element of BITree[index]. The next element can be obtained by incrementing the last set bit of the current index, i.e., index = index + (index & (-index))

 

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/BITUpdate12.png" alt="BITUpdate1" style="zoom:67%;" />

update(4, 10)

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231031142428708.png" alt="image-20231031142428708" style="zoom:50%;" />



The update function needs to make sure that all the BITree nodes which contain arr[i] within their ranges being updated. We loop over such nodes in the BITree by repeatedly adding the decimal number corresponding to the last set bit of the current index.
**How does Binary Indexed Tree work?** 
The idea is based on the fact that all positive integers can be represented as the sum of powers of 2. For example 19 can be represented as 16 + 2 + 1. Every node of the BITree stores the sum of n elements where n is a power of 2. For example, in the first diagram above (the diagram for getSum()), the sum of the first 12 elements can be obtained by the sum of the last 4 elements (from 9 to 12) plus the sum of 8 elements (from 1 to 8). The number of set bits in the binary representation of a number n is O(Logn). Therefore, we traverse at-most O(Logn) nodes in both getSum() and update() operations. The time complexity of the construction is O(nLogn) as it calls update() for all n elements. 
**Implementation:** 
Following are the implementations of Binary Indexed Tree.

```python
# Python implementation of Binary Indexed Tree 

# Returns sum of arr[0..index]. This function assumes 
# that the array is preprocessed and partial sums of 
# array elements are stored in BITree[]. 
def getsum(BITTree,i): 
	s = 0 #initialize result 

	# index in BITree[] is 1 more than the index in arr[] 
	i = i+1

	# Traverse ancestors of BITree[index] 
	while i > 0: 

		# Add current element of BITree to sum 
		s += BITTree[i] 

		# Move index to parent node in getSum View 
		i -= i & (-i) 
	return s 

# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def updatebit(BITTree , n , i ,v): 

	# index in BITree[] is 1 more than the index in arr[] 
	i += 1

	# Traverse all ancestors and add 'val' 
	while i <= n: 

		# Add 'val' to current node of BI Tree 
		BITTree[i] += v 

		# Update index to that of parent in update View 
		i += i & (-i) 


# Constructs and returns a Binary Indexed Tree for given 
# array of size n. 
def construct(arr, n): 

	# Create and initialize BITree[] as 0 
	BITTree = [0]*(n+1) 

	# Store the actual values in BITree[] using update() 
	for i in range(n): 
		updatebit(BITTree, n, i, arr[i]) 

	# Uncomment below lines to see contents of BITree[] 
	#for i in range(1,n+1): 
	#	 print BITTree[i], 
	return BITTree 


# Driver code to test above methods 
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9] 
BITTree = construct(freq,len(freq)) 
print("Sum of elements in arr[0..5] is " + str(getsum(BITTree,5))) 
freq[3] += 6
updatebit(BITTree, len(freq), 3, 6) 
print("Sum of elements in arr[0..5]"+
					" after update is " + str(getsum(BITTree,5))) 

# This code is contributed by Raju Varshney 
 
```

**Output**

```
Sum of elements in arr[0..5] is 12
Sum of elements in arr[0..5] after update is 18
```

**Time Complexity:** O(NLogN)
**Auxiliary Space:** O(N)

**Can we extend the Binary Indexed Tree to computing the sum of a range in O(Logn) time?** 
Yes. rangeSum(l, r) = getSum(r) – getSum(l-1).
**Applications:** 
The implementation of the arithmetic coding algorithm. The development of the Binary Indexed Tree was primarily motivated by its application in this case. See [this ](http://en.wikipedia.org/wiki/Fenwick_tree#Applications)for more details.
**Example Problems:** 
[Count inversions in an array | Set 3 (Using BIT)](https://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/) 
[Two Dimensional Binary Indexed Tree or Fenwick Tree](https://www.geeksforgeeks.org/two-dimensional-binary-indexed-tree-or-fenwick-tree/) 
[Counting Triangles in a Rectangular space using BIT](https://www.geeksforgeeks.org/counting-triangles-in-a-rectangular-space-using-2d-bit/)

**References:** 
http://en.wikipedia.org/wiki/Fenwick_tree 
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=binaryIndexedTrees



[力扣307] 线段树&树状数组，https://zhuanlan.zhihu.com/p/126539401



#### 307.区域和检索 - 数组可修改

https://leetcode.cn/problems/range-sum-query-mutable/

给你一个数组 `nums` ，请你完成两类查询。

1. 其中一类查询要求 **更新** 数组 `nums` 下标对应的值
2. 另一类查询要求返回数组 `nums` 中索引 `left` 和索引 `right` 之间（ **包含** ）的nums元素的 **和** ，其中 `left <= right`

实现 `NumArray` 类：

- `NumArray(int[] nums)` 用整数数组 `nums` 初始化对象
- `void update(int index, int val)` 将 `nums[index]` 的值 **更新** 为 `val`
- `int sumRange(int left, int right)` 返回数组 `nums` 中索引 `left` 和索引 `right` 之间（ **包含** ）的nums元素的 **和** （即，`nums[left] + nums[left + 1], ..., nums[right]`）

 

**示例 1：**

```
输入：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
[null, 9, null, 8]

解释：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
```



## 康托展开逆运算(cantor 2)

给出一个数N，再给出N的全排列的某一个排列的次序数，输出该排列。
**Input**
第1行为一个数$N(N≤9)$，第2行为N的全排列的某一个排列的次序数。

**Output**

一行字符串，即该排列。
Sample in
3
1
Sample out
123



思路：可以用康托展开的逆运算来求解。假设已有{1,2,3,4,5}的全排列，并且已经从小到大排序完毕，现要找出第96个数的排列是什么，则康托展开逆运算的具体计算过程如下：
首先用 96-1 得到 95；
用 95 去除 4! 得到 3 余 23，商为 3 表示有 3 个数比它小，则该数是 4，所以第 1 位是 4；
用 23 去除3! 得到 3 余 5，商为 3，表示有 3 个数比它小，即该数是 4，但4前面已经出现过了，所以第2位是5；
用 5 去除 2! 得到 2 余 1，商为 2，表示有 2 个数比它小，即该数是 3，所以第 3 位是 3；
用 1 去除 1! 得到 1 余 0，表示有 1 个数比它小，即该数是 2，所以第 4 位是 2；
最后一个数只能是 1。
所以这个排列是 4 5 3 2 1。
又如找出第 16 个数的排列的计算过程如下：
首先用 16-1 得到 15；
用 15 去除 4! 得到 0余 15，表示有 0 个数比它小，即该数是 1，第 1 位是 1；
用 15 去除 3! 得到 2 余 3，表示有 2 个数比它小，即该数是 3，但由于1已经在之前出现过了，所以第 2 位是 4（因为1在之前出现过了，所以实际上比4小的数是2）；
用 3 去除 2! 得到 1 余 1，表示有 1 个数比它小，即该数是 2，但由于 1 已经在之前出现过了，所以第 3 位是 3（因为 1 在之前出现过了，所以实际上比 3 小的数是1）；
用 1 去除 1! 得到 1 余 0，表示有 1 个数比它小，即该数是 2，但由于 1、3、4已经在之前出现过了，所以第 4 位是 5（因为1、3、4在之前出现过了，所以实际上比 5 小的数是1）。
最后一个数只能是 2，所以这个数是 14352。
参考代码如下。



```python
import math

def cantor(m, n):
    fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]   # 预处理求出阶乘的值
    hash = [0] * 10

    num = 0
    m -= 1
    for i in range(n - 1, 0, -1):
        used = 0
        digit = m // fac[i] + 1                             # 计算有几个数比它小后加1
        m %= fac[i]                                         # 更新m
        for j in range(1, used + digit + 1):                # 查找之前有哪些数已被用过
            if hash[j]:
                used += 1
        num += (used + digit) * math.pow(10, i)
        hash[used + digit] = 1                              # 标记该数被使用过

    for i in range(1, n + 1):                               # 取出最后的未被使用的数
        if hash[i] == 0:
            return int(num + i)

    return -1

num, n = map(int, input().split())
perm = cantor(n, num)
print(' '.join(str(perm)))

```



![image-20231029141904258](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231029141904258.png)



```c++
//康托展开逆运算
#include <bits/stdc++.h>
using namespace std;

int fac[10]= {1,1,2,6,24,120,720,5040,40320,362880};   //预处理求出阶乘的值
int Hash[10];

int Cantor(int m,int n)
{
  int num=0;
  int used,digit;
  m--;
  for(int i=n-1; i>0; i--)
  {
    used=0;
    digit = m/fac[i] + 1;                           //计算有几个数比它小后加1
    m %= fac[i];                                    //更新m
    for(int j=1; j<=used+digit; j++)                //查找之前有哪些数已被用过
      if(Hash[j])
        used++;
    num += (used+digit)*pow(10,i);
    Hash[used + digit]=1;                           //标记该数被使用过
  }
  for(int i=1; i<=n; i++)                           //取出最后的未被使用的数
    if(Hash[i] == 0)
      return num+i;

  return -1;
}

int main()
{
  int num,n;
  cin >> num >> n;
  printf("%d\n",Cantor(n,num));
  return 0;
}
```









## 读题 

#### 545C. Woodcutters

dp/greedy, 1500, https://codeforces.com/problemset/problem/545/C

Little Susie listens to fairy tales before bed every day. Today's fairy tale was about wood cutters and the little girl immediately started imagining the choppers cutting wood. She imagined the situation that is described below.

There are *n* trees located along the road at points with coordinates *x*~1~, *x*~2~, ..., *x~n~*. Each tree has its height *h~i~*. Woodcutters can cut down a tree and fell it to the left or to the right. After that it occupies one of the segments [*x~i~* - *h~i~*, *x~i~*] or [*x~i~*;*x~i~* + *h~i~*]. The tree that is not cut down occupies a single point with coordinate *x~i~*. Woodcutters can fell a tree if the segment to be occupied by the fallen tree doesn't contain any occupied point. The woodcutters want to process as many trees as possible, so Susie wonders, what is the maximum number of trees to fell.

**Input**

The first line contains integer *n* (1 ≤ *n* ≤ 10^5^) — the number of trees.

Next *n* lines contain pairs of integers *x~i~*, *h~i~* (1 ≤ *x~i~*, *h~i~* ≤ 10^9^) — the coordinate and the height of the *і*-th tree.

The pairs are given in the order of ascending *x~i~*. No two trees are located at the point with the same coordinate.

**Output**

Print a single number — the maximum number of trees that you can cut down by the given rules.

Examples

input

```
5
1 2
2 1
5 10
10 9
19 1
```

output

```
3
```

input

```
5
1 2
2 1
5 10
10 9
20 1
```

output

```
4
```

Note

In the first sample you can fell the trees like that:

- fell the 1-st tree to the left — now it occupies segment [ - 1;1]
- fell the 2-nd tree to the right — now it occupies segment [2;3]
- leave the 3-rd tree — it occupies point 5
- leave the 4-th tree — it occupies point 10
- fell the 5-th tree to the right — now it occupies segment [19;20]

In the second sample you can also fell 4-th tree to the right, after that it will occupy segment [10;19].



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190820436.png" alt="image-20231026190820436" style="zoom:50%;" />



#### 1793C. Dora and Search

constructive algorithms, data structures, two pointers, 1200, 

https://codeforces.com/problemset/problem/1793/C

As you know, the girl Dora is always looking for something. This time she was given a permutation, and she wants to find such a subsegment of it that none of the elements at its ends is either the minimum or the maximum of the entire subsegment. More formally, you are asked to find the numbers 𝑙 and 𝑟 (1≤𝑙≤𝑟≤𝑛) such that $𝑎𝑙≠min(𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟)$, $𝑎𝑙≠max(𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟)$ and $𝑎𝑟≠min(𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟)$, $𝑎𝑟≠max(𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟)$.

A permutation of length 𝑛 is an array consisting of 𝑛 distinct integers from 11 to 𝑛 in any order. For example, \[2,3,1,5,4] is a permutation, but \[1,2,2] is not a permutation (2 occurs twice in the array) and \[1,3,4][1,3,4] is also not a permutation (𝑛=3, but 4 is present in the array).

Help Dora find such a subsegment, or tell her that such a subsegment does not exist.

**Input**

Each test consists of multiple test cases. The first line contains a single integer $𝑡 (1≤𝑡≤10^4)$ — the number of test cases. Description of the test cases follows.

For each test case, the first line contains one integer $𝑛(1≤𝑛≤2⋅10^5)$ — the length of permutation.

The second line contains 𝑛 distinct integers $𝑎_1,𝑎_2,…,𝑎_𝑛 (1≤𝑎_𝑖≤𝑛)$ — the elements of permutation.

It is guarented that the sum of 𝑛 over all test cases doesn't exceed 2⋅1052⋅105.

**Output**

For each test case, output −1−1 if the desired subsegment does not exist.

Otherwise, output two indexes 𝑙,𝑟 such that $[𝑎_𝑙,𝑎_{𝑙+1},…,𝑎_𝑟]$ satisfies all conditions.

If there are several solutions, then output any of them.

Example

input

```
4
3
1 2 3
4
2 1 4 3
7
1 3 2 4 6 5 7
6
2 3 6 5 4 1
```

output

```
-1
1 4
2 6
-1
```

Note

In the first and fourth test cases, it can be shown that there are no desired subsegments.

In the second test case, the subsegment \[1,4] satisfies all the conditions, because $max(𝑎_1,𝑎_2,𝑎_3,𝑎_4)=4,min(𝑎_1,𝑎_2,𝑎_3,𝑎_4)=1$, as we see, all the conditions are met.

In the third test case, the subsegment \[2,6] also satisfies all the conditions described.



<img src="/Users/hfyan/Library/Application Support/typora-user-images/image-20231026190955752.png" alt="image-20231026190955752" style="zoom:50%;" />





**数学思维**

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026102551375.png" alt="image-20231026102551375" style="zoom:50%;" />



https://baike.baidu.com/item/戴德金原理/18881836

戴德金原理（Dedekind principle）亦称[戴德金分割](https://baike.baidu.com/item/戴德金分割/6095064?fromModule=lemma_inlink)，是保证直线连续性的基础，其内容为：如果把直线的所有点分成两类，使得：1.每个点恰属于一个类，每个类都不空。2.第一类的每个点都在第二类的每个点的前面，那么，或者在第一类里存在着这样的点，第一类中所有其余的点都在它的前面；或者在第二类里存在着这样的点，它在第二类的所有其余的点的前面 [3]。这个点决定直线的戴德金割切，此点称为戴德金点(或界点)，戴德金原理是戴德金((J.W.)R.Dedekind)于1872年提出来的，在构造欧氏几何的公理系统时，可以选取它作为连续公理，在希尔伯特公理组Ⅰ，Ⅱ，Ⅲ的基础上，[阿基米德公理](https://baike.baidu.com/item/阿基米德公理/1797603?fromModule=lemma_inlink)和康托尔公理合在一起与戴德金原理等价。



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026103418567.png" alt="image-20231026103418567" style="zoom:50%;" />



https://zhuanlan.zhihu.com/p/528662514?utm_id=0

图兰定理（Turan's graph theorem）图论（graph theory）的一条基本定理，它是极值图论（extremal graph theory）的开端。此定理有很多种证明方法，我们将要介绍其中的五个。在陈述图兰定理前，我们先介绍一些背景知识。令 G 为一个简单图（simple graph），即不包含多重边（multiple edges）也不包含自环（loop）。令 G 的顶点（vertex）集为 $V={v_1,...,v_n}$，边（edge）集为 E。若一个图的每对顶点都被唯一的一条边相连，则成此图为一个完全图（complete graph），而一个图的完全子图（complete subgraph）叫作团（clique）。我们将包含 p 的顶点的 p-团写作$K_p$。



#### 803A. Maximal Binary Matrix

constructive algorithms, 1400, https://codeforces.com/problemset/problem/803/A

You are given matrix with *n* rows and *n* columns filled with zeroes. You should put *k* ones in it in such a way that the resulting matrix is symmetrical with respect to the main diagonal (the diagonal that goes from the top left to the bottom right corner) and is lexicographically maximal.

One matrix is lexicographically greater than the other if the first different number in the first different row from the top in the first matrix is greater than the corresponding number in the second one.

If there exists no such matrix then output -1.

**Input**

The first line consists of two numbers *n* and *k* (1 ≤ *n* ≤ 100, 0 ≤ *k* ≤ 106).

**Output**

If the answer exists then output resulting matrix. Otherwise output -1.

Examples

input

```
2 1
```

output

```
1 0 
0 0 
```

input

```
3 2
```

output

```
1 0 0 
0 1 0 
0 0 0 
```

input

```
2 5
```

output

```
-1
```



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190632627.png" alt="image-20231026190632627" style="zoom:50%;" />



### 题目都有背景知识

#### 12560: 生存游戏

matrices, http://cs101.openjudge.cn/practice/12560/

有如下生存游戏的规则：

给定一个n*m(1<=n,m<=100)的数组，每个元素代表一个细胞，其初始状态为活着(1)或死去(0)。

每个细胞会与其相邻的8个邻居（除数组边缘的细胞）进行交互，并遵守如下规则：

任何一个活着的细胞如果只有小于2个活着的邻居，那它就会由于人口稀少死去。

任何一个活着的细胞如果有2个或者3个活着的邻居，就可以继续活下去。

任何一个活着的细胞如果有超过3个活着的邻居，那它就会由于人口拥挤而死去。

任何一个死去的细胞如果有恰好3个活着的邻居，那它就会由于繁殖而重新变成活着的状态。



请写一个函数用来计算所给定初始状态的细胞经过一次更新后的状态是什么。

注意：所有细胞的状态必须同时更新，不能使用更新后的状态作为其他细胞的邻居状态来进行计算。

**输入**

第一行为n和m，而后n行，每行m个元素，用空格隔开。

**输出**

n行，每行m个元素，用空格隔开。

样例输入

```
3 4
0 0 1 1
1 1 0 0
1 1 0 1
```

样例输出

```
0 1 1 0
1 0 0 1
1 1 1 0
```

来源：cs10116 final exam



康威生命游戏(Game of Life)  https://baike.baidu.com/item/康威生命游戏/22668799?fr=ge_ala

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190204167.png" alt="image-20231026190204167" style="zoom: 50%;" />



细胞自动机

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190253685.png" alt="image-20231026190253685" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231026190315997.png" alt="image-20231026190315997" style="zoom:50%;" />





## 语法

### 逻辑删除

在Python中，执行删除操作通常建议使用logic删除，而不是physic删除。也就是说，不直接从列表中删除元素，而是标记它已经删除了。删除操作消耗的时间更少。

布尔代数（Boolean Algebra）是一种数学上的代数系统，用于处理逻辑运算和关系。它涉及布尔值（true和false）以及与、或、非等逻辑运算符。在逻辑删除中，布尔代数的概念被用于标记和操作数据行的删除状态，因此可以说逻辑删除涉及布尔代数的使用。

> 布尔代数
> 世界上不可能有比二进制更简单的计数方法了，它只有两个数字:0和1。从单纯数学的角度讲，它甚至比我们的十进制更合理。但是我们人有十个手指，使用起来比二进制(或者八进制)方便得多，所以在进化和文明发展过程中人类采用了十进制。二进制的历史其实也很早，中国古代的阴阳学说可以认为是最早二进制的雏形。而二进制作为一个计数系统公元前 2-5 世纪时由印度学者完成，但是他们没有使用0和 1计数。到17 世纪，德国伟大的数学家莱布尼兹(Gottfried Leibniz)把它完善，并且用0和 1表示它的两个数字，成为我们今天使用的二进制。二进制除了是一种计数的方式外，它还可以表示逻辑的“是”与“非”。这第二个特性在索引中非常有用。布尔运算是针对二进制，尤其是二进制第二个特性的运算，它很简单，可能没有比布尔运算更简单的运算了。尽管今天每个搜索引擎都官称自己如何聪明、多么智能(这个词非常忽悠人)其实从根本上讲都没有逃出布尔运算的框框。
> 布尔( George Boole)是19 世纪英国的一位中学数学老师，还创办过一所中学。后来在爱尔兰科克( Cork)的一所学院当教授。生前没有人认为他是数学家，虽然他曾经在剑桥大学数学杂志( Cambridge Mathematical Journal)上发表过论文。(英国另一位生前没有被公认为科学家的是著名物理学家焦耳，虽然他生前已经是英国皇家科学院院士，但是他的公认身份是啤酒商。)布尔在工作之余，喜欢阅读数学论著，思考数学问题。1854 年，布尔的《思维规律》(An Investigation ofthe Laws of Thought, on which are founded the Mathematical Theories ofLogic and Probabilities)一书，第一次向人们展示了如何用数学的方法解决逻辑问题。在此之前，人们普遍的认识是数学和逻辑是两个不同的学科今天联合国教科文组织依然把它们严格分开。
> 布尔代数简单得不能再简单了。运算的元素只有两个:1(TRUE，真 )和0(FALSE，假)。基本的运算只有“与”(AND)、“或”(OR)和“非”(NOT) 三种(后来发现，这三种运算都可以转换成“与非”AND-NOT 一种运算)。全部运算只用下列几张真值表就能完全描述清楚。
>
> 表 8.1 与运算真值表
>
> | AND  | 1    | 0    |
> | ---- | ---- | ---- |
> | 1    | 1    | 0    |
> | 0    | 0    | 0    |
>
> 
>
> 表 8.1 说明，如果 AND 运算的两个元素有一个是 0，则运算结果总是 0。如果两个元素都是 1，运算结果是 1。例如，“太阳从西边升起”这个判断是假的(0)，“水可以流动”这个判断是真的(1)，那么，“太阳从西边升起并且水可以流动”就是假的(0)。
>
> 表 8.2 或运算真值表
>
> | OR   | 1    | 0    |
> | ---- | ---- | ---- |
> | 1    | 1    | 1    |
> | 0    | 1    | 0    |
>
>
> 表 8.2 说明，如果 OR 运算的两个元素有一个是 1，则运算结果总是 1。
>
> 如果两个元素都是 0，则运算结果是 0。比如说，“张三是比赛第一名“李四是比赛第一名”是真的(1)，那么“张这个结论是假的(0) 三或者李四是第一名”就是真的(1)。
>
> 表8.3非运算真值表
>
> | NOT  |      |
> | ---- | ---- |
> | 1    | 0    |
> | 0    | 1    |
>
> 
>
> 表 8.3 说明，NOT 运算把 1变成 0，把0变成 1。比如，如果“象牙是白的”是真的(1)，那么“象牙不是白的”必定是假的(0)。
> 这么简单的理论能解决什么实际问题。和布尔同时代的数学家们也有同样的疑问。事实上，在布尔代数提出后 80 多年里，它确实没有什么像样的应用，直到 1938 年香农在他的硕士论文中指出用布尔代数来实现开关电路，才使得布尔代数成为数字电路的基础。所有的数学和逻辑运算，加、减、乘、除、乘方、开方等等，全都能转换成二值的布尔运算。数学的发展实际上是不断地抽象和概括的过程，这些抽象了的方法看似离生活越来越远，但是它们最终能找到适用的地方，布尔代数便是如此。
>
> if控制语句在程序中用于根据条件的真假来进行逻辑推理和计算，并根据条件的结果选择性地执行特定的代码块。，就是逻辑推理与计算合二为一。

 

### 高效数组，array类

https://baijiahao.baidu.com/s?id=1770291275843443574&wfr=spider&for=pc

```python
import sys
import array

a = array.array('i', [0]*1000000)
size = sys.getsizeof(a)//(1024*1024) + 1

print(f'signed int: {size}MB')

b = [0]*1000000
size = sys.getsizeof(b)//(1024*1024) + 1
print(f'list: {size}MB')

for code in array.typecodes:
    arr = array.array(code)
    print(code, arr.itemsize)
```

```
signed int: 4MB
list: 8MB
b 1
B 1
u 4
h 2
H 2
i 4
I 4
l 8
L 8
q 8
Q 8
f 4
d 8
```









OrderedDict。但是Python标准库中的OrderedDict删除元素的复杂度是O(1)。

from collections import OrderedDict

for _ in range(int(input())):
    n, k = map(int, input().split())
    cc = list(map(int, input().split()))
    



## 递归

递归是dfs, dp的基础。需要朝向base case进行递归。



https://runestone.academy/ns/books/published/cppds/Recursion/WhatIsRecursion.html

What Is Recursion?

**Recursion** is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. Recursion involves a function calling itself. While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.

5.3. Calculating the Sum of a Vector of Numbers

We will begin our investigation with a simple problem that you already know how to solve without using recursion. Suppose that you want to calculate the sum of a vector of numbers such as: [1,3,5,7,9]. 

```python
#Example of summing a list using recurison.

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:]) #function makes a recursive call to itself.

print(listsum([1, 3, 5, 7, 9]))
```

Activity: 5.3.4 Recursion Summation Python (lst_recsumpy)



There are a few key ideas while using vector to look at. First, on line 4 we are checking to see if the vector is one element long. This check is crucial and is our escape clause from the function. The sum of a vector of length 1 is trivial; it is just the number in the vector. Second, on line 7 our function calls itself! This is the reason that we call the `vectsum` algorithm recursive. A recursive function is a function that calls itself.

Figure 1 shows the series of **recursive calls** that are needed to sum the vector [1,3,5,7,9]. You should think of this series of calls as a series of simplifications. Each time we make a recursive call we are solving a smaller problem, until we reach the point where the problem cannot get any smaller.

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/sumlistIn.png)

Figure 1: Series of Recursive Calls Adding a List of Numbers

When we reach the point where the problem is as simple as it can get, we begin to piece together the solutions of each of the small problems until the initial problem is solved. Figure 2 shows the additions that are performed as `vectsum` works its way backward through the series of calls. When `vectsum` returns from the topmost problem, we have the solution to the whole problem.

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/sumlistOut.png)

Figure2: Series of Recursive Returns from Adding a List of Numbers



### 1. The Three Laws of Recursion

Like the robots of Asimov, all recursive algorithms must obey three important laws:

> 1. A recursive algorithm must have a **base case**.
> 2. A recursive algorithm must change its state and move toward the base case.
> 3. A recursive algorithm must call itself, recursively.

Let’s look at each one of these laws in more detail and see how it was used in the `vectsum` algorithm. First, a base case is the condition that allows the algorithm to stop recursing. A base case is typically a problem that is small enough to solve directly. In the `vectsum` algorithm the base case is a list of length 1.

To obey the second law, we must arrange for a change of state that moves the algorithm toward the base case. A change of state means that some data that the algorithm is using is modified. Usually the data that represents our problem gets smaller in some way. In the `vectsum` algorithm our primary data structure is a vector, so we must focus our state-changing efforts on the vector. Since the base case is a list of length 1, a natural progression toward the base case is to shorten the vector. 

The final law is that the algorithm must call itself. This is the very definition of recursion. Recursion is a confusing concept to many beginning programmers. As a novice programmer, you have learned that functions are good because you can take a large problem and break it up into smaller problems. The smaller problems can be solved by writing a function to solve each problem. When we talk about recursion it may seem that we are talking ourselves in circles. We have a problem to solve with a function, but that function solves the problem by calling itself! But the logic is not circular at all; the logic of recursion is an elegant expression of solving a problem by breaking it down into smaller and easier problems.

It is important to note that regardless of whether or not a recursive function implements these three rules, it may still take an unrealistic amount of time to compute (and thus not be particularly useful). 



https://runestone.academy/ns/books/published/cppds/Recursion/TheThreeLawsofRecursion.html

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231121110930261.png" alt="image-20231121110930261" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231121111000626.png" alt="image-20231121111000626" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231121111024513.png" alt="image-20231121111024513" style="zoom:50%;" />



### 2. Converting an Integer to a String in Any Base

Suppose you want to convert an integer to a string in some base between binary and hexadecimal. For example, convert the integer 10 to its string representation in decimal as `"10"`, or to its string representation in binary as `"1010"`. While there are many algorithms to solve this problem, including the algorithm discussed in the stack section, the recursive formulation of the problem is very elegant.

Let’s look at a concrete example using base 10 and the number 769. Suppose we have a sequence of characters corresponding to the first 10 digits, like `convString = "0123456789"`. It is easy to convert a number less than 10 to its string equivalent by looking it up in the sequence. For example, if the number is 9, then the string is `convString[9]` or `"9"`. If we can arrange to break up the number 769 into three single-digit numbers, 7, 6, and 9, then converting it to a string is simple. A number less than 10 sounds like a good base case.

Knowing what our base is suggests that the overall algorithm will involve three components:

> 1. Reduce the original number to a series of single-digit numbers.
> 2. Convert the single digit-number to a string using a lookup.
> 3. Concatenate the single-digit strings together to form the final result.

The next step is to figure out how to change state and make progress toward the base case. Since we are working with an integer, let’s consider what mathematical operations might reduce a number. The most likely candidates are division and subtraction. While subtraction might work, it is unclear what we should subtract from what. Integer division with remainders gives us a clear direction. Let’s look at what happens if we divide a number by the base we are trying to convert to.

Using integer division to divide 769 by 10, we get 76 with a remainder of 9. This gives us two good results. First, the remainder is a number less than our base that can be converted to a string immediately by lookup. Second, we get a number that is smaller than our original and moves us toward the base case of having a single number less than our base. Now our job is to convert 76 to its string representation. Again we will use integer division plus remainder to get results of 7 and 6 respectively. Finally, we have reduced the problem to converting 7, which we can do easily since it satisfies the base case condition of n<base, where base=10. The series of operations we have just performed is illustrated in Figure 3. Notice that the numbers we want to remember are in the remainder boxes along the right side of the diagram.

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/toStr.png)

Figure 3: Converting an Integer to a String in Base 10

[ActiveCode 1](https://runestone.academy/ns/books/published/cppds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html#lst-rectostrcpp) shows the C++ and Python code that implements the algorithm outlined above for any base between 2 and 16.

```python
#Recursive example of converting an int to str.

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base] #function makes a recursive call to itself.


print(toStr(1453,16))
```

Notice that in line 5 we check for the base case where `n` is less than the base we are converting to. When we detect the base case, we stop recursing and simply return the string from the `convertString` sequence. In line 8 we satisfy both the second and third laws–by making the recursive call and by reducing the problem size–using division.

Let’s trace the algorithm again; this time we will convert the number 10 to its base 2 string representation (`"1010"`).

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/toStrBase2.png)

Figure 4: Converting the Number 10 to its Base 2 String Representation

[Figure 4](https://runestone.academy/ns/books/published/cppds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html#fig-tostr2) shows that we get the results we are looking for, but it looks like the digits are in the wrong order. The algorithm works correctly because we make the recursive call first on line 8, then we add the string representation of the remainder. If we reversed returning the `convertString` lookup and returning the `toStr` call, the resulting string would be backward! But ==by delaying the concatenation operation until after the recursive call has returned, we get the result in the proper order.== This should remind you of our discussion of stacks back in the previous chapter.

<img src="/Users/hfyan/Library/Application Support/typora-user-images/image-20231121113514094.png" alt="image-20231121113514094" style="zoom:50%;" />



### 3. Stack Frames: Implementing Recursion

Suppose that instead of concatenating the result of the recursive call to `toStr` with the string from `convertString`, we modified our algorithm to push the strings onto a stack instead of making the recursive call. The code for this modified algorithm is shown.

```python
rStack = []

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.append(convertString[n]) #adds string n to the stack.
        else:
            rStack.append(convertString[n % base]) #adds string n modulo base to the stack.
        n = n // base
    res = ""
    while rStack:
        #combines all the items in the stack to make the full string.
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))
```



Each time we make a call to `toStr`, we push a character on the stack. Returning to the previous example we can see that after the fourth call to `toStr` the stack would look like Figure 5. Notice that now we can simply pop the characters off the stack and concatenate them into the final result, `"1010"`.

![../_images/recstack.png](https://raw.githubusercontent.com/GMyhf/img/main/img/recstack.png)

Figure 5: Strings Placed on the Stack During Conversion

The previous example gives us some insight into how C++ implements a recursive function call. When a function is called in Python, a **stack frame** is allocated to handle the local variables of the function. When the function returns, the return value is left on top of the stack for the calling function to access. Figure 6 illustrates the call stack after the return statement on line 4.

![../_images/newcallstack.png](https://raw.githubusercontent.com/GMyhf/img/main/img/newcallstack.png)

Figure 6: Call Stack Generated from `toStr(10,2)`

Notice that the call to `toStr(2//2,2)` leaves a return value of `"1"` on the stack. This return value is then used in place of the function call (`toStr(1,2)`) in the expression `"1" + convertString[2%2]`, which will leave the string `"10"` on the top of the stack. In this way, the C++ call stack takes the place of the stack we used explicitly in [Listing 4](https://runestone.academy/ns/books/published/cppds/Recursion/StackFramesImplementingRecursion.html#lst-recstackcpp). In our list summing example, you can think of the return value on the stack taking the place of an accumulator variable.

The stack frames also provide a scope for the variables used by the function. Even though we are calling the same function over and over, each call creates a new scope for the variables that are local to the function.



### 4. 计算机原理：虚拟地址空间

三大计算机原理之一，@Book_my_flight_v0.3.md

​	计算机的基础架构自从 20 世纪 40 年代起就已经形成规范，包括处理器、存储指令和数据的内存、输入和输出设备。它通常叫作冯·诺依曼架构，以约翰·冯·诺依曼（德語：John Von Neumann，1903 年12 月 28 日－1957 年 2 月 8 日）的名字来命名，他在 1946 年发表的论文里描述了这一架构。论文的开头句，用现在的专门术语来说就是，CPU提 供算法和控制，而 RAM 和磁盘则是记忆存储，键盘、鼠标和显示器与操作人员交互。其中需要重点理解的是与存储相关的进程的虚拟地址空间。

​	在《深入理解计算机系统》[8]第一章中讲到了进程的虚拟地址空间。虚拟存储器是一个抽象概念，它为每个进程提供了一个假象，好像每个进程都在独占地使用主存。每个进程看到的存储器都是一致的，称之为虚拟地址空间。如图1-15所示的是 Linux 进程的虚拟地址空间（其他 Unix 系统的设计与此类似）。在 Linux 中，最上面的四分之一的地址空间是预留给操作系统中的代码和数据的，这对所有进程都一样。底部的四分之三的地址空间用来存放用户进程定义的代码和数据。请注意，图中的地址是从下往上增大的。



![image-20230109195232404](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230109195232404.png)

图1-15 进程的虚拟地址空间（Process virtual address space）（注：图片来源为 Randal Bryant[8]，2015年3月）



​	每个进程看到的虚拟地址空间由准确定义的区（area）构成，每个区都有专门的功能。简单看下每一个区，从最低的地址开始，逐步向上研究。

- 程序代码和数据（code and data）。代码是从同一固定地址开始，紧接着的是和全局变量相对应的数据区。代码和数据区是由可执行目标文件直接初始化的，示例中就是可执行文件hello。

- 堆（heap）。紧随代码和数据区之后的是运行时堆（Run-time heap）。代码和数据区是在进程一旦开始运行时就被指定了大小的，与此不同，作为调用像 malloc 和 free 这样的 C 标准库函数的结果，堆可以在运行时动态地扩展和收缩。

- 共享库（shared libraries）。在地址空间的中间附近是一块用来存放像标准库和数学库这样共享库的代码和数据的区域。共享库的概念非常强大。

- 栈（stack）。位于用户虚拟地址空间顶部的是用户栈，编译器用它来实现函数调用。和堆一样，用户栈（User stack）在程序执行期间可以动态地扩展和收缩。特别地，每次我们调用一个函数时，栈就会增长。每次我们从函数返回时，栈就会收缩。

- 内核虚拟存储器（kernal virtal memory）。内核是操作系统总是驻留在存储器中的部分。地址空间顶部是为内核预留的。应用程序不允许读写这个区域的内容或者直接调用内核代码定义的函数。

​	虚拟存储器的运作需要硬件和操作系统软件间的精密复杂的互相合作，包括对处理器生成的每个地址的硬件翻译。基本思想是把一个进程虚拟存储器的内容存储在磁盘上，然后用主存作为磁盘的高速缓存。



### 5. Tower of Hanoi

The Tower of Hanoi puzzle was invented by the French mathematician Edouard Lucas in 1883. He was inspired by a legend that tells of a Hindu temple where the puzzle was presented to young priests. At the beginning of time, the priests were given three poles and a stack of 64 gold disks, each disk a little smaller than the one beneath it. Their assignment was to transfer all 64 disks from one of the three poles to another, with two important constraints. They could only move one disk at a time, and they could never place a larger disk on top of a smaller one. The priests worked very efficiently, day and night, moving one disk every second. When they finished their work, the legend said, the temple would crumble into dust and the world would vanish.

Although the legend is interesting, you need not worry about the world ending any time soon. The number of moves required to correctly move a tower of 64 disks is $2^64−1=18,446,744,073,709,551,615$. At a rate of one move per second, that is 584,942,417,355 years! Clearly there is more to this puzzle than meets the eye.

Figure 1 shows an example of a configuration of disks in the middle of a move from the first peg to the third. Notice that, as the rules specify, the disks on each peg are stacked so that smaller disks are always on top of the larger disks. If you have not tried to solve this puzzle before, you should try it now. You do not need fancy disks and poles–a pile of books or pieces of paper will work.

![image](https://raw.githubusercontent.com/GMyhf/img/main/img/hanoi-20231121121735301.png)

Figure 1: An Example Arrangement of Disks for the Tower of Hanoi

How do we go about solving this problem recursively? How would you go about solving this problem at all? What is our base case? Let’s think about this problem from the bottom up. Suppose you have a tower of five disks, originally on peg one. If you already knew how to move a tower of four disks to peg two, you could then easily move the bottom disk to peg three, and then move the tower of four from peg two to peg three. But what if you do not know how to move a tower of height four? Suppose that you knew how to move a tower of height three to peg three; then it would be easy to move the fourth disk to peg two and move the three from peg three on top of it. But what if you do not know how to move a tower of three? How about moving a tower of two disks to peg two and then moving the third disk to peg three, and then moving the tower of height two on top of it? But what if you still do not know how to do this? Surely you would agree that moving a single disk to peg three is easy enough, trivial you might even say. This sounds like a base case in the making.

Here is a high-level outline of how to move a tower from the starting pole, to the goal pole, using an intermediate pole:

1. Move a tower of height-1 to an intermediate pole, using the final pole.
2. Move the remaining disk to the final pole.
3. Move the tower of height-1 from the intermediate pole to the final pole using the original pole.

As long as we always obey the rule that the larger disks remain on the bottom of the stack, we can use the three steps above recursively, treating any larger disks as though they were not even there. The only thing missing from the outline above is the identification of a base case. The simplest Tower of Hanoi problem is a tower of one disk. In this case, we need move only a single disk to its final destination. A tower of one disk will be our base case. In addition, the steps outlined above move us toward the base case by reducing the height of the tower in steps 1 and 3. Listing 1 shows the Python code to solve the Tower of Hanoi puzzle.

**Listing 1**

```python
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole) #Recursive call
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole) #Recursive call
```

Notice that the code in Listing 1 is almost identical to the English description. The key to the simplicity of the algorithm is that we make two different recursive calls, one on line 3 and a second on line 5. On line 3 we move all but the bottom disk on the initial tower to an intermediate pole. The next line simply moves the bottom disk to its final resting place. Then on line 5 we move the tower from the intermediate pole to the top of the largest disk. The base case is detected when the tower height is 0; in this case there is nothing to do, so the `moveTower` function simply returns. The important thing to remember about handling the base case this way is that simply returning from `moveTower` is what finally allows the `moveDisk` function to be called.

The function `moveDisk`, shown in Listing 2, is very simple. All it does is print out that it is moving a disk from one pole to another. If you type in and run the `moveTower` program you can see that it gives you a very efficient solution to the puzzle.

**Listing 2**

```python
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
```

The program in ActiveCode 1 provides the entire solution for three disks.

```python
#Simulation of the tower of hanoi.

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole) #Recursive call
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole) #Recursive call

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)


moveTower(3,"A","B","C")

```

Activity: 5.10.2 Solving Tower of Hanoi Recursively Python (hanoipy)

Now that you have seen the code for both `moveTower` and `moveDisk`, you may be wondering why we do not have a data structure that explicitly keeps track of what disks are on what poles. Here is a hint: if you were going to explicitly keep track of the disks, you would probably use three `Stack` objects, one for each pole. The answer is that Python provides the stacks that we need implicitly through the call stack.



#### 04147: 汉诺塔问题(Tower of Hanoi)

http://cs101.openjudge.cn/practice/04147

一、汉诺塔问题 

 有三根杆子A，B，C。A杆上有N个(N>1)穿孔圆盘，盘的尺寸由下到上依次变小。要求按下列规则将所有圆盘移至C杆： 每次只能移动一个圆盘； 大盘不能叠在小盘上面。 提示：可将圆盘临时置于B杆，也可将从A杆移出的圆盘重新移回A杆，但都必须遵循上述两条规则。 

 问：如何移？最少要移动多少次？

汉诺塔示意图如下：

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/1429931663.jpg)

三个盘的移动：

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/1429933148.gif)



二、故事由来 

法国数学家爱德华·卢卡斯曾编写过一个印度的古老传说：在世界中心贝拿勒斯（在印度北部）的圣庙里，一块黄铜板上插着三根宝石针。印度教的主神梵天在创造世界的时候，在其中一根针上从下到上地穿好了由大到小的64片金片，这就是所谓的汉诺塔。不论白天黑夜，总有一个僧侣在按照下面的法则移动这些金片：一次只移动一片，不管在哪根针上，小片必须在大片上面。僧侣们预言，当所有的金片都从梵天穿好的那根针上移到另外一根针上时，世界就将在一声霹雳中消灭，而梵塔、庙宇和众生也都将同归于尽。 

不管这个传说的可信度有多大，如果考虑一下把64片金片，由一根针上移到另一根针上，并且始终保持上小下大的顺序。这需要多少次移动呢?这里需要递归的方法。假设有n片，移动次数是f(n).显然f(1)=1,f(2)=3,f(3)=7，且f(k+1)=2*f(k)+1。此后不难证明f(n)=2^n-1。n=64时， 假如每秒钟一次，共需多长时间呢？一个平年365天有31536000 秒，闰年366天有31622400秒，平均每年31556952秒，计算一下： 18446744073709551615秒 这表明移完这些金片需要5845.54亿年以上，而地球存在至今不过45亿年，太阳系的预期寿命据说也就是数百亿年。真的过了5845.54亿年，不说太阳系和银河系，至少地球上的一切生命，连同梵塔、庙宇等，都早已经灰飞烟灭。

三、解法 

解法的基本思想是递归。假设有A、B、C三个塔，A塔有N块盘，目标是把这些盘全部移到C塔。那么先把A塔顶部的N-1块盘移动到B塔，再把A塔剩下的大盘移到C，最后把B塔的N-1块盘移到C。 每次移动多于一块盘时，则再次使用上述算法来移动。

**输入**

输入为一个整数后面跟三个单字符字符串。
整数为盘子的数目，后三个字符表示三个杆子的编号。

**输出**

输出每一步移动盘子的记录。一次移动一行。
每次移动的记录为例如3:a->b 的形式，即把编号为3的盘子从a杆移至b杆。
我们约定圆盘从小到大编号为1, 2, ...n。即最上面那个最小的圆盘编号为1，最下面最大的圆盘编号为n。

样例输入

```
3 a b c
```

样例输出

```
1:a->c
2:a->b
1:c->b
3:a->c
1:b->a
2:b->c
1:a->c
```

提示

可参考如下网址：
https://www.mathsisfun.com/games/towerofhanoi.html
http://blog.csdn.net/geekwangminli/article/details/7981570
http://www.cnblogs.com/yanlingyin/archive/2011/11/14/2247594.html

来源：重庆科技学院 WJQ



```python
# https://blog.csdn.net/geekwangminli/article/details/7981570

# 将编号为numdisk的盘子从init杆移至desti杆 
def moveOne(numDisk : int, init : str, desti : str):
    print("{}:{}->{}".format(numDisk, init, desti))

#将numDisks个盘子从init杆借助temp杆移至desti杆
def move(numDisks : int, init : str, temp : str, desti : str):
    if numDisks == 1:
        moveOne(1, init, desti)
    else: 
        # 首先将上面的（numDisk-1）个盘子从init杆借助desti杆移至temp杆
        move(numDisks-1, init, desti, temp) 
        
        # 然后将编号为numDisks的盘子从init杆移至desti杆
        moveOne(numDisks, init, desti)
        
        # 最后将上面的（numDisks-1）个盘子从temp杆借助init杆移至desti杆 
        move(numDisks-1, temp, init, desti)

n, a, b, c = input().split()
move(int(n), a, b, c)
```





#### 01958: Strange Towers of Hanoi

http://cs101.openjudge.cn/practice/01958/

Charlie Darkbrown sits in another one of those boring Computer Science lessons: At the moment the teacher just explains the standard Tower of Hanoi problem, which bores Charlie to death!

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/1958_1.jpg)

The teacher points to the blackboard (Fig. 4) and says: "So here is the problem:

- There are three towers: A, B and C.
- There are n disks. The number n is constant while working the puzzle.
- All disks are different in size.
- The disks are initially stacked on tower A increasing in size from the top to the bottom.
- The goal of the puzzle is to transfer all of the disks from tower A to tower C.
- One disk at a time can be moved from the top of a tower either to an empty tower or to a tower with a larger disk on the top.

So your task is to write a program that calculates the smallest number of disk moves necessary to move all the disks from tower A to C."
Charlie: "This is incredibly boring—everybody knows that this can be solved using a simple recursion.I deny to code something as simple as this!"
The teacher sighs: "Well, Charlie, let's think about something for you to do: For you there is a fourth tower D. Calculate the smallest number of disk moves to move all the disks from tower A to tower D using all four towers."
Charlie looks irritated: "Urgh. . . Well, I don't know an optimal algorithm for four towers. . . "
**Problem**
So the real problem is that problem solving does not belong to the things Charlie is good at. Actually, the only thing Charlie is really good at is "sitting next to someone who can do the job". And now guess what — exactly! It is you who is sitting next to Charlie, and he is already glaring at you.
Luckily, you know that the following algorithm works for n <= 12: At first k >= 1 disks on tower A are fixed and the remaining n-k disks are moved from tower A to tower B using the algorithm for four towers.Then the remaining k disks from tower A are moved to tower D using the algorithm for three towers. At last the n - k disks from tower B are moved to tower D again using the algorithm for four towers (and thereby not moving any of the k disks already on tower D). Do this for all k 2 ∈{1, .... , n} and find the k with the minimal number of moves.
So for n = 3 and k = 2 you would first move 1 (3-2) disk from tower A to tower B using the algorithm for four towers (one move). Then you would move the remaining two disks from tower A to tower D using the algorithm for three towers (three moves). And the last step would be to move the disk from tower B to tower D using again the algorithm for four towers (another move). Thus the solution for n = 3 and k = 2 is 5 moves. To be sure that this really is the best solution for n = 3 you need to check the other possible values 1 and 3 for k. (But, by the way, 5 is optimal. . . )

输入

There is no input.

输出

For each n (1 <= n <= 12) print a single line containing the minimum number of moves to solve the problem for four towers and n disks.

样例输入

```
No input.
```

样例输出

```
REFER TO OUTPUT.
```

来源

TUD Programming Contest 2002, Darmstadt, Germany



《短码之美》2007年，184页

汉诺塔，大家知道吗?汉诺塔由 3根柱子、大小不同的空心圆盘组成。所有圆盘最初都放在最左边的柱子上。圆盘的摆放规则是上面的圆盘必须小于下面的圆盘。把这些圆盘一个一个都移动到最右边的柱子上，如果圆盘的个数是 n，大家都知道一般需要移动 (2^2^-1)次。比如，n=3的时候，



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030193822757.png" alt="image-20231030193822757" style="zoom:50%;" />



的确是用了 2^3^-1=7 次完成了移动。那么，这次的问题不是基本的汉诺塔，而是把柱子的根数增加1根。如果柱子增加到 4根，原来需要移动 7次完成，现在只需要 5次就可以了。

<img src="/Users/hfyan/Library/Application Support/typora-user-images/image-20231030194009343.png" alt="image-20231030194009343" style="zoom:50%;" />

如果增加圆盘个数，就应该能省下更多的步数，但是这个规则还不是很清楚。题面要求编写程序计算 4根柱子的时候，1~12 个盘子所需的最小移动次数。



有 4根柱子的时候，可以利用2根空的柱子移动圆盘，圆盘数 n是 1、2、3的时候只需顺序移动，所以各需要 1、3、5次移动。4个圆盘以上:
(1)首先移动其中的几个盘子;
(2)把剩余的圆盘移动到指定的位置;
(3)把(1)的圆盘移动到(2)的上面。
这个时候，(1)和(3)可以有 2 根空柱子可以使用，所以可以互换，但是(2)的时候只有一根空柱子。也就是说移动所需的步数与一般汉诺塔 (3 根柱子)相同。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030194457296.png" alt="image-20231030194457296" style="zoom:50%;" />





具体地用 4个圆盘来考虑一下，如下图所示。4个圆盘的时候，①可移动2个圆盘 (3步)，②可移动2个圆盘 (3步)，③再移动2个圆盘 (3步)，总共最少需要 9步。如果①移动3个的时候，则需要 5步，②只移动一个需要 1步，③再移动3 个需要 5步，总共需要 11 步，不是最小的移动步数。但是，①只移动1个的话需要 1步，②只移动3个需7步，③再移动 1个需要1步，总共需要 9步，这才是最小步数。==在什么情况下移动步数最小不太容易看出来==，所以要像这样把 n个圆盘分成k个和 (n-k) 个来检查移动步数，找出最小移动步数的移法。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030195445757.png" alt="image-20231030195445757" style="zoom:50%;" />

圆盘个数增加后需要增加移动步数，如果每次都计算将是很庞大的计算量，所以需要使用DP(Dynamic Programming，动态规划法)求解。

```python
d = [0] * 15
f = [float('inf')] * 15

d[1] = 1
for i in range(2, 13):
    d[i] = d[i - 1] * 2 + 1

f[1] = 1
for i in range(2, 13):
    for j in range(1, i):
        f[i] = min(f[i], f[i - j] * 2 + d[j])

for i in range(1, 13):
    print(f[i])
```



```python
# 23n2300011072，蒋子轩
def hanoi_four_towers(n, source, target, auxiliary1, auxiliary2):
    if n == 0:
        return 0
    if n == 1:
        return 1
    min_moves = float('inf')
    for k in range(1, n):
        three_tower_moves = 2**(n-k)-1
        moves = hanoi_four_towers(k, source, auxiliary1, auxiliary2, target) +\
            three_tower_moves +\
            hanoi_four_towers(k, auxiliary1, target, source, auxiliary2)
        min_moves = min(min_moves, moves)
    return min_moves


for n in range(1, 13):
    print(hanoi_four_towers(n, 'A','D','B','C'))
```



POJ - 1958 Strange Towers of Hanoi 汉诺塔递推问题（4塔），

https://blog.csdn.net/qq_45432665/article/details/104825847

思路：我们先将3塔的情况递推出来，用d[i] 表示有i个盘的时候的最小移动次数，d[1] = 1



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030200714441.png" alt="image-20231030200714441" style="zoom:50%;" />

当有4塔时，也是一样的思路，f[1] = 1

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030200853087.png" alt="image-20231030200853087" style="zoom:50%;" />





4 柱汉诺塔游戏是否已经解决了？

https://www.zhihu.com/question/54353032

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231030201742852.png" alt="image-20231030201742852" style="zoom: 50%;" />



### 6.更多递归题目

#### 01661: Help Jimmy

dfs/dp, http://cs101.openjudge.cn/practice/01661

"Help Jimmy" 是在下图所示的场景上完成的游戏：
![img](https://raw.githubusercontent.com/GMyhf/img/main/img/2978_1-20230915145941944.jpg)
场景中包括多个长度和高度各不相同的平台。地面是最低的平台，高度为零，长度无限。

Jimmy老鼠在时刻0从高于所有平台的某处开始下落，它的下落速度始终为1米/秒。当Jimmy落到某个平台上时，游戏者选择让它向左还是向右跑，它跑动的速度也是1米/秒。当Jimmy跑到平台的边缘时，开始继续下落。Jimmy每次下落的高度不能超过MAX米，不然就会摔死，游戏也会结束。

设计一个程序，计算Jimmy到底地面时可能的最早时间。

**输入**

第一行是测试数据的组数t（0 ≤  t ≤  20）。每组测试数据的第一行是四个整数N，X，Y，MAX，用空格分隔。N是平台的数目（不包括地面），X和Y是Jimmy开始下落的位置的横竖坐标，MAX是一次下落的最大高度。接下来的N行每行描述一个平台，包括三个整数，X1[i]，X2[i]和H[i]。H[i]表示平台的高度，X1[i]和X2[i]表示平台左右端点的横坐标。1 ≤  N ≤  1000，-20000 ≤  X, X1[i], X2[i] ≤  20000，0 < H[i] < Y ≤  20000（i = 1..N）。所有坐标的单位都是米。

Jimmy的大小和平台的厚度均忽略不计。如果Jimmy恰好落在某个平台的边缘，被视为落在平台上。所有的平台均不重叠或相连。测试数据保证问题一定有解。

**输出**

对输入的每组测试数据，输出一个整数，Jimmy到底地面时可能的最早时间。

样例输入

```
1
3 8 17 20
0 10 8
0 10 13
4 14 3
```

样例输出

```
23
```

来源：POJ Monthly--2004.05.15, CEOI 2000, POJ 1661, 程序设计实习2007



```python
# 查达闻 2300011813
from functools import lru_cache

@lru_cache
def dfs(x, y, z):
    for i in range(z+1, N+1):
        if y - MaxVal > p[i][2]:
            return 1 << 30
        elif p[i][0] <= x <= p[i][1]:
            left = x - p[i][0] + dfs(p[i][0], p[i][2], i)
            right = p[i][1] - x + dfs(p[i][1], p[i][2], i)
            return min(left,right)
        
    if y <= MaxVal:
        return 0
    else:
        return 1 << 30


for _ in range(int(input())):
    N, ini_x, ini_y, MaxVal = map(int, input().split())
    
    p = []      #platform
    p.append( [0, 0, 1 << 30] ) # 1<<30 大于 20000*2*1000
    for _ in range(N):
        p.append([int(x) for x in input().split()])
    p.sort(key = lambda x:-x[2])

    print(ini_y + dfs(ini_x, ini_y, 0))
```



#### 02386: Lake Counting

dfs similar, http://cs101.openjudge.cn/practice/02386

Due to recent rains, water has pooled in various places in Farmer John's field, which is represented by a rectangle of N x M (1 <= N <= 100; 1 <= M <= 100) squares. Each square contains either water ('W') or dry land ('.'). Farmer John would like to figure out how many ponds have formed in his field. A pond is a connected set of squares with water in them, where a square is considered adjacent to all eight of its neighbors.

Given a diagram of Farmer John's field, determine how many ponds he has.

输入

\* Line 1: Two space-separated integers: N and M

\* Lines 2..N+1: M characters per line representing one row of Farmer John's field. Each character is either 'W' or '.'. The characters do not have spaces between them.

输出

\* Line 1: The number of ponds in Farmer John's field.

样例输入

```
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
```

样例输出

```
3
```

提示

OUTPUT DETAILS:

There are three ponds: one in the upper left, one in the lower left,and one along the right side.

来源: USACO 2004 November



```python
#1.dfs
import sys
sys.setrecursionlimit(20000)
def dfs(x,y):
	#标记，避免再次访问
    field[x][y]='.'
    for k in range(8):
        nx,ny=x+dx[k],y+dy[k]
        #范围内且未访问的lake
        if 0<=nx<n and 0<=ny<m\
                and field[nx][ny]=='W':
            #继续搜索
            dfs(nx,ny)
n,m=map(int,input().split())
field=[list(input()) for _ in range(n)]
cnt=0
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
for i in range(n):
    for j in range(m):
        if field[i][j]=='W':
            dfs(i,j)
            cnt+=1
print(cnt)
```



#### 05585: 晶矿的个数

matrices/dfs similar, http://cs101.openjudge.cn/practice/05585

在某个区域发现了一些晶矿，已经探明这些晶矿总共有分为两类，为红晶矿和黑晶矿。现在要统计该区域内红晶矿和黑晶矿的个数。假设可以用二维地图m[][]来描述该区域，若m[i][j]为#表示该地点是非晶矿地点，若m[i][j]为r表示该地点是红晶矿地点，若m[i][j]为b表示该地点是黑晶矿地点。一个晶矿是由相同类型的并且上下左右相通的晶矿点组成。现在给你该区域的地图，求红晶矿和黑晶矿的个数。

**输入**

第一行为k，表示有k组测试输入。
每组第一行为n，表示该区域由n*n个地点组成，3 <= n<= 30
接下来n行，每行n个字符，表示该地点的类型。

**输出**

对每组测试数据输出一行，每行两个数字分别是红晶矿和黑晶矿的个数，一个空格隔开。

样例输入

```
2
6
r##bb#
###b##
#r##b#
#r##b#
#r####
######
4
####
#rrb
#rr#
##bb
```

样例输出

```
2 2
1 2
```



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



#### 02786: Pell数列

dp, http://cs101.openjudge.cn/practice/02786/

Pell数列a1, a2, a3, ...的定义是这样的，a1 = 1, a2 = 2, ... , an = 2 * an − 1 + an - 2 (n > 2)。
给出一个正整数k，要求Pell数列的第k项模上32767是多少。

**输入**

第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数k (1 ≤ k < 1000000)。

**输出**

n行，每行输出对应一个输入。输出应是一个非负整数。

样例输入

```
2
1
8
```

样例输出

```
1
408
```





```python
#2300011786 裘思远
from functools import lru_cache

@lru_cache(maxsize=None)
def series(n):
    if n>2:
        return (series(n-1)*2+series(n-2))%32767
    elif n==2:
        return 2
    else:
        return 1

n=int(input())
for _ in range(n):
    k=int(input())%150
    ans=series(k)
    print(ans)
```





## Assignment #8 Mock Exam in Nov. 2023

作业包括 recursion, greedy, matrices, dp 类型。





# 1107-Week9 KMP

说明：11月份第2周是各科密集期中考试时间，我们继续讲拓展知识，便于同学均衡各科期中考试时间。



## 26999: 2023找出全部子串位置

http://cs101.openjudge.cn/practice/26999/

输入两个串 txt, pat，找出 pat 在 txt 中所有出现的位置

例如'aa'在 aaaa 里出现的位置有0,1,2

输入

第一行是整数n
接下来有n行，每行两个不带空格的字符串 txt, pat。$0 < len(pat) \le len(txt) < 2* 10^7$

输出

对每行，从小到大输出 pat 在 txt 中所有的出现位置。位置从0开始算
如果 pat 没出现过，输出 "no"
行末多输出空格没关系

样例输入

```
4
ababcdefgabdefab ab
aaaaaaaaa a
aaaaaaaaa aaa 
112123323 a
```

样例输出

```
0 2 9 14 
0 1 2 3 4 5 6 7 8 
0 1 2 3 4 5 6 
no
```



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231101105153610.png" alt="image-20231101105153610" style="zoom:50%;" />

### Naive Pattern Searching algorithm

Slide the pattern over text one by one and check for a match. If a match is found, then slide by 1 again to check for subsequent matches. 

```python
# https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
# Naive Pattern Searching algorithm.												Time Limit Exceeded, 8960ms

def search(pat, txt):
    M = len(pat)
    N = len(txt)

    res = []
    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while(j < M):
            if (txt[i + j] != pat[j]):			# i会backward,而不是顺序往右走
                break
            j += 1

        if (j == M):
            res.append(str(i))

    return res


n = int(input())
for _ in range(n):
    txt, pat = input().split()
    ans = search(pat, txt)
    if ans:
        print(' '.join(ans))
    else:
        print('no')
```

Time Complexity: $O(N^2)$
Auxiliary Space: $O(1)$

Worst Case: $O(n^2)$
When the pattern doesn’t appear in the text at all or appears only at the very end.
The algorithm will perform O((n-m+1)*m) comparisons, where n is the length of the text and m is the length of the pattern.
In the worst case, for each position in the text, the algorithm may need to compare the entire pattern against the text.



### KMP Algorithm

```python
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
# Python3 program for KMP Algorithm															时间：2783ms

def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    
    res = []

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            #print("Found pattern at index " + str(i-j))
            cur = i - j
            res.append(str(cur))

            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    
    return res


# Function to compute LPS array
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix

    lps[0] = 0 # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

n = int(input())
for _ in range(n):
    txt, pat = input().split()
    ans = KMPSearch(pat, txt)
    if ans:
        print(' '.join(ans))
    else:
        print('no')
```



用 str.find() 函数AC

```python
n = int(input())																					时间：63ms
for _ in range(n):
    s1, s2 = input().split()
    positions = []
    start = 0
    while True:
        pos = s1.find(s2, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    if positions:
        for pos in positions:
            print(pos, end=" ")
        print("")
    else:
        print("no")
```



## KMP Algorithm for Pattern Searching

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231107135044605.png" alt="image-20231107135044605" style="zoom: 33%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231107135333487.png" alt="image-20231107135333487" style="zoom:50%;" />



**Generative AI is experimental**. Info quality may vary.

The Knuth–Morris–Pratt (KMP) algorithm is **a computer science algorithm that searches for words in a text string**. The algorithm compares characters from left to right. 

When a mismatch occurs, the algorithm uses a preprocessed table called a "Prefix Table" to skip character comparisons.

How the KMP algorithm works

- The algorithm finds repeated substrings called LPS in the pattern and stores LPS information in an array.
- The algorithm compares characters from left to right.
- When a mismatch occurs, the algorithm uses a preprocessed table called a "Prefix Table" to skip character comparisons.
- The algorithm precomputes a prefix function that helps determine the number of characters to skip in the pattern whenever a mismatch occurs.
- The algorithm improves upon the brute force method by utilizing information from previous comparisons to avoid unnecessary character comparisons.

Benefits of the KMP algorithm

- The KMP algorithm efficiently helps you find a specific pattern within a large body of text.
- The KMP algorithm makes your text editing tasks quicker and more efficient.
- The KMP algorithm guarantees 100% reliability.



From Wikipedia, the free encyclopedia

https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

In computer science, the **Knuth–Morris–Pratt algorithm** (or **KMP algorithm**) is a string-searching algorithm that searches for occurrences of a "word" `W` within a main "text string" `S` by employing the observation that when a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin, thus bypassing re-examination of previously matched characters.

The algorithm was conceived by James H. Morris and independently discovered by Donald Knuth "a few weeks later" from automata theory. Morris and Vaughan Pratt published a technical report in 1970. The three also published the algorithm jointly in 1977. Independently, in 1969, Matiyasevich discovered a similar algorithm, coded by a two-dimensional Turing machine, while studying a string-pattern-matching recognition problem over a binary alphabet. This was the first linear-time algorithm for string matching.



下面是一个简单的KMP算法的Python实现示例：

```python
'''
计算模式字符串的最长公共前后缀数组
'''
def get_next(pattern):
    m = len(pattern)
    next = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = next[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        next[i] = j
    return next

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    next = get_next(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = next[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1


text = "ABABABABCABABABABCABABABABC"
pattern = "ABABCABAB"
index = kmp_search(text, pattern)
print("pos matched：", index)

# pos matched： 4

```

> 取自gpt
>
> `get_next` 函数用于计算模式字符串的最长公共前后缀数组，这个数组在 KMP 算法中起到了关键的作用。下面是对它的讲解：
>
> 假设模式字符串为 `pattern`，长度为 `m`。最长公共前后缀数组 `next` 是一个长度为 `m` 的数组，其中 `next[i]` 表示以 `pattern[i]` 结尾的子串的最长公共前后缀的长度。
>
> 下面是 get_next 的实现思路：
>
> 1. 创建一个长度为 `m` 的数组 `next`，并将所有元素初始化为 0。
>
> 2. 定义两个指针 `i` 和 `j`，并分别初始化为 1 和 0。
>
> 3. 开始循环遍历 `pattern` 的元素，从下标 1 到下标 `m-1`。
>
>    - 如果 `pattern[i]` 和 `pattern[j]` 相等，说明找到了更长的公共前后缀，所以将 `j` 值加 1，同时将 `next[i]` 赋值为 `j`。
>
>    - 如果 `pattern[i]` 和 `pattern[j]` 不相等：
>
>      - 如果 `j` 等于 0，则说明 `pattern[i]` 没有与任何前缀匹配，将 `next[i]` 置为 0，然后将 `i` 值加 1。
>
>      - 如果 `j` 不等于 0，则表示之前的前缀 `pattern[0:j]` 与 `pattern[i]` 的后缀不匹配，需要找到一个更短的前缀，检查前缀 `pattern[0:j-1]` 的最长公共前后缀的长度，通过 `next[j-1]` 获取。然后继续找 `pattern[i]` 与 `pattern[next[j-1]]` 是否匹配。重复这个过程，直到找到匹配或者 `j` 减小到 0。
>
> 4. 返回数组 `next`。
>
> 下面是两个示例来帮助理解：
>
> 假设模式字符串为 `pattern = "ABCDABD"`。下面是通过手动计算得到的最长公共前后缀数组 `next = [0, 0, 0, 0, 1, 2, 0]`。
>
> - 当 `i=0` 时，`pattern[0]` 没有前缀和后缀，所以 `next[0] = 0`。
> - 当 `i=1` 时，`pattern[1]` 和 `pattern[0]` 不相等，所以 `next[1] = 0`。
> - 当 `i=2` 时，`pattern[2]` 和 `pattern[0]` 不相等，所以 `next[2] = 0`。
> - 当 `i=3` 时，`pattern[3]` 和 `pattern[0]` 不相等，所以 `next[3] = 0`。
> - 当 `i=4` 时，`pattern[4]` 和 `pattern[0]` 相等，所以 `next[4]` 等于前一个元素的值加 1，也就是 `1`。
> - 当 `i=5` 时，`pattern[5]` 和 `pattern[1]` 相等，所以 `next[5]` 等于前一个元素的值加 1，也就是 `2`。
> - 当 `i=6` 时，`pattern[6]` 和 `pattern[2]` 不相等，也就是说当前前缀 `pattern[0:2]` 和后缀 `pattern[3:5]` 不匹配。因此，需要检查更短的前缀 `pattern[0:1]` 的最长公共前后缀的长度。通过 `next[1]` 获取到最长公共前后缀长度为 `0`，所以 `next[6] = 0`。
>
> 
>
> 当模式字符串为 `pattern = "ababaab"` 时，下面是通过手动计算得到的最长公共前后缀数组 `next = [0, 0, 1, 2, 3, 1, 1]`。
>
> - 当 `i=0` 时，`pattern[0]` 没有前缀和后缀，所以 `next[0] = 0`。
>
> - 当 `i=1` 时，`pattern[1]` 和 `pattern[0]` 不相等，所以 `next[1] = 0`。
>
> - 当 `i=2` 时，`pattern[2]` 和 `pattern[0]` 相等，所以 `next[2]` 等于前一个元素的值加 1，也就是 `1`。
>
> - 当 `i=3` 时，`pattern[3]` 和 `pattern[1]` 不相等，也就是说当前前缀 `pattern[0:1]` 和后缀 `pattern[2:3]` 不匹配。因此，需要检查更短的前缀 `pattern[0:0]` 的最长公共前后缀的长度。通过 `next[0]` 获取到最长公共前后缀长度为 `0`，所以 `next[3] = 0`。
>
> - 当 `i=4` 时，`pattern[4]` 和 `pattern[0]` 不相等，也就是说当前前缀 `pattern[0:3]` 和后缀 `pattern[1:4]` 不匹配。因此，需要检查更短的前缀 `pattern[0:2]` 的最长公共前后缀的长度。通过 `next[2]` 获取到最长公共前后缀长度为 `1`，所以 `next[4] = 1`。
>
> - 当 `i=5` 时，`pattern[5]` 和 `pattern[1]` 不相等，也就是说当前前缀 `pattern[0:3]` 和后缀 `pattern[2:5]` 不匹配。因此，需要检查更短的前缀 `pattern[0:1]` 的最长公共前后缀的长度。通过 `next[1]` 获取到最长公共前后缀长度为 `0`，所以 `next[5] = 0`。
>
> - 当 `i=6` 时，`pattern[6]` 和 `pattern[2]` 不相等，也就是说当前前缀 `pattern[0:3]` 和后缀 `pattern[3:6]` 不匹配。因此，需要检查更短的前缀 `pattern[0:0]` 的最长公共前后缀的长度。通过 `next[0]` 获取到最长公共前后缀长度为 `0`，所以 `next[6] = 0`。





https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

Pattern searching is an important problem in computer science. When we do search for a string in a notepad/word file or browser or database, pattern-searching algorithms are used to show the search results. 



We have discussed the Naive pattern-searching algorithm . The worst case complexity of the Naive algorithm is O(m(n-m+1)). The time complexity of the KMP algorithm is O(n+m) in the worst case. 

**KMP (Knuth Morris Pratt) Pattern Searching:**

The Naive pattern-searching algorithm doesn’t work well in cases where we see many matching characters followed by a mismatching character.

**Examples:**

> **1)** txt[] = “AAAAAAAAAAAAAAAAAB”, pat[] = “AAAAB”
> **2)** txt[] = “ABABABCABABABCABABABC”, pat[] =  “ABABAC” (not a worst case, but a bad case for Naive)

The KMP matching algorithm uses degenerating property (pattern having the same sub-patterns appearing more than once in the pattern) of the pattern and improves the worst-case complexity to **O(n+m)**. 

KMP匹配算法利用模式的退化特性(模式中具有相同子模式的模式出现多次)



The basic idea behind KMP’s algorithm is: whenever we detect a mismatch (after some matches), we already know some of the characters in the text of the next window. We take advantage of this information to avoid matching the characters that we know will anyway match. 

KMP算法背后的基本思想是:每当我们检测到不匹配时(在一些匹配之后)，已经知道下一个窗口文本中的一些字符。利用这些信息来避免匹配我们知道无论如何都会匹配的字符。



> **Matching Overview**
>
> txt = “AAAAABAAABA” 
> pat = “AAAA”
> We compare first window of **txt** with **pat**
>
> txt = “**AAAA**ABAAABA” 
> pat = “**AAAA**”  [Initial position]
> We find a match. This is same as Naive String Matching.
>
> In the next step, we compare next window of **txt** with **pat**.
>
> txt = “**AAAAA**BAAABA” 
> pat =  “**AAAA**” [Pattern shifted one position]
>
> This is where KMP does optimization over Naive. In this second window, we only compare fourth A of pattern
> with fourth character of current window of text to decide whether current window matches or not. Since we know 
> first three characters will anyway match, we skipped matching first three characters. 
>
> **Need of Preprocessing?**
>
> An important question arises from the above explanation, how to know how many characters to be skipped. To know this, 
> we pre-process pattern and prepare an integer array lps[] that tells us the count of characters to be skipped

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231107140956844.png" alt="image-20231107140956844" style="zoom:50%;" />



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231107141019553.png" alt="image-20231107141019553" style="zoom:50%;" />



### **Preprocessing Overview:**

- KMP algorithm preprocesses pat[] and constructs an auxiliary **lps[]** of size **m** (same as the size of the pattern) which is used to skip characters while matching.
- Name **lps** indicates the longest proper prefix which is also a suffix. A proper prefix is a prefix with a whole string not allowed. For example, prefixes of “ABC” are “”, “A”, “AB” and “ABC”. Proper prefixes are “”, “A” and “AB”. Suffixes of the string are “”, “C”, “BC”, and “ABC”. 真前缀（proper prefix）是一个串除该串自身外的其他前缀。
- We search for lps in subpatterns. More clearly we ==focus on sub-strings of patterns that are both prefix and suffix==.
- For each sub-pattern pat[0..i] where i = 0 to m-1, lps[i] stores the length of the maximum matching proper prefix which is also a suffix of the sub-pattern pat[0..i].

>   lps[i] = the longest proper prefix of pat[0..i] which is also a suffix of pat[0..i]. 

**Note:** lps[i] could also be defined as the longest prefix which is also a proper suffix. We need to use it properly in one place to make sure that the whole substring is not considered.

Examples of lps[] construction:

> For the pattern “AAAA”, lps[] is [0, 1, 2, 3]
>
> For the pattern “ABCDE”, lps[] is [0, 0, 0, 0, 0]
>
> For the pattern “AABAACAABAA”, lps[] is [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
>
> For the pattern “AAACAAAAAC”, lps[] is [0, 1, 2, 0, 1, 2, 3, 3, 3, 4] 
>
> For the pattern “AAABAAA”, lps[] is [0, 1, 2, 0, 1, 2, 3]
>
> ```python
> def kmp_next(s):
> 	# kmp算法计算最长相等前后缀
>  next = [0] * len(s)
>  j = 0
>  for i in range(1, len(s)):
>      while s[i] != s[j] and j > 0:
>          j = next[j - 1]
>      if s[i] == s[j]:
>          j += 1
>      next[i] = j
>  return next
> 
> strs = ["AAAA", "ABCDE", "AABAACAABAA", "AAACAAAAAC", "AAABAAA"]
> for i in strs:
>  lps = kmp_next(i)
>  print(f'For pattern "{i}", lps[] is {lps}')
> ```
>
> pythontutor
>
> ![image-20231102015322948](https://raw.githubusercontent.com/GMyhf/img/main/img/202311020153238.png)
>
> 

### **Preprocessing Algorithm:**

In the preprocessing part, 

- We calculate values in **lps[]**. To do that, we keep track of the length of the longest prefix suffix value (we use **len** variable for this purpose) for the previous index
- We initialize **lps[0]** and **len** as 0.
- If **pat[len]** and **pat[i]** match, we increment **len** by 1 and assign the incremented value to lps[i].
- If pat[i] and pat[len] do not match and len is not 0, we update len to lps[len-1]
- See **computeLPSArray()** in the below code for details

**Illustration of preprocessing (or construction of lps[]):**

> pat[] = “AAACAAAA”
>
> **=> len = 0, i = 0:** 
>
> - lps[0] is always 0, we move to i = 1
>
> **=> len = 0, i = 1:**
>
> - Since pat[len] and pat[i] match, do len++, 
> - store it in lps[i] and do i++.
> - Set len = 1, lps[1] = 1, i = 2
>
> **=> len = 1, i  = 2:**
>
> - Since pat[len] and pat[i] match, do len++, 
> - store it in lps[i] and do i++.
> - Set len = 2, lps[2] = 2, i = 3
>
> **=> len = 2, i = 3:**
>
> - Since pat[len] and pat[i] do not match, and len > 0, 
> - Set len = lps[len-1] = lps[1] = 1
>
> **=> len = 1, i = 3:**
>
> - Since pat[len] and pat[i] do not match and len > 0, 
> - len = lps[len-1] = lps[0] = 0
>
> **=> len = 0, i = 3:**
>
> - Since pat[len] and pat[i] do not match and len = 0, 
> - Set lps[3] = 0 and i = 4
>
> **=> len = 0, i = 4:**
>
> - Since pat[len] and pat[i] match, do len++, 
> - Store it in lps[i] and do i++. 
> - Set len = 1, lps[4] = 1, i = 5
>
> **=> len = 1, i = 5:**
>
> - Since pat[len] and pat[i] match, do len++, 
> - Store it in lps[i] and do i++.
> - Set len = 2, lps[5] = 2, i = 6
>
> **=> len = 2, i = 6:**
>
> - Since pat[len] and pat[i] match, do len++, 
> - Store it in lps[i] and do i++.
> - len = 3, lps[6] = 3, i = 7
>
> **=> len = 3, i = 7:**
>
> - Since pat[len] and pat[i] do not match and len > 0,
> - Set len = lps[len-1] = lps[2] = 2
>
> **=> len = 2, i = 7:**
>
> - Since pat[len] and pat[i] match, do len++, 
> - Store it in lps[i] and do i++.
> - len = 3, lps[7] = 3, i = 8
>
> We stop here as we have constructed the whole lps[].

### Implementation of KMP algorithm:

Unlike the [Naive algorithm](https://www.geeksforgeeks.org/searching-for-patterns-set-1-naive-pattern-searching/), where we slide the pattern by one and compare all characters at each shift, we use a value from lps[] to decide the next characters to be matched. ==The idea is to not match a character that we know will anyway match==.

How to use lps[] to decide the next positions (or to know the number of characters to be skipped)?

- We start the comparison of pat[j] with j = 0 with characters of the current window of text.

- We keep matching characters txt[i] and pat[j] and keep incrementing i and j while pat[j] and txt[i] keep **matching**.

- When we see a mismatch

  - We know that characters pat[0..j-1] match with txt[i-j…i-1] (Note that j starts with 0 and increments it only when there is a match).
  - We also know (from the above definition) that lps[j-1] is the count of characters of pat[0…j-1] that are both proper prefix and suffix.
  - From the above two points, we can conclude that we do not need to match these lps[j-1] characters with txt[i-j…i-1] because we know that these characters will anyway match. Let us consider the above example to understand this.

Below is the illustration of the above algorithm:

> Consider txt[] = “**AAAAABAAABA**“, pat[] = “**AAAA**“
>
> If we follow the above LPS building process then **lps[] = {0, 1, 2, 3}** 
>
> **-> i = 0, j = 0:** txt[i] and pat[j] match, do i++, j++
>
> **-> i = 1, j = 1:** txt[i] and pat[j] match, do i++, j++
>
> **-> i = 2, j = 2:** txt[i] and pat[j] match, do i++, j++
>
> **-> i = 3, j = 3:** txt[i] and pat[j] match, do i++, j++
>
> **-> i = 4, j = 4:** Since j = M, print pattern found and reset j, **j** = lps[j-1] = lps[3] = **3**
>
> 
>
> Here unlike Naive algorithm, we do not match first three characters of this window. Value of lps[j-1] (in above step) gave us index of next character to match.
>
> **-> i = 4, j = 3:** txt[i] and pat[j] match, do i++, j++
>
> **-> i = 5, j = 4:** Since j == M, print pattern found and reset j, **j** = lps[j-1] = lps[3] = **3**
> Again unlike Naive algorithm, we do not match first three characters of this window. Value of lps[j-1] (in above step) gave us index of next character to match.
>
> **-> i = 5, j = 3:** txt[i] and pat[j] do NOT match and j > 0, change only j. **j** = lps[j-1] = lps[2] = **2**
>
> **-> i = 5, j = 2:** txt[i] and pat[j] do NOT match and j > 0, change only j. **j** = lps[j-1] = lps[1] = **1**
>
> **-> i = 5, j = 1:** txt[i] and pat[j] do NOT match and j > 0, change only j. **j** = lps[j-1] = lps[0] = **0**
>
> **-> i = 5, j = 0:** txt[i] and pat[j] do NOT match and j is 0, we do i++. 
>
> **-> i = 6, j = 0:** txt[i] and pat[j] match, do i++ and j++
>
> **-> i = 7, j = 1:** txt[i] and pat[j] match, do i++ and j++
>
> We continue this way till there are sufficient characters in the text to be compared with the characters in the pattern…

Below is the implementation of the above approach:



```python
# Python3 program for KMP Algorithm

def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)

	# create lps[] that will hold the longest prefix suffix
	# values for pattern
	lps = [0]*M
	j = 0 # index for pat[]

	# Preprocess the pattern (calculate lps[] array)
	computeLPSArray(pat, M, lps)

	i = 0 # index for txt[]
	while (N - i) >= (M - j):
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			print("Found pattern at index " + str(i-j))
			j = lps[j-1]

		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i += 1


'''
计算最长前缀后缀（Longest Prefix Suffix，LPS）数组的函数。
LPS数组是一个用于字符串匹配算法中的辅助数组。
函数的输入参数包括待匹配的字符串pat、字符串的长度M和LPS数组lps。

通过遍历字符串pat来计算LPS数组。在遍历过程中，会比较当前位置 i 处的字符和之前的
最长前缀后缀长度len处的字符，如果相等，则说明前缀和后缀的长度可以增加1，
并将结果保存到LPS数组中，同时将i和len分别递增1。
如果不相等，则根据已经计算的LPS数组来更新len的值。
如果len不为0，表示已经找到了一个较短的前缀和后缀长度，需要将len更新为LPS数组中前一个位置的值，
然后继续比较当前位置i处的字符和更新后的len位置处的字符。
如果len为0，表示无法找到更短的前缀和后缀长度，将LPS数组当前位置i的值设置为0，并将i递增1。

该算法的时间复杂度为O(M)，其中M为输入字符串的长度。
'''
# Function to compute LPS array
def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] = 0 # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i] == pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is similar
			# to search step.
			if len != 0:
				len = lps[len-1]

				# Also, note that we do not increment i here
			else:
				lps[i] = 0
				i += 1


# Driver code
if __name__ == '__main__':
	txt = "ABABDABACDABABCABAB"
	pat = "ABABCABAB"
	KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain

```

**Output**

```
Found pattern at index 10 
```

**Time Complexity:** O(N+M) where N is the length of the text and M is the length of the pattern to be found.
**Auxiliary Space:** O(M)



## 关于 kmp 算法中 next 数组的周期性质

参考：https://www.acwing.com/solution/content/4614/

引理：
对于某一字符串 S[1～i]，在它众多的next[i]的“候选项”中，如果存在某一个next[i]，使得: i%(i-nex[i])==0，那么 S[1～ (i−next[i])] 可以为 S[1～i] 的循环元而 i/(i−next[i]) 即是它的循环次数 K。

证明如下：

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231107111654773.png" alt="image-20231107111654773" style="zoom: 50%;" />

如果在紧挨着之前框选的子串后面再框选一个长度为 m 的小子串(绿色部分)，同样的道理，

可以得到：S[m～b]=S[b～c]
又因为：S[1～m]=S[m～b]
所以：S[1～m]=S[m～b]=S[b～c]



### 02406: 字符串乘方

http://cs101.openjudge.cn/practice/02406/

给定两个字符串a和b,我们定义a*b为他们的连接。例如，如果a=”abc” 而b=”def”， 则a*b=”abcdef”。 如果我们将连接考虑成乘法，一个非负整数的乘方将用一种通常的方式定义：a^0^=””(空字符串)，a^(n+1)^=a*(a^n^)。

**输入**

每一个测试样例是一行可打印的字符作为输入，用s表示。s的长度至少为1，且不会超过一百万。最后的测试样例后面将是一个点号作为一行。

**输出**

对于每一个s，你应该打印最大的n，使得存在一个a，让$s=a^n$

样例输入

```
abcd
aaaa
ababab
.
```

样例输出

```
1
4
3
```

提示: 本问题输入量很大，请用scanf代替cin，从而避免超时。

来源: Waterloo local 2002.07.01



```python
'''
gpt
使用KMP算法的部分知识，当字符串的长度能被提取的"base字符串"的长度整除时，
即可判断s可以被表示为a^n的形式，此时的n就是s的长度除以"base字符串"的长度。

'''

import sys
while True:
    s = sys.stdin.readline().strip()
    if s == '.':
        break
    len_s = len(s)
    next = [0] * len(s)
    j = 0
    for i in range(1, len_s):
        while j > 0 and s[i] != s[j]:
            j = next[j - 1]
        if s[i] == s[j]:
            j += 1
        next[i] = j
    base_len = len(s)-next[-1]
    if len(s) % base_len == 0:
        print(len_s // base_len)
    else:
        print(1)

```



### 01961: 前缀中的周期

http://cs101.openjudge.cn/practice/01961/

http://poj.org/problem?id=1961

For each prefix of a given string S with N characters (each character has an ASCII code between 97 and 126, inclusive), we want to know whether the prefix is a periodic string. That is, for each $i \ (2 \le i \le N)$ we want to know the largest K > 1 (if there is one) such that the prefix of S with length i can be written as $A^K$ ,that is A concatenated K times, for some string A. Of course, we also want to know the period K.



一个字符串的前缀是从第一个字符开始的连续若干个字符，例如"abaab"共有5个前缀，分别是a, ab, aba, abaa,  abaab。

我们希望知道一个N位字符串S的前缀是否具有循环节。换言之，对于每一个从头开始的长度为 i （i 大于1）的前缀，是否由重复出现的子串A组成，即 AAA...A （A重复出现K次，K 大于 1）。如果存在，请找出最短的循环节对应的K值（也就是这个前缀串的所有可能重复节中，最大的K值）。

**输入**

输入包括多组测试数据。每组测试数据包括两行。
第一行包括字符串S的长度N（2 <= N <= 1 000 000）。
第二行包括字符串S。
输入数据以只包括一个0的行作为结尾。

**输出**

对于每组测试数据，第一行输出 "Test case #“ 和测试数据的编号。
接下来的每一行，输出前缀长度i和重复测数K，中间用一个空格隔开。前缀长度需要升序排列。
在每组测试数据的最后输出一个空行。

样例输入

```
3
aaa
12
aabaabaabaab
0
```

样例输出

```
Test case #1
2 2
3 3

Test case #2
2 2
6 2
9 3
12 4
```



【POJ1961】period，https://www.cnblogs.com/ve-2021/p/9744139.html

如果一个字符串S是由一个字符串T重复K次构成的，则称T是S的循环元。使K出现最大的字符串T称为S的最小循环元，此时的K称为最大循环次数。

现在给定一个长度为N的字符串S，对S的每一个前缀S[1~i],如果它的最大循环次数大于1，则输出该循环的最小循环元长度和最大循环次数。



题解思路：
1）与自己的前缀进行匹配，与KMP中的next数组的定义相同。next数组的定义是：字符串中以i结尾的子串与该字符串的前缀能匹配的最大长度。
2）将字符串S与自身进行匹配，对于每个前缀，能匹配的条件即是：S[i-next[i]+1 \~ i]与S[1~next[i]]是相等的，并且不存在更大的next满足条件。
3）当i-next[i]能整除i时，S[1 \~ i-next[i]]就是S[1 ~ i]的最小循环元。它的最大循环次数就是i/(i - next[i])。



这是刘汝佳《算法竞赛入门经典训练指南》上的原题（p213），用KMP构造状态转移表。在3.3.2 KMP算法。

```python
'''
gpt
这是一个字符串匹配问题，通常使用KMP算法（Knuth-Morris-Pratt算法）来解决。
使用了 Knuth-Morris-Pratt 算法来寻找字符串的所有前缀，并检查它们是否由重复的子串组成，
如果是的话，就打印出前缀的长度和最大重复次数。
'''

# 得到字符串s的前缀值列表
def kmp_next(s):
  	# kmp算法计算最长相等前后缀
    next = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while s[i] != s[j] and j > 0:
            j = next[j - 1]
        if s[i] == s[j]:
            j += 1
        next[i] = j
    return next


def main():
    case = 0
    while True:
        n = int(input().strip())
        if n == 0:
            break
        s = input().strip()
        case += 1
        print("Test case #{}".format(case))
        next = kmp_next(s)
        for i in range(2, len(s) + 1):
            k = i - next[i - 1]		# 可能的重复子串的长度
            if (i % k == 0) and i // k > 1:
                print(i, i // k)
        print()


if __name__ == "__main__":
    main()

```





## Assignment #9 Practice

作业包括 two pointers, greedy, matrices, dp 类型。



# 1114-Week10 动态规划

dp_questions.md



# 1121-Week11 递归、动态规划

recursion_questions.md



# 1128-Week12 搜索

searching_questions.md



1205-Week13 搜索 continue



# 1212-Week14 原理

principal.md



# 1219-Week15 汇总

topic_summary.md



1226-Week16 汇总 continue
