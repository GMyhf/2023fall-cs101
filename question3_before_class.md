# 计算概论(B) 课前问题3

Updated 1020 GMT+8 Aug 30, 2023



2023 fall, Complied by Hongfei Yan

Markdown（用 https://typoraio.cn 编辑）格式文件在，https://github.com/GMyhf/2023fall-cs101



| 课程号: 04831410		课程名: 计算概论(B)                  | 班号: 12                                              |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| 上课时间: 1-16周 每周 周二 7-9节                             | 地点: 理教208                                         |
| 上机时间: 1-15周 每周 周四 7-8节<br/>期末机考时间: 第16周 周四 7-8节 | 地点：理科1号楼计算中心，二层楼的6号和三层楼的7号机房 |
| 助教：张哲瑞、张以宁、彭亦男、涂程颖、陈威宇                 | 在课程微信群中的名字是“TA-”开始，地点：理科1号楼1220  |



## Q: Print all prime numbers less than or equal to N

Given a number N, the task is to print all prime numbers less than or equal to N.
**Examples:** 

```
Input: 7
Output: 2, 3, 5, 7

Input: 13
Output: 2, 3, 5, 7, 11, 13 
```



请分别给出Python, C++（选做）, C（选做）实现的代码，填写到下面作业模版中。



## Answer:

【张概论，中国语言文学系，2023年秋】 ==（请改为同学的姓名、院系、操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



思路：==（请改为同学的思路和代码）==

将⼀个数分成两个偶数。

参考了 https://www.geeksforgeeks.org/print-all-prime-numbers-less-than-or-equal-to-n/



### Python3 代码

```python
w = int(input())
if 3<=w<=100 and (w-2) % 2 == 0:
print('YES')
else:
print('NO')
```



Python代码运行截图 ==（请改为同学的截图）==

![image-20230830110535562](https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230830110535562.png)



### C++ 代码

```c++

```



C++ 代码运行截图



### C 代码

```c

```



C 代码运行截图





## 学习总结和收获

待书写
