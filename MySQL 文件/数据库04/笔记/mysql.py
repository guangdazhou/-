import pymysql

#连接数据库
db = pymysql.connect(user="root",password="123456",port=3306,charset="utf8",host="localhost",db="db")

#操作数据的游标
cur = db.cursor()

#通过这个游标来执行sql命令
#cur.execute("select * from user")

#获取上面sql命令执行的结果
#result = cur.fetchall()

#只获取一条结果
#result = cur.fetchone()

#这个结果是一个元组
#print(result)
#拿每一条
#for r in result:
 #   print(r)

#pymysql  数据库操作,默认就会有一个事务
myname = "孙七"
sql = "insert into user (name) values ('%s')"%(myname)

try:
    cur.execute(sql)
    #如果上面这句sql命令执行没有异常,那么就可以提交
    print("ok")
    db.commit()
except:
    #如果有异常.就会进行事务的回滚 .就相当于上面这个sql命令没有执行
    print("fail")
    db.rollback()

#数据库用完,关闭
db.close()