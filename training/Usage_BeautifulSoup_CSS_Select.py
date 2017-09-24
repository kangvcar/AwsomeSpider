#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-24 18:50:21
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

from bs4 import BeautifulSoup

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
###select()返回list####
########################

## 我们在写 CSS 时，标签名不加任何修饰，类名前加点，id名前加 #，
## 在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list

## 1.通过标签名查找
# print soup.select('title')
# print soup.select('a')
# print soup.select('b')

## 2.通过类名查找
# print soup.select('.sister')

## 3.通过 id 名查找
# print soup.select('#link1')

## 4.组合查找
# 查找 p 标签中，id 等于 link1的内容，二者需要用空格分开
# print soup.select('p #link1')
# print soup.select('head #link1')
# 直接子标签查找
# print soup.select('head > title')

## 5.属性查找
# 查找时还可以加入属性元素，属性需要用中括号括起来
# print soup.select('a[class="sister"]')
# print soup.select('a[href="http://example.com/elsie"]')
# print soup.select('p a[href="http://example.com/elsie"]')

## 6.使用get_text()方法获取内容
# print type(soup.select('title'))
# print soup.select('title')[0].get_text()




