import pymongo
from  pymongo import MongoClient
from bson.objectid import ObjectId

#连接
client =MongoClient()

#获取数据库
db = client.db2

#获取集合
collection = db.collection2

#增加
#collection.insert({"name":"lilei","money":10})

#增加多个文档
#collection.insert([{"name":"1111"},{"name":"2222"},{"name":"33333"}])

#删除
#collection.remove({"name":"1111"})

#修改
#collection.update({"name":"lilei"},{"$set":{"money":30}})

#获取读取结果
#排序
result = collection.find().sort("money",pymongo.DESCENDING)

for r in result:
 print(r)

