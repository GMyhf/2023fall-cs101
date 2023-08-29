#2023fall-cs101, 曹琦峻
import pandas as pd
df = pd.read_excel("studentListInCourse-20230828.xls")
group = [[],[],[],[],[]]
for i in range(df.shape[0]):
    list=[]
    for j in range(5):
        #定义每个人与各组的“相同值”，考虑“相同值”与组人数之间的关系
        same_value = len(group[j])*5
        for k in range(len(group[j])):
            number = group[j][k]
            #判断学院与学生类型
            for l in range(2,4):
                if df.iloc[number,l] == df.iloc[i,l]:
                    same_value += 1
            #判断年级
            if str(df.iloc[number,0])[0:2] == str(df.iloc[i,0])[0:2]:
                same_value += 1
        list.append(same_value)
    #选择“相同值“小的组加入
    group_i = list.index(min(list))
    group[group_i].append(i)
for x in range(5):
    for y in range(df.shape[0]):
        if y in group[x]:
            group[x][group[x].index(y)] = df.iloc[y,1]
            # group[x][group[x].index(y)] = df.iloc[y,0].astype(str)+'-'+df.iloc[y,1]+'-'+df.iloc[y,2]
df_group = pd.DataFrame(group,index=["group{}".format(str(p)) for p in range(1,6)])
print(df_group)
