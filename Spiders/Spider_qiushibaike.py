#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-25 16:00:58
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$


import urllib
import urllib2
import re
import thread
import time

#糗事百科爬虫类
class QSBK:
	"""docstring for QSBK"""
	#初始化方法，定义一些变量
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
		# 初始化headers
		self.headers = {'User-Agent': self.user_agent}
		# 存放段子的变量，每一个元素是每一页的段子们
		self.stories = []
		# 存放程序是否继续运行的变量
		self.enable = False

	#传入某一页的索引获得页面代码
	def getPage(self, pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			# 构建请求的request
			request = urllib2.Request(url, headers=self.headers)
			# 利用urlopen获取页面代码
			response = urllib2.urlopen(request)
			# 将页面转化为UTF-8编码
			pageCode = response.read().decode('utf-8')
			return pageCode
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"连接糗事百科失败，错误原因：", e.reason
				return None

	# 传入某一页代码，返回本页不带图片的段子列表
	def getPageItems(self, pageIndex):
		pageCode = self.getPage(pageIndex)
		if not pageCode:
			print "页面加载失败..."
			return None
		pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?">(.*?)</div>.*?<span>(.*?)</span>.*?<img src="(.*?)".*?<i class="number">(.*?)</i>', re.S)
		items = re.findall(pattern, pageCode)
		# 用来存储每页的段子们
		pageStories = []
		# 遍历正则表达式匹配的信息
		for item in items:
			# 是否存在图片
			haveImg = re.search("pictures", item[3])
			# 如果不含有图片，把它加入list中
			if not haveImg:
				replaceBR = re.compile('<br/>')
				text = re.sub(replaceBR, "\n", item[2])
				#item[0]是一个段子的发布者，item[1]是发布者年龄，item[2]是内容,item[4]是喜欢数
				pageStories.append([item[0].strip(), item[1].strip(), text.strip(), item[4].strip()])
		return pageStories

	# 加载并提取页面的内容，加入到列表中
	def loadPage(self):
		# 如果当前未看的页数少于2页，则加载新一页
		if self.enable == True:
			if len(self.stories) < 2:
				# 获取新一页
				pageStories = self.getPageItems(self.pageIndex)
				# 将该页的段子存放到全局list中
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1

	# 调用该方法，每次敲回车打印输出一个段子
	def getOneStory(self, pageStories, page):
		# 遍历一页的段子
		for story in pageStories:
			# 等待用户输入
			input = raw_input()
			# 每当输入回车一次，判断一下是否要加载新页面
			if input == 'Q':
				self.enable = False
				return
			print u"第%d页\t发布人:%s\t发布人年龄:%s\t喜欢数:%s\n%s" % (page, story[0], story[1], story[3], story[2])

	# 开始方法
	def start(self):
		print u"正在读取糗事百科,按回车查看新段子，Q退出"
		#使变量为True，程序可以正常运行
		self.enable = True
		self.loadPage()
		nowPage = 0
		while self.enable:
			if len(self.stories) >= 0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories, nowPage)
spider = QSBK()
spider.start()



# # 定义页数
# page = 1
# # 制定URL
# url = 'https://www.qiushibaike.com/hot/page/' + str(page)
# # 设置user_agent
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent': user_agent}

# try:
# 	request = urllib2.Request(url, headers = headers)
# 	response = urllib2.urlopen(request)
# 	# print response.read()
# 	# #将页面转化为UTF-8编码
# 	content = response.read().decode('utf-8')
# 	# 创建正则表达式
# 	pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?">(.*?)</div>.*?<span>(.*?)</span>.*?<img src="(.*?)".*?<i class="number">(.*?)</i>', re.S)
# 	# 用正则匹配并赋值给items
# 	items = re.findall(pattern, content)
# 	for item in items:
# 		# 判断段子是否存在图片
# 		haveImg = re.search("pictures", item[3])
# 		# 过滤掉包含图片的段子
# 		if not haveImg:
# 			print item[0], item[1], item[2], item[4]

# except urllib2.URLError, e:
# 	if hasattr(e, "code"):
# 		print e.code
# 	if hasattr(e, "reason"):
# 		print e.reason