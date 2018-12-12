## Day14 多态&文件操作

### 一、多态

#### 1.概念

> 一种事物的多种体现形式，函数的重写其实就是多态的一种体现
>
> 在Python中，多态指的是父类的引用指向子类的对象
>
> 代码演示：
>
> ```Python
> #父类
> class Animal(object):
>     pass
>
> #子类
> class Dog(Animal):
>     pass
>
> class Cat(Animal):
>     pass
>
> #定义变量
> a = []   #a是list类型
> b = Animal()  #b是Animal类型
> c = Cat()  #c是Cat类型
>
> #isinstance():判断一个对象是否属于某种类型【系统还是自定义的类型】
> print(isinstance(a,list))
> print(isinstance(b,Animal))
> print(isinstance(c,Cat))
>
> print(isinstance(c,Animal))  #True
>
> print(isinstance(b,Dog))   #False
>
> #结论：子类对象可以是父类类型，但是，父类的对象不能是子类类型
> ```

#### 2.使用

> 案例：人可以喂猫，喂狗
>
> 思路：
>
> a.定义动物类【父类】
>
> b.定义子类，继承自动物类
>
> c.定义人类
>
> d.使用多态，优化
>
> 代码演示：
>
> duoTaiDemo.py文件
>
> ```Python
> from duotai.person import Person
> from duotai.cat import Cat
> from duotai.dog import Dog
>
> #1.创建一个Person的对象
> p = Person()
>
> #2.创建一个Cat的对象
> c = Cat("小白")
>
> #3.人执行自己的行为
> p.feedAnimal(c)
>
> d = Dog("旺财")
> p.feedAnimal(d)
> ```
>
> person.py文件
>
> ```Python
> class Person(object):
>     """
>     def feedCat(self,cat):
>         print("喂猫:",cat.name)
>         cat.eat()
>     def feedDog(self,dog):
>         print("喂猫:",dog.name)
>         dog.eat()
>     """
>     #多态
>     #ani被当做父类的引用 ，当传参的时候，实参是一个子类对象的时候，则体现出了 多态的应用
>     def feedAnimal(self,ani):   #ani = c   c = Cat("")
>         print("喂动物:", ani.name)
>         ani.eat()
> ```
>
> animal.py文件
>
> ```Python
> class Animal(object):
>     def __init__(self,name):
>         self.name = name
>
>     def eat(self):
>         print("eating")
> ```
>
> cat.py文件
>
> ```Python
> from duotai.animal import Animal
>
> class Cat(Animal):
>     def __init__(self,name):
>         super(Cat,self).__init__(name)
> ```
>
> dog.py文件
>
> ```Python
> from duotai.animal import Animal
>
> class Dog(Animal):
>     def __init__(self,name):
>         super(Dog,self).__init__(name)
> ```
>
> 总结：
>
> ​	简化代码，提高代码的可读性，可维护性

### 二、获取对象信息

> type()   isintance()     dir()
>
> 代码演示：
>
> ```Python
> #1.type() :判断一个对象所属的类型
> num = 10
> print(type(num))
> print(type("hello"))
>
> class Check(object):
>     pass
> c = Check()
> print(type(c))
>
> #使用==判断type返回的结果
> print(type(12) == type(57))  #True
> print(type(12) == type("57"))  #False
>
> #使用type返回的结果和数据类型直接判断
> print(type(12) == int)
>
> #2.isintance()  :判断一个对象是否属于某种指定的数据类型
> #自定义的类中
> class Dog(object):
>     pass
>
> d = Dog()
> print(isinstance(d,Dog))
> print(isinstance([1,2,4],list))
>
> #特殊用法：可以判断一个对象是否属于多种数据类型中的某一种
> print(isinstance([1,2,4],(tuple,list)))
>
> #3.dir()  :列出指定对象中所包含的所有的内容【成员变量，成员方法】
> dict = {}
> print(dir(dict))
>
> print(dir("abc"))
>
> print(dir(d))
> ```

