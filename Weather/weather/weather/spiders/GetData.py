# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class GetdataSpider(scrapy.Spider):
    name = 'GetData'
    allowed_domains = ['mudanjiang.tianqi.com/hailin']
    start_urls = ['http://mudanjiang.tianqi.com/hailin/']

    def parse(self, response):
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

        div = response.xpath('//div[@class="today_data_w" or @class="today_data_r01"]')
        items = []
        # for div in two_div:
        item = WeatherItem()
        item['title'] = div[0].xpath('./div/h3/text()').extract()[0]
        print item['title']
        item['date'] = div[0].xpath('./div/ul/li[1]/text()').extract()[0]
        print item['date']
        templist = ''
        for temprange in div[0].xpath('./div/ul/li[3]//text()').extract():
            templist += temprange
        item['temp'] = templist.split()[0]
        print item['temp']
        item['sun'] = div[0].xpath('./div/ul/li[4]/text()').extract()[0]
        print item['sun']
        item['wind'] = div[0].xpath('./div/ul/li[5]/text()').extract()[0]
        print item['wind']
        item['img'] = div[0].xpath('./div/ul/li[2]/img/@src').extract()[0]
        print item['img']
        item['dressing'] = ' '.join(div[1].xpath('./ul/li[1]//text()').extract())
        print item['dressing']
        item['exercise'] = ' '.join(div[1].xpath('./ul/li[2]//text()').extract())
        print item['exercise']
        item['car_wash'] = ' '.join(div[1].xpath('./ul/li[3]//text()').extract())
        print item['car_wash']
        item['travel'] = ' '.join(div[1].xpath('./ul/li[4]//text()').extract())
        print item['travel']
        item['UV'] = ' '.join(div[1].xpath('./ul/li[5]//text()').extract())
        print item['UV']
        item['drying'] = ' '.join(div[1].xpath('./ul/li[6]//text()').extract())
        print item['drying']
        items.append(item)
        return items














