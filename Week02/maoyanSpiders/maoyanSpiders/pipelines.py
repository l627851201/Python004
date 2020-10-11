# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os,sys,csv
import pymysql

class MaoyanspidersPipeline:
    def writeDB(self, name, type, startDate):
        # 数据库信息
        dbInfo = {
            'host': "localhost",
            'port': 3306,
            'user': 'root',
            'password': 'Root123',
            'db': "spiders"
        }

        # sql
        sqls = 'insert into maoyandata(name, type, startDate) values("{}", "{}", "{}");'.format(name, type, startDate)
        print(f"sql is , {sqls}.\n")

        # 连接数据库
        conn = pymysql.connect(
            host = dbInfo['host'],
            port = dbInfo['port'],
            user = dbInfo['user'],
            password = dbInfo['password'],
            db = dbInfo['db']
        )

        # 游标
        cursor = conn.cursor()
        try:
            cursor.execute(sqls)

            # 关闭游标
            cursor.close()

            # 提交
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            conn.close()

    def process_item(self, item, spider):
        # return item
        getTitle = item['getTitle']
        getType = item['getType']
        getDate = item['getDate']

        # 写入数据库
        self.writeDB(getTitle, getType, getDate)

        return item

