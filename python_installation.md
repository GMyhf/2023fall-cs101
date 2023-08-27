# Python安装

Updated 0953 GMT+8 Aug 27, 2023



2023 fall, Complied by Hongfei Yan



1的内容，拷贝自 张维忠，张甜《Python机器学习原理与算法实现》的1.2节，出版时间2023-02-01.

2是同学们安装开发环境过程中遇到的问题。



# 1 Python的下载与安装

本节主要介绍Python的下载与安装的具体操作。

## 1.1 下载Python（Anaconda平台）

从Anaconda平台上进行下载。Anaconda平台不仅集成了大部分常用的Python标准库，也集成了Spyder、PyCharm以及Jupyter等常用开发环境，大大提升了用户的操作效率。

步骤01 登录Anaconda平台官网，打开如图1.3所示的界面。
步骤02 如果用户的操作系统恰好为Windows 64位，则可直接单击Download按钮进行下载；如果是其他操作系统，则单击Get Additional Installers链接，弹出如图1.4所示的下载选择列表。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827095511118.png" alt="image-20230827095511118" style="zoom:50%;" />

​																图1.3 Anaconda平台官网下载界面1

步骤03 图1.4中展示了Anaconda平台当前支持的操作系统。用户可根据自己计算机上操作系统的具体类型和版本选择下载对应的Anaconda版本。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827095616090.png" alt="image-20230827095616090" style="zoom:50%;" />

​															图1.4 Anaconda平台官网下载界面2

## 1.2 安装Python（Anaconda平台）

Python的安装步骤如下：
步骤01 在计算机上双击已下载的Anaconda平台安装包，安装包将自动进行解压缩操作，并弹出如图1.5所示的“欢迎安装”对话框。
步骤02 在图1.5中单击Next按钮，即可弹出如图1.6所示的“同意协议”对话框，在其中单击I Agree按钮后单击Next按钮，随后弹出如图1.7所示的“用户选择”对话框，建议在其中单击All Users单选按钮后单击Next按钮，会弹出如图1.8所示的“安装位置”对话框，我们需要在其中设置好安装软件的目标文件夹位置。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827095856620.png" alt="image-20230827095856620" style="zoom: 33%;" />

​															图1.5 “欢迎安装”对话框



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827095949605.png" alt="image-20230827095949605" style="zoom:33%;" />

​															图1.6 “同意协议”对话框



<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827100044926.png" alt="image-20230827100044926" style="zoom: 33%;" />

​															图1.7 “用户选择”对话框

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827100138677.png" alt="image-20230827100138677" style="zoom:33%;" />

​															图1.8 “安装位置”对话框

步骤03 设置完成后，单击Next按钮随即弹出如图1.9所示的“安装选项”对话框，对于新手，建议将对话框中的两个复选框全部勾选，若不勾选，软件可能无法正常运行，而对于较为熟练的技术人员，则可根据实际情况灵活选择。设置完成后单击Install按钮即可让系统自动完成安装。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827100325275.png" alt="image-20230827100325275" style="zoom:33%;" />

​															图1.9 “安装选项”对话框

安装完成后，计算机的开始菜单中会出现与Anaconda平台相关的6个快捷方式，包括Spyder (Anaconda3)、Anaconda Powershell Prompt (Anaconda3)、Reset Spyder Settings (Anaconda3)、Anaconda Navigator (Anaconda3)、Anaconda Prompt (Anaconda3)、Jupyter Notebook (Anaconda3)，如图1.10所示。其中最为常用的是Anaconda Prompt (Anaconda3)与Spyder (Anaconda3)。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827100446806.png" alt="image-20230827100446806" style="zoom: 50%;" />

​															图1.10 Anaconda平台组成

如果是Windows操作系统，但严格按照上述步骤操作仍未安装成功，则大概率是Windows操作系统版本与Anaconda平台版本不匹配的问题，解决方式有两个，一是升级Windows操作系统版本，比如升级至Windows 10；二是降低所使用的Anaconda平台版本（官网推荐安装的一般为最新版本，但事实上较低一些的版本仍能完成应用需求且兼容性更好），可从互联网上搜索旧的Anaconda平台版本进行安装。比如本书在写作过程中使用的Windows操作系统为Windows 7，安装Anaconda3-2022.05-Windows-x86_64就会提示错误，而安装Anaconda3-2021.05-Windows-x86_64则非常顺利。

