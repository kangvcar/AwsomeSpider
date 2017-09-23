# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
from project.spiders.suzhouSpider import SuzhouspiderSpider
import os
#设置编码为utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

# 编写处理类
class ProjectPipeline(object):
    def process_item(self, item, spider):
        print '----------------pipeline-------------------'
        # 获取当前目录
        current_dir = os.getcwd()
        # 用当前目录的路径和result.txt组建成新路径
        filename = os.path.join(current_dir,'result.txt')
        # filename = r'C:\Users\Think\Desktop\pyproject\project\result.txt'
        # 以追加模式打开文件
        with open(filename, 'a') as fp:
            fp.write(item['title'] + '\n')
            fp.write(item['week'] + '\n')
            fp.write(item['temp'] + '\n')
            fp.write(item['rain'] + '\n')
            fp.write(item['wind'] + '\n')
            fp.write(item['img'] + '\n\n')
        return item
