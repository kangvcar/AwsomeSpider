#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-13 11:40:41
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib2
from bs4 import BeautifulSoup
import re
import MySQLdb

class Item(object):
	'''定义Item类'''
	JobName = None
	CompanyName = None
	WorkPlace = None
	Salary = None
	Time = None
	
class getJobInfo(object):
	"""get www.51job.com Info"""
	def __init__(self, job):
		self.job = job
		self.baseurl = 'http://search.51job.com/list/030200,000000,0000,00,9,99,'
		self.url = self.baseurl + self.job + ',2,1.html'
		self.firstPage = self.getPage(self.url)
		self.urls = self.getUrls(self.firstPage)
		self.items = self.spider(self.urls)
		# self.pipelines2file(self.items)
		self.pipelines2mysql(self.items)
	
	def getPage(self, url):
		''' 获取网页源代码 '''
		response = urllib2.urlopen(url)
		html = response.read()
		return html
	
	def getUrls(self, firstPage):
		''' 获取urls列表 '''
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
		''' 爬取item类定义的信息'''
		items = []
		for url in urls:
			html = self.getPage(url)
			soup = BeautifulSoup(html, 'lxml')
			divs1 = soup.find('div', attrs={'id':'resultList'})
			divlists = divs1.find_all('div', attrs={'class': 'el'})
			for div in divlists:
				try:
					item = Item()
					print unicode(div.find('p', attrs={'class':'t1'}).get_text().strip())
					item.JobName = unicode(div.find('p', attrs={'class':'t1'}).get_text().strip())
					print unicode(div.find('span', attrs={'class':'t2'}).a.get_text())
					item.CompanyName = unicode(div.find('span', attrs={'class':'t2'}).a.get_text())
					print unicode(div.find('span', attrs={'class':'t3'}).get_text())
					item.WorkPlace = unicode(div.find('span', attrs={'class':'t3'}).get_text())
					print unicode(div.find('span', attrs={'class':'t4'}).get_text())
					item.Salary = unicode(div.find('span', attrs={'class':'t4'}).get_text())
					print unicode(div.find('span', attrs={'class':'t5'}).get_text())
					item.Time = unicode(div.find('span', attrs={'class':'t5'}).get_text())
				except:
					pass
					continue
				else:
					items.append(item)
		return items
	
	def pipelines2file(self, items):
		''' 把爬取到的数据存储到文件'''
		# Job = self.url.split(',')[-3]
		fileName = self.job + u'的招聘信息.txt'
		# fileName = u'51Job招聘信息.txt'
		with open(fileName, 'w') as fp:
			fp.write('%-35s \t| %-30s \t| %-20s \t| %20s \t| %20s \n' %('职位名', '公司名', '工作地点', '薪资', '发布时间'))
			for item in items:
				fp.write('%-40s \t| %-40s \t| %-20s \t| %20s \t| %20s \n' %(item.JobName.encode('utf-8'), item.CompanyName.encode('utf-8'), item.WorkPlace.encode('utf-8'), item.Salary.encode('utf-8'), item.Time.encode('utf-8')))

	def pipelines2mysql(self, items):
		''' 把爬取到的数据存储到数据库'''
		conn = MySQLdb.connect(
				host='192.168.10.10',
				port=3306,
				user='crawl123',
				passwd='crawl123',
				db='scrapyDB',
				charset = 'utf8')
		cur = conn.cursor()
		for item in items:
			JobName = item.JobName.encode('utf-8')
			CompanyName = item.CompanyName.encode('utf-8')
			WorkPlace = item.WorkPlace.encode('utf-8')
			Salary = item.Salary.encode('utf-8')
			Time1 = item.Time.encode('utf-8')
			cur.execute("INSERT INTO pythonjobs(JobName, CompanyName, WorkPlace, Salary, Time1) values(%s,%s,%s,%s,%s)", (JobName,CompanyName,WorkPlace,Salary,Time1))
		cur.close()
		conn.commit()
		conn.close()

JI = getJobInfo('python')


#创建数据表命令
#create database scrapyDB character set 'utf8' collate 'utf8_general_Ci'
#create table jobs( id int auto_increment, JobName char(60), CompanyName char(60), WorkPlace char(60), Salary char(60), Time1 char(60), primary key(id))engine=InnoDB DEFAULT CHARSET=utf8;