### 三、类中特殊的属性和方法

#### 1.实例属性和类属性

##### 1.1实例属性和类属性的区别【面试题】

> a.定义的位置不同，类属性时直接定义在类中，实例属性定义在构造函数中
>
> b.访问的方式不同，类属性使用类名直接访问，实例属性使用对象访问
>
> c.在内存中出现的时机不同，类属性随着类的出现而出现，实例属性随着对象的出现而出现
>
> d.优先级不同，实例属性的优先级高于类属性
>
> 代码演示：
>
> ```Python
> class Person(object):
>     #1.定义位置
>     #类属性：直接定义在类中
>     name = "abc"
>     age = 0
>
>     def __init__(self,name):
>         #实例属性：定义在构造函数中
>         self.name = name
>
>
> #2.访问方式
> print(Person.name)  #类属性：类名.属性 或者 对象.属性
>
> p = Person("hello")
> print(p.name)   #实例属性：对象.属性
>
> #3.优先级不同：实例属性的优先级高于类属性
> print(p.name)   #hello
>
> #4.不同对象的类属性在内存中是不是同一块空间？----->不是
> p1 = Person("小白")
> p2 = Person("小红")
> print(p1.age)
> print(p2.age)
> p1.age = 33
> print(p1.age)
> print(p2.age)
> print(id(p1.age))
> print(id(p2.age))
> """
> 0
> 0
> 33
> 0
> 1420404832
> 1420403776
> """
>
> #注意：尽量避免类属性和实例属性的重名
>
> #删除属性【类属性，实例属性】
> del p1.age
> ```

##### 1.2动态添加属性和方法

> 代码演示：
>
> ```Python
> from  types import MethodType
>
>
> class Person(object):
>     #__slots__ = ("name","age")
>     pass
>
>
> #1.动态添加属性
> per = Person()
> str = "fjsgh"
> per.name = str
>
> #2.动态添加方法
> def say(self):
>     print("fhsj")
> """
> per.test = say
> per.test(per)
> """
>
> #弊端：违背了普通函数定义
> #解决方案：MethodType类，存在于types模块下
>
> #类似于偏函数
> #参数：函数名，对象
> #作用：在现有函数的基础上生成了一个对象【新的函数】，赋值给成员变量，则认为给对象添加了一个成员方法
> per.test = MethodType(say,per)
> per.test()
> ```

#### 2.类方法和静态方法

> 类方法：使用@classmethod装饰器修饰的方法，被称为类方法，可以通过类名调用，也可以通过对象调用，但是一般情况下使用类名调用
>
> 静态方法：使用@staticmethod装饰器修饰的方法，被称为静态方法，可以通过类名调用，也可以通过对象调用，但是一般情况下使用类名调用
>
> 代码演示：
>
> ```Python
> class Test(object):
>     #1.类属性
>     age = 100
>
>     def __init__(self,name):
>         #2.实例属性
>         self.name = name
>
>     #3.成员方法,通过对象调用
>     #必须有一个参数，这个参数一般情况下为self，self代表是当前对象
>     def func(self):
>         print("func")
>
>     #4.类方法
>     """
>     a.必须有一个参数，这个参数一般情况下为cls，cls代表的是当前类
>     b.类方法是属于整个类的，并不是属于某个具体的对象，在类方法中禁止出现self
>     c.在类方法的内部，可以直接通过cls调用当前类中的属性和方法
>     d.在类方法的内部，可以通过cls创建对象
>     """
>     @classmethod
>     def test(cls):
>         print("类方法")
>         print(cls)   #<class 'methodDemo01.Test'>
>         print(cls.age)
>
>         #6
>         #注意：cls完全当做当前类使用
>         c = cls("hello")
>         c.func()
>
>     #7.静态方法
>     @staticmethod
>     def show():
>         print("静态方法")
>
> t = Test("hjfsh")
> t.func()
>
> #5,.调用类方法
> Test.test()   #类名.类方法的名称()
> t.test()       #对象.类方法的名称()
>
> #7。调用静态方法
> Test.show()
> t.show()
> ```
>
> 总结：实例方法【成员方法】、类方法以及静态方法之间的区别
>
> a.语法上
>
> ​	实例方法：第一个参数一般为self，在调用的时候不需要传参，代表的是当前对象【实例】
>
> ​	静态方法：没有特殊要求
>
> ​	类方法：第一个参数必须为cls，代表的是当前类
>
> b.在调用上
>
> ​	实例方法：只能对象
>
> ​	静态方法：对象  或者 类
>
> ​	类方法：对象 或者 类
>
> c.在继承上【相同点】
>
> ​	实例方法、静态方法、类方法：当子类中出现和父类中重名的函数的时候，子类对象调用的是子类中的方法【重写】
>
> 代码演示：
>
> ```Python
> class SuperClass(object):
>     @staticmethod
>     def show():
>         print("父类中的静态方法")
>
>     @classmethod
>     def check(cls):
>         print("父类中的类方法")
>
> class SubClass(SuperClass):
>     pass
>
> s = SubClass()
> s.show()
> s.check()
> ```
>
> 注意：注意区分三种函数的书写形式，在使用，没有绝对的区分	