## 1.3 Anaconda Prompt(Anaconda3)

安装成功后，在开始菜单的Anaconda3 (64-bit)文件夹中单击Anaconda Prompt (Anaconda3)，即可弹出如图1.11所示的命令行窗口。该窗口首先会自动给出路径<base>PS C:\Users\Administrator>，然后我们在命令提示符后面输入Python，即可出现我们已经安装的Python系统的版本信息（本书写作时安装的版本为Python 3.8.8）以及提示符“>>>”，我们在提示符的后面输入Python程序代码并按Enter键，即可执行这些程序代码。比如我们输入程序语句“print('对酒当歌，人生几何')”再按Enter键，该程序语句执行后的输出为“对酒当歌，人生几何”。
Anaconda Prompt只能以交互方式执行Python程序代码，每输入一行代码均需按Enter键才能执行，无法连续执行程序，所以在编写程序时这种方式并不多见。以命令行方式执行程序代码的优势在于可以立刻获得系统的响应，因此常用于管理与Python相关的库，比如需要安装某个第三方库，Anaconda Prompt提供的命令行交互方式相对于其他方式更为快捷。在编写程序代码方面，使用最多的是Spyder(Anaconda3)。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827100811188.png" alt="image-20230827100811188" style="zoom: 50%;" />

​														图1.11 Anaconda Prompt (Anaconda3)命令提示符窗口

## 1.4 Spyder(Anaconda3)的介绍及偏好设置

Spyder（前身是Pydee）是一个强大的交互式Python语言开发环境，提供高级的代码编辑、交互测试、调试等特性。在开始菜单的Anaconda3 (64-bit)文件夹中单击Spyder (Anaconda3)，即可弹出其窗口，如图1.12所示。Spyder (Anaconda3)是我们最为常用的环境，强烈建议将其快捷方式发送到桌面，方便以后使用。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827132911904.png" alt="image-20230827132911904" style="zoom: 50%;" />

​														图1.12 Spyder窗口

Spyder的界面为纯英文，而且为黑暗色，对于大多数国内用户来说，可能并不适应这种风格。我们可以采取以下方式调整界面（当然，这取决于用户偏好，如果用户认为当前界面风格是可以接受的，也可不进行下述调整）：
步骤01 依次单击菜单栏中的Tools→Preferences菜单选项（见图1.13），打开Preferences对话框。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827132949362.png" alt="image-20230827132949362" style="zoom:50%;" />

​														图1.13 Spyder

步骤02 在Preferences对话框中单击General选项，切换到Advanced setting选项卡，然后在General中的Language下拉列表中选择简体中文”，再单击对话框右下角的Apply按钮，最后单击OK按钮，如图1.14所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133023977.png" alt="image-20230827133023977" style="zoom:50%;" />

​														图1.14 Preferences对话框

步骤03 弹出如图1.15所示的Information对话框，单击其中的Yes按钮即可重启Spyder，重启后界面语言变成了简体中文。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133059550.png" alt="image-20230827133059550" style="zoom:33%;" />

​														图1.15 Information对话框

步骤04 依次单击菜单栏中的“工具”→“偏好设置”菜单选项，如图1.16所示，打开如图1.17所示的“偏好”对话框。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133125848.png" alt="image-20230827133125848" style="zoom:50%;" />

​														图1.16 选择“偏好设置”菜单选项

步骤05 在“偏好”对话框中单击“外观”选项，在“主界面”的“界面主题”下拉列表中选择Light，在“语法高亮主题”的下拉列表中选择Spyder，再单击对话框右下角的Apply按钮，单击OK按钮。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133152140.png" alt="image-20230827133152140" style="zoom:50%;" />

​														图1.17 “偏好”对话框

步骤06 弹出如图1.18所示的“信息”对话框，在其中单击Yes按钮即可重启Spyder，重启后界面变得更加明亮。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133216188.png" alt="image-20230827133216188" style="zoom:33%;" />

