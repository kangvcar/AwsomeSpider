#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-25 16:00:58
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib
import urllib2

page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
try:
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	print response.read()
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason
