# 20231128-Week12 搜索专题

Updated 2356 GMT+8 Nov 26 2023

2020 fall, Complied by Hongfei Yan



《算法笔记》第8章

## 1 深度优先搜索(DFS)

设想我们现在以第一视角身处一个巨大的迷宫当中，没有上帝视角，没有通信设施，更没有热血动漫里的奇迹，有的只是四周长得一样的墙壁。于是，我们只能自己想办法走出去。如果迷失了内心，随便乱走，那么很可能被四周完全相同的景色绕晕在其中，这时只能放弃所谓的侥幸，而去采取下面这种看上去很盲目但实际上会很有效的方法。

以当前所在位置为起点，沿着一条路向前走，当碰到岔道口时，选择其中一个岔路前进如果选择的这个岔路前方是一条死路，就退回到这个岔道口，选择另一个岔路前进。如果岔路中存在新的岔道口，那么仍然按上面的方法枚举新岔道口的每一条岔路。这样，只要迷宫存在出口，那么这个方法一定能够找到它。可能有读者会问，如果在第一个岔道口处选择了一条没有出路的分支，而这个分支比较深，并且路上多次出现新的岔道口，那么当发现这个分支是个死分支之后，如何退回到最初的这个岔道口?其实方法很简单，只要让右手始终贴着右边的墙壁一路往前走，那么自动会执行上面这个走法，并且最终一定能找到出口。图 8-1 即为使用这个方法走一个简单迷宫的示例。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231126163735204.png" alt="image-20231126163735204" style="zoom:50%;" />



从图 8-1 可知，从起点开始前进，当碰到岔道口时，总是选择其中一条岔路前进(例如图中总是先选择最右手边的岔路)，在岔路上如果又遇到新的岔道口，仍然选择新岔道口的其中一条岔路前进，直到碰到死胡同才回退到最近的岔道口选择另一条岔路。也就是说，当碰到岔道口时，总是以“**深度**”作为前进的关键词，不碰到死胡同就不回头，因此把这种搜索的方式称为**深度优先搜索**(Depth First Search，**DFS**)。
从迷宫的例子还应该注意到，深度优先搜索会走遍所有路径，并且每次走到死胡同就代表一条完整路径的形成。这就是说，**深度优先搜索是一种枚举所有完整路径以遍历所有情况的搜索方法**。



深度优先搜索 (DFS)可以使用栈来实现。但是实现起来却并不轻松，有没有既容易理解又容易实现的方法呢?有的——递归。现在从 DFS 的角度来看当初求解 Fibonacci 数列的过程。
回顾一下 Fibonacci数列的定义: $F(0)=1,F(1)=1,F(n)=F(n-1)+F(n-2)(n≥2)$。可以从这个定义中挖掘到，每当将 F(n)分为两部分 F(n-1)与 F(n-2)时，就可以把 F(n)看作迷宫的岔道口，由它可以到达两个新的关键结点 F(n-1)与 F(n-2)。而之后计算 F(n-1)时，又可以把 F(n-1)当作在岔道口 F(n)之下的岔道口。
既然有岔道口，那么一定有死胡同。很容易想象，当访问到 F(0)和 F(1)时，就无法再向下递归下去，因此 F(0)和 F(1)就是死胡同。这样说来，==递归中的递归式就是岔道口，而递归边界就是死胡同==，这样就可以把如何用递归实现深度优先搜索的过程理解得很清楚。为了使上面的过程更清晰，可以直接来分析递归图 (见图 4-3)：可以在递归图中看到，只要n > 1，F(n)就有两个分支，即把 F(n)当作岔道口；而当n为1或0时，F(1)与F(0)就是迷宫的死胡同，在此处程序就需要返回结果。这样当遍历完所有路径（从顶端的 F(4)到底层的所有 F(1)与 F(0)）后，就可以得到 F(4)的值。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20231126164549437.png" alt="image-20231126164549437" style="zoom: 50%;" />

因此，使用递归可以很好地实现深度优先搜索。这个说法并不是说深度优先搜索就是递归，只能说递归是深度优先搜索的一种实现方式，因为使用非递归也是可以实现 DFS 的思想的，但是一般情况下会比递归麻烦。不过，使用递归时，系统会调用一个叫系统栈的东西来存放递归中每一层的状态，因此使用递归来实现 DFS 的本质其实还是栈。



### 1.1 迷宫可行路径数

https://sunnywhy.com/sfbj/8/1/313

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置），且只能移动到平地上。求从迷宫左上角到右下角的所有可行路径的条数。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le5, 2 \le m \le 5)$，分别表示迷宫的行数和列数；

