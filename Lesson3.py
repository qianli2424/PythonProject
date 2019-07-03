import pymysql

db = None
dept = "INSERT INTO dept VALUES(60,'student','changsha')"
query = "select * from dept"
# 创建数据库对象，创建mysql数据库连接
db = pymysql.connect('localhost', 'root', '123456', 'learn')
# 使用cursor()方法创建一个游标对象cursor，该对象用来执行SQL语句
cursor = db.cursor()
# 使用execute()方法执行SQL，可以执行增删改查
try:
    cursor.execute(dept)
    #数据插入后，应commit提交
    db.commit()
    print('数据插入成功')
except:
    print('查询不到数据')
    #执行失败将回滚，回到执行前的状态
    db.rollback()

try:
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)
except:
    print('查询不到数据')
db.close()