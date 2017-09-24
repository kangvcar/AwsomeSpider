#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-24 20:51:15
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

## 安装
# pip install lxml

## 路径表达式
#	表达式		描述
#	nodename	选取此节点的所有子节点。
#	/			从根节点选取。
#	//			从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
#	.			选取当前节点。
#	..			选取当前节点的父节点。
#	@			选取属性

from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print result

# html = etree.parse('hello.html')
# result = etree.tostring(html, pretty_print=True)
# print result

# html = etree.HTML(text)
# result = html.xpath('//li')
# print result
# print len(result)
# print type(result)
# print type(result[0])

# html = etree.HTML(text)
# result = html.xpath('//li/@class')
# print result

# html = etree.HTML(text)
# result = html.xpath('//li/a[@href="link1.html"]')
# print result

# html = etree.HTML(text)
# result = html.xpath('//li//span')
# print result

# html = etree.HTML(text)
# result = html.xpath('//li/a//@class')
# print result

# html = etree.HTML(text)
# result = html.xpath('//li[last()]/a/@href')
# print result

# html = etree.HTML(text)
# result = html.xpath('//li[last()-1]/a')
# print result[0].text

# html = etree.HTML(text)
# result = html.xpath('//*[@class="bold"]')
# print result[0].text