# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()      #标题
    date = scrapy.Field()       #日期
    temp = scrapy.Field()       #温度
    sun = scrapy.Field()        #阳光
    wind = scrapy.Field()       #风向
    img= scrapy.Field()         #图片url
    dressing = scrapy.Field()   #穿衣指数
    exercise = scrapy.Field()   #晨练指数
    car_wash = scrapy.Field()   #洗车指数
    travel = scrapy.Field()     #旅游指数
    UV = scrapy.Field()         #紫外线指数
    drying = scrapy.Field()     #晾晒指数

