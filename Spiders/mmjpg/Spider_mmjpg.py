#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-14 16:28:34
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib2
import re
from lxml import html
import os

class get_mm_pic(object):
	def __init__(self, url):
		self.url = url
		self.sumpage = self.get_sum_page(self.url)
		print u'总共检测到有' + self.sumpage + u'页'
		self.urls = self.get_all_page_urls(self.sumpage)
		print u'已获取所有页面的url'
		self.page_links = self.get_page_links(self.urls)
		print u'已获取所有图集的link'
		self.download_all_pic = self.download_all_pic(self.page_links)
		print u'已下载所有图片'
		
	def get_sum_page(self, url):
		''' 获取总页数'''
		selector = self.get_source_page(url)
		sum_page = selector.xpath('//div[@class="page"]//a[last()]/@href')[0].split('/')[-1]
		return sum_page
	
	def get_all_page_urls(self, sumpage):
		''' 用总页数来组合拼接出所有页面的url 并返回包含所有url 的list '''
		urls = []
		ul = self.url.split('/')
		for page in range(1, int(sumpage)+1):
		# for page in range(1, 2):
			ul[-1] = str(page)
			url = '/'.join(ul)
			urls.append(url)
		return urls
	
	def get_page_links(self, urls):
		''' 获取每个图集的 link '''
		page_links = []
		for url in urls:
			try:
				selector = self.get_source_page(url)
				lis = selector.xpath('//div[@class="pic"]//li/a/@href')
			except:
				continue
			for li in lis:
				page_links.append(li)
		return page_links
	
	def download_all_pic(self, page_links):
		''' 进入所有图集，并下载所有图片 '''
		for page_link in page_links:
			try:
				selector = self.get_source_page(page_link)
				album_title = selector.xpath('//div[@class="article"]/h2/text()')[0]
				sum_pic = selector.xpath('//div[@id="page"]/a[last()-1]/text()')[0]
				path = self.mk_pic_dir(album_title)
			except:
				continue
			for pic in range(1, int(sum_pic)+1):
				try:
					print u'正在下载-->' + album_title + u'-->第' + str(pic) + u'张美图...'
					pic_link = page_link + '/' + str(pic)
					src = self.get_pic_link(pic_link)
					# filename = '%s%s.jpg' %(album_title, pic)
					filename = '%s.jpg' % (pic)
				except:
					continue
				else:
					try:
						with open(path + '/' + filename, 'wb') as fp:
							fp.write(urllib2.urlopen(src, timeout=3).read())
					except:
						continue
	
	def mk_pic_dir(self, dirname):
		''' 用图集名创建文件夹 '''
		path = dirname
		if not os.path.exists(path):
			os.mkdir(path)
		return path
	
	def get_pic_link(self, url):
		''' 获取图片的src属性'''
		try:
			selector = self.get_source_page(url)
			src = selector.xpath('//div[@id="content"]/a/img/@src')[0]
		except:
			src = None
		finally:
			return src
	
	def get_source_page(self, url):
		'''
		返回经过lxml.html.fromstring 模块处理的<Element html at 0x36e8278>
		可以用 XPath 来过滤数据
		'''
		try:
			response = urllib2.urlopen(url, timeout=3).read()
			selector = html.fromstring(response)
		except:
			selector = None
		finally:
			return selector
		
mm = get_mm_pic('http://www.mmjpg.com/home/1')
# mm = get_mm_pic('http://www.mmjpg.com/tag/xinggan/1')
# http://www.mmjpg.com/home/1
#http://www.mmjpg.com/tag/xinggan/3