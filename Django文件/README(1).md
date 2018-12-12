## 一、自我介绍
	钟远智(钟哥)

	笔记内容(简书): https://www.jianshu.com/u/44cde87b5c30

## 二、课程安排
	Ubuntu环境
	Django基本架构和基本流程
	Django模型
	Django视图
	Django模板
	Django高级
	Django站点

	Django项目(爱鲜蜂)
	Django项目部署
	Django考试

## 三、Ubuntu安装

## 四、windows和ubuntu
	git 
	Xshell(putty)/Xftp
	SSH

	备注： 虚拟机，安装VMware Tools!

## 五、虚拟环境
	python -> python2
	python -> python3 

	- 安装python3的pip
		sudo apt install python3-pip
	- pip的基本使用
		pip install xxx		安装
		pip uninstall xxx	卸载
		pip freeze		查看所安装的依赖包
	- 安装virtualenv
		pip3 install virtualenv
	- 安装统一管理工具
		pip3 install virtualenvwrapper -i https://pypi.douban.com/simple
	
		atom@ubuntu:~$ type virtualenvwrapper.sh
		virtualenvwrapper.sh is /home/atom/.local/bin/virtualenvwrapper.sh

	- 配置虚拟环境
		# 第一步: 配置用户环境变量
		vi ~/.bashrc
		# 文件最后添加以下两行 (根据自己的安装位置而定)
		export WORKON_HOME=/home/atom/.virtualenvs
		source /home/atom/.local/bin/virtualenvwrapper.sh

		# 第二步: 创建对应的虚拟目录
		mkdir /home/atom/.virtualenvs

		# 第三步: 刷新环境
		source ~/.bashrc

	- 虚拟环境的使用
		# 创建虚拟环境
		mkvirtualenv python1809 -p /usr/bin/python3

		# 进入虚拟环境
		workon python1809
		
		# 退出虚拟环境
		deactivate
		
		# 删除虚拟环境
		rmvirtualenv python1809


## 六、Django简介
	Django 最初被设计用于具有快速开发需求的新闻类站点，目的是要实现简单快捷的网站开发。
	官方文档: https://www.djangoproject.com/


## 七、MVC模式
	MVC设计模式，解耦；方便代码的重构，以及代码的复用；
	M: Model模型，负责数据库的数据存取
	V: View视图，负责数据展示
	C: Controller控制器，负责业务逻辑

## 八、MTV模式
	本质上是MVC！
	M: Model模型，负责数据存取
	T: Template模板，数据展示
	V: View视图，业务逻辑处理


## 九、安装Django
	# 先进入到虚拟环境
	pip install Django==1.11.4
	
	# 查看
	pip freeze

## 十、Django项目创建
	- 新建项目
		django-admin startproject HelloDjango

	- 文件说明
	    manage.py 项目入口文件，与Django交互
	    HelloDjango/__init__.py  Python包,初始化
	    HelloDjango/settings.py  项目配置文件
	    HelloDjango/urls.py      路由(URL控制器)
	    HelloDjango/wsgi.py      部署上线(网关接口)

	- 项目启动
	    # 默认端口号8000
	    python manage.py runserver
	    # 0.0.0.0绑定本机IP，端口号9000
	    python manage.py runserver 0.0.0.0:9000




## 十一、创建应用(一个项目可以包含多个应用)
- 创建应用
    python manage.py startapp Meituan

- 文件说明
    admin.py 站点配置(后台管理)
    modesl.py 模型(数据库操作)
    views.py 视图(业务逻辑处理)


## 十二、业务流程
请求request -> urls控制器 -> views视图 -> template模板 -> 响应response









	
