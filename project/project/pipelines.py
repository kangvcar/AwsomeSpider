# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
from project.spiders.suzhouSpider import SuzhouspiderSpider

reload(sys)
sys.setdefaultencoding('utf-8')

class ProjectPipeline(object):
    def process_item(self, item, spider):
        print '----------------pipeline-------------------'
        filename = r'C:\Users\Think\Desktop\pyproject\project\result.txt'
        with open(filename, 'a') as fp:
            fp.write(item['title'] + '\n')
            fp.write(item['week'] + '\n')
            fp.write(item['temp'] + '\n')
            fp.write(item['rain'] + '\n')
            fp.write(item['wind'] + '\n')
            fp.write(item['img'] + '\n\n')
        return item
