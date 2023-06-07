# -*- ecoding: utf-8 -*-
# @ModuleName: test002
# @Function:
# @Author: darling
# @Time: 2022-05-05 20:01
import configparser

import pymysql
from dbutils.pooled_db import PooledDB
from loguru import logger

db_config = configparser.ConfigParser()
db_config.read_file(open('E:/mjy-workspace/python/config.ini', encoding='utf-8', mode='rt'))

mysql_conf = {
    'host': db_config.get('DATABASE', 'host'),  # 连接名称，默认127.0.0.1
    'user': db_config.get('DATABASE', 'user'),  # 用户名
    'passwd': db_config.get('DATABASE', 'password'),  # 密码
    'port': int(db_config.get('DATABASE', 'port')),  # 端口，默认为3306
    'db': db_config.get('DATABASE', 'database'),  # 数据库名称
    'charset': db_config.get('DATABASE', 'charset'),  # 字符编码
}
pool = PooledDB(pymysql, 50, **mysql_conf)
print(pool)
# 连接池链接
conn = pool.connection()


# 根据SQL获取数据
def get_all_for_sql(sql):
    logger.info('开始执行数据SQL')
    logger.info(sql)
    # 打开数据库连接
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchall() 方法获取s所有数据.
    data = cursor.fetchall()

    conn.close()
    logger.info('数据SQL执行完毕')
    return list(data)


if __name__ == '__main__':
    result = get_all_for_sql('select * from tb_user')
    print(result)
