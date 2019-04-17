# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

HOST      = "119.3.55.220"
PORT      = 6789
USER      = "4287e7ae11008807e536c6283f82ea2f"
PASSWORD  = "2tU4yyHkwu"
DATABASE  = "jrj"
TABLE     = "j22"
COLUMN    = "mobile"
SAVE_TABLE = "jrj_registered"

STARTPAGE = 700
ENDPAGE   = 730
PAGESIZE  = 10000


class JrjScrapyPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host=HOST,
                                    port=PORT,
                                    user=USER,
                                    password=PASSWORD,
                                    database=DATABASE)

        self.cursor = self.conn.cursor()

    # 读取数据
    def get_phone(self, start_page):

        sql = "SELECT %s" % COLUMN + " FROM %s" % TABLE + " LIMIT %s, %s; " % (start_page*PAGESIZE, PAGESIZE)
        self.cursor.execute(sql)

        results = self.cursor.fetchall()  # 读取结果
        results = {result[0] for result in results}

        print("\n当前读取「%s」，页面大小「%s」\n" % (start_page, PAGESIZE))

        return results

    # 保存数据
    def process_item(self, item, spider):

        # 存200
        sql = "INSERT IGNORE INTO %s" % SAVE_TABLE + "(phone) VALUES(%s)" % item["phone"]
        self.cursor.execute(sql)
        self.conn.commit()

        return item



