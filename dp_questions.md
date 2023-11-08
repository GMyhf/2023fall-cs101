# Dynamic Programming

Updated 1022 GMT+8 Nov 8, 2023



2023 fall, Complied by Hongfei Yan



Plan: 从  23421: 小偷背包，找硬币讲起，最大上升子序列，最长公共字串，



## 23421: 小偷背包

dp, http://cs101.openjudge.cn/practice/23421

这是《算法图解》[1]书中第9章动态规划的例子：一个小贼正在一家店里偷商品。

假设一种情况如下：

一个小偷背着一个可装 4 磅东西的背包。商场有三件物品分别为：
价值 3000 美元重 4 磅的音响，价值 2000 美元重 3 磅的笔记本，价值1500 美元重 1 磅的吉他。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231108151147287.png" alt="image-20231108151147287" style="zoom: 50%;" />

问小偷应该怎样选择商品，才能使得偷取的价值最高？





[1]Grokking Algorithms by Aditya Bhargava, published by Manning Publications.   Copyright © 2016 by Manning Publications.
Simplified Chinese-language edition copyright © 2017 by Posts & Telecom Press.

**输入**

第一行是两个整数N和B，空格分隔。N表示物品件数，B表示背包最大承重。
第二行是N个整数，空格分隔。表示各个物品价格。
第三行是N个整数，空格分隔。表示各个物品重量（是与第二行物品对齐的）。

**输出**

输出一个整数。保证在满足背包容量的情况下，偷的价值最高。

样例输入

```
3 4
3000 2000 1500
4 3 1
```

样例输出

```
3500
```





### 基本思路

最简单的算法如下： 尝试各种可能的商品组合， 并找出价值最高的组合。这样可行， 但速度非常慢。 在有3件商品的情况下， 你需要计算8个不同的集合； 有4件商品时， 你需要计算16个集合。 每增加一件商品， 需要计算的集合数都将翻倍！ 这种算法的运行时间为$O(2^n)$， 真的是慢如蜗牛。

答案是使用动态规划！ 下面来看看动态规划算法的工作原理。 动态规划先解决子问题， 再逐步解决大问题。对于背包问题， 你先解决小背包（子背包） 问题， 再逐步解决原来的问题。

这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。每个动态规划算法都从一个网格开始， 背包问题的网格如下。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/empty_grid.png" alt="empty_grid" style="zoom: 25%;" />

The  rows  of  the  grid  are  the  items,  and  the  columns  are  knapsack  weights  from  1  lb  to  4  lb.  You  need  all  of  those  columns because they will help you calculate the values of the sub-knapsacks.

网格的各行为商品， 各列为不同容量（1～4磅） 的背包。 所有这些列你都需要， 因为它们将帮助你计算子背包的价值。

The grid starts out empty. You’re going to fill in each cell of the  grid.  Once  the  grid  is  filled  in,  you’ll  have  your  answer  to  this  problem!  Please  follow  along.  Make  your  own  grid,  and we’ll fill it out together. 

网格最初是空的。 你将填充其中的每个单元格， 网格填满后， 就找到了问题的答案！ 你一定要跟着做。 请你创建网格， 我们一起来填满它。



**THE GUITAR ROW**

I’ll show you the exact formula for calculating this grid later. Let’s do a walkthrough first. Start with the first row.

后面将列出计算这个网格中单元格值的公式。 我们先来一步一步做。 首先来看第一行。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/first_row.png" alt="first_row" style="zoom:25%;" />

This  is  the  guitar  row,  which  means  you’re  trying  to  fit  the  guitar  into  the  knapsack.  At  each  cell,  there’s  a  simple  decision: do you steal the guitar or not? Remember, you’re trying to find the set of items to steal that will give you the most value. 

这是吉他 行， 意味着你将尝试将吉他装入背包。 在每个单元格， 都需要做一个简单的决定： 偷不偷吉他？ 别忘了， 你要找出一个价值最高的商品集合。



该不该偷音响呢？
背包的容量为1磅， 能装下音响吗？ 音响太重了， 装不下！ 由于容量1磅的背包装不下音响， 因此最大价值依然是1500美元。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/cell_2_1.png" alt="cell_2_1" style="zoom:25%;" />

Same  thing  for  the  next  two  cells.  These  knapsacks  have  a  capacity  of  2  lb  and  3  lb.  The  old  max  value  for  both  was  $1,500. 

接下来的两个单元格的情况与此相同。 在这些单元格中， 背包的容量分别为2磅和3磅， 而以前的最大价值为1500美元。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/cell_2_3.png" alt="cell_2_3" style="zoom:25%;" />

The   stereo   still   doesn’t   fit,   so   your   guesses   remain   unchanged.What  if  you  have  a  knapsack  of  capacity  4  lb?  Aha:  the  stereo finally fits! The old max value was \$1,500, but if you put  the  stereo  in  there  instead,  the  value  is  \$3,000!  Let’s  take the stereo.

由于这些背包装不下音响， 因此最大价值保持不变。
背包容量为4磅呢？ 终于能够装下音响了！ 原来的最大价值为1500美元， 但如果在背包中装入音响而不是吉他， 价值将为3000美元！ 因此还是偷音响吧。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/cell_2_4.png" alt="cell_2_4" style="zoom:25%;" />

