## 一、参数传递
```
- 路径参数
- get请求参数
- post请求参数
```

## 二、视图函数
- 视图函数
```
视图函数，就是一个函数!
```

- 状态码
```
2xx: 成功
3xx: 重定向
4xx: 客户端错误
5xx: 服务端错误
```

## 三、请求HttpRequest对象
- 概述
```
Django会根据客户端发起的请求，创建HttpRequest对象;
作为视图函数的第一个参数传入;
```

- request对象属性
```
- path
- encoding
- method
- POST
- GET
- COOKIES
- FILES
- session
```

- GET属性
```
    # 方式一: 字典操作，如果key不存在，会报错
    # name = request.GET['name']
    # age = request.GET['age']

    # 方式二： 通过get方法
    # 如果不存在，设置为None
    # 预设置默认值
    name = request.GET.get('name')
    age = request.GET.get('age')
    score = request.GET.get('score', 0)
```
> 推荐使用get()方式

- POST属性
```
    name = request.POST.get('name')
    age = request.POST.get('age')
    score = request.POST.get('score', 0)
```

## 四、响应HttpResponse对象
- 概述
```
用于给客户端返回数据;
HttpResponse对象是自己创建;
```

- 响应
```
    response = HttpResponse('hello')

    response = render(request, 'responsetest.html')

    response = HttpResponseRedirect('/')
    response = HttpResponseRedirect('/randomview/')
    response = redirect('/randomview/')

    response = redirect('app:randomview')
    response = redirect('app:goods', 13)
    response = redirect('app:detail', 1,2,3)

    response = JsonResponse(stu)
```

## 五、会话技术
- 概述
```
- Http是属于无状态(一次请求，一次响应);
- 状态保持: 在一定时间内跟踪请求者的状态，延长会话时长;
- 分类: cookie、session、token
```

- cookie
```
客户端会话技术，数据存储在客户端;
由浏览器生成，每次请求时，浏览器会自动携带cookie;
```

- cookie使用
```
# 设置cookie
    response.set_cookie(key, value)

# 获取cookie
    request.COOKIE.get(key)

# 删除cookie
    response.delete_cookie(key)
```

## 六、项目
```
HTML: 首页、登录、注册、商品详情、购物车
JSON: 首页数据、详情页数据、商品数据

任务: 创建项目、Github仓库
```
