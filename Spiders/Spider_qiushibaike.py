#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-25 16:00:58
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib
import urllib2
import re

# 定义页数
page = 1
# 制定URL
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
# 设置user_agent
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	# print response.read()
	# #将页面转化为UTF-8编码
	content = response.read().decode('utf-8')
	# 创建正则表达式
	pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?">(.*?)</div>.*?<span>(.*?)</span>.*?<img src="(.*?)".*?<i class="number">(.*?)</i>', re.S)
	# 用正则匹配并赋值给items
	items = re.findall(pattern, content)
	for item in items:
		# 判断段子是否存在图片
		haveImg = re.search("pictures", item[3])
		# 过滤掉包含图片的段子
		if not haveImg:
			print item[0], item[1], item[2], item[4]

except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason