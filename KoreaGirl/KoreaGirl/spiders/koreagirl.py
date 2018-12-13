# -*- coding: utf-8 -*-
import scrapy

from KoreaGirl.items import KoreagirlItem


class KoreagirlSpider(scrapy.Spider):
    name = 'koreagirl'
    allowed_domains = ['135zyw.com']
    base_url = 'http://www.135zyw.com'
    start_urls = ['http://www.135zyw.com/?m=vod-type-id-20-pg-1.html']

    def parse(self, response):
        infourls = response.xpath('//div[@class="xing_vb"]//ul/li/span[2]/a/@href').extract()
        for infourl in infourls:
            infourl = self.base_url + infourl
            yield scrapy.Request(url=infourl, callback=self.infoparse)
        next = response.xpath('//div[@class="xing_vb"]//ul[last()]/li//span[@class="pagenow"]/following-sibling::a[1]/@href').extract_first()
        nexturl = self.base_url + next
        yield scrapy.Request(url=nexturl, callback=self.parse)
        # print(nexturl)

    def infoparse(self, response):
        item = KoreagirlItem()
        item['title'] = response.xpath('//div[@class="vodh"]/h2/text()').extract_first()
        item['playurl'] = response.xpath('//div[@class="vodplayinfo"]//ul[2]//input/@value').extract_first()
        yield item
        pass
