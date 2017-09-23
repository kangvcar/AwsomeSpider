# -*- coding: utf-8 -*-
import scrapy
from project.items import ProjectItem
#设置编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SuzhouspiderSpider(scrapy.Spider):
    #定义爬虫名称为suzhouSpider
    name = 'suzhouSpider'
    #定义允许的匿名
    allowed_domains = ['suzhou.tianqi.com']
    #定义起始url
    start_urls = ['http://suzhou.tianqi.com/']

    #定义过滤数据的parse
    def parse(self, response):

        # title = scrapy.Field()  #定义标题
        # week = scrapy.Field()   #定义星期
        # img = scrapy.Field()    #定义图片
        # temp = scrapy.Field()   #定义温度
        # rain = scrapy.Field()   #定义降雨
        # wind = scrapy.Field()   #定义风力
        
        # 过滤出包含六天天气的html代码,后续在用于循环
        sixday_detail = response.xpath('//div[@class="tqshow1"]')
        # 定义items,用于存储六天的天气信息
        items = []
        # 循环每天的天气信息，并提取指定信息
        for day in sixday_detail:
            # 调用item.py的ProjectItem()类来实例化一个item
            item = ProjectItem()

            # 提取标题,并循环成str
            datetitle = ''
            for date in day.xpath('./h3//text()').extract():
                datetitle += date

            item['title'] = datetitle

            # 提取星期,返回为list，加入[0]下标获得第一个值
            item['week'] = day.xpath('./p//text()').extract()[0]

            # 提取图片,返回为list，加入[0]下标获得第一个值
            item['img'] = day.xpath('./ul/li[@class="tqpng"]/img/@src').extract()[0]

            # 提取温度,并循环成str
            templist = ''
            for temprange in day.xpath('./ul/li[2]//text()').extract():
                templist += temprange
            item['temp'] =  templist

            # 提取降雨,返回为list，加入[0]下标获得第一个值
            item['rain'] = day.xpath('./ul/li[3]//text()').extract()[0]

            # 提取风力,返回为list，加入[0]下标获得第一个值
            item['wind'] = day.xpath('./ul/li[4]//text()').extract()[0]

            #把item存入items列表
            items.append(item)

        print '----------------bye from spider------------------------'
        return items