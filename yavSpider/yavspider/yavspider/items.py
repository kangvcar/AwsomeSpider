# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YavspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 影片标题
    duration = scrapy.Field()   # 影片时长
    actor = scrapy.Field()  # 影片演员
    updated = scrapy.Field()    # 影片更新时间
    introduction = scrapy.Field()   # 影片介绍
    cover = scrapy.Field()    # 影片封面
    imgs = scrapy.Field()     # 影片截图
    link = scrapy.Field()   # 影片播放链接
