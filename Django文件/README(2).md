## 一、模型操作
- 配置数据库
```
默认使用sqlite
```

- 定义模型类
```
# 定义 学生 模型类
class Student(models.Model):
    # id、name、age、math、english、chinese
    # 默认Django会自动创建
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    math = models.IntegerField()
    english = models.IntegerField()
    chinese = models.IntegerField()
```

- 生成迁移文件
```
python manage.py makemigrations
python manage.py makemigrations Meituan
```
> 备注: 只是生成，并没有执行，所以表单还没创建!!!!

- 执行迁移文件
```
python manage.py migrate
```

- 模型操作(数据库的数据操作)
```
增删改查
```

## 二、ORM
- 概述
对象关系映射。O对象， R关系，M映射

- 作用
```
将对象操作转换为数据库操作，屏蔽掉不同数据库的操作!
关注点是数据的业务逻辑处理，而不是关注数据库的具体操作!
```

## 三、属性定义
- 数据类型
```
- AutoField 自增长(前提主键)
- CharField 字符串
- IntegerField 整形
- FloatField 浮点型
- DecimalField 浮点型 【设置显示位数】
    max_digits 总长度
    decimal_places 小数点后几位
- BooleanField 布尔类型
- NullBooleanField 支持null/true/flase
- DateField 日期
- TimeField 时间
- DateTimeField  日期+时间
- FileField 文件
- ImageField 图片
```

- 约束
```
- null 设置null=True可以为空，null=False不能为空
- primary_key 设置True标识为主键
- unique 设置True唯一标示
- db_colum 设置字段名，没指定属性名即为字段名
- blank 设置为True，表示可以为空白
```