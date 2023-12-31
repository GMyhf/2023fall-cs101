# 计算概论(B) 课前问题2

Updated 2359 GMT+8 Aug 24, 2023



2023 fall, Complied by Hongfei Yan

Markdown（用 https://typoraio.cn 编辑）格式文件在，https://github.com/GMyhf/2023fall-cs101



| 课程号: 04831410		课程名: 计算概论(B)                  | 班号: 12                                              |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| 上课时间: 1-16周 每周 周二 7-9节                             | 地点: 理教208                                         |
| 上机时间: 1-15周 每周 周四 7-8节<br/>期末机考时间: 第16周 周四 7-8节 | 地点：理科1号楼计算中心，二层楼的6号和三层楼的7号机房 |
| 助教：张哲瑞、张以宁、彭亦男、涂程颖、陈威宇                 | 在课程微信群中的名字是“TA-”开始，地点：理科1号楼1220  |



往年是我留作业，我改作业，每周一次。好的作业在其中加批注标亮，会截图、或者整个作业发到课程微信群。今年想把选课同学分一下，届时五位助教批改自己负责的同学作业，好的发到群里。尽量做到不吝发现学生的优点，促进大家互相学习，互相答疑。



可以导出选课名单到Excel，例如：studentListInCourse-20230814.xls。目前还看不到性别信息。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230816141341659.png" alt="image-20230816141341659" style="zoom:67%;" />

使用下面这段代码（不要求掌握，如果看不懂，可以跳过代码）可以生成选课学生的院系分布

```python
import pandas as pd

df = pd.read_excel('studentListInCourse-20230824.xls')
df_schools = df['所属院系'].value_counts().reset_index()
df_schools.columns = ['所属院系', 'Count']
#print(df_schools)

import itertools
#print(*df_schools.loc[:, ['所属院系']].values)
#print(*df_schools.loc[:, ['Count']].values)
labels = list(itertools.chain(*df_schools.loc[:, ['所属院系']].values))
sizes = list(itertools.chain(*df_schools.loc[:, ['Count']].values))

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Heiti TC']

fig, ax = plt.subplots(figsize=(15, 15))
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title(label="2023/8/24 选课院系分布",
          fontsize=20,
          loc="left",
          color="green")
plt.show()
```

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/202308250000043.png" alt="image-20230824235919701" style="zoom:67%;" />

现在问题是，如何把不同年级、不同院系、是否留学生的同学均衡分配给助教们。请用Python，C 或者 C++实现。完成的同学可以把程序直接发到课程微信群里面，方便大家参考。
