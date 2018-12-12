## Day07 字符串&JSON&算法

### 一、字符串操作

##### 6.4填充

> 代码演示：
>
> ```Python
> #5.填充【了解】
> #center（width[,fillchar]）  返回一个指定宽度的居中字符串，width是填充之后整个字符串的长度，fillchar为需要填充的字符串，默认使用空格填充
> str1 = "hello"
> print(str1.center(20))
> print(str1.center(10,"*"))
>
> #ljust（width[,fillchar]） 返回一个指定宽度的字符串，将原字符串居左对齐，width是填充之后整个字符串的长度
> print(str1.ljust(40,"%"))
>
> #rjust width[,fillchar]）  返回一个指定宽度的字符串，将原字符串居右对齐，width是填充之后整个字符串的长度
> print(str1.rjust(40,"%"))
>
> #zfill（width）   返回一个指定宽度的字符串,将原字符串居右对齐,剩余的部分使用的数字0填充
> print(str1.zfill(40))
> ```

##### 6.5查找

> 代码演示：
>
> ```Python
> #6.查找【掌握】
> str2 = "abcdefhello123hello"
> #find（str[,start,end]）  从左到右依次检测，str是否在原字符串中，，也可以指定查找的范围
> #特点;得到的子字符串第一次出现的开始字符的下标，如果查找不到则返回-1
> print(str2.find("hello"))    #6
> print(str2.find("e"))
> print(str2.find("yyy"))    #-1
> print(str2.find("e",3,10))
>
> #rfind(str[,start,end]）   类似于find，从右向左进行检测
> print(str2.rfind("hello"))  #14
>
> #index   和find的使用基本相同，唯一的区别在于如果子字符串查找不到，find返回-1，而index则直接报错
> print(str2.index("hello"))
> #print(str2.index("yyy"))   #ValueError: substring not found
>
> #rindex  和rfind的使用基本相同
>
> #max(str)   获取str中最大的字母【在字典中的顺序】
> #"abcdefhello123hello"
> print(max(str2))
>
> str3 = "46732647"
> print(max(str3))
>
> #min（str）  获取str中最小的字母【在字典中的顺序】
> ```

##### 6.6提取

> 代码演示：
>
> ```Python
> #7.提取字符串
> #strip(str)    使用str作为条件提取字符串，除了两头指定的字符串
> str1 = "********today is *********a good day*******"
> print(str1.strip("*"))   #today is *********a good day
>
> #lstrip(str)    提取字符串，除了左边的指定字符串
> str11 = "********today is *********a good day*******"
> print(str11.lstrip("*"))
>
> #rstrip()
> str12 = "********today is *********a good day*******"
> print(str12.rstrip("*"))
> ```

##### 6.7分割和合并

> 代码演示：
>
> ```Python
> #8.分割和合并【掌握：正则表达式】
> #split(str[,num)]   将str作为分隔符切割原字符串，结果为一个列表,如果制定了num，则仅使用num个字符串截取原字符串
> str3 = "today is a good day"
> print(str3.split(" "))   #['today', 'is', 'a', 'good', 'day']
> print(str3.split(" ",2))   #['today', 'is', 'a good day']
>
> #splitlines(flag)   按照换行符【\n，\r,\r\n】分隔，结果为列表
> #flag:False或者不写，则表示忽略换行符；如果True，则表示保留换行符
> str4 = """today
> is
> a
> good
> day
> """
> print(str4.splitlines(True))   #['today', 'is', 'a', 'good', 'day']    ['today\n', 'is\n', 'a\n', 'good\n', 'day\n']
>
> #join(list)    将原字符串作为连接符号，将列表中的元素分别连接起来，结果为字符串，作用和split是相反的
> str5 = "*"
> list1 = ["shangsan","lisi","jack"]
> print(str5.join(list1))
> ```

##### 6.8替换

> 代码演示：
>
> ```Python
> #9.替换
> #replace(old,new[,max])   用new的字符串将old的字符串替换掉.max表示可以替换的最大次数【从左到右】
> str1 = "this is a easy test test test test"
> print(str1.replace("test","exam"))
> print(str1.replace("test","exam",2))
>
> #使用场景：在一定情境下，可以实现字符串的简单加密，加密规则可以自定义
> #maketrans()   创建字符映射的转换表,结果为字典，通过key:value的方式
> #translate(table)
>
> t = str.maketrans("aco","123")
> print(t)   #{97: 49, 99: 50, 111: 51}
>
> str2 = "today is a good day"
> print(str2.translate(t))  #t3d1y is 1 g33d d1y
> ```

##### 6.9判断

