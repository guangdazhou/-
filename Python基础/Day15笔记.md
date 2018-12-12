## Day15 异常处理&代码调试&单例模式

### 一、错误和异常

#### 1.概念

> 两种容易辨认的错误
>
> ​	语法错误：一些关于语法的错误【缩进】
>
> ​	异常：代码完全正确，但是，程序运行之后，会报出 的错误
>
> exception/error
>
> 代码演示：
>
> ```Python
> list1 = [23,54,6,6]
> print(list1[2])
> print(list1[3])
> print(list1[4])  
>
> print("over")
>
> """
> 6
> 6
> Traceback (most recent call last):
>   File "C:/Users/Administrator/Desktop/SZ-Python/Day15Code/textDemo01.py", line 4, in <module>
>     print(list1[4])
> IndexError: list index out of range
> """
> ```
>
> 异常特点：当程序在执行的过程中遇到异常，程序将会终止在出现异常的代码处，代码不会继续向下执行
>
> 解决问题：越过异常，保证后面的代码继续执行【实质：将异常暂时屏蔽起来，目的是为了让后面的代码的执行不受影响】

#### 2.常见的异常

> NameError:变量未被定义
>
> TypeError:类型错误
>
> IndexError:索引异常
>
> keyError:
>
> ValueError:
>
> AttributeError:属性异常
>
> ImportError:导入模块的时候路径异常
>
> SyntaxError:代码不能编译
>
> UnboundLocalError:试图访问一个还未被设置的局部变量

#### 3.异常处理方式【掌握】

> 捕获异常
>
> 抛出异常

##### 3.1捕获异常

##### try-except-else

> 语法：
>
> ​	try:
>
> ​		可能存在异常的代码
>
> ​	except 错误表示码 as 变量：
>
> ​		语句1
>
> ​	except 错误表示码 as 变量：
>
> ​		语句2
>
> ​	。。。
>
> ​	else:
>
> ​		语句n
>
> 说明：
>
> ​	a.try-except-else的用法类似于if-elif-else
>
> ​	b.else可有可无，根据具体的需求决定
>
> ​	c.try后面的代码块被称为监测区域【检测其中的代码是否存在异常】
>
> ​	d.工作原理：首先执行try中的语句，如果try中的语句没有异常，则直接跳过所有的except语句，执行else；如果try中的语句有异常，则去except分支中进行匹配错误码，如果匹配到了，则执行except后面的语句；如果没有except匹配，则异常仍然没有被拦截【屏蔽】
>
> 代码演示：
>
> ```Python
> #一、try-except-else的使用
>
> #1.except带有异常类型
> try:
>     print(10 / 0)
> except ZeroDivisionError as e:
>     print("被除数不能为0",e)
>
> print("~~~~")
> """
> 总结：
> a.try-except屏蔽了异常，保证后面的代码可以正常执行
> b.except ZeroDivisionError as e相当于声明了一个ZeroDivisionError类型的变量【对象】，变量e中携带了错误的信息
> """
>
> #2.try后面的except语句可以有多个
> class Person(object):
>     __slots__ = ("name")
> try:
>     p = Person()
>     p.age = 19
>
>     print(10 / 0)
> except AttributeError as e:
>     print("属性异常",e)
> except ZeroDivisionError as e:
>     print("被除数不能为0",e)
>
> print("over")
>
> """
> 总结：
> a.一个try语句后面可以有多个except分支
> b.不管try中的代码有多少个异常，except语句都只会被执行其中的一个，哪个异常处于try语句的前面，则先先执行对应的except语句
> c.后面的异常不会报错【未被执行到】
> """
>
> #3.except语句的后面可以不跟异常类型
> try:
>     print(10 / 0)
> except:
>     print("被除数不能为0")
>
>
> #4.一个except语句的后面可以跟多种异常的类型
> #注意：不同的异常类型使用元组表示
> try:
>     print(10 / 0)
> except (ZeroDivisionError,AttributeError):
>     print("出现了异常")
>
>
> #5.else分支
> try:
>     print(10 / 4)
> except ZeroDivisionError as e:
>     print("出现了异常",e)
> else:
>     print("hello")
>
> """
> 总结：
> a.如果try中的代码出现了 异常，则直接去匹配except，else分支不会被执行
> b.如果try中的代码没有出现异常，则try中的代码正常执行，except不会被执行，else分支才会被执行
> """
>
> #6.try中不仅可以直接处理异常，还可以处理一个函数中的异常
> def show():
>     x = 1 / 0
>
> try:
>     show()
> except:
>     print("出现了异常")
>
> #7.直接使用BaseException代替所有的异常
> try:
>     y = 10 / 0
> except BaseException as e:
>     print(e)
>
> """
> 总结：在Python中，所有的异常其实都是类，他们都有一个共同的父类BaseException，可以使用BaseException将所有异常“一网打尽”
> """
> ```

