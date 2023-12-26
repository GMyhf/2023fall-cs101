# 正则表达式



Updated 1852 GMT+8 Dec 26, 2023



2023 fall, Complied by 程卓



## 一.正则表达式的常见符号解释

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/watermark%252Ctype_ZmFuZ3poZW5naGVpdGk%252Cshadow_10%252Ctext_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzM0NzU1MA%253D%253D%252Csize_16%252Ccolor_FFFFFF%252Ct_70.png" alt="img" style="zoom: 50%;" />

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/watermark%252Ctype_ZmFuZ3poZW5naGVpdGk%252Cshadow_10%252Ctext_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzM0NzU1MA%253D%253D%252Csize_16%252Ccolor_FFFFFF%252Ct_70-20231226192317732.png" alt="img" style="zoom:50%;" />



## 二.逐一详解

### 1.首先导入模块

```python
import re
```

### 2.匹配多种可能（使用[]）

```python
#'run' or 'ran'
res = re.search(r'r[au]n','dog runs to cat')
print(res)
>>> <re.Match object; span=(4, 7), match='run'> 

res = re.search(r'r[au]n','dog rans to cat')
print(res)
>>> <re.Match object; span=(4, 7), match='ran'>

#continue 匹配更多种可能
res = re.search(r'r[A-Z]n','dog rans to cat')
print(res)
>>> None

res = re.search(r'r[a-z]n','dog rans to cat')
print(res)
>>> <re.Match object; span=(4, 7), match='ran'>

res = re.search(r'r[0-9]n','dog rans to cat')
print(res)
>>>None

res = re.search(r'r[0-9a-z]n','dog rans to cat')
print(res)
>>> <re.Match object; span=(4, 7), match='ran'>
```

### 3.匹配数字\d and \D

```python
# \d : decimal digit 数字的
res = re.search(r'r\dn','run r9n')
print(res)
>>> <re.Match object; span=(4, 7), match='r9n'>

# \D : any non-decimal digit 任何不是数字的
res = re.search(r'r\Dn','run r9n')
print(res)
>>> <re.Match object; span=(0, 3), match='run'>
```

### 4.匹配空白\s and \S

```python
# \s : any white space [\t \n \r \f \v]
res = re.search(r'r\sn','r\nn r9n')
print(res)
>>> <re.Match object; span=(0, 3), match='r\nn'>

# \S : 和\s相反，any non-white space
res = re.search(r'r\Sn','r\nn r9n')
print(res)
>>> <re.Match object; span=(4, 7), match='r9n'>
```

### 5.匹配所有的字母、数字以及’_‘ \w and \W

```python
# \w : [a-zA-Z0-9_]
res = re.search(r'r\wn','r\nn r9n')
print(res)
>>> <re.Match object; span=(4, 7), match='r9n'>

# \W : opposite to \w 即与\w相反
res = re.search(r'r\Wn','r\nn r9n')
print(res)
>>> <re.Match object; span=(0, 3), match='r\nn'>
```

### 6.匹配空白字符 \b and \B

```python
# \b : (only at the start or end of the word)
res = re.search(r'\bruns\b','dog runs to cat')
print(res)
>>> <re.Match object; span=(4, 8), match='runs'>
res = re.search(r'\bruns\b','dogrunsto cat')
print(res)
>>> None

# \B : ( but not at the start or end of the word)
res = re.search(r'\Bruns\B','dog runs to cat')
print(res)
>>> None
res = re.search(r'\Bruns\B','dogrunsto cat')
print(res)
>>> <re.Match object; span=(5, 11), match=' runs '>
```

### 7.匹配特殊字符 任意字符 \ and .

```python
# \\ : 匹配 \
res = re.search(r'runs\\','dog runs\ to cat')
print(res)
>>> <re.Match object; span=(4, 9), match='runs\\'>

# . : 匹配 anything （except \n）
res = re.search(r'r.ns','dog r;ns to cat')
print(res)
>>> <re.Match object; span=(4, 8), match='r;ns'>
>res = re.search(r'r.ns','dog r\nns to cat')
print(res)
>>> None
```

### 8.匹配句尾句首 $ and ^

```python
# ^ : 匹配line beginning
res = re.search(r'^runs','dog runs to cat')
print(res)
>>> None
res = re.search(r'^dog','dog runs to cat')
print(res)
>>> <re.Match object; span=(0, 3), match='dog'>

# $ : 匹配line ending
res = re.search(r'runs$','dog runs to cat')
print(res)
>>> None
res = re.search(r'cat$','dog runs to cat')
print(res)
>>> <re.Match object; span=(12, 15), match='cat'>
```

### 9.是否匹配 ？

```python
# ？ ： may or may nt occur
res = re.search(r'r(u)?ns','dog runs to cat')
print(res)
>>> <re.Match object; span=(4, 8), match='runs'>

res = re.search(r'r(u)?ns','dog rns to cat')
print(res)
>>><re.Match object; span=(4, 7), match='rns'>
```

### 10.多行匹配 re.M

```python
# 匹配代码后面加上re.M
string = """ 123.
dog runs to cat.
You run to dog.
"""
res = re.search(r'^You',string)
print(res)
>>> None

res = re.search(r'^You',string,re.M)
print(res)
>>> <re.Match object; span=(10, 13), match='run'>
```

### 11.匹配零次或多次 *

```python
# * ： occur 0 or more times
res = re.search(r'ab*','a')
print(res)
>>> <re.Match object; span=(0, 1), match='a'>

res = re.search(r'ab*','abbbbbbbbbb')
print(res)
>>> <re.Match object; span=(0, 11), match='abbbbbbbbbb'>
```

### 12.匹配一次或多次 +

```python
# + ：occur 1 or more times
res = re.search(r'ab+','a')
print(res)
>>> None

res = re.search(r'ab+','abbbbbbbbbb')
print(res)
>>> <re.Match object; span=(0, 11), match='abbbbbbbbbb'>
```

### 13.可选次数匹配 {n,m}

```python
# {n, m} : occur n to m times
res = re.search(r'ab{1,10}','a')
print(res)
>>> None

res = re.search(r'ab{1,10}','abbbbbbbbbb')
print(res)
>>> <re.Match object; span=(0, 11), match='abbbbbbbbbb'>
```

### 14.匹配后group组输出

```python
# group
res = re.search(r'ID: (\d+), Name: (.+)','ID: 123456789, Name: a/b*c;d')
print(res.group())
print(res.group(1))
print(res.group(2))
>>> ID: 123456789, Name: a/b*c;d
>>> 123456789
>>> a/b*c;d

# 给group组命名  ?P<name>
res = re.search(r'ID: (?P<id>\d+), Name: (?P<name>.+)','ID: 123456789, Name: a/b*c;d')
print(res.group('id'))
print(res.group('name'))
>>> 123456789
>>> a/b*c;d
```

### 15.寻找所有匹配 findall

```python
# re.findall()
res = re.findall(r'r[ua]n','run ran ren')
print(res)
>>> ['run', 'ran']

# 另一种写法
res = re.findall(r'(run|ran)','run ran ren')
print(res)
>>> ['run', 'ran']
```

### 16.替换匹配内容 sub

```python
# re.sub(   ,replace,   )
res = re.sub(r'runs','catches','dog runs to cat')
print(res)
>>> dog catches to cat
```

### 17.分裂内容 split

```python
# re.split()
res = re.split(r'[,;\.\\]', 'a,b;c.d\e')
print(res)
>>> ['a', 'b', 'c', 'd', 'e']
```

### 18.包装正则表达式 compile

```python
# re. compile()
compile_re = re.compile(r'r[ua]n')
res = compile_re.findall('run ran ren')
print(res)
>>> ['run', 'ran']
```



## 三.一些常见的正则表达式

### 1.校验数字的表达式

```python
1、数字：^[0-9]*$
2、n位的数字：^\d{n}$
3、至少n位的数字：^\d{n,}$
4、m-n位的数字：^\d{m,n}$
5、零和非零开头的数字：^(0|[1-9][0-9]*)$
6、非零开头的最多带两位小数的数字：^([1-9][0-9]*)+(.[0-9]{1,2})?$
7、带1-2位小数的正数或负数：^(\-)?\d+(\.\d{1,2})?$
8、正数、负数、和小数：^(\-|\+)?\d+(\.\d+)?$
9、有两位小数的正实数：^[0-9]+(.[0-9]{2})?$
10、有1~3位小数的正实数：^[0-9]+(.[0-9]{1,3})?$
11、非零的正整数：^[1-9]\d*$ 或 ^([1-9][0-9]*){1,3}$ 或 ^\+?[1-9][0-9]*$
12、非零的负整数：^\-[1-9][]0-9"*$ 或 ^-[1-9]\d*$
13、非负整数：^\d+$ 或 ^[1-9]\d*|0$
14、非正整数：^-[1-9]\d*|0$ 或 ^((-\d+)|(0+))$
15、非负浮点数：^\d+(\.\d+)?$ 或 ^[1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0$
16、非正浮点数：^((-\d+(\.\d+)?)|(0+(\.0+)?))$ 或 ^(-([1-9]\d*\.\d*|0\.\d*[1-9]\d*))|0?\.0+|0$
17、正浮点数：^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$ 或 ^(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$
18、负浮点数：^-([1-9]\d*\.\d*|0\.\d*[1-9]\d*)$ 或 ^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$
19、浮点数：^(-?\d+)(\.\d+)?$ 或 ^-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)$
```

### 2.校验字符的表达式

