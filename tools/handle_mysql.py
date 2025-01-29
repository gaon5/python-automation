import pymysql
from pymysql.cursors import DictCursor
from loguru import logger

class HandleMysql:
    def __init__(self,user,password,database,port,host):
        # 实例属性 -数据库链接
        self.conn = pymysql.connect(
            user=user,
            password=password,
            database=database,
            port=port,  # 不要加引号  数字
            host=host,
            charset="utf8mb4",
            cursorclass=DictCursor  # 数据读取默认格式是元组，不方便确实数据字段，加上这个之后就会以字典格式存储数据。
        )
        # 数据库游标
        self.cursor = self.conn.cursor()

    # 实例方法--查询方法
    def query_data(self,sql,fetch_num=1,size=None):
        """
        这是数据库的查询的方法，可以支持查询1条数据/多条数据/所有数据
        :param sql: 查询的sql语句
        :param fetch_num: 默认值为1；
             - 选择获取查询结果的条数据，传入1获取1条数据，传入-1获取所有结果，传入2获取多条结果
        :param size:当传入fetchnum为2的时候，再传size控制具体几条数据。 size默认为None
        :return: 获取的查询结果
        """
        try:
            result = self.cursor.execute(sql)
            logger.info(f"数据库的查询结果条数是：{result}")
            if result > 0 :  #判断是否有查询结果  有的话再获取详细数据
                if fetch_num == 1:
                    data = self.cursor.fetchone()
                    logger.info(f"数据库的查询数据结果为：{data}")
                    return data
                elif fetch_num == 2:
                    data = self.cursor.fetchmany(size=size)
                    logger.info(f"数据库的查询数据结果为：{data}")
                    return data
                elif fetch_num == -1:
                    data = self.cursor.fetchall()
                    logger.info(f"数据库的查询数据结果为：{data}")
                    return data
            logger.info("数据库没有查询任何结果！")
        except Exception as err:
            logger.error(f"数据库操作异常了！{err}")
        finally:  #不管捕获了异常与否 都执行关闭游标和数据库的操作
            self.cursor.close()
            self.conn.close()

if __name__ == '__main__':
    from data.setting import my_db
    sql = 'select mobile_code,user_phone,rec_date from tz_sms_log where user_phone like "1785%";'
    HandleMysql(**my_db).query_data(sql)  # 字典解包 **my_db