​														图1.18 “信息”对话框



## 1.5 Spyder(Anaconda3)窗口介绍

Spyder(Anaconda3)窗口如图1.19所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133244075.png" alt="image-20230827133244075" style="zoom:50%;" />

​														图1.19 Spyder (Anaconda3)窗口

### 1.菜单栏

菜单栏(Menu bar)包括文件、编辑、查找、源代码、运行、调试、控制台、项目、工具、查看、帮助等菜单，如图1.20所示。通过菜单可以使用Spyder的各项功能。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133326857.png" alt="image-20230827133326857" style="zoom:50%;" />

​														图1.20 菜单栏

### 2.工具栏

工具栏(Tools bar)：提供了Spyder中常用功能的快捷操作按钮（图标按钮），如图1.21所示。用户单击图标按钮即可执行相应的功能，将鼠标光标悬停在某个图标按钮上可以获取相应的功能说明。工具栏中各个图标按钮及其功能说明如表1.1所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133413243.png" alt="image-20230827133413243" style="zoom:50%;" />

​														图1.21 工具栏

表1.1 工具栏图标按钮及其功能说明

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133432394.png" alt="image-20230827133432394" style="zoom:50%;" />

其中最为常用的是￼“运行文件”<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827101443182.png" alt="image-20230827101443182" style="zoom:33%;" />以及￼<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827101528233.png" alt="image-20230827101528233" style="zoom:33%;" />“运行选定的代码或当前行”。两者的区别在于，“运行文件”是运行整个代码编辑区内的所有代码，而“运行选定的代码或当前行”是运行选中的一行或多行代码。

### 3.路径窗口

路径窗口(Python path)显示文件当前所在的路径，通过其下拉列表以及后面的两个图标<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827101613815.png" alt="image-20230827101613815" style="zoom:33%;" />￼“浏览工作目录”和<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827101817262.png" alt="image-20230827101817262" style="zoom:33%;" />￼“切换到上级目录”可以选择文件路径，如图1.22所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133523272.png" alt="image-20230827133523272" style="zoom:50%;" />

​														图1.22 路径窗口

### 4.代码编辑区

代码编辑区(Editor)如图1.23所示，这是最为重要的窗口，是编写Python代码的窗口，左边的行号区域显示代码所在行。
￼<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133543800.png" alt="image-20230827133543800" style="zoom:50%;" />

​														图1.23 代码编辑区(Editor)窗口

### 5.变量管理器

变量管理器(Variable explorer)如图1.24所示，可以在此查看代码运行后载入或计算生成的变量，包括变量的名称、类型、大小、值等属性。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827133611366.png" alt="image-20230827133611366" style="zoom:50%;" />

​														图1.24 “变量管理器”窗口

变量管理器、帮助、绘图、文件共用一个窗口，通过选项卡之间的切换来实现变换。

### 6.帮助

帮助(Help)功能是非常重要的，当用户不了解某代码的含义或者需要深度了解其具体用法及参数选择信息时，就需要查看相应代码的帮助信息，对于初学者来说更是如此。帮助信息会在代码编辑区的一个对象之后自动显示出来。实现方法是：在菜单栏依次单击“工具”→“偏好设置”→“帮助”菜单选项，勾选其中的全部复选框，如图1.25所示，激活自动显示帮助信息的功能。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134011794.png" alt="image-20230827134011794" style="zoom:50%;" />

​														图1.25 激活自动显示帮助信息的功能

设置完成后，如果用户想要了解LinearRegression用法，可以把鼠标光标放到代码编辑区中的代码LinearRegression上面，就会自动出现有关它的帮助信息，如图1.26所示。用户可通过阅读这些信息掌握LinearRegression的具体用法、参数选择等。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134031690.png" alt="image-20230827134031690" style="zoom:50%;" />

​														图1.26 “LinearRegression”有关的帮助信息1

用户还可以通过在代码编辑区中按Ctrl+选中对象来获得该对象的帮助信息。例如在图1.26中，用户可先按住键盘上的Ctrl键，然后将鼠标光标移至代码LinearRegression处，待出现手形鼠标指针后单击该代码，即可出现如图1.27所示的帮助信息。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134054477.png" alt="image-20230827134054477" style="zoom:50%;" />