接下来 n 行，每行 m 个整数（值为`0`或`1`），表示迷宫。

**输出**

一个整数，表示可行路径的条数。

样例1

输入

```
3 3
0 0 0
0 1 0
0 0 0
```

输出

```
2
```

解释

假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角有两条路径：

1. (1,1)=>(1,2)=>(1,3)=>(2,3)=>(3,3)
2. (1,1)=>(2,1)=>(3,1)=>(3,2)=>(3,3)



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

def dfs(maze, x, y):
    global cnt
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
            
        if maze[nx][ny] == 'e':
            cnt += 1
            continue
            
        if maze[nx][ny] == 0:
            maze[x][y] = 1
            dfs(maze, nx, ny)
            maze[x][y] = 0
    
    return
            
n, m = map(int, input().split())
maze = []
maze.append( [-1 for x in range(m+2)] )
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] )

maze[1][1] = 's'
maze[n][m] = 'e'

cnt = 0
dfs(maze, 1, 1)
print(cnt)
```



#### 辅助visited空间

```python
# gpt translated version of the C++ code
MAXN = 5
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
counter = 0

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]

def DFS(x, y):
    global counter
    if x == n - 1 and y == m - 1:
        counter += 1
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if is_valid(nextX, nextY):
            DFS(nextX, nextY)
    visited[x][y] = False

DFS(0, 0)
print(counter)

```



#### C++

```c++
#include <cstdio>

const int MAXN = 5;
int n, m, maze[MAXN][MAXN];
bool visited[MAXN][MAXN] = {false};
int counter = 0;

const int MAXD = 4;
int dx[MAXD] = {0, 0, 1, -1};
int dy[MAXD] = {1, -1, 0, 0};

bool isValid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && maze[x][y] == 0 && !visited[x][y];
}

void DFS(int x, int y) {
    if (x == n - 1 && y == m - 1) {
        counter++;
        return;
    }
    visited[x][y] = true;
    for (int i = 0; i < MAXD; i++) {
        int nextX = x + dx[i];
        int nextY = y + dy[i];
        if (isValid(nextX, nextY)) {
            DFS(nextX, nextY);
        }
    }
    visited[x][y] = false;
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maze[i][j]);
        }
    }
    DFS(0, 0);
    printf("%d", counter);
    return 0;
}
```



### 1.2 指定步数的迷宫问题

https://sunnywhy.com/sfbj/8/1/314

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置），且只能移动到平地上。现从迷宫左上角出发，问能否在恰好第步时到达右下角。

**输入**

第一行三个整数$n、m、k \hspace{1em} (2 \le n \le5, 2 \le m \le 5, 2 \le k \le n*m)$，分别表示迷宫的行数、列数、移动的步数；

接下来行，每行个整数（值为`0`或`1`），表示迷宫。

**输出**

如果可行，那么输出`Yes`，否则输出`No`。

样例1

输入

```
3 3 4
0 1 0
0 0 0
0 1 0
```

输出

```
Yes
```

解释

假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的步数为`4`的路径为：(1,1)=>(2,1)=>(2,2)=>(2,3)=>(3,3)。

样例2

输入

```
3 3 6
0 1 0
0 0 0
0 1 0
```

输出

```
No
```

解释

由于不能移动到曾经经过的位置，因此无法在恰好第`6`步时到达右下角。



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

canReach = False
def dfs(maze, x, y, step):
    global canReach
    if canReach:
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] == 'e':
            if step==k-1:
                canReach = True
            
            return
            
        if maze[nx][ny] == 0:
            if step < k:
                maze[x][y] = -1
                dfs(maze, nx, ny, step+1)
                maze[x][y] = 0
    

n, m, k = map(int, input().split())
maze = []
maze.append( [-1 for x in range(m+2)] )
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] )

maze[1][1] = 's'
maze[n][m] = 'e'

dfs(maze, 1, 1, 0)
print("Yes" if canReach else "No")
```



#### 辅助visited空间

```python
# gpt translated version of the C++ code
MAXN = 5
n, m, k = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
canReach = False

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not visited[x][y]

def DFS(x, y, step):
    global canReach
    if canReach:
        return
    if x == n - 1 and y == m - 1:
        if step == k:
            canReach = True
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if step < k and is_valid(nextX, nextY):
            DFS(nextX, nextY, step + 1)
    visited[x][y] = False

DFS(0, 0, 0)
print("Yes" if canReach else "No")

```



#### C++

