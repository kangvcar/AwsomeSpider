# -*- coding: utf-8 -*-

import urllib
import urllib2

response = urllib2.urlopen('http://fanyi.youdao.com')
html = response.read()
f = open('Youdao.txt', 'w')
f.write(html)
f.close()