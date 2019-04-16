import redis
import cx_Oracle
import time

# 连接oracle提取数据
def f():
    # db = cx_Oracle.connect('此处填oracle账号/此处填oracle密码@此处填oracle地址:此处填端口/此处填oracle名称')
    db = cx_Oracle.connect('ABC2019/ABC20191QAZ@100.10.100.10:8017/xe')

    cr = db.cursor()
    cr.execute('select * from hyl_table_a')
    rs = cr.fetchall()
    cr.close()
    #方法一：系统list
    return list(rs)

# 连接redis数据库
# res = redis.Redis(host="此处填redis地址", port=此处填redis端口, password="此处填redis密码")
res = redis.Redis(host="100.0.0.0", port=0000, password="ABC")

插入单条
list=[1,2,3]
for i in list:
    res.set("5",i)
print(res.get("5"))

# list = f()
start = time.clock()
print("开始时间 ：", start)
# 读取list
res.lrange("7",0,-1)
end = time.clock()
print("结束时间 ：", end)
print("总共耗时 ：", end - start)
print("lrange success!")





