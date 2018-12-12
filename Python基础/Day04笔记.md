 ## Day04. List列表的基本操作&for循环和while循环

### 一、list列表

#### 1.概述

> 变量：使用变量存储数据，但是，缺点:一个变量每次只能存储一个数据 
>
> 思考：如果一次性存储多个数据，怎么做？
>
> 解决：采用列表 
>
> 作用：列表相当于是一个容器，可以同时存储多个数据 
>
> 本质：列表是一种有序的集合 
>
> 说明：有序指的就是有顺序【数据的存放的顺序和底层存储的顺序是相同的】
>
> 代码演示： 
>
> ```Python
> #需求：求5个人的平均年龄
> age1 = 10
> age2 = 13
> age3 = 16
> age4 = 39
> age5 = 20
>
> #list
> #在栈空间中有一个变量【列表的名字】
> #变量指向了堆空间中的一个列表，列表中存储了5个变量
> ```

#### 2.创建列表

> num = 10
>
> 语法：变量名 = 列表
>
> ​	   列表名称 = [数据1，数据2.。。。。。]
>
> 说明：使用[]表示创建列表
>
> ​	   列表中存储的数据被称为元素
>
> ​	   列表中的元素被从头到尾自动进行了编号，编号从0开始，这个编号被称为索引，角标或者下标
>
> ​	   索引的取值范围：0~元素的个数 - 1【列表的长度 - 1】
>
> ​	   超过索引的范围：列表越界
>
> 代码演示：
>
> ```Python
> #语法：列表名【标识符】 = [元素1，元素2.。。。。]
> #1.创建列表
> #1.1创建一个空列表
> list1 = []
> print(list1)
>
> #1.2创建一个带有元素的列表
> list2 = [52,463,6,473,53,65]
> print(list2)
>
> #2.思考问题：列表中能不能存储不同类型的数据？
> list3 = ['abc',10,3.14,True]
> print(list3)
>
> #注意：将需要存储的数据放到列表中，不需要考虑列表的大小，如果数据量很大的情况，在进行存储数据的时候，列表底层自动扩容
> ```

#### 3.列表元素的访问

> 访问方式：通过索引访问列表中的元素【有序，索引：决定了元素在内存中的位置】

##### 3.1获取元素

> 语法：列表名[索引]
>
> 代码演示：
>
> ```Python
> #元素的访问
> #创建列表
> list1 = [5,51,6,76,98,3]
>
> #需求：获取索引为3的位置上的元素
> num = list1[3]
> print(num)
> print(list1[3])
> ```

##### 3.2修改元素

> 语法：列表名[索引] = 值
>
> 注意：列表中存储的是其实是变量，所以可以随时修改值
>
> 代码演示：
>
> ```Python
> #需求：将索引为1位置上的元素修改为100
> print(list1[1])
> list1[1] = 100
> print(list1[1])
>
> #问题：超过索引的取值范围，则会出现索引越界的错误
> #解决办法：检查列表索引的取值范围
> #print(list1[6])   #IndexError: list index out of range   索引越界
> ```

#### 4.列表的基本操作

##### 4.1列表元素组合

> 代码演示：
>
> ```Python
> #列表组合【合并】
> #使用加号
> list1 = [432,435,6]
> list2 = ["abc","dhfj"]
> list3 = list1 + list2
> print(list3)  #[432, 435, 6, 'abc', 'dhfj']
> ```

##### 4.2列表元素重复

> 代码演示：
>
> ```Python
> #列表元素的重复
> #使用乘号
> list4 = [1,2,3]
> list5 = list4 * 3
> print(list5)  #[1, 2, 3, 1, 2, 3, 1, 2, 3]
> ```

##### 4.3判断元素是否在列表中

> 代码演示：
>
> ```Python
> #判断指定元素是否在指定列表中
> #成员运算符   in  not in
> list6 = [32,43,546,"hello",False]
> print(43 in list6)
> print(43 not in list6)
> print(100 in list6)
> print(100 not in list6)
> """
> 工作原理：使用指定数据在列表中和每个元素进行比对，只要元素内容相等，则说明存在的
> True
> False
> False
> True
> """
> ```

##### 4.4列表截取【切片】

> 代码演示：
>
> ```Python
> #列表的截取
> list7 = [23,34,6,57,6878,3,5,4,76,7]
> print(list7[4])
>
> #使用冒号:
> #截取指定的区间：列表名[开始索引：结束索引],特点：包头不包尾    前闭后开区间
> print(list7[2:6])
>
> #从开头截取到指定索引，特点：不包含指定的索引
> print(list7[0:6])
> print(list7[:6])
>
> #从指定索引截取到结尾
> #注意：因为包头不包尾，所以如果要取到最后一个元素，可以超过索引的范围，不会报错
> print(list7[4:20])
> print(list7[4:])
> ```

### 二、for循环和while循环【掌握】

#### 1.用法

> 语法：
>
> 初始化表达式
>
> while  条件表达式：
>
> ​	循环体
>
> ​	循环之后操作表达式
>
> for 变量名 in 列表：
>
> ​	循环体
>
> 功能：for-in循环主要用在列表中【实现列表的遍历：依次访问列表中的每一个元素，获取元素值】
>
> 说明;在列表中按照顺序获取元素值获取出来，赋值给变量，再执行循环体，如此往复，直到遍历到列表的最后一个元素
>
> 代码演示：
>
> ```Python
> list1 = ["lisi","zhangsan","hack"]
>
> print(list1[0])
> print(list1[1])
> print(list1[2])
>
> #for循环
> for name in list1:
>     print(name)
>
> #while循环
> index = 0
> while index < len(list1):
>     print(list1[index])
>     index += 1
>
> #注意：for语句中操作的是列表中的元素，while语句中操作的是索引
>
> #else分支,当for循环执行结束之后，else分支肯定会被执行
> for name1 in list1:
>     print(name1)
> else:
>     print("Ok")
> ```

#### 2.range

> range([start,]end[,step])      注：[]表示start和step可写可不写
>
> start:开始数字
>
> end；结束数字
>
> step；步长
>
> start默认为0，step默认为1 
>
> 功能：生成具有一定规律的列表
>
> 代码演示：
>
> ```Python
> #range()
> """
> range([start,]end[,step])
> l例如：
> range(100)    可以生成一个0~99的整数列表【不包含100】
> range（1,100）  可以生成一个1~99的整数列表
> range(1,100,2)  可以生成一个1~99之间的奇数列表
> """
>
> #需求1：计算1~100之间所有整数的和
> num1 = 1
> sum1 = 0
> while num1 <= 100:
>     sum1 += num1
>     num1 += 1
>
> sum11 = 0
> #借助于列表生成器生成一个1~100之间所有整数的列表，然后使用for循环进行遍历这个列表
> for x in range(1,101):
>     sum11 += x
>
> #需求2：计算1~100之间所有偶数的和
> num2 = 1
> sum2 = 0
> while num2 <= 100:
>     if num2 % 2 == 0:
>         sum2 += num2
>     num2 += 1
>
> num2 = 0
> sum2 = 0
> while num2 <= 100:
>     sum2 += num2
>     num2 += 2
>
> sum22 = 0
> for y in range(0,101,2):
>     sum22 += y
> ```

#### 3.遍历列表

> 代码演示：
>
> ```Python
> #列表的遍历
>
> list2 = [23,54,6,45,56]
> #1.直接操作的是元素
> for num in list2:
>     print(num)
>
> #2.通过索引的方式操作元素
> #思路：使用列表生成器生成一个和索引有关的列表 0~len(list2) -1
> for index in range(len(list2)):
>     #index中保存的是0,1,2....
>     n = list2[index]
>     print(n)
>
> #3.同时遍历索引和元素
> #enumerate  枚举【类似于一个容器】
> #index,n1----->索引，元素值
> for index,n1 in enumerate(list2):
>     print(index,n1)
> ```

#### 4.嵌套for循环

> 代码演示：
>
> ```Python
> #需求：打印九九乘法表
>
> #while实现
> line = 1
> while line <= 9:
>     colum = 1
>     while colum <= line:
>         print("%dx%d=%d"%(colum,line,line*colum),end=" ")
>         colum += 1
>     print("")
>     line += 1
>
>
> #for实现
> #外层循环：控制行
> for i in range(1,10):
>     #内层循环：控制列
>     for j in range(1,i + 1):
>         print("%dx%d=%d"%(j,i,i*j),end=" ")
>     print("")
> ```

5.练习

> 代码演示：
>
> ```Python
> #1.显示列表list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]中索引为奇数的元素
> #思路：
> list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
> #1.先获取所有的索引【列表生成器】
> indexList = range(len(list1))   #[0,1,2,3,4,....]
>
> #2.遍历和索引有关的列表
> for index in indexList:
>
>     #4.将为奇数的索引获取出来
>     if index % 2 == 1:
>
>         #3.将索引对应的元素获取出来
>         str = list1[index]
>         print(str)
>
> #2.将属于list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]，但不属于list2 = ["Sun","Wed","Thu","Sat"]的所有的元素组成一个新的列表list3
>
> #in   not in
> list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
> list2 = ["Sun","Wed","Thu","Sat"]
> list3 = []
>
> #1.遍历list1
> for str1 in list1:
>     #str1
>     #2.判断从list1中取出的元素是不是不在list2中
>     if str1 not in list2:
>         #3.将str1添加到list3中
>         list3.append(str1)
>
> print(list3)
>
>
> #3.已知列表list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]，removeList = ["Sun","Wed","Thu","Sat"],
> #将属于removeList的元素从list1中全部删除【注意：属于removeList，但不属于list1的直接忽略】
>
> #remove
> list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
> removeList = ["Sun","Wed","Thu","Sat"]
> """
> list1.remove(removeList[0])
> print(list1)
> list1.remove(removeList[1])
> print(list1)
> list1.remove(removeList[2])
> print(list1)
> list1.remove(removeList[3])
> print(list1)"""
>
> for i in range(len(removeList)):
>     list1.remove(removeList[i])
> print(list1)
> ```

### 三、break、continue和pass语句的使用

#### 1.break

> 作用:跳出循环【直接跳出整个循环，继续执行循环后面的代码】
>
> 代码演示：

```python
# break的使用
# 1.while
n = 0
while n < 5:
    print("n = %d"%(n))
    #print("n =" ,n)
    #注意：if语句充当的是一个条件判断
    if n == 3:
        break
    n += 1
print("over")

# 2.for
list1 = [1,2,3,4,5]
for x in list1:
    print("x = %d"%(x))
    if x == 3:
        break
# 结论：不管是while语句还是for语句，break的作用结束整个循环

# 3.特殊情况一
# 不管while中的条件是否满足，else分支都会被执行
# 思考问题：如果在while循环体中出现了break，else分支还会执行吗？-------不会
m = 0
while m < 3:
    print(m)
    if m == 1:
        break
    m += 1
else:
    print("else")

# 4.特殊情况二
# 当break使用在嵌套循环中的时候，结束的是当前循环【就近原则】
x = 0
y = 0
while x < 20:
    print("hello Python",x)
    x += 1
    while y < 5:
        print("hello Python~~~~",y)
        if y == 2:
            break
        y += 1
    #break

# 注意：break是一个关键字，使用的过程中，单独就可以成为一条语句，后面不能跟任何的变量或者语句

```

#### 2.continue

> 作用：跳出当前正在执行的循环，继续执行下一次循环
>
> 代码演示：

```python
# continue的使用
# 1.for
for i in range(10):
    print(i)
    if i == 3:
        continue
    print("*")

for i in range(10):
    print(i)
    if i == 3:
        break
    print("*")
# 总结：continue只是结束当前正在执行的循环，而break表示直接结束整个循环

# 2.while
"""
num = 0
while num < 10:
    print("num = %d"%(num))
    num += 1
    if num == 3:
        continue
"""
num = 0
while num < 10:
    if num == 3:
        num += 1
        continue
    print("num = %d" % (num))
    num += 1
```

#### 3.pass

> Python中的pass是一条空语句
>
> 作用：为了保持代码结构的完整性，pass不做任何操作，只是充当了一个占位语句，保证代码可以正常的运行起来
>
> 应用场景：if，while，for中使用，可以在代码块的部分不添加任何语句，代码正常运行
>
> 代码演示：

```python
while True:
    pass

print("over")
```

#### 4.自己练习

> 代码演示：

```python
# 需求;判断一个数是否是素数【质数】
# 方式一
num1 = int(input("请输入一个数："))
# 思路：一个数能被其他数整除，将次数记录下来
# 条件：在2~num1 - 1的范围内，找到一个数能将num1整除，count1 + 1

count1 = 0
for i in range(2,num1):
    #整除：求余【大数对小数求余】
    if num1 % i == 0:
        count1 += 1

if count1 == 0 and num1 != 1:
    print("是质数")
else:
    print("不是质数")

# 方式二：
# 思路：假设num2是质数，寻找不成立的条件【有数能被整除】将假设推翻掉
num2 = int(input("请输入一个数："))
# 定义一个布尔类型的变量，用于记录这个数是不是一个质数
is_prime  = True
for j in range(2,num2):
    if num2 % j == 0:
        is_prime = False
        break

if is_prime == True and num2 != 1:
    print("是质数")
else:
    print("不是质数")

```

