#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-13 18:47:39
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import re
from bs4 import BeautifulSoup
import urllib2

class movieItem(object):
	''' 定义 movieItem 类 '''
	MovieName = None
	UpdateTime = None
	Summary = None
	
class getMovieInfo(object):
	''' 爬取 www.ygdy8.net 站点的电影 '''
	def __init__(self, url):
		self.url = url
		self.sumPages = self.getSumPage(self.url)
		self.urls = self.getUrls(self.sumPages)
		self.items = self.spider(self.urls)
		self.pipelines(self.items)
		
	def getSumPage(self, url):
		''' 获取总页数 '''
		response = urllib2.urlopen(url)
		html = response.read()
		s = u'共(.*?)页'
		dSumpage = re.compile(s)
		fSumpage = re.search(dSumpage, html.decode('gbk')).group(1)
		# print fSumpage
		return fSumpage
		
	def getUrls(self, sumPages):
		''' 获取所有页面的url '''
		urls = []
		ul = self.url.split('_')
		for page in range(1, int(sumPages)+1):
			ul[-1] = str(page) + '.html'
			url = '_'.join(ul)
			urls.append(url)
		return urls
	
	def spider(self, urls):
		''' 爬取Item定义的信息'''
		items = []
		for url in urls:
			html = self.getContentPage(url)
			if html == None:
				continue
			soup = BeautifulSoup(html, 'lxml')
			tables = soup.find_all('table', attrs={'class':'tbspan'})
			for table in tables:
				item = movieItem()
				try:
					# item.MovieName = unicode(''.join(table.b.get_text().split()))
					item.MovieName = unicode(table.b.get_text().replace('\n', ''))
					item.UpdateTime = unicode(table.find_all('tr')[2].get_text().split()[0].split('：'.decode('utf-8'))[1])
					item.Summary = unicode(table.find_all('tr')[3].get_text().strip())
				except:
					pass
					continue
				else:
					items.append(item)
		return items
	
	def pipelines(self, items):
		''' 处理爬取到的内容'''
		filename = u'国内电影.txt'
		with open(filename, 'w') as fp:
			for item in items:
				fp.write('片名:%s \n更新时间:%s \n影片摘要:%s \n\n' %(item.MovieName.encode('utf-8'), item.UpdateTime.encode('utf-8'), item.Summary.encode('utf-8')))
	
	def getContentPage(self, url):
		''' 获取网页源代码'''
		try:
			response = urllib2.urlopen(url, timeout=4)
		except:
			return None
		else:
			html = response.read()
			return html

ZXDY = getMovieInfo('http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html')
# ZXDY = getMovieInfo('http://www.ygdy8.net/html/gndy/oumei/list_7_2.html')
#http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html
#http://www.ygdy8.net/html/gndy/china/list_4_2.html