#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-25 11:08:58
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

## 安装
# pip install pyquery

# print "================================================"
## 初始化
# 1.直接字符串
# from pyquery import PyQuery as pq
# doc = pq("<html></html>")

# 2.lxml.etree
# from lxml import etree
# doc = pq(etree.fromstring("<html></html>"))

# 3.直接传URL
# from pyquery import PyQuery as pq
# doc = pq('http://www.baidu.com')

# 4.传文件
# from pyquery import PyQuery as pq
# doc = pq(filename='hello.html')


# print "================================================"
# 
# hello.html 内容如下
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>

# from pyquery import PyQuery as pq
# doc = pq(filename='hello.html')
# print doc.html()
# print type(doc)
# li = doc('li')
# print type('li')
# print li.text()

# print "================================================"
## 属性操作
# from pyquery import PyQuery as pq
# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.attr("id")
# print p.attr("id", "plop")
# print p.attr("id", "hello")

# from pyquery import PyQuery as pq
# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.addClass('beauty')
# print p.removeClass('hello')
# print p.css('font-size', '16px')
# print p.css({'background-color': 'yellow'})

# print "================================================"
## DOM操作
# from pyquery import PyQuery as pq
 
# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>')
# print p.prepend('Oh yes!')
# d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
# p.prependTo(d('#test'))
# print p
# print d
# d.empty()
# print d

# print "================================================"
## 遍历
# 遍历用到 items 方法返回对象列表，或者用 lambda
# from pyquery import PyQuery as pq
# doc = pq(filename='hello.html')
# lis = doc('li')
# for li in lis.items():
#     print li.html()
 
# print lis.each(lambda e: e)

# print "================================================"
# 网页请求
# PyQuery 本身还有网页请求功能，而且会把请求下来的网页代码转为 PyQuery 对象。
# from pyquery import PyQuery as pq
# print pq('http://cuiqingcai.com/', headers={'user-agent': 'pyquery'})
# print pq('http://httpbin.org/post', {'foo': 'bar'}, method='post', verify=True)