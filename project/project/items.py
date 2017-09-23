# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()   #定义标题
    week = scrapy.Field()   #定义星期
    img = scrapy.Field()    #定义图片
    temp = scrapy.Field()   #定义温度
    rain = scrapy.Field()   #定义降雨
    wind = scrapy.Field()   #定义风力
