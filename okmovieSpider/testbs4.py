#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import lxml

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b>
<a href="http://example.com/elsie" class="sister14" id="link14">11</a>
<a href="http://example.com/lacie" class="sister" id="link22">22</a>
<a href="http://example.com/elsie" class="sister" id="link12">11</a>
<a href="http://example.com/elsie" class="sister" >15</a>
</p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "lxml")
# r = soup.select("p:nth-of-type(1) > a:nth-of-type(1)")
r1 = soup.select('a[href="http://example.com/tillie"]')
r2 = soup.select("#link22 + .sister")
print(r1)