#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-14 22:20:36
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib2
from lxml import html
import os

class get_elitebabes_pic(object):
	def __init__(self, url):
		print u'开始爬虫...'
		print u'正在爬取 www.elitebabes.com 站点的所有模特图集...'
		self.url = url
		self.sum_pages = self.get_sum_page(self.url)	#获取总页数
		print u'总共需要爬取' + str(self.sum_pages) + u'页数据,请耐心等待...'
		self.all_page_urls = self.get_all_page_urls(self.sum_pages)		#获取所有页数的url
		print u'已获取' + str(len(self.all_page_urls)) + u'个页面的url.'
		self.all_modle_urls = self.get_all_modle_urls(self.all_page_urls)	#获取所有模特的主页url
		print u'已获取' + str(len(self.all_modle_urls)) + u'个模特的主页url.'
		self.all_modle_album_urls = self.get_all_modle_album_urls(self.all_modle_urls)	#获取所有模特的所有图集url并返回字典以模特名为key, 该模特图集url为values
		print u'已获取' + str(len(self.all_modle_album_urls)) + u'个模特的图集url.'
		# for k,v in self.all_modle_album_urls.items():
		# 	print k
		# 	for l in v:
		# 		print l
		self.download_modle_dir_album(self.all_modle_album_urls)	#下载所有图片，并保存到相应的文件夹
		print u'下载所有图片完成，并保存到相应的文件夹'
		
	def get_sum_page(self, url):
		'''获取总页数'''
		print u'正在获取总页数...'
		sum_pages = 67
		# sum_pages = 1
		return sum_pages
	
	def get_all_page_urls(self, sum_pages):
		'''获取所有页数的url'''
		print u'正在获取所有页数的url...'
		all_page_urls = []
		url = self.url + 'page/'
		ul = url.split('/')
		for page in range(1, int(sum_pages)+1):
		# for page in range(67, 68):
			ul[-1] = str(page)
			url = '/'.join(ul)
			all_page_urls.append(url)
		return all_page_urls

	def get_all_modle_urls(self, all_page_urls):
		'''获取所有模特的主页url'''
		print u'正在获取所有模特的主页url...'
		all_modle_urls = []
		for page_url in all_page_urls:
			try:
				selector = self.get_source_page(page_url)
				modles = selector.xpath('//article[@id="content"]//ul[@class="gallery-a a d"]//li/a/@href')
				for modle in modles:
					all_modle_urls.append(modle)
			except:
				print u'get_all_modle_urls()方法出现错误,已跳过..................'
				continue
		return all_modle_urls
	
	def get_all_modle_album_urls(self, all_modle_urls):
		'''获取所有模特的所有图集url, 并返回字典以模特名为key, 该模特图集url为values'''
		print u'正在获取所有模特的所有图集url...'
		all_modle_album_urls = {}
		for modle_url in all_modle_urls:
			try:
				selector = self.get_source_page(modle_url)
				modle_name = selector.xpath('//article[@id="content"]/h2/text()')[0]
				# modle_name = modle_url.split('/')[-2]
				modle_album_urls = selector.xpath('//article[@id="content"]//ul[@class="gallery-a b"]//li/a/@href')
				all_modle_album_urls[modle_name] = modle_album_urls
			except:
				print u'get_all_modle_album_urls()方法出现错误,已跳过..................'
				continue
		return all_modle_album_urls
		
	def download_modle_dir_album(self, all_modle_album_urls):
		''' 下载所有图集并保持在以图集名命名的文件夹内'''
		print u'正在下载所有图片中...并保存到相应的文件夹'
		for modle_name, modle_album_urls in all_modle_album_urls.items():	#注意：传入的all_modle_album_urls是一个dict
			modle_dir = self.mk_dir(modle_name)
			for modle_album_url in modle_album_urls:
				try:
					# print modle_album_url
					selector = self.get_source_page(modle_album_url)
					try:
						album_title = selector.xpath('//article//p[@class="mobile-hide description-a"]/text()')[0]
					except:
						album_title = 'album'
					# album_title = modle_album_url.split('/')[-2]
					album_pic_srcs = selector.xpath('//article//ul[@class="gallery-b"]/li/a/@href')	#获取一个图集里的所有图片的src,返回list
					modle_dir_album = modle_name + '/' + album_title
					modle_dir_album_name = self.mk_dir(modle_dir_album)
					
				except:
					print album_title + u'  download_modle_dir_album()方法出现错误,已跳过..................'
					continue
				else:
					# try:
					for a, album_pic_src in enumerate(album_pic_srcs):
						pic_name = str(a) + '.jpg'
						with open(modle_name + '/' + album_title + '/' + pic_name, 'wb') as fp:
							try:
								fp.write(urllib2.urlopen(album_pic_src).read())
							except:
								print u'下载模特' + modle_name + u' 图集<' + album_title + u'>某张图片失败!!!'
								continue
					print u'下载模特' + modle_name + u' 图集<' + album_title + u'>成功...'
					# except:
					# 	print u'下载模特' + modle_name + u' 图集<' + album_title + u'>失败!!!'
					# 	continue
					# else:
					# 	print u'下载模特' + modle_name + u' 图集<' + album_title + u'>成功...'

				
	def mk_dir(self, dirname):
		'''创建目录方法'''
		path = dirname
		if not os.path.exists(path):
			os.makedirs(path)
		return path

	def get_source_page(self, url):
		'''返回经过lxml.html.fromstring 模块处理的<Element html at 0x36e8278>，可以用 XPath 来过滤数据'''
		try:
			response = urllib2.urlopen(url, timeout=10).read()
			selector = html.fromstring(response)
		except:
			selector = None
		finally:
			return selector
		
modle_pic = get_elitebabes_pic('http://www.elitebabes.com/top-rated-babes/')
#http://www.elitebabes.com/top-rated-babes/		#此主题总共67页,需要手动修改get_sum_page()函数的sum_page参数为 sum_page = 67

#由于次站点为国外站点，所以爬虫速度一般