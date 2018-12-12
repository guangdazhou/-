## Day05.Boolean&None&Number&List&Tuple 

### 一、布尔值和空值

#### 1.布尔值

> 一个布尔类型的变量一般有两个值，True,False
>
> 作用：用于分支和循环语句中作为条件判断
>
> 代码演示：
>
> ```Python
> #Boolean
> b1 = True
> b2 = False
>
> #条件表达式或者逻辑表达式结果都是布尔值
> print(4 > 5)
> print(1 and 0)
> ```

#### 2.空值

> Python中的一种特殊的数据类型，使用None表示
>
> 区别与0：0是数字类型，None本身就是一种数据类型
>
> 代码演示：
>
> ```Python
> #空值
> n = None
> print(n)   #None
> ```

### 二、数字类型Number

#### 1.分类

##### 1.1整数

> 可以处理Python中任意大小的整型
>
> 代码演示：
>
> ```Python
> num1 = 10
> num2 = num1
> print(num1,num2)
>
> #1.可以连续定义多个同种类型的变量,初始值相同
> num3 = num4 = num5 = 100
>
> #2.同时定义多个变量，初始值不同
> num6,num7 = 60,70
> print(num6,num7)
>
> #3.可以交换两个变量的值【掌握】
> #自己实现
> nn1 = 22
> nn2 = 33
> temp = nn1
> nn1 = nn2
> nn2 = temp
> print(nn1,nn2)
>
> n1 = 22
> n2 = 33
> print(n1,n2)   #22  33
> n1,n2 = n2,n1
> print(n1,n2)
>
> #4.获取变量在内存中的地址
> print(id(num1),id(num2))
> ```

##### 1.2浮点数

> 由整数部分和小数部分组成
>
> 注意：浮点数在计算机中运算的时候可能会出现四舍五入

##### 1.3复数

> 由实数部分和虚数部分组成
>
> 表示形式：a + bj或者complex(a,b)

#### 2.数字类型转换

> int(x):将x转换为整数
>
> float(x)：将x转换为一个浮点数
>
> 代码演示：
>
> ```Python
> print(int(1.9))   #1   取整
> print(float(1))   #1.0
> print(int("123"))   #123
> print(float("12.3")) #12.3
>
> #使用int或者float进行转换的时候，如果字符串中出现特殊符号，则转换失败
> #print(int("abc123"))   #ValueError: invalid literal for int() with base 10: 'abc123'
>
> print(int("+123"))   #123，当做数学上的正负号
> #print(int("12+3"))   #ValueError: invalid literal for int() with base 10: '12+3'
> print(int("-123"))  #-123
> #print(int("12-3"))  #ValueError: invalid literal for int() with base 10: '12-3'
> ```

#### 3.系统功能

##### 3.1数学功能

> abs(x):  absolute 求x的绝对值
>
> max():求最大值
>
> min()：求最小值
>
> pow(n,m):求一个数的多少次幂
>
> round(x，n):返回浮点数x的四舍五入值,如果给出n值，则表示舍入到小数点后几位
>
> 代码演示：
>
> ```Python
> print(abs(-10))
>
> print(max(23,34,6,56,57,6))
> print(min(23,34,6,56,57,6))
>
> print(pow(3,5))
>
> print(round(3.456))   #3
> print(round(3.656))   #4
> print(round(3.656,2))  #3.66
> print(round(3.646,1))   #3.6
> ```
>
> 导入math模块，math.功能名()
>
> 代码演示：
>
> ```Python
> #以下的功能必须导入math模块
> import  math
>
> #使用格式：math.功能名称
>
> #19向上取整
> print(math.ceil(18.1))
> print(math.ceil(18.9))
>
> #18向下取整
> print(math.floor(18.1))
> print(math.floor(18.9))
>
> #求平方
> print(pow(3,2))
> #开平方【掌握】
> print(math.sqrt(9))
>
> #获取整数部分和小数部分，得到的结果为元组
> print(math.modf(22.3))
> ```

##### 3.2随机数random【掌握】

> 代码演示：
>
> ```Python
> import random
>
> #1.random.choice(列表)  从指定列表中随机选择一个元素出来
> #指定列表
> num1 = random.choice([1,3,5,7,9])
> print(num1)
>
> #列表生成器
> num2 = random.choice(range(5))   #等价于[0,1,2,3,4]
> print(num2)
>
> #使用字符串，相当于使用了元素为字母的列表
> num3 = random.choice("hello")  #等价于["h","e","l","l","o"]
> print(num3)
>
> #需求;产生一个4~10之间的随机数
> print(random.choice([4,5,6,7,8,9,10]))
> print(random.choice(range(4,11)))
>
> #2.random.randrange(start,end,step)
> """
> start:指定范围的开始值，包含在范围内，默认为0
> end:指定范围的结束值，不包含在范围内
> step:步长，指定的递增基数，默认为1
> """
>
> #需求1：从1~100之间选取一个奇数随机数
> print(random.choice(range(1,100,2)))
> print(random.randrange(1,100,2))
> #需求2：生成一个0~99之间的随机数
> print(random.randrange(100))
>
> #3.random.random()   获取0~1之间的随机数，结果为浮点型
> n = random.random()
> #需求：保留小数点后两位
> print(round(n,2))
>
> #需求1：获取4~10之间的随机数
> n1 = random.random() * 6 + 4
> """
> [0,1] * 6 --------->[0,6]
> [0,6] + 4 -------->[4,10]
> """
>
> #4.将列表中的元素进行随机排序【了解】
> list1 = [23,5435,4,6]
> random.shuffle(list1)
> print(list1)
>
> #5.随机生成一个实数，它在[3,9]范围内，结果为浮点型
> print(random.uniform(3,9))
>
> #需求：求50~100之间的随机数，包括浮点数
> n2 = random.uniform(50,100)
> ```

