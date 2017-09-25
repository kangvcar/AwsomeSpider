#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-25 19:47:32
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

from bs4 import BeautifulSoup


html = """
<div class="tqshow1"><h3>苏州<font color="#0066cc">今日</font>天气</h3><p>星期一</p><ul><li class="tqpng"><img class="pngtqico" align="absmiddle" src="http://img.tianqi.com/static/images/tianqibig/b8.png" style="border:0;width:46px;height:46px"></li><li><font color="#f00">26℃</font>~<font color="#4899be">23℃</font></li><li>中雨</li><li style="height:18px;overflow:hidden">东南风 1级</li></ul></div>
<div class="tqshow1"><h3>苏州<font color="red">明日</font>天气</h3><p>星期二</p><ul><li class="tqpng"><img class="pngtqico" align="absmiddle" src="http://img.tianqi.com/static/images/tianqibig/b3.png" style="border:0;width:46px;height:46px"></li><li><font color="#f00">29℃</font>~<font color="#4899be">24℃</font></li><li>阵雨</li><li style="height:18px;overflow:hidden">西风 3-4级</li></ul></div>
<div class="tqshow1"><h3>苏州<font color="red">后天</font>天气</h3><p>星期三</p><ul><li class="tqpng"><img class="pngtqico" align="absmiddle" src="http://img.tianqi.com/static/images/tianqibig/b3.png" style="border:0;width:46px;height:46px"></li><li><font color="#f00">28℃</font>~<font color="#4899be">23℃</font></li><li>阵雨</li><li style="height:18px;overflow:hidden">北风 4-5级</li></ul></div>
<div class="tqshow1"><h3>苏州28日天气</h3><p>星期四</p><ul><li class="tqpng"><img class="pngtqico" align="absmiddle" src="http://img.tianqi.com/static/images/tianqibig/b1.png" style="border:0;width:46px;height:46px"></li><li><font color="#f00">24℃</font>~<font color="#4899be">19℃</font></li><li>多云</li><li style="height:18px;overflow:hidden">东北风 4-5级</li></ul></div>
<div class="tqshow1"><h3>苏州29日天气</h3><p>星期五</p><ul><li class="tqpng"><img class="pngtqico" align="absmiddle" src="http://img.tianqi.com/static/images/tianqibig/b1.png" style="border:0;width:46px;height:46px"></li><li><font color="#f00">23℃</font>~<font color="#4899be">20℃</font></li><li>多云</li><li style="height:18px;overflow:hidden">东南风 3-4级</li></ul></div>
<div class="tqshow1"><h3>苏州30日天气</h3><p><font color="green">星期六</font></p><ul><li class="tqpng"><img class="pngtqico" align="absmiddle" src="http://img.tianqi.com/static/images/tianqibig/b1.png" style="border:0;width:46px;height:46px"></li><li><font color="#f00">25℃</font>~<font color="#4899be">21℃</font></li><li>多云</li><li style="height:18px;overflow:hidden">东南风 3-4级</li></ul></div>
"""
# 用 BeautifulSoup 实例化对象soup
soup = BeautifulSoup(html, "lxml")
# soup.find_all('div') 返回list , 可迭代
for div in soup.find_all('div'):
	# print type(div) # div 类型为bs4.element.Tag,不可实例化,所以先用str函数处理
	soup2 = BeautifulSoup(str(div), "lxml")
	print soup2.h3.get_text()
	print soup2.p.get_text()
	print soup2.ul.find_all('li')[1].get_text()
	print soup2.ul.find_all('li')[2].get_text()
	print soup2.ul.find_all('li')[3].get_text()
	print soup2.ul.find_all('li')[0].img['src']
	print '\n'
	# print type(soup2)
# print len(soup.find_all('div'))