You   just   updated   your   estimate!   If   you   have   a   4   lb

你更新了最大价值！ 如果背包的容量为4磅， 就能装入价值至少3000美元的商品。 在这个网格中， 你逐步地更新最大价值。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/cell_3_3.png" alt="cell_3_3" style="zoom:25%;" />

对于容量为4磅的背包， 情况很有趣。 这是非常重要的部分。 当前的最大价值为3000美元， 你可不偷音响， 而偷笔记本电脑， 但它只值2000美元。价值没有原来高。 但等一等， 笔记本电脑的重量只有3磅， 背包还有1磅的容量没用！

根据之前计算的最大价值可知， 在1磅的容量中可装入吉他， 价值1500美元。 因此， 你需要做如下比较。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231108161055553.png" alt="image-20231108161055553" style="zoom:33%;" />



你可能始终心存疑惑： 为何计算小背包可装入的商品的最大价值呢？ 但愿你现在明白了其中的原因！ 余下了空间时， 你可根据这些子问题的答案来确定余下的空间可装入哪些商品。 笔记本电脑和吉他的总价值为
3500美元， 因此偷它们是更好的选择。最终的网格类似于下面这样。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/cell_3_4.png" alt="cell_3_4" style="zoom:25%;" />

There’s  the  answer:  the  maximum  value  that  will  fit  in  the  knapsack is $3,500, made up of a guitar and a laptop!Maybe you think that I used a different formula to calculate the  value  of  that  last  cell.  That’s  because  I  skipped  some  unnecessary  complexity  when  filling  in  the  values  of  the  earlier cells. Each cell’s value gets calculated with the same formula. Here it is.

答案如下： 将吉他和笔记本电脑装入背包时价值最高， 为3500美元。你可能认为， 计算最后一个单元格的价值时， 我使用了不同的公式。 那是因为填充之前的单元格时， 我故意避开了一些复杂的因素。 其实， 计算每个单元格的价值时， 使用的公式都相同。 这个公式如下。

