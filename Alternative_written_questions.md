# 备选笔试题目

Updated 1501 GMT+8 Feb 2, 2024

2024 spring, Complied by Hongfei Yan



（5分）请优化下面程序。

```python
V = [int(i) for i in input().split()]
preV = [0]*(len(V)+1)
for i in range(len(V)):
    preV[i+1] = preV[i] ^ V[i]
for i in range(10000):
    L, R = map(int, input().split())
    print(preV[R+1] ^ preV[L])
```

A:

i/o优化，1w输入输出

```python
# 23n2300017735(夏天明BrightSummer)
import sys
input = sys.stdin.readline

V = [int(i) for i in input().split()]
preV = [0]*(len(V)+1)
for i in range(len(V)):
    preV[i+1] = preV[i] ^ V[i]

results = []
for i in range(10000):
    L, R = map(int, input().split())
    results.append(str(preV[R+1] ^ preV[L]))

sys.stdout.write('\n'.join(results) + '\n')
```





（5分）如何修正openjudge的pylint报错？

状态：Compile Error
编译错误信息：Value dir' is unsubscriptable(unsubscriptable-object)

```python
s = input()
dir = (0, 1)
x, y = 0, 0

for i in range(4):
    for t in s:
        if t == 'G':
            x, y = x + dir[0], y + dir[1]
        elif t == 'L':
            dir = (-dir[1], dir[0])
        else:
            dir = (dir[1], -dir[0])

if x == 0 and y == 0:
    print(1)
else:
    print(0)
```

A: dir是内置函数。可以改为 direction = (0, 1)



（5分）这个函数为什么可能Runtime Error？

```python
def expProcessor(fpexp):
    temp = re.findall('[0-9.a-zA-Z]+|[**]+|[//]+|[+\-*/()]?|[not]?|[and]?|[or]?|[True]?|[False]?|.',\
    fpexp)
    fplist = [i for i in temp if i not in ["", " "]]
    i = 1
    while True:
        if (fplist[i] == "-") and (fplist[i-1] in ["(","+","-","*","/","**","//","not","and","or"]):
            fplist[i+1] = "-"+fplist[i+1]
            fplist.pop(i)
        else:
            i += 1
            if i >= len(fplist)-1:
                break
    return fplist
```

A: i可能越界。修正如下：

```python
def expProcessor(fpexp):
    temp = re.findall('[0-9.a-zA-Z]+|[**]+|[//]+|[+\-*/()]?|[not]?|[and]?|[or]?|[True]?|[False]?|.',\
    fpexp)
    fplist = [i for i in temp if i not in ["", " "]]

    i = 1
    while i < len(fplist):
        if (fplist[i] == "-") and (fplist[i - 1] in ["(", "+", "-", "*", "/", "**", "//", "not", "and", "or"]):
            fplist[i + 1] = "-" + fplist[i + 1]
            fplist.pop(i)
        else:
            i += 1

    return fplist
```

（5分）证明哈夫曼编码的正确性。

Page 433, Introduction to Algorithm-3rd



（5分）中缀表达式转换为后缀表达式的算法？

A:

Shunting Yard 算法是一种用于将中缀表达式转换为后缀表达式的算法。它由荷兰计算机科学家 Edsger Dijkstra 在1960年代提出，用于解析和计算数学表达式。

Shunting Yard 算法的主要思想是使用两个栈（运算符栈和输出栈）来处理表达式的符号。算法按照运算符的优先级和结合性，将符号逐个处理并放置到正确的位置。最终，输出栈中的元素就是转换后的后缀表达式。

以下是 Shunting Yard 算法的基本步骤：

1. 初始化运算符栈和输出栈为空。
2. 从左到右遍历中缀表达式的每个符号。
   - 如果是操作数（数字），则将其添加到输出栈。
   - 如果是左括号，则将其推入运算符栈。
   - 如果是运算符：
     - 如果运算符的优先级大于运算符栈顶的运算符，或者运算符栈顶是左括号，则将当前运算符推入运算符栈。
     - 否则，将运算符栈顶的运算符弹出并添加到输出栈中，直到满足上述条件（或者运算符栈为空）。
     - 将当前运算符推入运算符栈。
   - 如果是右括号，则将运算符栈顶的运算符弹出并添加到输出栈中，直到遇到左括号。将左括号弹出但不添加到输出栈中。
3. 如果还有剩余的运算符在运算符栈中，将它们依次弹出并添加到输出栈中。
4. 输出栈中的元素就是转换后的后缀表达式。

（5分）