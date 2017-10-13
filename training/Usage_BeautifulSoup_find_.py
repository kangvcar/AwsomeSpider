#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-24 17:27:33
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

from bs4 import BeautifulSoup
import re

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
soup = BeautifulSoup(html, "lxml")

########################
###find_all()返回list####
########################

## 查找文档中所有的<b>标签,返回list
# print soup.find_all('b')

## 查找文档中所有的<a>标签,返回list
# for i in soup.find_all('a'):
# 	print i

## 找出所有以b开头的标签,返回list
# print soup.find_all(re.compile("^b"))
# for tag in soup.find_all(re.compile("^b")):
# 	print tag

## 找到文档中所有<a>标签和<b>标签,返回list
# print soup.find_all(['a','b'])

## 找到所有的tag,但是不会返回字符串节点,返回list
# for tag in soup.find_all(Tag):
# 	print tag.name

## 传入方法，如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
# def has_class_but_no_id(tag):
# 	return tag.has_attr('class') and not tag.has_attr('id')
# print soup.find_all(has_class_but_no_id)

## 匹配id=link2的tag
# print soup.find_all(id='link2')
 
## Beautiful Soup会搜索每个tag的”href”属性
# print soup.find_all(href=re.compile("elsie"))
 
## 使用多个指定名字的参数可以同时过滤tag的多个属性 
# print soup.find_all(href=re.compile("elsie"), id='link1')

## class 是 python 的关键词，这怎么办？加个下划线就可以
# print soup.find_all("a", class_="sister")

## 通过 text 参数可以搜搜文档中的字符串内容
## 与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True
# print soup.find_all(text="Elsie")
# print soup.find_all(text=["Tillie", "Elsie", "Lacie"])
# print soup.find_all(text=re.compile("Dormouse"))

## 当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.
# print soup.find_all("a", limit=2)

## 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
# print soup.html.find_all("title")
# print soup.html.find_all("title", recursive=False)

## find_all() 方法的返回结果是值包含一个元素的list
## find() 方法直接返回结果,非list
# print soup.find('a')

## find_parents()  find_parent() 用来搜索当前节点的父辈节点
# print soup.head.title.find_parents()
# print soup.head.title.find_parent()


## find_next_siblings()  方法返回所有符合条件的后面的兄弟节点,返回list
## find_next_sibling()  只返回符合条件的后面的第一个tag节点,非list
# print soup.body.p.find_next_siblings()
# print soup.body.p.find_next_sibling()

## find_previous_siblings()  方法返回所有符合条件的前面的兄弟节点,返回list
## find_previous_sibling()  方法返回第一个符合条件的前面的兄弟节点,非list
# print soup.body.find_previous_siblings()
# print soup.body.find_previous_sibling()

## find_all_next()  方法返回所有符合条件的节点,返回list
## find_next()  方法返回第一个符合条件的节点,非list
# print soup.head.find_all_next()
# print soup.head.find_next()

## find_all_previous()  方法返回所有符合条件的节点,返回list
## find_previous()  方法返回第一个符合条件的节点,非list
# print soup.head.title.find_all_previous()
# print soup.head.title.find_previous()