#### 3.类常用属性

> ```
> __name__
> 	通过类名访问，获取类名字符串
> 	不能通过对象访问，否则报错
> 	
> __dict__
> 	通过类名访问，获取指定类的信息【类方法，静态方法，成员方法】，返回的是一个字典
> 	通过对象访问，获取的该对象的信息【所有的属性和值】，，返回的是一个字典
> 	
> __bases__
> 	通过类名访问，查看指定类的所有的父类【基类】
> ```

> 代码演示：
>
> ```Python
> class Animal(object):
>     def __init__(self,arg):
>         super(Animal, self).__init__()
>         self.arg = arg
>
>
> class Tiger(Animal):
>     age = 100
>     height = 200
>
>     def __init__(self,name):
>         #super(Tiger, self).__init__(name)
>         self.name = name
>
>     def haha(self):
>         print("haha")
>
>     @classmethod
>     def test(cls):
>         print("cls")
>
>     @staticmethod
>     def show():
>         print("show")
>
>
> if __name__ == "__main__":
>
>     #1.__name__
>     print(Tiger.__name__)  #Tiger
>
>     t = Tiger("")
>     #print(t.__name__)  #AttributeError: 'Tiger' object has no attribute '__name__'
>
>     #2.__dict__
>     print(Tiger.__dict__)  #类属性，所有的方法
>     print(t.__dict__)   #实例属性
>
>     #3.__bases__，获取指定类的所有的父类，返回的是一个元组
>     print(Tiger.__bases__)
> ```

### 四、运算符重载【了解】

> 运算符重载其实就是函数重写
>
> 代码演示：
>
> ```Python
> print(1 + 1)
> print("1" + "1")
> #print("1" + 1)
> #不同的数据类型进行加法运算得到的是不同的解释
>
> #思考问题：两个对象相加？
> class Person(object):
>     def __init__(self,num):
>         self.num = num
>
>     def __str__(self):
>         return "num=" + str(self.num)
>
>     def __add__(self, other):
>         #两个对象相加得到的结果仍然为一个对象
>         return Person(self.num + other.num)   #Peson(30)
>
>
> p1 = Person(10)
> p2 = Person(20)
>
> print(p1)  #10
> print(p2)  #20
>
> print(p1 + p2)  #30
>
> #p1 + p2----->p1.__add__(p2),
> ```

### 五、文件读写

#### 1.概念

> 在Python中，通过打开文件生成一个文件对象【文件描述符】操作磁盘上的文件，操作主要由文件读写

#### 2.普通文件的读写

> 普通文件包含：txt文件，图片，视频，音频等

##### 2.1读文件

