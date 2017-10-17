#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-17 09:45:36
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib2
from lxml import html

class newsItem(object):
	news_title = None
	news_link = None
	news_source = None
	news_time = None
	news_info = None

class get_news_zhibo8_info(object):
	def __init__(self, url):
		print u'爬虫开始...'
		self.url = 'https://news.zhibo8.cc/nba/more.htm'
		self.page_title = self.get_page_title(self.url)
		self.news_title_lists = self.get_news_title_list(self.url)
		self.news_info_lists = self.get_news_info_list(self.news_title_lists)
		self.print_news_title(self.news_title_lists)
		self.write_news_title(self.news_title_lists)
		self.print_news_info(self.news_info_lists)
		self.write_news_info(self.news_info_lists)
		print u'爬虫完成...'

	def get_page_title(self, url):
		'''获取页面的大标题'''
		selector = self.get_source_page(url)
		page_title = selector.xpath('//div[@id="boxlist"]/div[@class="title"]/span/text()')[0]
		return page_title
		
	def get_news_title_list(self, url):
		'''获取页面的所有新闻标题'''
		selector = self.get_source_page(url)
		news_lists = selector.xpath('//div[@id="boxlist"]//div[@class="dataList"]//ul[@class="articleList"]//li')
		news_items = []
		for news_list in news_lists:
			item = newsItem()
			try:
				item.news_title = news_list.xpath('./span[@class="articleTitle"]/a/text()')[0]
				item.news_link = 'http:' + news_list.xpath('./span[@class="articleTitle"]/a/@href')[0]
				item.news_source = news_list.xpath('./span[@class="source"]/text()')[0]
				item.news_time = news_list.xpath('./span[@class="postTime"]/text()')[0]
			except:
				continue
			else:
				news_items.append(item)
		return news_items
		
	def get_news_info_list(self, news_title_lists):
		news_info_lists = []
		for i, news in enumerate(news_title_lists):
			news_info_items = newsItem()
			selector = self.get_source_page(news.news_link)
			news_info_items.news_info = selector.xpath('.//div[@id="signals"]//p/text()')		#list
			news_info_items.news_title = news.news_title
			news_info_items.news_link = news.news_link
			news_info_items.news_source = news.news_source
			news_info_items.news_time = news.news_time
			news_info_lists.append(news_info_items)
			print u'正在获取第' + str(i+1) + u'条新闻的详细内容...'
		return news_info_lists
			
	def print_news_title(self, news_title_lists):
		'''打印所有新闻标题'''
		print self.page_title
		for new_title_list in news_title_lists:
			print u'新闻标题 >>> ' + new_title_list.news_title
			print u'新闻链接 >>> ' + new_title_list.news_link
			print u'新闻来源 >>> ' + new_title_list.news_source
			print u'发布时间 >>> ' + new_title_list.news_time
			print '>>>>>>>>>>>>>>>>' * 5
			
	def write_news_title(self, news_title_lists):
		'''把所有新闻标题写入文件'''
		filename = u'NBA篮球滚动新闻-标题.txt'
		with open(filename, 'w') as f:
			f.write(self.page_title.encode('utf-8') + '\n')
			for new_title_list in news_title_lists:
				f.write(u'新闻标题 >>> '.encode('utf-8') + new_title_list.news_title.encode('utf-8') + '\n')
				f.write(u'新闻链接 >>> '.encode('utf-8') + new_title_list.news_link.encode('utf-8') + '\n')
				f.write(u'新闻来源 >>> '.encode('utf-8') + new_title_list.news_source.encode('utf-8') + '\n')
				f.write(u'发布时间 >>> '.encode('utf-8') + new_title_list.news_time.encode('utf-8') + '\n')
				f.write(u'>>>>>>>>>>>>>>>>' * 5 + '\n')
			
	def print_news_info(self, news_info_lists):
		'''打印所有新闻的详细内容'''
		print self.page_title
		for news_info_list in news_info_lists:
			print u'新闻标题 >>> ' + news_info_list.news_title
			print u'新闻链接 >>> ' + news_info_list.news_link
			print u'新闻内容 >>> ' + '\n'.join(news_info_list.news_info)
			print u'新闻来源 >>> ' + news_info_list.news_source
			print u'发布时间 >>> ' + news_info_list.news_time
			print '>>>>>>>>>>>>>>>>' * 5
			
	def write_news_info(self, news_info_lists):
		'''把所有新闻的详细内容写入文件'''
		filename = u'NBA篮球滚动新闻-标题-详细内容.txt'
		with open(filename, 'w') as f:
			f.write(self.page_title.encode('utf-8') + '\n')
			for news_info_list in news_info_lists:
				f.write(u'新闻标题 >>> '.encode('utf-8') + news_info_list.news_title.encode('utf-8') + '\n')
				f.write(u'新闻链接 >>> '.encode('utf-8') + news_info_list.news_link.encode('utf-8') + '\n')
				f.write(u'新闻内容 >>> '.encode('utf-8') + '\n'.join(news_info_list.news_info).encode('utf-8') + '\n')
				f.write(u'新闻来源 >>> '.encode('utf-8') + news_info_list.news_source.encode('utf-8') + '\n')
				f.write(u'发布时间 >>> '.encode('utf-8') + news_info_list.news_time.encode('utf-8') + '\n')
				f.write(u'>>>>>>>>>>>>>>>>' * 5 + '\n')
		
	def get_source_page(self, url):
		'''获取网页源码，并使用lxml格式化源码'''
		try:
			request_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
			request = urllib2.Request(url, None, request_headers)
			response = urllib2.urlopen(request).read()
			selector = html.fromstring(response)
		except:
			selector = None
		finally:
			return selector

zhibo8 = get_news_zhibo8_info('https://news.zhibo8.cc/nba/more.htm')
#https://news.zhibo8.cc/nba/more.htm