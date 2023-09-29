# Dynamic Programming

Updated 0758 GMT+8 Sep 29, 2023



2023 fall, Complied by Hongfei Yan







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