> 操作步骤：
>
> ​	a.打开文件：open（）
>
> ​	b.读取文件内容：read()
>
> ​	c.关闭文件:close()
>
> 说明：最后一定不要忘了文件关闭，避免系统资源的浪费【因为一个文件对象会占用系统资源】
>
> 代码演示：
>
> ```Python
> #一、打开文件
> """
> open(path,flag[,encoding,errors])
> path:指定文件的路径【绝对路径和相对路径】
> flag:打开文件的方式
>     r:只读、
>     rb:read binary,以二进制的方式打开，只读【图片，视频，音频等】
>     r+:读写
>
>     w:只能写入
>     wb:以二进制的方式打开，只能写入【图片，视频，音频等】
>     w+:读写
>
>     a:append,如果一个文件不为空，当写入的时候不会覆盖掉原来的内容
> encoding：编码格式：gbk,utf-8
> errors:错误处理
> """
> path = r"C:\Users\Administrator\Desktop\SZ-Python\Day15\笔记\致橡树.txt"
> #调用open函数，得到了文件对象
> f = open(path,"r",encoding="gbk")
>
> """
> 注意：
> a.以r的方式打开文件时，encoding是不是必须出现
>     如果文件格式为gbk,可以不加encoding="gbk"
>     如果文件格式为utf-8,必须添加encoding="utf-8"
> b。如果打开的文件是图片，音频或者视频等，打开方式采用rb,但是，此时，不能添加encoding="xxx"
> """
>
> #二、读取文件内容
> #1.读取全部内容   ***********
> #str = f.read()
> #print(str)
>
> #2.读取指定的字符数
> #注意：如果每一行的结尾有个"\n",也被识别成字符
> """
> str1 = f.read(2)
> print(str1)
> str1 = f.read(2)
> print(str1)
> str1 = f.read(2)
> print(str1)
>
>
> #3.读取整行，不管该行有多少个字符    *********
> str2 = f.readline()
> print(str2)
> str2 = f.readline()
> print(str2)
> """
>
> #4.读取一行中的指定的字符
> #str3 = f.readline(3)
> #print(str3)
>
> #5.读取全部的内容，返回的结果为一个列表，每一行数据为一个元素
> #注意：如果指明参数，则表示读取指定个数的字符
> str4 = f.readlines()
> print(str4)
>
> #三、关闭文件
> f.close()
> ```
>
> 其他写法：
>
> ```Python
> #1.读取文件的简写形式
> #with open()  as 变量
>
> #好处：可以自动关闭文件，避免忘记关闭文件导致的资源浪费
> path = "致橡树.txt"
> with open(path,"r",encoding="gbk") as f:
>     result = f.read()
>     print(result)
>
> #2.
> try:
>     f1 = open(path,"r",encoding="gbk")
>     print(f1.read())
> except FileNotFoundError as e:
>     print("文件路径错误",e)
> except LookupError as e:
>     print("未知的编码格式",e)
> except UnicodeDecodeError as e:
>     print("读取文件解码错误",e)
> finally:
>     if f1:
>         f1.close()
> ```
>
> 读取图片等二进制文件：
>
> ```Python
> #1.
> f = open("dog.jpg","rb")
>
> result = f.read()
> print(result)
>
> f.close()
>
> #2
> with open("dog.jpg","rb") as f1:
>     f1.read()
>
> #注意：读取的是二进制文件，读取到的内容为\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x0
> ```

##### 2.2写文件

