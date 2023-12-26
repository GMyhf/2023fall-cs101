# Dijkstra算法



Updated 1852 GMT+8 Dec 26, 2023



2023 fall, Complied by 卢卓然



**用于计算有权图中一个节点到其他节点的最短路径。**

## 基本原理

从起始点出发，重复寻找所有点中距离源点最近的且未访问过的结点，把该节点设置为已访问，然后利用该结点更新该节点的邻居节点的**距离数组**，直到访问过全部结点为止，最终的距离数组即为源点到其余各点的最短路径距离。

注：

距离数组：用于记录当前所有点到源点的距离，D[i]表示从源点到第i个点的最短路径距离。初始时数组中的每个值应该为无穷大。这个数组在算法进行中被不断更新，Dijkstra算法结束后，此数组中各个值应该表示源点到其余各点的最短路径距离。

已访问的点：每一次重复中找到的、**距离源点最近（D[i]最小）**且未访问过的节点。

## 算法正确性

![img](https://raw.githubusercontent.com/GMyhf/img/main/img/watermark%252Ctype_ZmFuZ3poZW5naGVpdGk%252Cshadow_10%252Ctext_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2dvb2R4aW5faWU%253D%252Csize_16%252Ccolor_FFFFFF%252Ct_70.png)

如图，0是源点。与0相连的三个点中，0-2的距离是最短的，那么从0到2的最短路径长就是2，即`D[2]=2`。原因是从0出发，若走中途不经过2的路径到达2，那么一定会经过1或3，从0到1或从0到3的距离就已经比从0直接到2的距离长了。若中途经过2最后又回到2，那么就绕了圈，也是比从0直接到2长的。所以`D[2]=2`。然后把2设置为已访问，代表已经确定了从源点出发到2的最短路径长，后续不应该再更新`D[2]`了（体现了dp的思想）。

2是已访问的点，1和3是他的邻居节点。根据算法，还要把点1和点3距离源点的距离`D[1]`和`D[3]`进行更新。虽然不能确定此时的`D[1]`和`D[3]`就一定是从源点到点1和点3的最短路径，但是对于这样的点，可以一边遍历所有节点一边不断更新`D[i]`为更小的值，来找到可能的最短路径。

接下来，按照距离数组中的数据，找到与源点距离最短的点，标记为已访问。目前，距离数组中最小值为`D[1]=3`，根据算法，可以确定从0到1的最小距离就是3。

我们这样做是否正确，就决定了这个算法是否正确。一般地，设集合S表示**“已访问点”的集合**，（对于本例，S的初始成员显然地就是0/0和2）对于每一个已访问点i，其到源点的最短距离已然确定，那么`D[i]+点i到其邻居节点的距离`就是从源点出发，经过节点i，到达这个邻居节点的最短路径。在算法进行的过程中，在S集合到达这个状态之前，我们已经遍历过所有已访问点，并且按照上述方法**更新了**所有他们的邻居节点k的D[k]**最小值**。那么此时所有不在S中的点k，且不为无穷大的D[k]值就表示**从源点出发，只能经过集合S中的点，最终到达该点k**的最小距离。每一个D[k]值都对应着唯一的一条这样的线路。

现在假设有一条比这条线路还短的线路，起点终点不变。那么他就无法“只能经过集合S中的点”了，设路径中第一个不在S中的点为w。那么“起点—w”长度<“起点—w—k”长度<D[k]。而w是第一个不在S中的点，那么在S中必然能找到一个点，使w是他的邻居节点。说明对于所有不在S中的点，且不为无穷大的D值，是D[w]而不是D[k]，这就与前提条件矛盾。因此，说明D中的最小值D[k]对应的线路，就是从源点出发到节点k的最小距离。

```python
# 北京 天津 郑州 济南 长沙 海南
# 0    1    2    3    4    5

# 模拟从文件中读入图的各个路径
a = """
0 1 500
0 2 100
1 2 900
1 3 300
2 3 400
2 4 500
3 4 1300
3 5 1400
4 5 1500
"""

INF = float('inf')

# 定义邻接矩阵 记录各城市之间的距离
weight = [[INF if j != i else 0 for j in range(6)] for i in range(6)]

# 解析数据
b = [[int(i) for i in i.split(' ')] for i in a.split('\n') if i != '']

for i in b:
    weight[i[0]][i[1]] = i[2]
    weight[i[1]][i[0]] = i[2]


def dijkstra(src, target):
    """
    src : 起点索引
    dist: 终点索引
    ret:  最短路径的长度
    """
    # 未到的点
    u = [i for i in range(6)]
    # 距离列表
    dist = weight[src][:]
    # 把起点去掉
    u.remove(src)

    # 用于记录最后更新结点
    last_update = [src if i != INF else -1 for i in dist]

    while u != []:

        idx = 0
        min_dist = INF

        # 找最近的点
        for i in range(6):
            if i in u and dist[i] < min_dist:
                min_dist = dist[i]
                idx = i

        # 从未到列表中去掉这个点
        u.remove(idx)

        # 更新dist（借助这个点连接的路径更新dist）
        for j in range(6):
            if j in u and weight[idx][j] + min_dist < dist[j]:
                dist[j] = weight[idx][j] + min_dist

                # 记录更新该结点的结点编号
                last_update[j] = idx

    # 输出从起点到终点的路径结点
    tmp = target
    path = []
    while tmp != src:
        path.append(tmp)
        tmp = last_update[tmp]
    path.append(src)
    print("->".join([str(i) for i in reversed(path)]))

    return dist[target]
'''
示例输出：
1->0->2->4
1100
'''
```

## 走山路与heap优化

描述

某同学在一处山地里，地面起伏很大，他想从一个地方走到另一个地方，并且希望能尽量走平路。 现有一个m*n的地形图，图上是数字代表该位置的高度，"#"代表该位置不可以经过。 该同学每一次只能向上下左右移动，每次移动消耗的体力为移动前后该同学所处高度的差的绝对值。现在给出该同学出发的地点和目的地，需要你求出他最少要消耗多少体力。

输入

第一行是整数 m,n,p，m是行数，n是列数，p是测试数据组数。 0 <= m,n,p <= 100 接下来m行是地形图 再接下来n行每行前两个数是出发点坐标（前面是行，后面是列），后面两个数是目的地坐标（前面是行，后面是列）（出发点、目的地可以是任何地方，出发点和目的地如果有一个或两个在"#"处，则将被认为是无法达到目的地）

输出

n行，每一行为对应的所需最小体力，若无法达到，则输出"NO"

样例输入

```
4 5 3
0 0 0 0 0
0 1 1 2 3
# 1 0 0 0
0 # 0 0 0
0 0 3 4
1 0 1 4
3 4 3 0
```

样例输出

``````
2
3
NO
``````

#### Dijkstra做法

```python
m,n,case=map(int,input().split())#行数、列数、测试用例
output=[]#输出
mount_map=[]#地形图，内涵有权图的信息
for _ in range(m):
    mount_map.append(input().split())#str型
direction=[(-1,0),(1,0),(0,1),(0,-1)]#邻居节点的方向

for _ in range(case):#多个测试用例
    sx,sy,ex,ey=map(int,input().split())#起点坐标、终点坐标
    #起点终点不可到达
    if mount_map[sx][sy]=='#' or mount_map[ex][ey]=='#':
        output.append('NO')
        continue

    visited=set()#已访问节点，已知最短路径的点
    D=[[float('inf')]*n for _ in range(m)]#距离数组
    #起点已访问(查找之后标记)
    D[sx][sy]=0
    for j in range((m+1)*(n+1)):#最多循环(m+1)*(n+1)次
        #查找距离源点最近的点
        minimum=float('inf')
        minx=miny=0
        for _x in range(m):
            for _y in range(n):
                if D[_x][_y]<minimum and (_x,_y) not in visited:
                    minimum=D[_x][_y]
                    minx=_x
                    miny=_y
        if minx==ex and miny==ey:
            output.append(minimum)
            visited.add((ex,ey))
            break
        #标记已访问，更新邻居节点
        visited.add((minx,miny))
        for i in range(4):
            dx, dy = direction[i]
            x1,y1=minx+dx,miny+dy
            if 0<=x1<m and 0<=y1<n and mount_map[x1][y1]!='#' and (x1,y1) not in visited:
                D[x1][y1]=min(D[x1][y1],minimum+abs(int(mount_map[minx][miny])-int(mount_map[x1][y1])))
    if (ex,ey) not in visited:
        output.append('NO')

for o in output:
    print(o)
```

查找D中最小值双重循环会超时，但是答案是正确的。因为heapq每次弹出的是最小值（对于元组来说是元组的第一个元素最小的那个元组），所以可以把距离放在元组的第一个位置，坐标放在元组的第2、3个位置。接着使用heapq进行弹出和推入。这样就不需要初始化和遍历距离数组D了。`heapq.heappop()`出来的坐标就是当前距离源点最近的点。代码思路和Dijkstra完全一样。

#### heapq优化

``````python
from heapq import *
m,n,case=map(int,input().split())#行数、列数、测试用例
output=[]#输出
mount_map=[]#地形图，内涵有权图的信息
for _ in range(m):
    mount_map.append(input().split())#str型
direction=[(-1,0),(1,0),(0,1),(0,-1)]#邻居节点的方向

for _ in range(case):#多个测试用例
    sx,sy,ex,ey=map(int,input().split())#起点坐标、终点坐标
    #起点终点不可到达
    if mount_map[sx][sy]=='#' or mount_map[ex][ey]=='#':
        output.append('NO')
        continue
    visited=set()#已访问节点，已知最短路径的点
    heap=[]
    heappush(heap,(0,sx,sy))
    while heap:
        mintire,minx,miny=heappop(heap)
        if minx==ex and miny==ey:
            output.append(mintire)
            visited.add((ex,ey))
            break
        #标记已访问，更新邻居节点
        visited.add((minx,miny))
        for i in range(4):
            dx, dy = direction[i]
            x1,y1=minx+dx,miny+dy
            if 0<=x1<m and 0<=y1<n and mount_map[x1][y1]!='#' and (x1,y1) not in visited:
                heappush(heap,(mintire+abs(int(mount_map[minx][miny])-int(mount_map[x1][y1])),x1,y1))
    if (ex,ey) not in visited:
        output.append('NO')

for o in output:
    print(o)
``````