```python
1、汉字：^[\u4e00-\u9fa5]{0,}$
2、英文和数字：^[A-Za-z0-9]+$ 或 ^[A-Za-z0-9]{4,40}$
3、长度为3-20的所有字符：^.{3,20}$
3、由26个英文字母组成的字符串：^[A-Za-z]+$
5、由26个大写英文字母组成的字符串：^[A-Z]+$
6、由26个小写英文字母组成的字符串：^[a-z]+$
7、由数字和26个英文字母组成的字符串：^[A-Za-z0-9]+$
8、由数字、26个英文字母或者下划线组成的字符串：^\w+$ 或 ^\w{3,20}$
9、中文、英文、数字包括下划线：^[\u4E00-\u9FA5A-Za-z0-9_]+$
10、中文、英文、数字但不包括下划线等符号：^[\u4E00-\u9FA5A-Za-z0-9]+$ 或 ^[\u4E00-\u9FA5A-Za-z0-9]{2,20}$
11、可以输入含有^%&',;=?$\"等字符：[^%&',;=?$\x22]+
12、禁止输入含有~的字符：[^~\x22]+
```

### 3.特殊需求表达式

```python
1、Email地址：^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$
2、域名：[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?
3、 InternetURL：[a-zA-z]+://[^\s]* 或 ^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$
4、手机号码：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
5、电话号码("XXX-XXXXXXX"、"XXXX-XXXXXXXX"、"XXX-XXXXXXX"、"XXX-XXXXXXXX"、"XXXXXXX"和"XXXXXXXX)：^(\(\d{3,4}-)|\d{3.4}-)?\d{7,8}$
6、国内电话号码(0511-4405222、021-87888822)：\d{3}-\d{8}|\d{4}-\d{7}
7、身份证号(15位、18位数字)：^\d{15}|\d{18}$
8、短身份证号码(数字、字母x结尾)：^([0-9]){7,18}(x|X)?$ 或 ^\d{8,18}|[0-9x]{8,18}|[0-9X]{8,18}?$
9、帐号是否合法(字母开头，允许5-16字节，允许字母数字下划线)：^[a-zA-Z][a-zA-Z0-9_]{4,15}$
10、密码(以字母开头，长度在6~18之间，只能包含字母、数字和下划线)：^[a-zA-Z]\w{5,17}$
11、强密码(必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-10之间)：^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$
12、日期格式：^\d{4}-\d{1,2}-\d{1,2}
13、一年的12个月(01～09和1～12)：^(0?[1-9]|1[0-2])$
14 、一个月的31天(01～09和1～31)：^((0?[1-9])|((1|2)[0-9])|30|31)$
15、钱的输入格式：
* 有四种钱的表示形式我们可以接受:"10000.00" 和 "10,000.00", 和没有 "分" 的 "10000" 和 "10,000"：^[1-9][0-9]*$
* 这表示任意一个不以0开头的数字,但是,这也意味着一个字符"0"不通过,所以我们采用下面的形式：^(0|[1-9][0-9]*)$
* 一个0或者一个不以0开头的数字.我们还可以允许开头有一个负号：^(0|-?[1-9][0-9]*)$
* 这表示一个0或者一个可能为负的开头不为0的数字.让用户以0开头好了.把负号的也去掉,因为钱总不能是负的吧.下面我们要加的是说明可能的小数部分：^[0-9]+(.[0-9]+)?$
* 5.必须说明的是,小数点后面至少应该有1位数,所以"10."是不通过的,但是 "10" 和 "10.2" 是通过的：^[0-9]+(.[0-9]{2})?$
* 6.这样我们规定小数点后面必须有两位,如果你认为太苛刻了,可以这样：^[0-9]+(.[0-9]{1,2})?$
* 这样就允许用户只写一位小数.下面我们该考虑数字中的逗号了,我们可以这样：^[0-9]{1,3}(,[0-9]{3})*(.[0-9]{1,2})?$
* 1到3个数字,后面跟着任意个 逗号+3个数字,逗号成为可选,而不是必须：^([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(.[0-9]{1,2})?$
* 备注：这就是最终结果了,别忘了"+"可以用"*"替代如果你觉得空字符串也可
* 以接受的话(奇怪,为什么?)最后,别忘了在用函数时去掉去掉那个反斜杠,一般的错误都在这里
16、xml文件：^([a-zA-Z]+-?)+[a-zA-Z0-9]+\\.[x|X][m|M][l|L]$
17、中文字符的正则表达式：[\u4e00-\u9fa5]
18、双字节字符：[^\x00-\xff] (包括汉字在内，可以用来计算字符串的长度(一个双字节字符长度计2，ASCII字符计1))
19、空白行的正则表达式：\n\s*\r (可以用来删除空白行)
20、HTML标记的正则表达式：<(\S*?)[^>]*>.*?</\1>|<.*? /> (网上流传的版本太糟糕，上面这个也仅仅能部分，对于复杂的嵌套标记依旧无能为力)
21、首尾空白字符的正则表达式：^\s*|\s*$或(^\s*)|(\s*$) (可以用来删除行首行尾的空白字符(包括空格、制表符、换页符等等)，非常有用的表达式)
22、 腾讯QQ号：[1-9][0-9]{4,} (腾讯QQ号从10000开始)
23、中国邮政编码：[1-9]\d{5}(?!\d) (中国邮政编码为6位数字)
24、IP地址：\d+\.\d+\.\d+\.\d+ (提取IP地址时有用)
25、 IP地址：((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))
```