##### try-except-finally

> 语法：
>
> ​	try:
>
> ​		可能存在异常的代码
>
> ​	except 错误表示码 as 变量：
>
> ​		语句1
>
> ​	except 错误表示码 as 变量：
>
> ​		语句2
>
> ​	。。。
>
> ​	finally:
>
> ​		语句n
>
> 说明:不管try中的语句是否存在异常，不管异常是否匹配到了except语句，finally语句都会被执行
>
> 作用：表示定义清理行为，表示无论什么情况下都需要进行的操作
>
> 代码演示：
>
> ```Python
> #二、try-except-finally的使用
>
> #1.
> try:
>     print(10 / 5)
> except ZeroDivisionError as e:
>     print(e)
>
> finally:
>     print("finally被执行")
>
>
> #2.特殊情况
> #注意：当在try或者except中出现return语句时，finally语句仍然会被执行
> def show():
>     try:
>         print(10 / 0)
>         return
>     except ZeroDivisionError as e:
>         print(e)
>
>     finally:
>         print("finally被执行~~~~")
>
> show()
> ```

##### 3.2抛出异常

> raise抛出一个指定的异常对象
>
> 语法：raise 异常对象     或者  raise
>
> 说明：异常对象通过错误表示码创建，一般来说错误表示码越准确越好
>
> 代码演示：
>
> ```Python
> #raise的使用主要体现在自定义异常中
>
> #1.raise表示直接抛出一个异常对象【异常是肯定存在的】
> #创建对象的时候，参数表示对异常信息的描述
> try:
>     raise NameError("hjafhfja")
> except NameError as e:
>     print(e)
>
> print("over")
>
> """
> 总结：
> 通过raise抛出的异常，最终还是需要通过try-except处理
> """
>
> #2.如果通过raise抛出的异常在try中不想被处理，则可以通过raise直接向上抛出
> try:
>     raise NameError("hjafhfja")
> except NameError as e:
>     print(e)
>     raise
> ```

#### 4.assert断言

> 对某个问题做一个预测，如果预测成功，则获取结果；如果预测失败，则打印预测的信息
>
> 代码演示：
>
> ```Python
> def func(num,divNum):
>
>     #语法：assert表达式，当出现异常时的信息描述
>     #assert关键字的作用：预测表达式是否成立，如果成立，则执行后面的代码；如果不成立，则将异常的描述信息打印出来
>     assert (divNum != 0),"被除数不能为0"
>
>     return  num / divNum
>
> print(func(10,20))
> print(func(10,0))
> ```

#### 5.异常的嵌套

> 代码演示：
>
> ```Python
> #需求：去拉萨，乘坐各种交通工具
> print("我要去拉萨")
>
> try:
>     print("我准备乘飞机过去")
>     raise Exception("由于大雾，飞机不能起飞")
>     print("到拉萨了，拉萨真漂亮")
> except Exception as e:
>     print(e)
>     try:
>         print("我准备乘火车过去")
>         raise  Exception("由于大暴雨，铁路断了")
>         print("到拉萨了，拉萨真漂亮")
>     except Exception as e:
>         print(e)
>         print("我准备跑过去")
>         print("到拉萨了，拉萨真漂亮")
> ```

