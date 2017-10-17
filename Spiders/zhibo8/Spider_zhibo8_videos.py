#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-17 09:45:36
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib2
from lxml import html


class videoItem(object):
	video_title = None
	video_link = None
	video_source = None
	video_time = None
	video_src = None
	
class get_video_zhibo8_info(object):
	def __init__(self, url):
		print u'爬虫开始...'
		self.url = url
		self.page_title = self.get_page_title(self.url)
		self.video_title_lists = self.get_video_title_list(self.url)
		self.video_info_lists = self.get_video_info_list(self.video_title_lists)
		self.print_video_info(self.video_info_lists)
		self.write_video_info(self.video_info_lists)
		print u'爬虫完成...'
	
	def get_page_title(self, url):
		'''获取页面的大标题'''
		selector = self.get_source_page(url)
		page_title = selector.xpath('//div[@id="boxlist"]/div[@class="title"]/span/text()')[0]
		return page_title
	
	def get_video_title_list(self, url):
		'''获取页面的所有新闻标题'''
		selector = self.get_source_page(url)
		video_lists = selector.xpath('//div[@id="boxlist"]//div[@class="dataList"]//ul[@class="articleList"]//li')
		video_items = []
		for video_list in video_lists:
			item = videoItem()
			try:
				item.video_title = video_list.xpath('./span[@class="articleTitle"]/a/text()')[0]
				item.video_link = 'http://www.zhibo8.cc' + video_list.xpath('./span[@class="articleTitle"]/a/@href')[0]
				item.video_time = video_list.xpath('./span[@class="postTime"]/text()')[0]
			except:
				continue
			else:
				video_items.append(item)
		return video_items
	
	def get_video_info_list(self, video_title_lists):
		video_info_lists = []
		for i, video in enumerate(video_title_lists):
			video_info_items = videoItem()
			try:
				selector = self.get_source_page(video.video_link)
				video_info_items.video_src = selector.xpath('.//div[@id="signals"]//div[@class="video_thumb"]/a/@href')[0]
				video_info_items.video_title = video.video_title
				video_info_items.video_source = selector.xpath('.//div[@id="signals"]//div[@class="video_box"]/p/text()')[0].split(' ')[0].strip()
				video_info_items.video_time = video.video_time
			except:
				continue
			else:
				print u'已获取第' + str(i+1) + u'条视频信息...'
				video_info_lists.append(video_info_items)
		return video_info_lists
	
	def print_video_info(self, video_info_lists):
		'''打印所有视频的信息和链接'''
		print self.page_title
		for video_info_list in video_info_lists:
			print u'视频标题 >>> ' + video_info_list.video_title
			print u'视频来源 >>> ' + video_info_list.video_source
			print u'视频链接 >>> ' + video_info_list.video_src
			print u'发布时间 >>> ' + video_info_list.video_time
			print '>>>>>>>>>>>>>>>>' * 5
			
	def write_video_info(self, video_info_lists):
		'''打印所有视频的信息和链接'''
		filename = u'NBA篮球滚动视频-标题-链接.txt'
		with open(filename, 'w') as f:
			f.write(self.page_title.encode('utf-8') + '\n')
			for video_info_list in video_info_lists:
				f.write(u'视频标题 >>> '.encode('utf-8') + video_info_list.video_title.encode('utf-8') + '\n')
				f.write(u'视频来源 >>> '.encode('utf-8') + video_info_list.video_source.encode('utf-8') + '\n')
				f.write(u'视频链接 >>> '.encode('utf-8') + video_info_list.video_src.encode('utf-8') + '\n')
				f.write( u'发布时间 >>> '.encode('utf-8') + video_info_list.video_time.encode('utf-8') + '\n')
				f.write(u'>>>>>>>>>>>>>>>>' * 5 + '\n')
	
	def get_source_page(self, url):
		'''获取网页源码，并使用lxml格式化源码'''
		try:
			request_headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
			request = urllib2.Request(url, None, request_headers)
			response = urllib2.urlopen(request).read()
			selector = html.fromstring(response)
		except:
			selector = None
		finally:
			return selector


zhibo8 = get_video_zhibo8_info('https://www.zhibo8.cc/nba/more.htm')
# https://www.zhibo8.cc/nba/more.htm