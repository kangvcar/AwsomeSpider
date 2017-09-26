#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-26 19:02:49
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import ssl
from selenium import webdriver
from bs4 import BeautifulSoup

# 取消证书认证
ssl._create_default_https_context = ssl._create_unverified_context()
# 调用PhantomJS启动浏览器
browser = webdriver.PhantomJS()
# 打开链接
browser.get('https://www.jisilu.cn/data/cbnew/#tlink_3')
# 延迟3秒，等待页面加载完成
browser.implicitly_wait(3)
# 打开文件并以追加模式写入
content2 = ''
with open('kzz.txt', 'a') as fp:
    soup = BeautifulSoup(browser.page_source, "lxml")
    soup2 = soup.find('table', id="flex3")
    x = 0
    for th in soup2.find_all('th'):
        # print str(th.string).encode('utf-8'),
        x += 1
        if x == 12: break
        for n in th.strings:
            content2 = n.encode('utf-8')
            # print type(content2)
            fp.write(content2)
        fp.write('\t')
    fp.write('\n')
    # 匹配前四行数据，并循环处理
    for tr in browser.find_elements_by_xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr[position()<5]'):
        # 获取每行的前面11条数据
        for i in range(11):
            # 以空格分割每行数据，并迭代获取数据
            content=tr.text.split(' ')[i] + "\t"
            # content 为 tuple 类型，用下表取值后进行硬编码为utf-8
            fp.write(content.encode('utf-8'))
        # 写入一行数据后换行
        fp.write('\n')

## kzz.txt
# 113009	广汽转债	127.16	0.47%	广汽集团	27.21	0.52%	3.73	21.430	126.97	0.15%
# 128016	雨虹转债	100.00	0.00%	东方雨虹	38.24	-5.16%	6.23	38.480	99.38	0.52%
# 132001	14宝钢EB	140.50	0.03%	新华保险	59.14	0.14%	2.49	42.310	139.78	1.41%
# 128014	永东转债	117.41	0.88%	永东股份	22.72	1.84%	4.02	20.460	111.05	5.73%