# mysql包
# 1.导包
import pprint

import pymysql

# 2.创建和mysql服务段的连接对象
try:
    conn = pymysql.Connect(host='localhost',
                           user='root',
                           password='mjyxy',
                           database='communitypension',
                           port=3306,
                           charset='utf8'
                           )
    # 3.获取游标对象
    cursor = conn.cursor()

    # 4.执行sql语句
    sql = 'select * from tb_user'

    # 5.使用游标对象去调用sql
    cursor.execute(sql)

    # 获取查询结果并打印出来
    result = cursor.fetchall()
    print(result)

    # 6.将增加和修改操作提交到数据库
    # conn.commit()

    # 7.回滚数据
    # conn.rollback()

    # 8.关闭游标对象
    cursor.close()

    # 9.关闭连接
    conn.close()

except Exception as e:
    print(e)

