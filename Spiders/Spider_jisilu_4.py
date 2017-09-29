#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-28 21:06:29
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import ssl
from selenium import webdriver

#集思录爬虫类
class JSL:
	#初始化变量
	#传入url
	#传入filename文件名
	#传入is_ssl的值,1为使用ssl认证,0为禁用ssl认证
	#传入single_line的值,1为获取单行数据,2为获取双行数据,默认为0获取所有数据
	def __init__(self, url, filename, is_ssl, single_line=0):
		#爬虫的url
		self.url = url
		#保存内容的文件名
		self.filename = filename
		#设置是否启用ssl
		self.ssl = is_ssl
		#设置获取哪些行
		self.single_line = single_line
		#定义xpath
		self.xpath = '/html/body/div[3]/div[1]/div[1]/table/tbody/tr'
		#调用setSsl方法
		self.setSsl()

	#定义ssl方法
	def setSsl(self):
		if self.ssl == 0:
			ssl._create_default_https_context = ssl._create_unverified_context()
		elif self.ssl == 1:
			pass
		else:
			return None

	#设置浏览器驱动方法
	def setWebdrive(self):
		browser = webdriver.PhantomJS()
		return browser

	#传入浏览器驱动和url,返回网页源码
	def getPageSource(self, browser, url):
		# page = browser.get(url)
		browser.get(url)
		browser.implicitly_wait(3)
		return browser

	#传入网页源码，获取匹配的内容，然后写入contents并返回
	def getContent(self, browser):
		contents = []
		for tr in browser.find_elements_by_xpath(self.xpath):
			content = tr.text.encode('utf-8')
			contents.append(content)
		return contents

	#传入获取匹配的内容，把所需数据写入文件的方法
	def writeData(self, contents):
		file = open(self.filename, 'a')
		if self.single_line == 1:
			for index, content in enumerate(contents):
				if index % 2 == 0:
					file.write(content + '\n')
		elif self.single_line == 2:
			for index, content in enumerate(contents):
				if index % 2 == 1:
					file.write(content + '\n')
		else:
			for content in contents:
				file.write(content + '\n')
		file.close()

	#开始方法
	def start(self):
		browser = self.setWebdrive()
		page = self.getPageSource(browser, self.url)
		contents = self.getContent(page)
		if not contents:
			print u"获取内容失败,请确认URL是否正确"
			return
		else:
			self.writeData(contents)
			print u"内容已写入" + self.filename


#实例化对象jsl
#传入url
#传入filename文件名
#传入is_ssl的值,1为使用ssl认证,0为禁用ssl认证
#传入single_line的值,1为获取单行数据,2为获取双行数据,默认为0获取所有数据
jsl = JSL("https://www.jisilu.cn/data/cbnew/#tlink_3", '07150214-2.txt', 0, 2)
# jsl = JSL("https://www.jisilu.cn/data/cf/#stock",'kkk2.txt', 0, 0)
# jsl = JSL("https://www.jisilu.cn/data/sfnew/#tlink_3",'kkk2.txt', 0, 0)	#更改xpath为//*[@id="flex3"]/tbody/tr
#调用start方法
jsl.start()
