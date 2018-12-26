# -*- coding: utf-8 -*-
import scrapy
from hdvipspider.items import HdvipspiderItem


class PornhdSpider(scrapy.Spider):
    name = 'pornhd'
    sum_pages = 848
    allowed_domains = ['pornhd.vip']
    start_urls = ['https://pornhd.vip']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="related"]//a[position()<49]/@href').extract()
        for detail_url in detail_urls:
            detail_url = self.start_urls[0] + detail_url
            yield scrapy.Request(url=detail_url, callback=self.detailparse)
            # print(detail_url)
        for page in range(802, self.sum_pages+1):
            next_url = self.start_urls[0] + '/video/' + str(page)
            yield scrapy.Request(url=next_url, callback=self.parse)

    def detailparse(self, response):
        item = HdvipspiderItem()
        try:
            info = response.xpath('//section/h1[@class="info fss"]/text()').extract()
            item['title'] = info[2].strip()
            item['duration'] = info[1].strip()
            item['cover'] = response.xpath('//section//video[1]/@poster').extract_first(default='no-cover')
            item['link'] = response.xpath('//section//video[1]/source/@src').extract_first(default='no-link')
        except:
            print('信息匹配失败！')
            pass
        yield item