​														图1.27 “LinearRegression”有关的帮助信息2

### 7.绘图

绘图窗口展示代码运行后产生的图形。“绘图”窗口如图1.28所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134116591.png" alt="image-20230827134116591" style="zoom:50%;" />

​														图1.28 “绘图”窗口

最上面的￼<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134144557.png" alt="image-20230827134144557" style="zoom:50%;" />提供了绘图常用快捷操作对应的图标按钮，用户单击图标按钮即可执行相应绘图的操作，将鼠标光标悬停在某个图标按钮上可以获取该图标按钮的功能说明。“绘图”窗口中各图标按钮及功能说明如表1.2所示。



表1.2 “绘图”窗口图标按钮及功能说明

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134216625.png" alt="image-20230827134216625" style="zoom:50%;" />



## 8.文件查看器

文件查看器(File explorer)可以方便地查看当前文件路径下的文件。文件查看器中“文件”窗口如图1.29所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134239791.png" alt="image-20230827134239791" style="zoom:50%;" />

​														图1.29 “文件”窗口

### 9.IPython控制台

IPython控制台(IPython console)类似Stata中的命令行窗格，可以一行行地交互执行。如图1.30所示，当用户选中代码编辑区的代码来执行时，控制台中就会将这些被执行的代码以In[ ]展示，执行结果以out[ ]展示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134307325.png" alt="image-20230827134307325" style="zoom:50%;" />

​														图1.30 IPython控制台
IPython控制台和代码的执行历史共用一个窗格，可通过选项卡进行切换。

### 10.历史

历史(History)本质上是一种日志，按时间顺序记录输入Spyder控制台的每个命令，如图1.31所示。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134331524.png" alt="image-20230827134331524" style="zoom:50%;" />

​															图1.31 历史窗格记录日志

在实际应用中，大多数情形下都是首先在代码编辑区逐行输入代码，完成代码编写；然后针对需要执行的代码，单击<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827101528233.png" alt="image-20230827101528233" style="zoom:33%;" />￼图标按钮来运行这些选定的代码；最后在IPython控制台中查看代码执行结果，其中属于绘制图形的代码运行结果将在“绘图”窗口进行展示。在IPython控制台中右击，即可弹出如图1.32所示的菜单，通过选择菜单选项，可以复制(Copy)、粘贴(Paste)运行结果，也可将运行结果导出为HTML/XML(Save as HTML/XML)或打印(Print)输出，以便将结果应用到论文写作中或作为工作成果等。

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827134406383.png" alt="image-20230827134406383" style="zoom: 33%;" />

​															图1.32 右击IPython控制台后弹出的快捷菜单



# 2 安装开发环境过程中遇到的问题

## 2.1 安装好了anaconda，spyder不启动

| 报错信息：                                                   |
| ------------------------------------------------------------ |
| C:\anaconda\Lib\site-packages\paramiko\transport.py:219: CryptographyDeprecationWarning: Blowfish has been deprecated<br/>"class": algorithms.Blowfish,<br/>Bad file descriptor (C:\ci\zeromq_1616055400030\work\src\epoll.cpp:100) |

把报错信息输入搜索引擎，如：baidu.com, 或者 bing.com。查到，https://blog.csdn.net/weixin_44670018/article/details/130400188

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827132425379.png" alt="image-20230827132425379" style="zoom: 33%;" />



如法操作后，问题变成

| 报错信息：                                                   |
| ------------------------------------------------------------ |
| Bad file descriptor (C:\ci\zeromq_1616055400030\work\src\epoll.cpp:100) |

继续搜索引擎，查到，https://stackoverflow.com/questions/65733680/bad-file-descriptor-c-ci-zeromq-1602704446950-work-src-epoll-cpp100

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827132623841.png" alt="image-20230827132623841" style="zoom:33%;" />

https://blog.csdn.net/weixin_45150180/article/details/131135570

<img src="https://raw.githubusercontent.com/GMyhf/img/main/img/image-20230827132642792.png" alt="image-20230827132642792" style="zoom:33%;" />

如法操作，已经可以启动 Spyder 了。
