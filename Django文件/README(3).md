## 一、关系
```
一对一
一对多
多对多
```

## 二、一对一
- 关系声明(表单创建)
```
关系表，设置外键，并且是唯一!
# 主表
-- auto-generated definition
create table App_person
(
  id     int auto_increment
    primary key,
  p_name varchar(80) not null,
  p_age  int         not null
);



# 从表
create table App_idcard
(
  id          int auto_increment
    primary key,
  i_num       varchar(40)  not null,
  i_addr      varchar(256) not null,
  i_person_id int          not null,
  constraint i_person_id
  unique (i_person_id),
  constraint App_idcard_i_person_id_a973d7fa_fk_App_person_id
  foreign key (i_person_id) references App_person (id)
);
```

- 获取数据
```
- 主表 获取 从表  【隐性】
    对象.关系模型(小写)

- 从表 获取 主表   【显性】
    对象.关系属性
```

## 三、删除级联数据的模式
```
    ## 情况一: 默认models.CASECADE删除级联数据
    # 删除人时，身份证存在，人和身份证一起删除

    ## 情况二: models.PROTECT保护模式
    # 删除人时，身份证存在，抛出'ProtectedError'

    ## 情况三: models.SET_NULL 置空模式
    # 删除人时，身份证存在，设置为NULL

    ## 情况四: SET_DEFAULT 设置默认值
    # 删除人时，身份证存在，设置为默认值
```

## 四、一对多
- 关系
```
# 班级
create table App_grade
(
  id     int auto_increment
    primary key,
  g_name varchar(100) not null
);


# 学生
create table App_student
(
  id         int auto_increment
    primary key,
  s_name     varchar(40) not null,
  s_score    int         not null,
  s_grade_id int         not null,
  constraint App_student_s_grade_id_797e4cc7_fk_App_grade_id
  foreign key (s_grade_id) references App_grade (id)
);

```
> 一个班级 对应 多个学生

- 数据获取
```
- 主表 获取 从表  【隐性】
    # 关系模型_set 和 objects 同源
    对象.关系模型_set.all()

- 从表 获取 主表   【显性】
    对象.关系属性
```

## 五、多对多
- 关系
```
# 用户
create table App_user
(
  id     int auto_increment
    primary key,
  u_name varchar(100) not null,
  u_tel  varchar(20)  not null
);

# 商品
create table App_goods
(
  id      int auto_increment
    primary key,
  g_name  varchar(100) not null,
  g_price int          not null
);

# 关系表
create table App_goods_g_user
(
  id       int auto_increment
    primary key,
  goods_id int not null,
  user_id  int not null,
  constraint App_goods_g_user_goods_id_user_id_699246f7_uniq
  unique (goods_id, user_id),
  constraint App_goods_g_user_goods_id_65ebeef8_fk_App_goods_id
  foreign key (goods_id) references App_goods (id),
  constraint App_goods_g_user_user_id_093343ff_fk_App_user_id
  foreign key (user_id) references App_user (id)
);
```

- 数据获取
```
- 主表 获取 从表  【隐性】
    # 关系模型_set 和 objects 同源
    对象.关系模型_set.all()

- 从表 获取 主表   【显性】
    对象.关系属性.all()
```



