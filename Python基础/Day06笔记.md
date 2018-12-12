## Day06 Dict字典&Set集合&字符串

### 一、dict字典

#### 1.概述

> 思考问题：保存多个学生的成绩
>
> list1 = [65,7,8,99,100]
>
> tuple1 = (65,7,8,99,100)
>
> 存在的问题：无法学生和成绩的匹配
>
> 解决问题：字典，将学生姓名作为key，成绩作为value，进行存储，方便查找
>
> 本质：也只一种存储数据的方式，数据是以键值对的形式存储的，但是字典是无序的
>
> 优点：具有快速查找的优势

#### 2.key的特性

> a.字典中的key必须是唯一的
>
> b.字典中的key必须是不可变的
>
> ​	list是可变的，不能充当key		
>
> ​	tuple是不可变的，可以充当key，整数，字符串都可以充当key

#### 3.字典的创建

> 语法：字典名称 = {key1:value1,key2:value2,.......}
>
> 代码演示：
>
> ```Python
> #创建空字典
> dict1 = {}
>
> #创建带有键值对的字典
> dict2 = {"zhangsan":96,"lisi":60,"jack":80}
> print(dict2)
> ```

#### 4.元素访问【掌握】

##### 4.1 获取

> 语法：字典名[key]
>
> 代码演示：
>
> ```Python
> #字典中元素的访问
> dict1 = {"zhangsan":96,"lisi":60,"jack":80}
> #1.获取
> #通过key获取对应的value
> score = dict1["lisi"]
> print(score)
>
> #如果key不存在的时候，无法访问
> #print(dict1["tom"])  #KeyError: 'tom'
>
> #虽然key不存在，但是不会报错，返回的是None
> result = dict1.get("tom")
> print(result)
> if result == None:
>     print("key不存在")
> else:
>     print("key是存在的")
> ```

##### 4.2 添加

> 代码演示：
>
> ```Python
> #2.修改和添加
> print(dict1)
> #当key不存在的时候，表示添加一对键值对
> dict1["tom"] = 70
> print(dict1)
> #当key存在的时候，表示修改对应的value
> dict1["lisi"] = 88
> print(dict1)
> ```

##### 4.3 删除

> 代码演示：
>
> ```Python
> #3.删除
> #注意：删除指定的key，则对应的value也会随着被删除
> dict1.pop("lisi")
> print(dict1)
> ```

#### 5.字典的遍历【掌握】

> 代码演示：
>
> ```Python
> dict1 = {'zhangsan': 96, 'lisi': 88, 'jack': 80, 'tom': 70}
>
> #1.只获取key【掌握】
> for key in dict1:
>     #通过key获取value
>     value = dict1[key]
>     print(key,"=",value)
>
> #2.只获取value
> #将所有的value重新生成了一个列表
> list1 = dict1.values()
> print(list1)
> for value in list1:
>     print(value)
>
> #3.同时获取键值对的索引以及key
> for i,key in enumerate(dict1):
>     print(i,key)
>     print(dict1[key])
>
> #4.同时获取key和value【掌握】
> for key,value in dict1.items():
>     print(key,value)
> ```

#### 6.自己练习

> 代码演示：
>
> ```python
> #1.逐一显示指定字典中的所有键，并在显示结束之后输出总键数
> dict1= {"x":1,"y":2,"z":3}
> #count1 = 0
> for key in dict1:
>     print(key)
>     #count1 += 1
> else:
>     print(len(dict1))
>
> #2.list1 = [0,1,2,3,4,5,6],list2 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"].以list1中的元素作为key，
> # 以list2中的元组作为value生成一个新的字典dict2
> list1 = [0,1,2,3,4,5,6]
> list2 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
> dict2 = {}
> #{0:"Sun",1:"Mon".....}
>
> #定义一个变量，作为list1和list2的索引
> index = 0
>
> #前提：两个列表的长度相等
> if len(list1) == len(list2):
>
>     while index < len(list1):
>         #当字典中不存在某个key-value时，赋值于相当于添加一对键值对
>         dict2[list1[index]] = list2[index]    #dict2[0] = "Sun"
>         #为了循环可以在适当的时机停止下来，可以将list1和list2中的元素全部获取出来，赋值给字典
>         index += 1
>
> print(dict2)
> ```

### 二、set集合【了解】

#### 1.概述

> 和数学上的集合基本是一样的，
>
> 特点:不允许有重复元素，可以进行交集，并集，差集的运算
>
> 本质：无序，无重复元素的集合

#### 2.创建

