#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-14 00:11:29
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import re
import urllib2
from bs4 import BeautifulSoup
import MySQLdb
import time

class xixiItem(object):
	''' 定义xixiItem类'''
	mtype = None
	mtitle = None
	mauthor = None
	mtime = None

class getMovieInfo(object):
	def __init__(self, url):
		self.url = url
		self.filename = self.getFileName(self.url)
		print u'获取文件名成功.'
		self.urls = self.getUrls(self.url)
		print u'获取urls成功.正在爬取网页...'
		self.items = self.spider(self.urls)
		print u'已爬取所有网页.'
		print time.time()
		self.pipeline2print = self.pipeline2print(self.items)
		print u'已全部输出到屏幕'
		# self.pipeline2file = self.pipeline2file(self.items)
		# print u'写入文件成功'
		# self.pipeline2mysql = self.pipeline2mysql(self.items)
		# print u'写入数据库成功'
		print time.time()

	def getUrls(self, url):
		urls = []
		html = self.getSourcePage(url)
		s = '共(.*?)页'
		dPage = re.compile(s)
		fPage = re.search(dPage, html).group(1)
		# print fPage
		ul= self.url.split('-')
		# print ul
		for page in range(1, int(fPage)+1):
		# for page in range(1, 10):
			ul[-1] = str(page) + '.html'
			url = '-'.join(ul)
			urls.append(url)
		# print urls
		return urls
	
	def spider(self, urls):
		items = []
		for i,url in enumerate(urls):
			print u'正在爬取第' + str(i) + u'页数据...'
			html = self.getSourcePage(url)
			soup = BeautifulSoup(html, 'lxml')
			table = soup.find('table', attrs={'id':'threadlisttableid'})
			# print table
			tbodys = table.find_all('tbody')
			# print len(tbody)
			for tbody in tbodys:
				item = xixiItem()
				try:
					# print tbody.em.get_text()
					item.mtype = tbody.em.get_text()
					# print tbody.th.find('a', attrs={'class':'s xst'}).get_text()
					item.mtitle = tbody.th.find('a', attrs={'class':'s xst'}).get_text()
					# print tbody.find('td', attrs={'class':'by'}).cite.get_text().strip()
					item.mauthor = tbody.find('td', attrs={'class':'by'}).cite.get_text().strip()
					# print tbody.find('td', attrs={'class':'by'}).em.get_text()
					item.mtime = tbody.find('td', attrs={'class':'by'}).em.get_text()
				except:
					pass
					continue
				else:
					items.append(item)
		return items
	
	def getFileName(self, url):
		html = self.getSourcePage(url)
		soup = BeautifulSoup(html, 'lxml')
		filename = soup.find('div', attrs={'class':'bm_h cl'}).h1.a.get_text().strip().encode('utf-8')
		return filename

	def pipeline2print(self, items):
		for item in items:
			print('类型:%s \t片名:%s \t发布者:%s \t发布时间:%s\n\n' %(item.mtype.encode('utf-8'), item.mtitle.encode('utf-8'), item.mauthor.encode('utf-8'), item.mtime.encode('utf-8')))
			
	def pipeline2file(self, items):
		filename = self.filename.decode('utf-8') + '.txt'
		# print self.filename
		with open(filename, 'w') as fp:
			for item in items:
				fp.write('类型:%s \t片名:%s \t发布者:%s \t发布时间:%s\n\n' %(item.mtype.encode('utf-8'), item.mtitle.encode('utf-8'), item.mauthor.encode('utf-8'), item.mtime.encode('utf-8')))
		
	def pipeline2mysql(self, items):
		conn = MySQLdb.connect(
			host='192.168.10.10',
			port=3306,
			user='crawl123',
			passwd='crawl123',
			db='scrapyDB',
			charset='utf8')
		cur = conn.cursor()
		for item in items:
			mtype = item.mtype.encode('utf-8')
			mtitle = item.mtitle.encode('utf-8')
			mauthor = item.mauthor.encode('utf-8')
			mtime = item.mtime.encode('utf-8')
			cur.execute("INSERT INTO xixizhan(mtype, mtitle, mauthor, mtime) values(%s,%s,%s,%s)",
						(mtype, mtitle, mauthor, mtime))
		cur.close()
		conn.commit()
		conn.close()

	def getSourcePage(self, url):
		response = urllib2.urlopen(url)
		html = response.read()
		return html


test = getMovieInfo('http://www.xixizhan.com/forum-41-1.html')
#http://www.xixizhan.com/forum-39-1.html