#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-24 15:45:17
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

## 首先必须要导入 bs4 库
from bs4 import BeautifulSoup

## 创建一个字符串，后面的例子我们便会用它来演示
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

## 创建 beautifulsoup 对象,并处理html字符串，处理结果会自动补全html代码
soup = BeautifulSoup(html, "lxml")
# soup = BeautifulSoup(open(index.html), "lxml")
# print soup
## 打印一下 soup 对象的内容，格式化输出
# print soup.prettify()
#
## 点选法，返回匹配的第一个
# print soup.title
# print soup.head
# print soup.a
# print soup.p
# print type(soup.a)	#<class 'bs4.element.Tag'>
# 
## Tag
# print soup.name 			#[document]
# print soup.head.name 		#head
# print soup.p.attrs		#{'class': ['title'], 'name': 'dromouse'}
# print soup.p['class']		#['title']
# print soup.p.get('class')	#['title']
# soup.p['class'] = "newClass"	#修改属性
# print soup.p
# del soup.p['class']		#删除属性
# print soup.p

# NavigableString
# print soup.p.string 		#获取p标签里的内容,只能匹配第一个p标签
# print type(soup.p.string)	#<class 'bs4.element.NavigableString'>

# BeautifulSoup
# print type(soup.name)		#<type 'unicode'>
# print soup.name 			#[document]
# print soup.attrs 			#{}

# Comment
# print soup.a
# print soup.a.string 		# Elsie 
# print type(soup.a.string) 	#<class 'bs4.element.Comment'>

## 遍历文档树
# 1.直接子节点
# .contents  属性(获取子节点)
# print soup.head.contents	# .content 属性可以将tag的子节点以列表的方式输出
# print soup.head.contents[0]	#输出方式为列表，我们可以用列表索引来获取它的某一个元素

# .children  属性(获取子节点)
# print soup.head.children		#它返回的不是一个list,它是一个 list 生成器对象,不过我们可以通过遍历获取所有子节点。
# for child in soup.body.children:
# 	print child

# 2.所有子孙节点
# .descendants 属性(获取子孙节点)
# print soup.descendants	#它返回的不是一个 list 生成器对象,我们可以通过遍历获取所有子孙节点。
# for child in soup.descendants:
# 	print child

# 3.节点内容
# .string 属性
# print soup.head.string	#如果标签里面只有唯一的一个标签了,那么 .string 也会返回最里面的内容。
# print soup.title.string 	#如果一个标签里面没有标签了,那么 .string 就会返回标签里面的内容。
# print soup.html.string		#如果tag包含了多个子节点,tag就无法确定.string 方法应该调用哪个子节点的内容, .string 的输出结果是 None

# 4.多个内容
# .strings	属性
# for string in soup.strings:		#获取多个内容，不过需要遍历获取
# 	print repr(string)

# .stripped_strings 属性
# for string in soup.stripped_strings:	#去掉输出的字符串中包含的很多空格或空行
# 	print repr(string)

# 5.父节点
# .parent 属性
# p = soup.p
# print p.parent.name 		#获取父节点的name
# content = soup.head.title.string
# print content.parent.name 	#获取父节点的name

# 6.全部父节点
# .parents 属性
# content = soup.head.title.string
# for parent in content.parents: 	#递归得到元素的所有父辈节点,返回的是一个生成器,需要遍历获取
# 	print parent.name
# print content.parents

# 7.兄弟节点	(兄弟节点可以理解为和本节点处在统一级的节点)
# .next_sibling  属性
# print soup.p.next_sibling	# 返回下一个兄弟节点
# print soup.p.next_sibling.next_sibling 		# 返回下下个兄弟节点

# .previous_sibling 属性
# print soup.p.previous_sibling	## 返回上一个兄弟节点
#注意：实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白，
#因为空白或者换行也可以被视作一个节点，所以得到的结果可能是空白或者换行

# 8.全部兄弟节点
# .next_siblings  属性 
# .previous_siblings 属性
# .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出
# for sibling in soup.a.next_siblings:
# 	print repr(sibling)

# 9.前后节点		(它并不是针对于兄弟节点，而是在所有节点，不分层次)
# .next_element 属性
# print soup.head.next_element	#获取前一个element

# .previous_element 属性
# print soup.b.previous_element 	#获取后一个element

# 10.所有前后节点
# .next_elements  属性
# for element in soup.head.next_elements:
# 	print repr(element)

# .previous_elements 属性
# for element in soup.head.previous_elements:
# 	print repr(element)

## 搜索文档树
# 1.find_all( name , attrs , recursive , text , **kwargs )
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
	# name 参数
	# name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
		# A.传字符串
			# soup.find_all('b')
		# B.传正则表达式,使用match() 来匹配内容
			# 找出所有以b开头的标签
			# import re
			# for tag in soup.find_all(re.complie("^b")):
			# 	print tag.name
		# C.传列表
		# 如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回
			# 找到文档中所有<a>标签和<b>标签
			# soup.find_all(["a", "b"])
		# D.传 True
		# True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
			# for tag in soup.find_all(True):
			# 	print tag.name
		# E.传方法
		# 如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数
		# 如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
			# def has_class_but_no_id(tag):
			# 	return tag.has_attr('class') and not tag.has_attr('id')
			# soup.find_all(has_class_but_no_id)

	# keyword 参数
		# soup.find_all(id='link2')
		# soup.find_all(href=re.complie("elsie"))
		# soup.find_all(href=re.complie("elsie"), id='link1')
		# soup.find_all("a", class_="sister")
		# soup.find_all(attrs={"data-foo":"value"})

	# text 参数
	# 通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, 
	# text 参数接受 字符串 , 正则表达式 , 列表, True
		# soup.find_all(text="Elsie")
		# soup.find_all(text=["Tillie", "Elsie", "Lacie"])
		# soup.find_all(text=re.complie("Dormouse"))

	# limit 参数
	# 当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
		# soup.find_all("a", limit=2)

	# recursive 参数
	# 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
	# 如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
		# soup.html.find_all("title")
		# soup.html.find_all("title", recursive=False)

# 2.find( name , attrs , recursive , text , **kwargs )
# 它与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果

# 3.find_parents()  find_parent()
# find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容

# 4.find_next_siblings()  find_next_sibling()
# 这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,find_next_sibling() 只返回符合条件的后面的第一个tag节点

# 5.find_previous_siblings()  find_previous_sibling()
# 这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代, find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点
 
# 6.find_all_next()  find_next()
# 这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代, find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点

# 7.find_all_previous() 和 find_previous()
# 这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代, find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点