> set(列表或者元组或者字典)
>
> 代码演示：
>
> ```Python
> #注意：set的创建需要借助于list和tuple
>
> #1.通过list创建set
> list1 = [432,5,5,46,65]
> s1 = set(list1)
> print(list1)
> print(s1)
>
> #注意1：set中会自动将重复元素过滤掉
>
> #2.通过tuple创建set
> tuple1 = (235,45,5,656,5)
> s2 = set(tuple1)
> print(tuple1)
> print(s2)
>
> #3.通过dict创建set
> dict1 = {1:"hello",2:"good"}
> s3 = set(dict1)
> print(dict1)   #{1: 'hello', 2: 'good'}
> print(s3)   #{1, 2}
>
> #注意2：set跟dict类似，都使用{}表示，但是与dict之间的区别在于：set中相当于只存储了一组key，没有value
> ```

#### 3.操作

##### 3.1添加

> 代码演示：
>
> ```Python
> #1.添加
> #add()   在set的末尾进行追加
> s1 = set([1,2,3,4,5])
> print(s1)
> s1.add(6)
> print(s1)
>
> #注意：如果元素已经存在，则添加失败
> s1.add(3)
> print(s1)
> #print(s1.add(3))
>
> #s1.add([7,8,9])   #TypeError: unhashable type: 'list'  list是可变的，set中的元素不能是list类型
> s1.add((7,8,9))
> #s1.add({1:"a"})  #TypeError: unhashable type: 'dict'  ，dict中的键值对可以改变，set中的元素不能是dict类型
> print(s1)
>
> #update()   插入【末尾添加】，打碎插入【直接将元组，列表中的元素添加到set中，将字符串中的字母作为小的字符串添加到set中】
> s2 = set([1,2,3,4,5])
> print(s2)
> s2.update([6,7,8])
> s2.update((9,10))
> s2.update("good")
> #注意：不能添加整型，因为整型不能使用for循环遍历
> #s2.update(11)   #TypeError: 'int' object is not iterable
> print(s2)
> ```

##### 3.2删除

> 代码演示：
>
> ```Python
> #2.删除
> #remove()
> s3 = set([1,2,3,4,5])
> print(s3)
> s3.remove(3)
> print(s3)
> ```

##### 3.3遍历

> 代码演示：
>
> ```Python
> #3.set的遍历
> s4 = set([1,2,3,4,5])
> for i in s4:
>     print(i)
>
> #注意：set是没有索引的，所以不能通过s4[2]获取元素，原因：set是无序的
> #print(s4[2])  #TypeError: 'set' object does not support indexing
>
> #注意：获取的是编号和元素值
> for i,num in enumerate(s4):
>     print(i,num)
> ```

##### 3.4交集和并集

> 代码演示：
>
> ```Python
> #4.交集和并集
> s4 = set([1,2,3])
> s5 = set([4,5,3])
>
> #交集：&【按位与】    and
> r1 = s4 & s5
> print(r1)
> print(type(r1))
>
> #并集:|【按位或】   or
> r2 = s4 | s5
> print(r2)
> ```

### 三、String字符串

#### 1.概述

> 由多个字母，数字，特殊字符组成的有限序列
>
> 在Python中，使用单引号或者双引号都可以表示字符串
>
> 注意:没有单符号的数据类型
>
> 'a'   "a"

#### 2.创建字符串

> 代码演示：
>
> ```Python
> str1 = "hello"
>
> str2 = "abc1234"
>
> str3 = "***fhhg%%%"
>
> str4 = "中文"
> ```

#### 3.字符串运算

> 代码演示：
>
> ```Python
> #1.+   字符串连接
> s1 = "welcome"
> s2 = " to China"
> print(s1 + s2)
>
> #注意：在Python中，使用+。只能是字符串和字符串之间。和其他数据类型使用的话不支持
> #print("abc" + 10)
> #print("123" + 1)
> #print(1 + "12" + 12)
> #print("hello" + True)
>
> #2. *   字符串重复
> s3 = "good"
> print(s3 * 3)
>
> #3.获取字符串中的某个字符
> """
> 类似于列表和元组的使用，通过索引来获取指定位置的字符
> 注意索引的取值范围【0~长度 - 1】，同样会出现索引越界
> 访问方式：字符串名称[索引]
> """
> s4 = "abcdef"
> print(s4[1])
> #print(s4[10])  #IndexError: string index out of range
>
> #获取字符串的长度：len()
> #遍历字符串,和list，tuple的用法完全相同
> for element in s4:
>     print(element)
> for index in range(0,len(s4)):
>     print(s4[index])
> for index,str in enumerate(s4):
>     print(index,str)
>
> #4.截取字符串【切片】
> str1 = "hello world"
> #指定区间
> print(str1[3:7])
> #从指定位置到结尾，包含指定位置
> print(str1[3:])
> #从开头到指定位置，但是不包含指定位置
> print(str1[:7])
>
> str2 = "abc123456"
> print(str2[2:5]) #c12
> print(str2[2:])  #c123456
> print(str2[2::2])  #c246
> print(str2[::2])   #ac246
> print(str2[::-1])  #654321cba   倒序
> print(str2[-3:-1])  #45   -1表示最后一个字符
>
> #5.判断一个子字符串是否在原字符串中
> #in  not in
> str3 = "today is a good day"
> print("good"  in str3)
> print("good1"  not in str3)
> ```

