# -*- coding: utf-8 -*-
import scrapy
from project.items import ProjectItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SuzhouspiderSpider(scrapy.Spider):
    name = 'suzhouSpider'
    allowed_domains = ['suzhou.tianqi.com']
    start_urls = ['http://suzhou.tianqi.com/']

    def parse(self, response):
        # 过滤出包含六天天气的html代码
        sixday_detail = response.xpath('//div[@class="tqshow1"]')
        # 定义items
        items = []
        # 循环每天的天气信息，并提取指定信息
        for day in sixday_detail:
            # 定义一个item类
            item = ProjectItem()
            # 提取标题
            datetitle = ''
            for date in day.xpath('./h3//text()').extract():
                datetitle += date

            item['title'] = datetitle
            # 提取星期
            item['week'] = day.xpath('./p//text()').extract()[0]
            # 提取图片
            item['img'] = day.xpath('./ul/li[@class="tqpng"]/img/@src').extract()[0]
            # 提取温度
            templist = ''
            for temprange in day.xpath('./ul/li[2]//text()').extract():
                templist += temprange
            item['temp'] =  templist
            # 提取降雨
            item['rain'] = day.xpath('./ul/li[3]//text()').extract()[0]
            # 提取风力
            item['wind'] = day.xpath('./ul/li[4]//text()').extract()[0]
            items.append(item)

        print '----------------bye from spider------------------------'
        return items