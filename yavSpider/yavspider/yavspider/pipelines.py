# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings

# 此类是把信息写入文档，写入时末尾都加了一个逗号，是为了数据的观看与直观性
class YanspiderPipeline2file(object):
    def process_item(self, item, spider):
        with open('yavmovie_list.txt', 'a', encoding='utf-8') as f:
            f.write(item['link'] + ',')
            f.write(item['title']+',')
            f.write(item['duration']+',')
            f.write(item['actor']+',')
            f.write(item['updated']+',')
            f.write(item['cover'])
            f.write('\n')


#下面是将爬取到的信息插入到MySQL数据库中
class YavspiderPipeline(object):
    def process_item(self, item, spider):
        host = settings['MYSQL_HOST']
        user = settings['MYSQL_USER']
        passwd = settings['MYSQL_PASSWORD']
        db = settings['MYSQL_DB']
        port = settings['MYSQL_PORT']

        # 连接数据库
        con = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port)
        # 创建数据库游标
        cue = con.cursor()
        print('MySQL connect sussess.')
        try:
            cue.execute("INSERT INTO movie (title, duration, actor, updated, introduction, cover, link) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['title'], item['duration'], item['actor'], item['updated'], item['introduction'], item['cover'], item['link']))
            print('Insert Success.')
        except Exception as e:
            print('Insert Error.')
            con.rollback()
        else:
            con.commit()
        con.close()
        return item