> 操作步骤：
>
> ​	a.打开文件：open()
>
> ​	b.写入数据：write()
>
> ​	c.刷新管道【内部缓冲区】：flush()
>
> ​	d.关闭文件：close()
>
> 代码演示：
>
> ```Python
> path = "file1.txt"
>
> #1.打开文件
> #注意：写入文件的时候，文件可以不存在，当open的时候会自动创建文件
> #读取文件的时候，文件必须先存在，才能open
> f = open(path,"w",encoding="utf-8")
>
> #2.写入数据
> #注意：将数据写入文件的时候，默认是没有换行的，如果向换行，则可以手动添加\n
> f.write("Python1805高薪就业，走上人生巅峰")
>
> #3.刷新数据缓冲区
> #作用：加速数据的流动，保证缓冲区的流畅
> f.flush()
>
> #4.关闭文件
> f.close()
>
> #简写形式
> with open(path,"w",encoding="utf-8") as f1:
>     f1.write("hello")
>     f.flush()
> ```

#### 3.编码和解码

> 编码：encode，字符串类型转换为字节类型
>
> 解码：decode，字节类型转换为字符串类型
>
> 注意：编码和解码的格式必须保持一致
>
> 代码演示：
>
> ```Python
> path = "file2.txt"
>
> #编码:字符串----》字节
> with open(path,"wb") as f1:
>     str = "today is a good day 今天是个好天气"
>     f1.write(str.encode("utf-8"))
>
> #解码：字节----->字符串
> with open(path,"rb") as f2:
>     data = f2.read()
>     print(data)
>     print(type(data))
>
>     newData = data.decode("utf-8")
>     print(newData)
>     print(type(newData))
> ```

#### 4.csv文件的读写

> csv:逗号分隔值【Comma Separated  Values】
>
> 一种文件格式，.csv,本质是一个纯文本文件，可以作为不同程序之间数据交互的格式
>
> 打开方式:记事本，excel

##### 4.1读文件

> 代码演示：
>
> ```Python
> #C:\Users\Administrator\Desktop\SZ-Python\Day15\笔记\text.csv
> import  csv
>
>
> #方式一：三部曲
> def readCsv1(path):
>     #1.打开文件
>     csvFile = open(path,"r")
>
>     #2.将文件对象封装成可迭代对象
>     reader= csv.reader(csvFile)
>
>     #3.读取文件内容
>     #遍历出来的结果为列表
>     for item in reader:
>         print(item)
>
>     #4.关闭文件
>     csvFile.close()
>
> readCsv1(r"C:\Users\Administrator\Desktop\SZ-Python\Day15\笔记\text.csv")
>
> #方式二：简写
> def readCsv2(path):
>     with open(path,"r") as f:
>         reader = csv.reader(f)
>         for item in reader:
>             print(item)
>
> readCsv2(r"C:\Users\Administrator\Desktop\SZ-Python\Day15\笔记\text.csv")
> ```

##### 4.2写文件

> 代码演示：
>
> ```Python
> import  csv
>
> #1.从列表写入数据
> def writeCsv1(path):
>     infoList = [['username', 'password', 'age', 'address'],['zhangsan', 'abc123', '17', 'china'],['lisi', 'aaabbb', '10', 'england']]
>
>     #1.打开文件
>     #注意：如果不设置newline，每一行会自动有一个空行
>     csvFile = open(path,"w",newline="")
>
>     #2.将文件对象封装成一个可迭代对象
>     writer = csv.writer(csvFile)
>
>     #3.写入数据
>     for i in range(len(infoList)):
>         writer.writerow(infoList[i])
>
>     #4.关闭文件
>     csvFile.close()
>
> writeCsv1("file3.csv")
>
> #2.从字典写入文件
> def writeCsv2(path):
>     dic = {"张三":123,"李四":456,"王麻子":789}
>     csvFile = open(path, "w", newline="")
>     writer = csv.writer(csvFile)
>
>     for key in dic:
>         writer.writerow([key,dic[key]])
>
>     csvFile.close()
>
> #3.简写形式
> def writeCsv3(path):
>     infoList = [['username', 'password', 'age', 'address'], ['zhangsan', 'abc123', '17', 'china'],
>                 ['lisi', 'aaabbb', '10', 'england']]
>     with open(path, "w", newline="") as f:
>         writer = csv.writer(f)
>
>         for rowData in infoList:
>             writer.writerow(rowData)
> ```



