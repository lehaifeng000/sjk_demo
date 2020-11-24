
import pymysql

db = pymysql.connect("10.11.47.114","lhf","lhf123","sjk_demo" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor(pymysql.cursors.DictCursor)

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from user")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()

print(data)

# 关闭数据库连接
db.close()