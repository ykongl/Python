
import pymysql
import datetime
# 添加，修改，删除
conn = pymysql.Connect(
        host='localhost',
        user='root',
        password='mjyxy',
        database='communitypension',
        port=3306,
        charset='utf8'
    )

# 创建游标对象
cur = conn.cursor()

try:
    # sql语句
    # sql = 'insert into tb_user values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    # add_data = [22,'雷电将军', 1, '123456', '18851269705', 4, '002', 1, 1, 0, 1, datetime.datetime.now(), 1,
    #             datetime.datetime.now()]
    # sql = 'update tb_user set username = %s where id = 21'
    # update_data = ['钟离']

    sql = 'delete from tb_user where id = %s'
    del_data = ['22']

    # 使用游标对象执行sql
    # cur.execute(sql, add_data)
    # cur.execute(sql, update_data)
    cur.execute(sql, del_data)

    # 提交操作
    conn.commit()
except Exception as e:
    print(e)
    # 数据回滚
    conn.rollback()

finally:
    # 关闭游标
    cur.close()

    # 关闭连接
    conn.close()