```c++
#include <cstdio>

const int MAXN = 5;
int n, m, k, maze[MAXN][MAXN];
bool visited[MAXN][MAXN] = {false};
bool canReach = false;

const int MAXD = 4;
int dx[MAXD] = {0, 0, 1, -1};
int dy[MAXD] = {1, -1, 0, 0};

bool isValid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && maze[x][y] == 0 && !visited[x][y];
}

void DFS(int x, int y, int step) {
    if (canReach) {
        return;
    }
    if (x == n - 1 && y == m - 1) {
        if (step == k) {
            canReach = true;
        }
        return;
    }
    visited[x][y] = true;
    for (int i = 0; i < MAXD; i++) {
        int nextX = x + dx[i];
        int nextY = y + dy[i];
        if (step < k && isValid(nextX, nextY)) {
            DFS(nextX, nextY, step + 1);
        }
    }
    visited[x][y] = false;
}

int main() {
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maze[i][j]);
        }
    }
    DFS(0, 0, 0);
    printf(canReach ? "Yes" : "No");
    return 0;
}
```



### 1.3 矩阵最大权值

https://sunnywhy.com/sfbj/8/1/315

现有一个 n*m 大小的矩阵，矩阵中的每个元素表示该位置的权值。现需要从矩阵左上角出发到达右下角，每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置）。求最后到达右下角时路径上所有位置的权值之和的最大值。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le5, 2 \le m \le 5)$，分别表示矩阵的行数和列数；

接下来 n 行，每行 m 个整数（$-100 \le 整数 \le 100$），表示矩阵每个位置的权值。

**输出**

一个整数，表示权值之和的最大值。

样例1

输入

```
2 2
1 2
3 4
```

输出

```
8
```

解释

从左上角到右下角的最大权值之和为。



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

maxValue = float("-inf")
def dfs(maze, x, y, nowValue):
    global maxValue
    if x==n and y==m:
        if nowValue > maxValue:
            maxValue = nowValue
        
        return
  
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
  
        if maze[nx][ny] != -9999:
            tmp = maze[x][y]
            maze[x][y] = -9999
            nextValue = nowValue + maze[nx][ny]
            dfs(maze, nx, ny, nextValue)
            maze[x][y] = tmp
    

n, m = map(int, input().split())
maze = []
maze.append( [-9999 for x in range(m+2)] )
for _ in range(n):
    maze.append([-9999] + [int(_) for _ in input().split()] + [-9999])
maze.append( [-9999 for x in range(m+2)] )


dfs(maze, 1, 1, maze[1][1])
print(maxValue)
```



#### 辅助visited空间

```python
# gpt translated version of the C++ code
MAXN = 5
INF = float('inf')
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
maxValue = -INF

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def DFS(x, y, nowValue):
    global maxValue
    if x == n - 1 and y == m - 1:
        if nowValue > maxValue:
            maxValue = nowValue
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if is_valid(nextX, nextY):
            nextValue = nowValue + maze[nextX][nextY]
            DFS(nextX, nextY, nextValue)
    visited[x][y] = False

DFS(0, 0, maze[0][0])
print(maxValue)

```



#### C++

```c++
#include <cstdio>

const int MAXN = 5;
const int INF = 0x3f;
int n, m, maze[MAXN][MAXN];
bool visited[MAXN][MAXN] = {false};
int maxValue = -INF;

const int MAXD = 4;
int dx[MAXD] = {0, 0, 1, -1};
int dy[MAXD] = {1, -1, 0, 0};

bool isValid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && !visited[x][y];
}

void DFS(int x, int y, int nowValue) {
    if (x == n - 1 && y == m - 1) {
        if (nowValue > maxValue) {
            maxValue = nowValue;
        }
        return;
    }
    visited[x][y] = true;
    for (int i = 0; i < MAXD; i++) {
        int nextX = x + dx[i];
        int nextY = y + dy[i];
        if (isValid(nextX, nextY)) {
            int nextValue = nowValue + maze[nextX][nextY];
            DFS(nextX, nextY, nextValue);
        }
    }
    visited[x][y] = false;
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maze[i][j]);
        }
    }
    DFS(0, 0, maze[0][0]);
    printf("%d", maxValue);
    return 0;
}
```



### 1.4 矩阵最大权值路径

https://sunnywhy.com/sfbj/8/1/316

现有一个 n*m 大小的矩阵，矩阵中的每个元素表示该位置的权值。现需要从矩阵左上角出发到达右下角，每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置）。假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。求最后到达右下角时路径上所有位置的权值之和最大的路径。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le5, 2 \le m \le 5)$，分别表示矩阵的行数和列数；

接下来 n 行，每行 m 个整数（$-100 \le 整数 \le 100$），表示矩阵每个位置的权值。

**输出**

从左上角的坐标开始，输出若干行（每行两个整数，表示一个坐标），直到右下角的坐标。

数据保证权值之和最大的路径存在且唯一。

样例1

输入

```
2 2
1 2
3 4
```

输出

```
1 1
2 1
2 2
```

解释

显然当路径是(1,1)=>(2,1)=>(2,2)时，权值之和最大，即 1+3+4 = 8。



#### 辅助visited空间

```python
# gpt translated version of the C++ code
MAXN = 5
INF = float('inf')
n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
maxValue = -INF
tempPath, optPath = [], []

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def DFS(x, y, nowValue):
    global maxValue, tempPath, optPath
    if x == n - 1 and y == m - 1:
        if nowValue > maxValue:
            maxValue = nowValue
            optPath = list(tempPath)
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if is_valid(nextX, nextY):
            nextValue = nowValue + maze[nextX][nextY]
            tempPath.append((nextX, nextY))
            DFS(nextX, nextY, nextValue)
            tempPath.pop()
    visited[x][y] = False

tempPath.append((0, 0))
DFS(0, 0, maze[0][0])
for pos in optPath:
    print(pos[0] + 1, pos[1] + 1)
```



#### C++

```c++
#include <cstdio>
#include <vector>
#include <utility>
using namespace std;

typedef pair<int, int> Position;

const int MAXN = 5;
const int INF = 0x3f;
int n, m, maze[MAXN][MAXN];
bool visited[MAXN][MAXN] = {false};
int maxValue = -INF;
vector<Position> tempPath, optPath;

const int MAXD = 4;
int dx[MAXD] = {0, 0, 1, -1};
int dy[MAXD] = {1, -1, 0, 0};

bool isValid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && !visited[x][y];
}

void DFS(int x, int y, int nowValue) {
    if (x == n - 1 && y == m - 1) {
        if (nowValue > maxValue) {
            maxValue = nowValue;
            optPath = tempPath;
        }
        return;
    }
    visited[x][y] = true;
    for (int i = 0; i < MAXD; i++) {
        int nextX = x + dx[i];
        int nextY = y + dy[i];
        if (isValid(nextX, nextY)) {
            int nextValue = nowValue + maze[nextX][nextY];
            tempPath.push_back(Position(nextX, nextY));
            DFS(nextX, nextY, nextValue);
            tempPath.pop_back();
        }
    }
    visited[x][y] = false;
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maze[i][j]);
        }
    }
    tempPath.push_back(Position(0, 0));
    DFS(0, 0, maze[0][0]);
    for (int i = 0; i < optPath.size(); i++) {
        printf("%d %d\n", optPath[i].first + 1, optPath[i].second + 1);
    }
    return 0;
}
```



### 1.5 迷宫最大权值

https://sunnywhy.com/sfbj/8/1/317

题目描述

现有一个大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。现需要从迷宫左上角出发到达右下角，每次移动只能向上下左右移动一格（不允许移动到曾经经过的位置），且只能移动到平地上。假设迷宫中每个位置都有权值，求最后到达右下角时路径上所有位置的权值之和的最大值。

**输入**

第一行两个整数$n、m \hspace{1em} (2 \le n \le5, 2 \le m \le 5)$，分别表示矩阵的行数和列数；

接下来 n 行，每行个 m 整数（值为`0`或`1`），表示迷宫。

再接下来行，每行个整数（$-100 \le 整数 \le 100$），表示迷宫每个位置的权值。

**输出**

一个整数，表示权值之和的最大值。

样例1

输入

```
3 3
0 0 0
0 1 0
0 0 0
1 2 3
4 5 6
7 8 9
```

输出

```
29
```

解释：从左上角到右下角的最大权值之和为 1+4+7+8+9 = 29。



#### 加保护圈，原地修改

```python
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]

maxValue = float("-inf")
def dfs(maze, x, y, nowValue):
    global maxValue
    if x==n and y==m:
        if nowValue > maxValue:
            maxValue = nowValue
        
        return
  
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
  
        if maze[nx][ny] == 0:
            maze[nx][ny] = -1
            tmp = w[x][y]
            w[x][y] = -9999
            nextValue = nowValue + w[nx][ny]
            dfs(maze, nx, ny, nextValue)
            maze[nx][ny] = 0
            w[x][y] = tmp
    

n, m = map(int, input().split())
maze = []
maze.append( [-1 for x in range(m+2)] )
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append( [-1 for x in range(m+2)] )

w = []
w.append( [-9999 for x in range(m+2)] )
for _ in range(n):
    w.append([-9999] + [int(_) for _ in input().split()] + [-9999])
w.append( [-9999 for x in range(m+2)] )


dfs(maze, 1, 1, w[1][1])
print(maxValue)
```



#### 辅助visited空间

```python
# gpt translated version of the C++ code
MAXN = 5
INF = float('inf')
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
w = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
maxValue = -INF

MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and not maze[x][y] and not visited[x][y]

def dfs(x, y, nowValue):
    global maxValue
    if x == n - 1 and y == m - 1:
        if nowValue > maxValue:
            maxValue = nowValue
        return
    visited[x][y] = True
    for i in range(MAXD):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if is_valid(nextX, nextY):
            nextValue = nowValue + w[nextX][nextY]
            dfs(nextX, nextY, nextValue)
    visited[x][y] = False

dfs(0, 0, w[0][0])
print(maxValue)

```



#### C++

```c++
#include <cstdio>

const int MAXN = 5;
const int INF = 0x3f;
int n, m, maze[MAXN][MAXN], isWall[MAXN][MAXN];
bool visited[MAXN][MAXN] = {false};
int maxValue = -INF;

const int MAXD = 4;
int dx[MAXD] = {0, 0, 1, -1};
int dy[MAXD] = {1, -1, 0, 0};

bool isValid(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && !isWall[x][y] && !visited[x][y];
}

void DFS(int x, int y, int nowValue) {
    if (x == n - 1 && y == m - 1) {
        if (nowValue > maxValue) {
            maxValue = nowValue;
        }
        return;
    }
    visited[x][y] = true;
    for (int i = 0; i < MAXD; i++) {
        int nextX = x + dx[i];
        int nextY = y + dy[i];
        if (isValid(nextX, nextY)) {
            int nextValue = nowValue + maze[nextX][nextY];
            DFS(nextX, nextY, nextValue);
        }
    }
    visited[x][y] = false;
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &isWall[i][j]);
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maze[i][j]);
        }
    }
    DFS(0, 0, maze[0][0]);
    printf("%d", maxValue);
    return 0;
}
```





## 2 广度优先搜索(DFS)

前面介绍了深度优先搜索，可知 DFS 是以深度作为第一关键词的，即当碰到岔道口时总是先选择其中的一条岔路前进,而不管其他岔路,直到碰到死胡同时才返回岔道口并选择其他岔路。接下来将介绍的**广度优先搜索** (Breadth FirstSearch,**BFS**)则是以广度为第一关键词，当碰到岔道口时,总是先依次访问从该岔道口能直接到达的所有结点,然后再按这些结点被访问的顺序去依次访问它们能直接到达的所有结点，以此类推,直到所有结点都被访问为止。这就跟平静的水面中投入一颗小石子一样,水花总是以石子落水处为中心,并以同心圆的方式向外扩散至整个水面(见图 8-2),从这点来看和 DFS 那种沿着一条线前进的思路是完全不同的。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/202311262216546.png" alt="image-20231126221551540" style="zoom:50%;" />

广度优先搜索 (BFS)一般由队列实现,且总是按层次的顺序进行遍历，其基本写法如下(可作模板用):

```c++
void BFS(int s) {
    queue<int> q;
    q.push(s);
    while(!q.empty()) {
        取出队首元素 top;
        访问队首元素 top;
      	将队首元素出队;
        将 top 的下一层结点中未曾入队的结点全部入队，并设置为已入队;
    }
}
```



下面是对该模板中每一个步骤的说明,请结合代码一起看: 

① 定义队列 q，并将起点s入队。
② 写一个 while 循环，循环条件是队列q非空。
③ 在 while 循环中，先取出队首元素 top，然后访问它（访问可以是任何事情，例如将其输出）。访问完后将其出队。
④ 将top 的下一层结点中所有**未曾入队**的结点入队，并标记它们的层号为 now 的层号加1，同时设置这些入队的结点已入过队。
 ⑤ 返回 ② 继续循环。



再强调一点,在BFS 中设置的 inq 数组的含义是判断结点是否已入过队，而不是**结点是否已被访问**。区别在于:如果设置成是否已被访问，有可能在某个结点正在队列中(但还未访问)时由于其他结点可以到达它而将这个结点再次入队，导致很多结点反复入队，计算量大大增加。因此BFS 中让每个结点只入队一次，故需要设置 inq 数组的含义为**结点是否已入过队**而非结点是否已被访问。



### 2.1 数字操作

https://sunnywhy.com/sfbj/8/2/318

从整数`1`开始，每轮操作可以选择将上轮结果加`1`或乘`2`。问至少需要多少轮操作才能达到指定整数。

输入描述

一个整数 $n \hspace{1em} (2 \le n \le 10^5)$，表示需要达到的整数。

输出描述

输出一个整数，表示至少需要的操作轮数。

样例1

输入

复制

```
7
```

输出

复制

```
4
```

解释

第`1`轮：1 + 1 = 2

第`2`轮：2 + 1 =3

第`3`轮：3 * 2 = 6

第`4`轮：6 + 1 = 7

因此至少需要操作`4`轮。



#### Python

```python
# gpt translated version of the C++ code
from collections import deque

MAXN = 100000
in_queue = [False] * (MAXN + 1)

def get_step(n):
    step = 0
    q = deque()
    q.append(1)
    while True:
        cnt = len(q)
        for _ in range(cnt):
            front = q.popleft()
            if front == n:
                return step
            in_queue[front] = True
            if front * 2 <= n and not in_queue[front * 2]:
                q.append(front * 2)
            if front + 1 <= n and not in_queue[front + 1]:
                q.append(front + 1)
        step += 1

if __name__ == "__main__":
    n = int(input())
    print(get_step(n))

```



#### C++

```c++
#include <cstdio>
#include <queue>
using namespace std;

const int MAXN = 100000;
bool inQueue[MAXN + 1] = {false};

int getStep(int n) {
    int step = 0;
    queue<int> q;
    q.push(1);
    while (true) {
        int cnt = q.size();
        for (int i = 0; i < cnt; i++) {
            int front = q.front();
            q.pop();
            if (front == n) {
                return step;
            }
            inQueue[front] = true;
            if (front * 2 <= n && !inQueue[front * 2]) {
                q.push(front * 2);
            }
            if (front + 1 <= n && !inQueue[front + 1]) {
                q.push(front + 1);
            }
        }
        step++;
    }
}

int main() {
    int n, step = 0;
    scanf("%d", &n);
    printf("%d", getStep(n));
    return 0;
}
```



### 2.2 矩阵中的块

https://sunnywhy.com/sfbj/8/2/319

题目描述

现有一个 n*m 的矩阵，矩阵中的元素为`0`或`1`。然后进行如下定义：

1. 位置(x,y)与其上下左右四个位置 $(x,y + 1)、(x,y - 1)、(x + 1,y)、(x-1,y)$ 是相邻的；
2. 如果位置 (x1,y1) 与位置 (x2,y2) 相邻，且位置 (x2,y2) 与位置 (x3,y3) 相邻，那么称位置(x1,y1)与位置(x3,y3)也相邻；
3. 称个数尽可能多的相邻的`1`构成一个“块”。

求给定的矩阵中“块”的个数。

**输入**

第一行两个整数 n、m（$2 \le n \le 100, 2 \le m \le 100$），分别表示矩阵的行数和列数；

接下来 n 行，每行 m 个`0`或`1`（用空格隔开），表示矩阵中的所有元素。

**输出**

输出一个整数，表示矩阵中“块”的个数。

样例1

输入

```
6 7
0 1 1 1 0 0 1
0 0 1 0 0 0 0
0 0 0 0 1 0 0
0 0 0 1 1 1 0
1 1 1 0 1 0 0
1 1 1 1 0 0 0
```

输出

```
4
```

解释

矩阵中的`1`共有`4`块，如下图所示。

![矩阵中的块_样例.png](https://raw.githubusercontent.com/GMyhf/img/main/img/202311262246785.png)



#### inq 数组，结点是否已入过队

```python
# gpt translated version of the C++ code
from collections import deque

# Constants
MAXN = 100
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# Functions
def can_visit(x, y):
    return 0 <= x < n and 0 <= y < m and matrix[x][y] == 1 and not in_queue[x][y]

def bfs(x, y):
    q = deque([(x, y)])
    in_queue[x][y] = True
    while q:
        front = q.popleft()
        for i in range(MAXD):
            next_x = front[0] + dx[i]
            next_y = front[1] + dy[i]
            if can_visit(next_x, next_y):
                in_queue[next_x][next_y] = True
                q.append((next_x, next_y))

# Input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
in_queue = [[False] * MAXN for _ in range(MAXN)]

# Main process
counter = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and not in_queue[i][j]:
            bfs(i, j)
            counter += 1

# Output
print(counter)

```



#### C++

```c++
#include <cstdio>
#include <queue>
#include <utility>
using namespace std;

typedef pair<int, int> Position;

const int MAXN = 100;
int n, m, matrix[MAXN][MAXN];
bool inQueue[MAXN][MAXN] = {false};

const int MAXD = 4;
int dx[MAXD] = {0, 0, 1, -1};
int dy[MAXD] = {1, -1, 0, 0};

bool canVisit(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && matrix[x][y] == 1 && !inQueue[x][y];
}

void BFS(int x, int y) {
    queue<Position> q;
    q.push(Position(x, y));
    inQueue[x][y] = true;
    while (!q.empty()) {
        Position front = q.front();
        q.pop();
        for (int i = 0; i < MAXD; i++) {
            int nextX = front.first + dx[i];
            int nextY = front.second + dy[i];
            if (canVisit(nextX, nextY)) {
                inQueue[nextX][nextY] = true;
                q.push(Position(nextX, nextY));
            }
        }
    }
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    int counter = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] == 1 && !inQueue[i][j]) {
                BFS(i, j);
                counter++;
            }
        }
    }
    printf("%d", counter);
    return 0;
}
```



### 2.3 迷宫问题

https://sunnywhy.com/sfbj/8/2/320

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格，且只能移动到平地上。求从迷宫左上角到右下角的最小步数。

**输入**

第一行两个整数 $n、m \hspace{1em} (2 \le n \le 100, 2 \le m \le 100)$，分别表示迷宫的行数和列数；

接下来 n 行，每行 m 个整数（值为`0`或`1`），表示迷宫。

**输出**

输出一个整数，表示最小步数。如果无法到达，那么输出`-1`。

样例1

输入

```
3 3
0 1 0
0 0 0
0 1 0
```

输出

```
4
```

解释: 假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的前进路线：(1,1)=>(2,1)=>(2,2)=>(2,3)=>(3,3)。

因此最少需要`4`步。

样例2

输入

```
3 3
0 1 0
0 1 0
0 1 0
```

输出

```
-1
```

解释: 显然从左上角无法到达右下角。



#### inq 数组，结点是否已入过队

```python
# gpt translated version of the C++ code
from collections import deque

# 声明方向变化的数组，代表上下左右移动
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 检查是否可以访问位置 (x, y)
def can_visit(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not in_queue[x][y]

# BFS函数 实现广度优先搜索
def bfs(x, y):
    q = deque()
    q.append((x, y))
    in_queue[x][y] = True
    step = 0
    while q:
        for _ in range(len(q)):
            cur_x, cur_y = q.popleft()
            if cur_x == n - 1 and cur_y == m - 1:
                return step
            for direction in range(4):
                next_x = cur_x + dx[direction]
                next_y = cur_y + dy[direction]
                if can_visit(next_x, next_y):
                    in_queue[next_x][next_y] = True
                    q.append((next_x, next_y))
        step += 1
    return -1

# 主函数
if __name__ == '__main__':
    # 读取 n 和 m
    n, m = map(int, input().split())
    maze = []
    in_queue = [[False] * m for _ in range(n)]

    # 填充迷宫和访问状态数组
    for i in range(n):
        maze.append(list(map(int, input().split())))

    # 执行BFS并输出步数
    step = bfs(0, 0)
    print(step)

```



#### C++

```c++
#include <cstdio>
#include <queue>
#include <utility>
using namespace std;

typedef pair<int, int> Position;

const int MAXN = 100;
int n, m, maze[MAXN][MAXN];
bool inQueue[MAXN][MAXN] = {false};

const int MAXD = 4;
int dx[MAXD] = {0, 0, 1, -1};
int dy[MAXD] = {1, -1, 0, 0};

bool canVisit(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && maze[x][y] == 0 && !inQueue[x][y];
}

int BFS(int x, int y) {
    queue<Position> q;
    q.push(Position(x, y));
    inQueue[x][y] = true;
    int step = 0;
    while (!q.empty()) {
        int cnt = q.size();
        while (cnt--) {
            Position front = q.front();
            q.pop();
            if (front.first == n - 1 && front.second == m - 1) {
                return step;
            }
            for (int i = 0; i < MAXD; i++) {
                int nextX = front.first + dx[i];
                int nextY = front.second + dy[i];
                if (canVisit(nextX, nextY)) {
                    inQueue[nextX][nextY] = true;
                    q.push(Position(nextX, nextY));
                }
            }
        }
        step++;
    }
    return -1;
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maze[i][j]);
        }
    }
    int step = BFS(0, 0);
    printf("%d", step);
    return 0;
}
```



### 2.4 迷宫最短路径

https://sunnywhy.com/sfbj/8/2/321

现有一个 n*m 大小的迷宫，其中`1`表示不可通过的墙壁，`0`表示平地。每次移动只能向上下左右移动一格，且只能移动到平地上。假设左上角坐标是(1,1)，行数增加的方向为增长的方向，列数增加的方向为增长的方向，求从迷宫左上角到右下角的最少步数的路径。

**输入**

第一行两个整数$n、m \hspace{1em} (2 \le n \le 100, 2 \le m \le 100)$，分别表示迷宫的行数和列数；

接下来 n 行，每行 m 个整数（值为`0`或`1`），表示迷宫。

**输出**

从左上角的坐标开始，输出若干行（每行两个整数，表示一个坐标），直到右下角的坐标。

数据保证最少步数的路径存在且唯一。

样例1

输入

```
3 3
0 1 0
0 0 0
0 1 0
```

输出

```
1 1
2 1
2 2
2 3
3 3
```

解释

假设左上角坐标是(1,)，行数增加的方向为增长的方向，列数增加的方向为增长的方向。

可以得到从左上角到右下角的最少步数的路径为：(1,1)=>(2,1)=>(2,2)=>(2,3)=>(3,3)。



#### inq 数组，结点是否已入过队

```python
# gpt translated version of the C++ code
from queue import Queue

MAXN = 100
MAXD = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def canVisit(x, y):
    return x >= 0 and x < n and y >= 0 and y < m and maze[x][y] == 0 and not inQueue[x][y]

def BFS(x, y):
    q = Queue()
    q.put((x, y))
    inQueue[x][y] = True
    while not q.empty():
        front = q.get()
        if front[0] == n - 1 and front[1] == m - 1:
            return
        for i in range(MAXD):
            nextX = front[0] + dx[i]
            nextY = front[1] + dy[i]
            if canVisit(nextX, nextY):
                pre[nextX][nextY] = (front[0], front[1])
                inQueue[nextX][nextY] = True
                q.put((nextX, nextY))

def printPath(p):
    prePosition = pre[p[0]][p[1]]
    if prePosition == (-1, -1):
        print(p[0] + 1, p[1] + 1)
        return
    printPath(prePosition)
    print(p[0] + 1, p[1] + 1)

n, m = map(int, input().split())
maze = []
for _ in range(n):
    row = list(map(int, input().split()))
    maze.append(row)

inQueue = [[False] * m for _ in range(n)]
pre = [[(-1, -1)] * m for _ in range(n)]

BFS(0, 0)
printPath((n - 1, m - 1))
```



#### C++

```python
#include <cstdio>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;

typedef pair<int, int> Position;

const int MAXN = 100;
int n, m, maze[MAXN][MAXN];
bool inQueue[MAXN][MAXN] = {false};
Position pre[MAXN][MAXN];

const int MAXD = 4;
int dx[MAXD] = {0, 0, 1, -1};
int dy[MAXD] = {1, -1, 0, 0};

bool canVisit(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m && maze[x][y] == 0 && !inQueue[x][y];
}

void BFS(int x, int y) {
    queue<Position> q;
    q.push(Position(x, y));
    inQueue[x][y] = true;
    while (!q.empty()) {
        Position front = q.front();
        q.pop();
        if (front.first == n - 1 && front.second == m - 1) {
            return;
        }
        for (int i = 0; i < MAXD; i++) {
            int nextX = front.first + dx[i];
            int nextY = front.second + dy[i];
            if (canVisit(nextX, nextY)) {
                pre[nextX][nextY] = Position(front.first, front.second);
                inQueue[nextX][nextY] = true;
                q.push(Position(nextX, nextY));
            }
        }
    }
}

void printPath(Position p) {
    Position prePosition = pre[p.first][p.second];
    if (prePosition == Position(-1, -1)) {
        printf("%d %d\n", p.first + 1, p.second + 1);
        return;
    }
    printPath(prePosition);
    printf("%d %d\n", p.first + 1, p.second + 1);
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &maze[i][j]);
        }
    }
    fill(pre[0], pre[0] + n * m, Position(-1, -1));
    BFS(0, 0);
    printPath(Position(n - 1, m - 1));
    return 0;
}
```



## Recap 6 部分递归题目

### 01661: Help Jimmy

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



### 02386: Lake Counting

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



### 05585: 晶矿的个数

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



### 02786: Pell数列

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





