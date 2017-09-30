# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
from weather.spiders.GetData import GetdataSpider
import os
#设置编码为utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

class WeatherPipeline(object):
    def process_item(self, item, spider):
        # 获取当前目录
        current_dir = os.getcwd()
        # 用当前目录的路径和result.txt组建成新路径
        filename = os.path.join(current_dir, '07150214-1.txt')
        # filename = r'C:\Users\Think\Desktop\pyproject\project\result.txt'
        # 以追加模式打开文件
        with open(filename, 'a') as fp:
            fp.write(item['title'] + '\n')
            fp.write(item['date'] + '\n')
            fp.write(item['temp'] + '\n')
            fp.write(item['sun'] + '\n')
            fp.write(item['wind'] + '\n')
            fp.write(item['img'] + '\n')
            fp.write(item['dressing'] + '\n')
            fp.write(item['exercise'] + '\n')
            fp.write(item['car_wash'] + '\n')
            fp.write(item['travel'] + '\n')
            fp.write(item['UV'] + '\n')
            fp.write(item['drying'] + '\n')
        return item

        # title = scrapy.Field()  # 标题
        # date = scrapy.Field()  # 日期
        # temp = scrapy.Field()  # 温度
        # sun = scrapy.Field()  # 阳光
        # wind = scrapy.Field()  # 风向
        # img = scrapy.Field()  # 图片url
        # dressing = scrapy.Field()  # 穿衣指数
        # exercise = scrapy.Field()  # 晨练指数
        # car_wash = scrapy.Field()  # 洗车指数
        # travel = scrapy.Field()  # 旅游指数
        # UV = scrapy.Field()  # 紫外线指数
        # drying = scrapy.Field()  # 晾晒指数