![formula](https://raw.githubusercontent.com/GMyhf/img/main/img/formula.png)

用子问题定义状态：即 CELL\[i][j] 表示前 i 件物品恰放入一个容量为 j 的背包可以获得的最大价值。则其状态转移方程便是：

$CELL[i][j] = max(CELL[i−1][j]; V_i + CELL[i−1][j− W_i]$

这个方程非常重要，基本上所有跟背包相关的问题的方程都是由它衍生出来的。所以有必要将它详细解释一下：“将前 i 件物品放入容量为 j 的背包中”这个子问题，若只考虑第 i 件物品的策略（放或不放），那么就可以转化为一个只和前 i − 1 件物品相关的问题。如果不放第 i 件物品，那么问题就转化为“前 i − 1 件物品放入容量为 j 的背包中”，价值为 $CELL[i − 1][j]$；如果放第 i 件物品，那么问题就转化为“前 i − 1 件物品放
入剩下的容量为 $j − W_i$ 的背包中”，此时能获得的最大价值就是 $CELL[i − 1][j − Wi]$ 再加上通过放入第 i 件物品获得的价值 Vi。

You  can  use  this  formula  with  every  cell  in  this  grid,  and  you  should  end  up  with  the  same  grid  I  did.  Remember  how  I  talked  about  solving  subproblems?  You  combined  the  solutions  to  two  subproblems  to  solve  the  bigger  problem.

你可以使用这个公式来计算每个单元格的价值， 最终的网格将与前一个网格相同。 现在你明白了为何要求解子问题吧？ 你可以合并两个子问题的解来得到更大问题的解。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/subproblems_with_items.png" alt="subproblems_with_items" style="zoom:25%;" />

```python
# 动态规划之背包问题（算法图解书中例子实现）

#第一步建立网格(横坐标表示[0,c]整数背包承重):(n+1)*(c+1)
def knapsack(n, c, w, p):
    cell = [[0 for j in range(c+1)]for i in range(n+1)]
    for j in range(c+1):
        #第0行全部赋值为0，物品编号从1开始.为了下面赋值方便
        cell[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, c+1):
            #生成了n*c有效矩阵，以下公式w[i-1],p[i-1]代表从第一个元素w[0],p[0]开始取。
            if j >= w[i-1]:
                cell[i][j] = max(cell[i-1][j], p[i-1] + cell[i-1][j - w[i-1]])
            else:
                cell[i][j] = cell[i-1][j]
    return cell


goodsnum, bagsize = map(int, input().split())
#goodsnum, bagsize = 3, 4
*value, = map(int, input().split())
*weight, = map(int, input().split())
#value, weight = [1500, 3000, 2000], [1, 4, 3]  # guitar, stereo, laptop

cell = knapsack(goodsnum, bagsize, weight, value)
print(cell[goodsnum][bagsize])
```





```python
n,b=map(int, input().split())
price=[0]+[int(i) for i in input().split()]
weight=[0]+[int(i) for i in input().split()]
bag=[[0]*(b+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        if weight[i]<=j:
            bag[i][j]=max(price[i]+bag[i-1][j-weight[i]], bag[i-1][j])
        else:
            bag[i][j]=bag[i-1][j]
print(bag[-1][-1])
```



### 优化空间复杂度

以上方法的时间和空间复杂度均为 $O(B N)$，其中时间复杂度应该已经不能再优化了，但空间复杂度却可以优化到 O(B)。
先考虑上面讲的基本思路如何实现，肯定是有一个主循环 $i \larr 1...N$，每次算出来二维数组 $CELL[i;0...B]$ 的所有值。那么，如果只用一个数组 $CELL[0...B]$，能不能保证第 i次循环结束后 $F [B]$ 中表示的就是我们定义的状态 $CELL[i; B]$ 呢？ $CELL[i; B]$ 是由 $CELL[i−1; B]$ 和
$CELL[i − 1; B − W_i]$ 两个子问题递推而来，能否保证在推 $CELL[i; B]$ 时（也即在第 i 次主循环中
推 $CELL[B]$ 时）能够取用 $CELL[i − 1; B]$ 和 $CELL[i−1; B − W_i]$ 的值呢？事实上，这要求在每次主循环中我们以 $B...0$ 的递减顺序计算 $CELLF[B]$，这样才能保证计算 $CELL[B]$ 时 $CELL[B − W_i]$ 保存的是状态 $CELL[i − 1; B − W_i]$ 的值。

```python
# 压缩矩阵/滚动数组 方法
N,B = map(int, input().split())
*p, = map(int, input().split())
*w, = map(int, input().split())

dp=[0]*(B+1)
for i in range(N):
    for j in range(B, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j-w[i]]+p[i])
            
print(dp[-1])
```





## Top 20 Dynamic Programming Interview Questions

https://www.geeksforgeeks.org/top-20-dynamic-programming-interview-questions/

**Following are the most important Dynamic Programming problems.**

1. [Longest Common Subsequence](https://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/)
2. [Longest Increasing Subsequence](https://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)
3. [Edit Distance](https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/)
4. [Minimum Partition](https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/)
5. [Ways to Cover a Distance](https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/)
6. [Longest Path In Matrix](https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/)
7. [Subset Sum Problem](https://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/)
8. [Optimal Strategy for a Game](https://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/)
9. [0-1 Knapsack Problem](https://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/)
10. [Boolean Parenthesization Problem](https://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/)
11. [Shortest Common Supersequence](https://www.geeksforgeeks.org/shortest-common-supersequence/)
12. [Matrix Chain Multiplication](https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/)
13. [Partition problem](https://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/)
14. [Rod Cutting](https://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/)
15. [Coin change problem](https://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/)
16. [Word Break Problem](https://www.geeksforgeeks.org/dynamic-programming-set-32-word-break-problem/)
17. [Maximal Product when Cutting Rope](https://www.geeksforgeeks.org/dynamic-programming-set-36-cut-a-rope-to-maximize-product/)
18. [Dice Throw Problem](https://www.geeksforgeeks.org/dice-throw-problem/)
19. [Box Stacking](https://www.geeksforgeeks.org/dynamic-programming-set-21-box-stacking-problem/)
20. [Egg Dropping Puzzle](https://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/)

Last Updated : 22 Jun, 2022



## 0/1 Knapsack Problem

https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

**Prerequisites:** [Introduction to Knapsack Problem, its Types and How to solve them](https://www.geeksforgeeks.org/introduction-to-knapsack-problem-its-types-and-how-to-solve-them/)

Given **N** items where each item has some weight and profit associated with it and also given a bag with capacity **W**, [i.e., the bag can hold at most **W** weight in it]. The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 

**Note:** The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag].

**Examples:**

> ***Input:*** N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
> ***Output:*** 3
> ***Explanation:*** There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.
>
> ***Input:*** N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
> ***Output:*** 0



## Problems:

### OJ23421: ⼩偷背包

dp, http://cs101.openjudge.cn/practice/23421

### OJ02773: 采药

dp, http://cs101.openjudge.cn/practice/02773



### OJ2757: 最⻓上升⼦序列

dp, http://cs101.openjudge.cn/practice/02757

### OJ02806:公共子序列

http://cs101.openjudge.cn/practice/02806/

### OJ02711/1713:合唱队形

http://cs101.openjudge.cn/practice/02711/





选自《挑战程序设计竞赛》第2版 Page 135

### OJ2229: Sumsets				

http://cs101.openjudge.cn/routine/02229/

### 2385:Apple Catching			

http://bailian.openjudge.cn/practice/2385/

### 1742: Coins					

http://bailian.openjudge.cn/practice/1742/



9267: 核电站

http://bailian.openjudge.cn/tm2023cis/D/



## References:

https://www.geeksforgeeks.org/top-20-dynamic-programming-interview-questions/

https://www.geeksforgeeks.org/top-50-dynamic-programming-coding-problems-for-interviews/

Introduction to Knapsack Problem, its Types and How to solve them

https://www.geeksforgeeks.org/introduction-to-knapsack-problem-its-types-and-how-to-solve-them/