> 代码演示：
>
> ```Python
> #10.判断
> #isalpha()   如果字符串中至少包含一个字符并且所有的字符都是字母，才返回True
> print("".isalpha())
> print("abc".isalpha())
> print("abc123".isalpha())   #False
>
> #isalnum   如果字符串中至少包含一个字符并且所有字符都是字母或者数字的时候才返回True
> print("".isalnum())   #False
> print("abc".isalnum())
> print("abc123".isalnum())
> print("123".isalnum())
> print("1abc".isalnum())
> print("1abc￥".isalnum())  #False
>
> #isupper  如果字符串中至少包含一个字符并且出现的字母必须是大写字母才返回True，数字的出现没有影响
> print("".isupper())
> print("aBC".isupper())
> print("123A".isupper())   #True
> print("abc".isupper())
>
> #islower
>
> #istitle   每个单词的首字母必须全部大写才返回True
> print("Good Day".istitle())
> print("good Day".istitle())
>
> #isdigit() 【掌握】   如果字符串中只包含数字，则返回True
> print("abc123".isdigit())
> print("2364".isdigit())
>
> #需求：将用户从控制台输入的字符串转化为整型【全数字】
> str = input()
> if str.isdigit():
>     int(str)
>     print("yes")
>
> ```

##### 6.10前缀和后缀

> 代码演示：
>
> ```Python
> #11.前缀和后缀【掌握】  子字符串是连续的
> #startswith
> str1 = "helloPython"
> print(str1.startswith("hello"))
>
> #endswith
> print(str1.endswith("on"))
> ```

##### 6.11编解码

> 代码演示：
>
> ```Python
> #12.字符串编码和解码
> #注意：主要针对的是中文
> #encode()   默认的编码格式为utf-8
> str2 = "this is 千锋教育"
> print(str2.encode())
> print(str2.encode("utf-8"))
> print(str2.encode("gbk"))
>
> #decode()   bytes对象
> #\xe5\x8d\x83\xe9\x94\x8b\xe6\x95\x99\xe8\x82\xb2
> #print(r"\xe5\x8d\x83\xe9\x94\x8b\xe6\x95\x99\xe8\x82\xb2".decode())    错误
> ```

##### 6.12 ASCII码转换

> 代码演示：
>
> ```Python
> #13。ASCII吗的转换
> #ord()
> print(ord("A"))
> print(ord("0"))
>
> #chr()
> print(chr(65))
> print(chr(110))
> ```

#### 7.自己练习

> 需求一：
>
> ```Python
> #需求1：统计下面字符串中每个单词的出现次数，并生成一个字典，单词为key，次数为value
> """
> 实现思路：
> 1.以空格为切割符切割字符串
> 2.遍历第一步中得到的list
> 3.将单词提取出来，去一个字典中判断
> 4.如果单词不存在，就以该单词作为key，1作为value存储到字典中
> 5.如果单词存在，将对应key的value递增1【修改指定key的value】
> """
> str1 = "tomorrow is sunny day tomorrow is sunny day tomorrow is wind day"
> dict1 = {}    #创建一个空字典，备用
> list1 = str1.split(" ")    #切割字符串
> #方式一：get（）
> """
> for word in list1:      #遍历列表
>     value = dict1.get(word)    #None
>     if value == None:
>         dict1[word] = 1      #往字典中添加键值对
>     else:
>         dict1[word] += 1     #给字典中指定key的value修改值
>
> print(dict1)
> """
> #方式二：成员运算符
> for word in list1:      #遍历列表
>     if word not in dict1:
>         dict1[word] = 1
>     else:
>         dict1[word] += 1
> print(dict1)
> ```

> 需求二：
>
> ```Python
>
> #需求2：从控制台输入一个字符串，表示时间，编写程序，获取这个时间的下一秒
> #例如输入：12:23:33    输出12:23:34
> """
> 思路分析：
> 1.将字符串切割，得到时分秒的数据
> 2.得到时间的下一秒：给秒加1
> 3.12:23:59----》12:24:00    当秒数增加完之后为60的时候，分钟需要增加1，秒数应该置为0
> 4.12:59:59----》13:00：00   当分钟增加完之后为60的时候，时钟需要增加1，分钟置为0
> 5.当时钟增加完之后为24的时候，时钟置为0
> """
> timeStr = input("请输入正确格式的时间：")
>
> timeList = timeStr.split(":")
> h = int(timeList[0])
> m = int(timeList[1])
> s = int(timeList[2])
>
> s += 1
>
> if s == 60:
>     m += 1
>     s = 0
>     if m == 60:
>         h += 1
>         m = 0
>         if h == 24:
>             h = 0
>
> print("%.2d:%.2d:%.2d"%(h,m,s))
>
> #%.2f
> ```

