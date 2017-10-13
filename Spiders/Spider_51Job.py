#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-13 11:40:41
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib2
from bs4 import BeautifulSoup
import re

class Item(object):
	'''定义Item类'''
	JobName = None
	CompanyName = None
	WorkPlace = None
	Salary = None
	Time = None
	
class getJobInfo(object):
	"""get www.51job.com Info"""
	def __init__(self, url):
		self.url = url
		self.firstPage = self.getPage(self.url)
		self.urls = self.getUrls(self.firstPage)
		self.items = self.spider(self.urls)
		self.pipelines(self.items)
	
	def getPage(self, url):
		response = urllib2.urlopen(url)
		html = response.read()
		return html
	
	def getUrls(self, firstPage):
		s = '共(.*?)页'.decode('utf-8')
		defPage = re.compile(s)
		# print self.firstPage.decode('gbk')
		fullPage = re.search(defPage, self.firstPage.decode('gbk')).group(1)
		# print fullPage
		# fullPage = 65
		urls = []
		ul = self.url.split(',')
		for page in range(1, int(fullPage)+1):
			ul[-1] = str(page) + '.html'
			url = ','.join(ul)
			urls.append(url)
		return urls
	
	def spider(self, urls):
		items = []
		for url in urls:
			html = self.getPage(url)
			soup = BeautifulSoup(html, 'lxml')
			divs1 = soup.find('div', attrs={'id':'resultList'})
			divlists = divs1.find_all('div', attrs={'class': 'el'})
			divlists.pop(0)
			for div in divlists:
				item = Item()
				if len(div.get_text().split()) == 5:
					item.JobName = div.get_text().split()[0]
					item.CompanyName = div.get_text().split()[1]
					item.WorkPlace = div.get_text().split()[2]
					item.Salary = div.get_text().split()[3]
					item.Time = div.get_text().split()[4]
					items.append(item)
				else:
					pass
					continue
				# item.JobName = div.a.get_text().strip()
				# item.CompanyName = div.find('span', attrs={'class':'t2'}).a.string.strip()
				# item.WorkPlace = div.find('span', attrs={'class':'t3'}).get_text().strip()
				# item.Salary = div.find('span', attrs={'class':'t4'}).get_text().strip()
				# item.Time = div.find('span', attrs={'class':'t5'}).get_text().strip()
				
		return items
	
	def pipelines(self, items):
		# Job = self.url.split(',')[-3].encode('GBK')
		# fileName = Job + '.txt'
		fileName = u'51Job招聘信息.txt'
		with open(fileName, 'w') as fp:
			fp.write('%-35s \t| %-30s \t| %-20s \t| %20s \t| %20s \n' %('职位名', '公司名', '工作地点', '薪资', '发布时间'))
			for item in items:
				fp.write('%-40s \t| %-40s \t| %-20s \t| %20s \t| %20s \n' %(item.JobName.encode('utf-8'), item.CompanyName.encode('utf-8'), item.WorkPlace.encode('utf-8'), item.Salary.encode('utf-8'), item.Time.encode('utf-8')))

# JI = getJobInfo('http://search.51job.com/list/030200,000000,0000,00,9,99,Python%2B%25E7%2588%25AC%25E8%2599%25AB,2,1.html')
# JI = getJobInfo('http://search.51job.com/list/030200,000000,0000,00,9,99,linux%25E8%25BF%2590%25E7%25BB%25B4,2,1.html')
JI = getJobInfo('http://search.51job.com/list/030200,000000,0000,00,9,99,PHP,2,1.html')
# JI = getJobInfo('http://search.51job.com/list/030200,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE,2,1.html')
# http://search.51job.com/list/030200,000000,0000,00,9,99,Python%2B%25E7%2588%25AC%25E8%2599%25AB,2,1.html
# http://search.51job.com/list/030200,000000,0000,00,9,99,Python%2B%25E7%2588%25AC%25E8%2599%25AB,2,2.html