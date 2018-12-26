# -*- coding: utf-8 -*-
import scrapy
from yavspider.items import YavspiderItem

class YavtubeSpider(scrapy.Spider):
    name = 'yavtube'
    base_url = 'https://yavtube.com'
    sum_pages = 60
    allowed_domains = ['yavtube.com']
    start_urls = ['https://yavtube.com/videos/javtube']


    def parse(self, response):
        detail_urls = response.xpath('//section/ul/child::node()//div[@class="card-image valign-wrapper"]/a/@href').extract()
        for detail_url in detail_urls:
            detail_url = self.base_url + detail_url
            yield scrapy.Request(url=detail_url, callback=self.detailparse)
            # print(detail_url)
        for page in range(2, self.sum_pages+1):
            next_page = self.start_urls[0] + '/page/' + str(page)
            yield scrapy.Request(url=next_page, callback=self.parse)



    def detailparse(self, response):
        item = YavspiderItem()
        try:
            item['title'] = response.xpath('//div[@class="player-wrapper"]/h1/text()').extract_first(default='not-title')
            item['duration'] = response.xpath('//div[@class="card-stacked"]//ul[@class="information"]//li[1]//span[2]/text()').extract_first(default='not-duration')
            item['actor'] = response.xpath('//div[@class="card-stacked"]//ul[@class="information"]//li[2]//span[2]//text()').extract_first(default='not-actor')
            item['updated'] = response.xpath('//div[@class="card-stacked"]//ul[@class="information"]//li[4]//span[2]/text()').extract_first(default='not-updated')
            item['introduction'] = ''.join(response.xpath('//span[@class="description text-left text-multi-ellipsis"]//text()').extract())
            item['cover'] = response.xpath('//div[@class="player-container"]//video[1]/@poster').extract_first(default='not-img')
            item['imgs'] = response.xpath('//div[@class="card-stacked"]//ul[@class="row videos-images movies-images margin-top-5"]//li/@data-src').extract()
            item['link'] = response.xpath('//div[@class="player-container"]//video[1]/@source').extract_first(default='not-link')
        except:
            pass
        yield item
        #
        # print(response.xpath('//div[@class="player-wrapper"]/h1/text()').extract_first())
        # print(response.xpath('//div[@class="card-stacked"]//ul[@class="information"]//li[1]//span[2]/text()').extract_first())
        # print(response.xpath('//div[@class="card-stacked"]//ul[@class="information"]//li[2]//span[2]//text()').extract_first())
        # print(response.xpath('//div[@class="card-stacked"]//ul[@class="information"]//li[4]//span[2]/text()').extract_first())
        # print(''.join(response.xpath('//span[@class="description text-left text-multi-ellipsis"]//text()').extract()))
        # print(response.xpath('//div[@class="card-stacked"]//ul[@class="row videos-images movies-images margin-top-5"]//li/@data-src').extract())
        # print(response.xpath('//div[@class="player-container"]//video[1]/@source').extract_first())
