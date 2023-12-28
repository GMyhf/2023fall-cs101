### 27373: 最大整数

2023 fall, Complied by 卢卓然

dp, greedy, string, sort, http://cs101.openjudge.cn/practice/27373



思路：这道题的tag很对，dp, greedy, string, sort都有成分，是非常综合、非常好、当然也非常难的一道题。

首先关于bubble sort和string的成分，是这道题中的“最大整数”模型。要做此题，要先明白这个模型：给定一个序列，输出这些数字随意拼接所能产生的最大整数。借助冒泡排序实现这一点。

```python
for i in range(n):
    for j in range(n-1-i):
        if l[j] + l[j+1] > l[j+1] + l[j]:
            l[j],l[j+1] = l[j+1],l[j]
```

然后，关于dp的部分，是0-1背包的变形。`dp[i][j]`状态定义为在`l`的前i个数中随意选择，满足拼凑起来不超过j位，得到的整数的最大可能数值。那么`dp[n][m]`即为所求。

接着，dp数组的建立，dp数组初始化最好用`''`，也就是空字符串。因为如果用0，会把0看作数字后续操作中进行拼接，这显然是不对的。

dp状态转移方程。如果`weight[i-1]>j`，说明不能选第i个数字，否则会超位数。否则，可以选第i个也可以不选。这时需要取选第i个和不选第i个的更大的值。对于不选第i个的情况，很好理解，就是`dp[i-1][j]`。而对于选第i个的情况，为什么是`int(l[i-1]+dp[i-1][j-weight[i-1]])`就需要解释一下了。

对列表l进行排序后，结果是对任意两个相邻的字符串型的数字，i+j<j+i。但是这样的排序，能否保证对于这个列表的任意一个子列，其顺序是这个子列中数字所组成的最大整数呢？

```
from 23 元培 夏天明
是的，因为不难验证由i+j≤j+i所定义的i与j的关系i€j满足：
1）若i€j，j€k，则i€k
2）对任意的i，i€i
3）若i€j，j€i，则i=j
4）对任意的i，j，都有i€j和j€i至少成立一个
这意味着€是全序，所以由冒泡排序原理知道，可以将整个列表排成有序列.
```

所以，`l`是一个全序集。那么对于选第i个数的情况，根据0-1背包的思路，需要找到“前i-1个数里，拼接后总位数不超过[j-weight[i]]的数字组合”，这些数字组合里的数和第j个数一起构成数字组合。因为`l`是一个全序集，所以要想保证值最大，就还需要这些数**按照l中的相对位置的相反顺序**进行排布，也就是说，第i个数的位置一定在前i-1个数的数字组合之前，也就是在i个数的整体数字组合的最前面。所以前i-1个数的数字组合仍然是挨在一起的。而这些前i-1个数的数字组合中，值最大的那个就是`dp[i-1][j-weight[i]]`对应的数字组合。所以才有这样的递推关系，这个分析过程也可以看作是一种greedy。

至此，代码的主要逻辑都已分析完毕。代码开头的函数f是为了处理dp数组中空字符串不能转化为整型的问题。



##### 代码

```python
def f(string):
    if string=='':
        return 0
    else:
        return int(string)
m=int(input())#最大位数
n=int(input())#正整数数量
l=input().split()
#冒泡排序
for i in range(n):
    for j in range(n-1-i):
        if l[j] + l[j+1] > l[j+1] + l[j]:
            l[j],l[j+1] = l[j+1],l[j]
weight=[]#每个元素的位数
for num in l:
    weight.append(len(num))
#dp[i][j]在前i数中选择，不超过j位，最大可能数值
dp=[['']*(m+1) for _ in range(n+1)]
for k in range(m+1):
    dp[0][k]=''#无法组成整数
for q in range(n+1):
    dp[q][0]=''#无法组成整数
for i in range(1,n+1):
    for j in range(1,m+1):
        if weight[i-1]>j:#不能选第i个，因为会超位数
            dp[i][j]=dp[i-1][j]
        else:#可以选第i个也可以不选
                dp[i][j]=str(max(f(dp[i-1][j]),int(l[i-1]+dp[i-1][j-weight[i-1]])))
print(dp[n][m])
```