##### 3.3三角函数功能【了解】



### 三.List列表的功能【掌握】

#### list列表的增删改查

代码演示：

```python
# 功能的使用：列表名.功能的名字()
# 一、添加元素
# 1.append()   追加，在列表的末尾添加元素
# 特点：是在原列表的基础上操作的
list12 = [1,2,3,4,5]
print(list12)
# 追加单个元素
list12.append(6)
# 追加多个元素,不能直接追加，通过列表的形式追加，形成了一个二维列表
list12.append([7,8])
print(list12)

# 2.extend()   扩展，在列表的末尾添加元素
# list12.extend(9)   TypeError: 'int' object is not iterable
list12.extend([9,10])
print(list12)
# 注意：append可以添加单个元素，但是extend不可以
# append添加多个元素的时候，以整个列表的形式添加进去；但是，extend只添加元素

# 3.insert()   插入 ,在指定的索引处插入一个元素,后面的其他元素向后顺延
# insert(索引，插入的数据)
list13 = [1,2,3,4,5]
print(list13)
# 需求：在索引为2的位置插入一个数字100
list13.insert(2,100)
print(list13)

# 将整个列表作为一个整体，插入到原列表中
list13.insert(2,[7,8])
print(list13)

# 二、删除元素
# 1.pop()    弹出，移除列表中指定索引处的元素
list14 = [1,2,3,4,5]
print(list14)
# 注意1：默认移除的是最后一个元素
# 注意2：返回的是被移除的数据

result14 = list14.pop()
print(list14)  #[1, 2, 3, 4]
print(result14)   #5

print(list14.pop(1))
print(list14)

# 2.remove()  移除   特点;移除指定元素在列表中匹配到的第一个元素【从左往右】
# remove(元素值)
list15 = [1,2,3,4,5,4,6,4]
print(list15)
list15.remove(4)
print(list15)

# 3.clear()      清除  清除列表中的所有的元素，原列表变为空列表
list16 = [25,36,673]
print(list16)
list16.clear()
print(list16)

# 三、获取
# 直接使用功能：  功能名称(列表)
# 1.len()    length,长度，获取列表的长度或者获取列表中元素的个数
list17 = [425.74,8,58679,7,65,65,64,6]
# 索引的取值范围：0~len(list17) - 1
length = len(list17)
print(length)

# 2.max()  获取列表中的最大值
print(max(list17))

# 3.min() 获取列表中的最小值
print(min(list17))

# 4.index()     索引,从列表中匹配到的第一个指定元素的索引值
# index(元素值)
list18 = [10,20,30,40,50,30,40,50]
inx1 = list18.index(30)
print(inx1)   #2
inx2 = list18.index(50)
print(inx2)   #4

# 5.count()   个数，查找指定元素在列表中出现的次数
print(list18.count(50))   #2

# 四、其他用法
# 1.reverse()      反转，将列表中的元素倒序输出
list19 = [10,20,30,40,50]
# 注意;在列表的内部进行反转，并没有生成新的列表
list19.reverse()
print(list19)

# 2.sort()    排序,默认为升序排序   注意：在列表的内部操作
list20 = [34,65,768,23]
# 升序
# list20.sort()
# 降序
list20.sort(reverse=True)
print(list20)

# 3.sorted()  排序,默认为升序排序   注意：生成一个新的列表
list21 = [34,65,768,23]
# 升序
# list22 = sorted(list21)
# print(list22)
# 降序
list23 = sorted(list21,reverse=True)
print(list23)

# 按照元素的长度来进行排序
list00 = ["abc","hello","g","fhekfgjahgjkq"]
list24 = sorted(list00,key=len)
print(list24)

# 4.拷贝【面试题】
list25 = [23,3,546]
list26 = list25
list26[1] = 100
print(list25)    #[23, 100, 546]
print(list26)    #[23, 100, 546]
print(id(list25))
print(id(list26))

# 浅拷贝copy
list27 = [23,3,546]
list28 = list27.copy()
list28[1] = 200
print(list27)
print(list28)
print(id(list27))
print(id(list28))

# 深拷贝deepcopy
list1 = [23,3,[4,5]]
list2 = copy.deepcopy(list1)

# 练习：remove()
list30 = [23,435,5656,6767,435,23,23,54,64,5676,23,23,23]
# 需求：移除列表中指定的所有的元素，例如：23
"""
list30.remove(23)
print(list30)
list30.remove(23)
print(list30)
list30.remove(23)
print(list30)
list30.remove(23)
print(list30)
list30.remove(23)
print(list30)
"""

# 定义一个变量，用于记录元素的位置【索引】
# 问题：remove功能是在列表的内部操作的
num = 0
# length = len(list30)
all  = list30.count(23)
while num < all:
    #依据：remove每次删除的第一次匹配的元素【从左到右】
    list30.remove(23)
    num += 1
print(list30)
```



