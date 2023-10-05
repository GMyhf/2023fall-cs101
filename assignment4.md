# Assignment #4: 国庆节月考

Updated 1641 GMT+8 Oct 5, 2023



2023 fall, Complied by Hongfei Yan==（请改为同学的姓名、院系）==



**说明：**

1）国庆节⽉考： AC8==（请改为同学的通过数）== 。摸底题⽬都在“练习”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 必做题目

#### 02701: 与7无关的数

math, http://cs101.openjudge.cn/practice/02701

一个正整数,如果它能被7整除,或者它的十进制表示法中某一位上的数字为7,则称其为与7相关的数.现求所有小于等于n(n < 100)的与7无关的正整数的平方和.

**输入**

输入为一行,正整数n(n < 100)

**输出**

输出一行，包含一个整数，即小于等于n的所有与7无关的正整数的平方和。

样例输入

```
21
```

样例输出

```
2336
```

来源

计算概论05





【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==

思路：==（请改为同学的思路和代码）==



##### 代码

```python
# 请改为同学的代码

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





#### 02712: 细菌繁殖 

math, http://cs101.openjudge.cn/practice/02712

一种细菌的繁殖速度是每天成倍增长。例如：第一天有10个，第二天就变成20个，第三天变成40个，第四天变成80个，……。现在给出第一天的日期和细菌数目，要你写程序求出到某一天的时候，细菌的数目。

**输入**

第一行有一个整数n，表示测试数据的数目。其后n行每行有5个整数，整数之间用一个空格隔开。第一个数表示第一天的月份，第二个数表示第一天的日期，第三个数表示第一天细菌的数目，第四个数表示要求的那一天的月份，第五个数表示要求的那一天的日期。已知第一天和要求的一天在同一年并且该年不是闰年，要求的一天一定在第一天之后。数据保证要求的一天的细菌数目在长整数（long）范围内。

**输出**

对于每一组测试数据，输出一行，该行包含一个整数，为要求的一天的细菌数。

样例输入

```
2
1 1 1 1 2
2 28 10 3 2
```

样例输出

```
2
40
```

来源

2005~2006医学部计算概论期末考试





【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==

思路：==（请改为同学的思路和代码）==



##### 代码

```python
# 请改为同学的代码

```



代码运行截图 ==（请替换为同学的AC代码截图，至少包含有"Accepted"的截图）==





#### 02753: 菲波那契数列

math, http://cs101.openjudge.cn/practice/02753

菲波那契数列是指这样的数列: 数列的第一个和第二个数都为1，接下来每个数都等于前面2个数之和。
给出一个正整数a，要求菲波那契数列中第a个数是多少。
**输入**
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数a(1 <= a <= 20)
**输出**
输出有n行，每行输出对应一个输入。输出应是一个正整数，为菲波那契数列中第a个数的大小
样例输入

```
4
5
2
19
1
```

样例输出

```
5
1
4181
1
```





【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==

思路：==（请改为同学的思路和代码）==



##### 代码

```python
# 请改为同学的代码

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





#### 02810: 完美立方

bruteforce, http://cs101.openjudge.cn/practice/02810

形如$a^3= b^3 + c^3 + d^3$的等式被称为完美立方等式。例如$12^3= 6^3 + 8^3 + 10^3$ 。编写一个程序，对任给的正整数N (N ≤ 100)，寻找所有的四元组 (a, b, c, d)，使得 $a^3 = b^3 + c^3 + d^3$，其中 a,b,c,d 大于 1, 小于等于N，且 b ≤ c ≤ d。

**输入**

一个正整数N (N≤100)。

**输出**

每行输出一个完美立方。输出格式为：
Cube = a, Triple = (b,c,d)
其中a,b,c,d所在位置分别用实际求出四元组值代入。

请按照a的值，从小到大依次输出。当两个完美立方等式中a的值相同，则b值小的优先输出、仍相同则c值小的优先输出、再相同则d值小的先输出。

样例输入

```
24
```

样例输出

```
Cube = 6, Triple = (3,4,5)
Cube = 12, Triple = (6,8,10)
Cube = 18, Triple = (2,12,16)
Cube = 18, Triple = (9,12,15)
Cube = 19, Triple = (3,10,18)
Cube = 20, Triple = (7,14,17)
Cube = 24, Triple = (12,16,20)
```





【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==

思路：==（请改为同学的思路和代码）==



##### 代码

```python
# 请改为同学的代码

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





#### 04138: 质数的和与积

math, http://cs101.openjudge.cn/practice/04138

两个质数的和是S，它们的积最大是多少？

**输入**

一个不大于10000的正整数S，为两个质数的和。

**输出**

一个整数，为两个质数的最大乘积。数据保证有解。

样例输入

```
50
```

样例输出

```
589
```

来源

《奥数典型题举一反三（小学五年级）》 (ISBN 978-7-5445-2882-5) 第三章 第二讲 例1





【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==

思路：==（请改为同学的思路和代码）==



##### 代码

```python
# 请改为同学的代码

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





#### 04146: 数字方格

math, http://cs101.openjudge.cn/practice/04146

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/2747_1.jpg)
如上图，有3个方格，每个方格里面都有一个整数a1，a2，a3。已知0 <= a1, a2, a3 <= n，而且a1 + a2是2的倍数，a2 + a3是3的倍数， a1 + a2 + a3是5的倍数。你的任务是找到一组a1，a2，a3，使得a1 + a2 + a3最大。

输入

一行，包含一个整数n (0 <= n <= 100)。

输出

一个整数，即a1 + a2 + a3的最大值。

样例输入

```
3
```

样例输出

```
5
```





【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==

思路：==（请改为同学的思路和代码）==



##### 代码

```python
# 请改为同学的代码

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 选做题目

#### 02746: 约瑟夫问题

implementation, http://cs101.openjudge.cn/practice/02746

约瑟夫问题：有ｎ只猴子，按顺时针方向围成一圈选大王（编号从１到ｎ），从第１号开始报数，一直数到ｍ，数到ｍ的猴子退出圈外，剩下的猴子再接着从1开始报数。就这样，直到圈内只剩下一只猴子时，这个猴子就是猴王，编程求输入ｎ，ｍ后，输出最后猴王的编号。

**输入**

每行是用空格分开的两个整数，第一个是 n, 第二个是 m ( 0 < m,n <=300)。最后一行是：

0 0

**输出**

对于每行输入数据（最后一行除外)，输出数据也是一行，即最后猴王的编号

样例输入

```
6 2
12 4
8 3
0 0
```

样例输出

```
5
1
7
```





【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==

思路：==（请改为同学的思路和代码）==



##### 代码

```python
# 请改为同学的代码

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





#### CF1364A: A. XXXXX

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



【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系）==

思路：==（请改为同学的思路和代码）==



##### 代码

```python
# 请改为同学的代码

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 3. 学习总结和收获

如果作业题目简单，有否额外练习题目，比如：OJ“每日选做”中每天推出的3个题目、CF、洛谷等网站题目。





