from redis import  *

#链接redis数据库
sr = StrictRedis(host="localhost",port=6379,db=0)


try:
    #增加
    result = sr.set("name","xiaoming")
    sr.set("age","18")
    print(result)
except Exception as e:
    print(e)

#修改
sr.set("name","lily")

#删除
#sr.delete("name")

#读取 查
#result = sr.get("name")
#print(result)
#print(result.decode())

#读取所有键
result = sr.keys()
print(result)