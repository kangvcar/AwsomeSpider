#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-15 19:14:54
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib2
from lxml import html
import os
import time

class get_babehub_pic(object):
	def __init__(self, url):
		print self.get_current_time() + u' 爬虫开始...'
		self.url = url
		print self.get_current_time() + u' 正在爬取' + self.url + u'站点...'
		self.sum_pages = self.get_sum_page(self.url)	#获取总页数
		print self.get_current_time() + u' 总共获取' + str(self.sum_pages) + u'页...'
		self.all_page_urls = self.get_all_page_urls(self.sum_pages)	#获取所有页面的url
		print self.get_current_time() + u' 总共获取' + str(len(self.all_page_urls)) + u'个页面的url...'
		self.all_album_urls = self.get_all_album_urls(self.all_page_urls)		#获取所有图集的url,返回的是一个dict字典
		print self.get_current_time() + u' 总共获取' + str(len(self.all_album_urls)) + u'个图集的url成功...'
		self.download_album_to_dir = self.get_download_album_to_dir(self.all_album_urls)		#下载所有图片并保存到以图集名称命名的文件夹
		print self.get_current_time() + u' 已载所有图片并保存到以图集名称命名的文件夹...'
		
	def get_sum_page(self, url):
		'''获取总页数...'''
		print self.get_current_time() + u' 正在获取总页数...'
		sum_pages = 2
		return sum_pages
	
	def get_all_page_urls(self, sum_pages):
		'''根据总页数，获取所有页面的url...'''
		print self.get_current_time() + u' 正在根据总页数，获取所有页面的url...'
		all_page_urls_list = []
		ul = self.url.split('/')
		for page in range(2, int(sum_pages) + 1):
			ul[-1] = str(page)
			url = '/'.join(ul)
			all_page_urls_list.append(url)
		return all_page_urls_list
		
	def get_all_album_urls(self, all_page_urls):
		'''获取所有图集的url...'''
		print self.get_current_time() + u' 正在获取所有图集的url...'
		all_album_urls_dict = {}
		for page_url in all_page_urls:
			try:
				selector = self.get_source_page(page_url)
				album_li_tags = selector.xpath('//article[@id="content"]/ul//li')
			except:
				continue
			for album_li_tag in album_li_tags:
				try:
					album_title = album_li_tag.xpath('./a/span/text()')[0]
					album_url = album_li_tag.xpath('./a/@href')[0]
				except:
					continue
				else:
					all_album_urls_dict[album_title] = album_url
		return all_album_urls_dict
	
	# 注意：传入的all_album_urls 为dict字典
	def get_download_album_to_dir(self, all_album_urls):
		'''下载所有图片并保存到以图集名称命名的文件夹...'''
		print self.get_current_time() + u' 正在载所有图片并保存到以图集名称命名的文件夹...'
		a = 0
		for album_title, album_url in all_album_urls.items():
			a += 1
			album_dir_name = self.mk_album_dir(album_title)
			try:
				selector = self.get_source_page(album_url)
				album_pic_srcs = selector.xpath('//article[@id="content"]//ul[1]//li/a/@href')
			except:
				continue
			else:
				try:
					for pic_num, album_pic_src in enumerate(album_pic_srcs):
						filename = album_dir_name + '/' +  str(pic_num + 1) + '.jpg'
						with open(filename, 'wb') as fp:
							fp.write(urllib2.urlopen(album_pic_src).read())
				except:
					print self.get_current_time() + u' 下载图集 <' + album_title + u'> 失败!!!'
					continue
			print self.get_current_time() + u' 下载图集' + str(a) + u' <' + album_title + u'> 成功...'
		
	def mk_album_dir(self, dirname):
		'''创建文件夹'''
		print self.get_current_time() + u' 正在创建文件夹' + dirname + u'...'
		path = dirname
		if not os.path.exists(path):
			os.mkdir(path)
		return path
	
	def get_current_time(self):
		'''获取当前时间'''
		at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		return at
	
	def get_source_page(self, url):
		try:
			response = urllib2.urlopen(url).read()
			selector = html.fromstring(response)
		except:
			selector = None
		finally:
			return selector
	
babehub = get_babehub_pic('http://www.babehub.com/page/1')
#http://www.babehub.com/page/1