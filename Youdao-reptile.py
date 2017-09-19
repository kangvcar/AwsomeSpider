# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
# #爬取网页
# response = urllib2.urlopen('http://fanyi.youdao.com')
# html = response.read()
# #写入文件
# f = open('Youdao.html', 'w')
# f.write(html)
# f.close()
keyword = raw_input("请输入你要翻译的中文：")
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

values = {'i':keyword}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
result_page = response.read()
f = open('Youdao_result.html', 'w')
f.write(result_page)
f.close()