### 四、tuple元组

#### 1.概述

> 和列表相似，本质上是一种有序的集合
>
> 元组和列表的不同之处：
>
> ​	a.列表:[]     元组：()
>
> ​	b.列表中的元素可以进行增加和删除操作，但是，元组中的元素不能修改【元素：一旦被初始化，将不能发生改变】

#### 2.创建元组

> 创建列表:
>
> ​	创建空列表：list1 = []
>
> ​	创建有元素的列表：list1 = [元素1，元素2，。。。。。]
>
> 创建元组
>
> ​	创建空元组：tuple1 = ()
>
> ​	创建有元素的元组：tuple1 = (元素1，元素2，。。。。)
>
> 代码演示：
>
> ```Python
> #创建空元组：
> tuple1 = ()
>
> #创建有元素的元组：
> tuple2 = (10,20,30)
>
> #在元组中可以存储不同类型的数据
> tuple3 = ("hello",True,100)
>
> #注意：创建只有一个元素的元组
> #按照下面的方式书写，表示定义了一个整型的变量，初始值为1
> tuple4 = (1)
> tuple4 = 1
> #为了消除歧义，修改如下：
> tuple4 = (1,)
>
> num1 = 10
> num2 = (10)
> print(num1,num2)
> ```

#### 3.元组元素的访问（和list列表类似）

> 代码演示：
>
> ```Python
> #元组元素的访问
> #格式：元组名[索引],和列表完全相同
> tuple1 = (10,20,30,40,50)
> #1.获取元素值
> print(tuple1[2])
> #获取元组中的最后一个元素
> print(tuple1[4])
> #print(tuple1[5])  #IndexError: tuple index out of range  索引越界
>
> #正数表示从前往后获取，负数表示从后往前获取
> print(tuple1[-1])
> print(tuple1[-2])
> print(tuple1[-5])
> # print(tuple1[-6])   #IndexError: tuple index out of range  索引越界
>
> #2.修改元素值----->不能修改，本质原因不能修改元素的地址
> #和列表不同的地方：元组的元素值不能随意的更改
> #tuple1[1] = 100
> tuple2 = (1,35,54,[4,5,6])
> #获取元组中列表中的元素
> print(tuple2)   #(1, 35, 54, [4, 5, 6])
> tuple2[3][1] = 50
> print(tuple2)  #(1, 35, 54, [4, 50, 6])
>
> #3.删除元组
> tuple3 = (53,6,7,76)
> del tuple3
> ```

#### 4.元组操作

> 代码演示：
>
> ```Python
> #1.元组组合
> # + 
> tuple1 = (3,43,5,4)
> tuple2 = (3,5,45,4)
> print(tuple1 + tuple2)
>
> #2.元组重复
> # *
> print(tuple1 * 3)
>
> #注意：元组组合和元组重复得到的是一个新的元组，原来的元组并没有发生任何改变
>
> #3.判断元素是否在元组中
> #成员运算符
> # in  not in
> print(100 in tuple1)
> print(100 not in  tuple1)
>
> # 4.元组截取【切片】
> tuple3 = (1,23,43,54,54,656,57,6)
> print(tuple3[2:4])
> print(tuple3[2:])
> print(tuple3[:4])
>
> ```

#### 5. 元组功能

> 代码演示：
>
> ```Python
> #1.获取元组的元素个数
> tuple1 = (54,3,5,46,56)
> print(len(tuple1))
>
> #2.获取元组中元素的最大值和最小值
> print(max(tuple1))
> print(min(tuple1))
>
>
> #3.元组和列表之间的相互转换:取长补短
> #3.1   元组-----》列表
> #list()
> list1 = list(tuple1)    #int()   float()
> print(list1)
>
> #3.2  列表 --> 元组
> #tuple()
> list2 = [34,5,46,4]
> tuple2 = tuple(list2)
> print(tuple2)
>
> #4.遍历元组
> #4.1直接遍历元素
> for element in tuple1:
>     print(element)
>
> #4.2遍历索引
> for index in range(len(tuple1)):
>     print(tuple1[index])
>
> #4.3同时遍历索引和元素
> for i,num in enumerate(tuple1):
>     print(i,num)
> ```

#### 6.二维元组

> 代码演示：
>
> ```Python
> #当做一维元组进行处理，实质：一维元组中的元素为一个一维元组
> tuple1 = ((2,43,5),(54,65,6),(5,54,54,54))
> print(tuple1[1][1])
>
> #遍历二维列表或者二维元组的思路：嵌套循环
> #遍历外层元组
> for element in tuple1:
>   	#遍历内层元组
>     for num in elment:
>       print(num)
> ```