#### 6.自定义异常

> 实现思路：
>
> a.定义一个类，继承自Exception类
>
> b.书写构造函数，属性保存异常信息【调用父类的构造函数】
>
> c.重写__str__函数，打印异常的信息
>
> d.定义一个成员函数，用来处理自己的异常
>
> 代码演示：
>
> ```Python
> class MyException(Exception):
>     def __init__(self,msg):
>         super(MyException,self).__init__()
>         self.msg = msg
>
>     def __str__(self):
>         return self.msg
>
>     def handle(self):
>         print("出现了异常")
>
> try:
>      raise MyException("自己异常的类型")
> except MyException as e:
>      print(e)
>      e.handle()
> ```

### 二、单例设计模式【扩展】

#### 1.概念

> 什么是设计模式
>
> ​	经过已经总结好的解决问题的方案
>
> ​	23种设计模式，比较常用的是单例设计模式，工厂设计模式，代理模式，装饰模式
>
> 什么是单例设计模式
>
> ​	单个实例【对象】
>
> ​	在程序运行的过程中，确保某一个类只能有一个实例【对象】，不管在哪个模块中获取对象，获取到的都是同一个对象
>
> ​	单例设计模式的核心：一个类有且仅有一个实例，并且这个实例需要应用在整个工程中

#### 2.应用场景

> 实际应用：数据库连接池操作-----》应用程序中多处需要连接到数据库------》只需要创建一个连接池即可，避免资源的浪费

#### 3.实现

##### 3.1模块

> Python的模块就是天然的单例设计模式
>
> 模块的工作原理：
>
> ​	import xxx,模块被第一次导入的时候，会生成一个.pyc文件，当第二次导入的时候，会直接加载.pyc文件，将不会再去执行模块源代码

##### 3.2使用new【掌握】

> ```
> __new__（）:实例从无到有的过程【对象的创建过程】
> ```
>
> 代码演示：
>
> ```Python
> class Singleton(object):
>     #类属性
>     instance = None
>
>     #类方法
>     @classmethod
>     def __new__(cls, *args, **kwargs):
>         #如果instance的值不为None，说明已经被实例化了，则直接返回；如果为NOne，则需要被实例化
>         if not cls.instance:
>             cls.instance = super(Singleton,cls).__new__(*args, **kwargs)
>
>         return cls.instance
>
> class MyClass(Singleton):
>     pass
>
> #当创建对象的时候自动被调用
> one = MyClass()
> two = MyClass()
>
> print(id(one))
> print(id(two))
>
> print(one is two)
> ```

##### 3.3装饰器【掌握】

> 代码演示：
>
> ```Python
> #单例类：将装饰器作用于一个类上
> def singleton(cls):
>     #类属性
>     instance = {}
>
>     #成员方法
>     def getSingleton(*args, **kwargs):
>         #思路：如果cls在字典中，则直接返回；如果不存在，则cls作为key，对象作为value，添加到字典中
>         if cls not in instance:
>             instance[cls] = cls(*args, **kwargs)
>         return  instance[cls]
>
>     return getSingleton
>
> @singleton
> class Test(object):
>     pass
>
> t1 = Test()
> t2 = Test()
>
> print(id(t1) == id(t2))
> print(t1 is t2)
> ```

##### 3.4使用在类中【掌握】

> 代码演示：
>
> ```Python
> #单例类
> class Foo(object):
>     #1.声明一个变量【类属性】
>     instance = None
>
>     #2.向外界提供一个公开的方法，用于返回当前类唯一的对象
>     #方法命名格式：defaultInstance,currentInstance ,getInstance
>     @classmethod
>     def getInstance(cls):
>         if cls.instance:
>             return cls.instance
>         else:
>             #实例化
>             cls.instance = cls()
>             return  cls.instance
>
> obj1 = Foo.getInstance()
> obj2 = Foo.getInstance()
>
> print(id(obj1) == id(obj2))
> print(obj1 is obj2)
> ```



##### 