#### 4.格式化输出

> 通过%来改变后面字母或者数字的含义，%被称为占位符
>
> ​	%d          整数
>
> ​	%f		浮点型，特点：可以指定小数点后的位数
>
> ​	%s		字符串
>
> 代码演示：
>
> ```Python
> #6.格式化输出
> num = 10
> string1 = "hello"
> print("string1=",string1,"num=",num)
> #注意：变量的书写顺序尽量和前面字符串中出现的顺序保持一致
> print("string1=%s,num=%d"%(string1,num))
>
> f = 12.247
> print("string1=%s,num=%d,f=%f"%(string1,num,f))
> #需求：浮点数保留小数点后两位
> print("string1=%s,num=%d,f=%.2f"%(string1,num,f))    #round(12.247,2)
> ```

#### 5.常用转义字符

> 通过\来改变后面字母或者特殊字符的含义
>
> ​	\t  		相当于tab键
>
> ​	\n		相当于enter键
>
> ​	\b		相当于backspace
>
> 代码演示：
>
> ```Python
> #7.转义字符
> string2 = "hello\tworld"
> string21 = "hello   world"
> print(string2)
> print(string21)
>
> #换行：\n    多行注释
> string3 = "hello\nPython"
> string31 = """hello
> python2354623
> """
> print(string3)
> print(string31)
>
> #需求："hello"
> print("\"hello\"")
>
> #C:\Users\Administrator\Desktop\SZ-Python1805\Day6\视频
> print("C:\\Users\\Administrator\\Desktop")
> #注意;如果一个字符串中有多个字符需要转义，则可以在字符串的前面添加r,可以避免对字符串中的每个特殊字符进行转义
> print(r"C:\Users\Administrator\Desktop")
> ```

#### 6.常用功能

##### 6.1获取长度和次数

> 代码演示：
>
> ```Python
> #1.计算字符串长度  len
> #类似于list和tuple的中获取长度的用法
> str1 = "hfufhja"
> l = len(str1)
> print(l)
>
> #2,计算某个字符或者子字符串在原字符串中出现的次数   count
> str2 = "this is a good day good day"
> #count(str,[start,end])
> #在整个字符串中进行查找
> print(str2.count("day"))
> #在指定区间内进行查找
> print(str2.count("day",3,10))
> ```

##### 6.2大小写转换

> 代码演示：
>
> ```Python
> #注意：使用字符串中的功能，一般情况下，都是生成一个新的字符串，原字符串没有发生任何变化
> #3.大小写字母转换
> #lower()   将字符串中的大写字母转换为小写
> str31 = "Today Is a Good day"
> astr31 = str31.lower()
> print(astr31)
>
> #uppper()   将字符串中小写字母转换为大写
> str32 = "Today Is a Good day"
> astr32 = str2.upper()
> print(astr32)
>
> #swapcase()     将字符串中小写字母转换为大写，大写字母转换为小写
> str33 = "Today Is a Good day"
> astr33 = str33.swapcase()
> print(astr33)
>
> #capitalize()   将一句英文中首单词的首字母转化为大写，其他小写
> str34 = "today Is a Good day"
> astr34 = str34.capitalize()
> print(astr34)
>
> #title()       将一句英文中每个单词的首字母大写
> str35 = "today is a good day"
> astr35 = str35.title()
> print(astr35)
> ```

##### 6.3整数和字符串转换

> 代码演示：
>
> ```Python
> 4.字符串和数字之间的转换
> #int()     float()      str()
> #eval(str)   将str转换为有效的表达式，参与运算，并返回运算结果
> num1 = eval("123")
> print(num1)
> #print("123")
> print(type(num1))
> print(int("123"))
>
> #eval和int将+和-当做正负号处理
> print(eval("+123"))
> print(int("+123"))
> print(eval("-123"))
> print(int("-123"))
>
> #将12+3字符串转换为了有效的表达式，并运算了结果
> print(eval("12+3"))    #15
> #不成立
> #print(int("12+3"))   #ValueError: invalid literal for int() with base 10: '12+3'
>
> print(eval("12-3"))   #9
> #print(int("12-3"))    #ValueError: invalid literal for int() with base 10: '12-3'
>
> #print(eval("a123"))  #NameError: name 'a123' is not defined
> #print(int("a123"))  #ValueError: invalid literal for int() with base 10: 'a123'
>
> #总结：注意区分eval和int【eval：转换有效的表达式   int:将字符串转换为整型】
> ```