> 需求三：
>
> ```Python
> #需求3：实现简单的购物车功能
> """
> 思路分析
> 1.引导用户选择商品【提供】
> 2.引导用户输入金额
> 3.加入购物车
> 4.查看购物车，计算余额
> """
> product_list  = [
>     ("Mac",10000),
>     ("kindle",500),
>     ("iphone x",8000),
>     ("bike",3000)
> ]
>
> saving = input("请输入金额：")
>
> #定义一个列表，充当购物车
> shopping_car  = []
>
> #判断金额是否是数字
> if saving.isdigit():
>     #将saving转换为整数
>     saving = int(saving)
>
>     while True:
>         #打印商品信息，提供给用户选择
>         for index,p in enumerate(product_list):
>             print(index,":",p)
>
>         #引导用户选择商品
>         choice = input("请输入商品的编号[输入q退出]:")
>
>         #判断编号是否合法
>         if choice.isdigit():
>             choice = int(choice)
>
>             if choice >= 0 and choice < len(product_list):
>                 #将用户选择的商品从product_list取出来
>                 item = product_list[choice]   #元组
>
>                 #item[0] :商品名称   item[1]：商品的价格
>                 if item[1] <= saving:
>
>                     #saving减少
>                     saving -= item[1]
>
>                     #需要将商品添加到购物车对应的list中
>                     shopping_car.append(item)
>
>                 else:
>                     print("余额不足")
>
>             else:
>                 print("不存在的编号")
>         elif choice == "q":
>             print("-------你已经购买如下商品：-------")
>             for i in shopping_car:
>                 print(i)
>
>             print("你还剩余%d元钱"%(saving))
>
>             break
>         else:
>             print("不合法的编号")
> else:
>     print("invalid input")
> ```

### 二、JSON

​	JSON : 一种数据格式，数据的表现形式， 常用于前后端进行交互的数据格式

​	JSON的表现形式可以分为： json字符串和json对象

```python
import json

# JSON解析: JSON字符串 => JSON对象
# json.loads()
json_str = '{"name": "张三", "age": 33}'  # 里面写双引号，外面写单引号
json_obj = json.loads(json_str)
print(json_obj)  # {'name': '张三', 'age': 33}
print(type(json_obj))  # <class 'dict'>

# JSON序列化: JSON对象 => JSON字符串
# json.dumps()
json_obj = {"name": "张三", "age": 33}
json_str = json.dumps(json_obj)
print(json_str)  # '{"name": "\u5f20\u4e09", "age": 33}'
print(type(json_str))  # <class 'str'>
```
### 三、简单算法【掌握】

代码演示：

> ```Python
> #需求：求列表中元素的最大值，不能借助于系统功能
> list1 = [5,54,6,774,43,44]
>
> #方式一
> #定义一个变量，用于记录最大值【参照物】
> #思路：如果要操作列表，初始值一般使用列表的第一个元素
> maxValue = list1[0]
> for num in list1:
>     if num > maxValue:
>         #给maxValue重新赋值
>         maxValue = num
> print(maxValue)
>
> #方式二
> maxValue1 = list1[0]
> for index in range(1,len(list1)):
>     if list1[index]  > maxValue1:
>         maxValue1 = list1[index]
>
> print(maxValue1)
>
> #需求升级：获取最大值以及最大值对应的下标
> maxValue2 = list1[0]
> maxIndex = 0
> for index in range(1, len(list1)):
>     if list1[index] > maxValue2:
>         maxValue2 = list1[index]
>         maxIndex = index
>
> print(maxValue2,maxIndex)
> ```

#### 1.排序

##### 1.1冒泡排序

> 排序思路：比较两个相邻下标对应的元素，如果以升序为例的话，则最大值出现在最右边
>
> 代码实现：
>
> ```Python
> list1 = [34,5,46,23,23,54,65,54]
>
> #升序排序：冒泡
> #外层循环：控制比较的轮数
> for out in range(0,len(list1) - 1):
>     #内层循环;控制每一轮比较的次数，兼顾参与比较的下标
>     for inner in range(0,len(list1) - out - 1):
>         if list1[inner] > list1[inner + 1]:
>             #方式一
>             temp = list1[inner]
>             list1[inner] = list1[inner + 1]
>             list1[inner + 1] = temp
>
>             #方式二：简写
>             #list1[inner],list1[inner + 1] = list1[inner + 1],list1[inner]
> print(list1)
>
> """"
> for inner in range(0,len(list1) - out):
> IndexError: list index out of range
>
> 原因分析：当out取值为0的时候，inner的取值范围为0~len(list1) - 1
>           当使用if list1[inner] > list1[inner + 1]:，当inner取值为len(list1) - 1，此时inner+1变成了len(list1)
> 解决办法：for inner in range(0,len(list1) - out - 1):
>         当out取值为0的时候，此时inner的取值范围：0~len(list1) - 2
>         假设元素个数为5，inner当取值为3的时候，inner+1取值为4，正好是索引的最大值的边界
> """
> ```

##### 1.2选择排序

> 排序思路：固定一个下标，然后拿这个下标对应的元素和其他的元素依次进行比较，最小值出现在最左边
>
> 代码演示：
>
> ```Python
> list1 = [34,5,46,23,23,54,65,54]
>
> #排序方式：选择排序
>
> #外层循环：控制比较的轮数
> for out in range(0,len(list1) - 1):
>     #内层循环：控制每一轮比较的次数，兼顾参与比较的下标
>     for inner in range(out + 1,len(list1)):
>         """
>             0-1  0-2  0-3  0-4
>             1-2  1-3  1-4
>             2-3  2-4
>             3-4
>         """
>         #out表示小的下标，inner的最小值out+1
>         if list1[out] > list1[inner]:
>             temp = list1[out]
>             list1[out] = list1[inner]
>             list1[inner] = temp
> print(list1)
>
> #注意：注意区分冒泡和选择的边界问题
> ```





