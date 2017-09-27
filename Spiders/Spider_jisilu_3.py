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
with open('kzz.txt', 'a') as fp:
    # 调用BeautifulSoup类实例化对象soup
    soup = BeautifulSoup(browser.page_source, "lxml")
    # 过滤出id="flex3" 的table
    soup2 = soup.find('table', id="flex3")
    x = 0
    # 过滤出table里的th, 并循环处理
    for th in soup2.find_all('th'):
        x += 1
        # 截取前12个
        if x == 12: break
        # 获取th下的全部内容，并循环处理
        for n in th.strings:
            content2 = n.split(' ')
            # print type(content2)
            # 返回list, 用下标提取并进行硬编码为utf-8
            fp.write(content2[0].encode('utf-8'))
        fp.write('\t')
    fp.write('\n')
    # 匹配前四行数据，并循环处理
    for tr in browser.find_elements_by_xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr[position()<5]'):
        # 获取每行的前面11条数据
        for i in range(11):
            # 以空格分割每行数据，并迭代获取数据
            content = tr.text.split(' ')[i]
            # content 为 tuple 类型，用小标提取后进行硬编码为utf-8
            fp.write(content.encode('utf-8'))
            fp.write('\t')
        # 写入一行数据后换行
        fp.write('\n')

## kzz.txt
#  代 码     转债名称    现 价    涨跌幅 正股名称    正股价 正股涨跌    PB  转股价 转股价值    溢价率 
# 128016  雨虹转债    100.00  0.00%   东方雨虹    39.01   -3.25%  6.23    38.480  101.38  -1.36%  
# 113009  广汽转债    127.00  0.35%   广汽集团    27.21   0.52%   3.73    21.430  126.97  0.02%   
# 132001  14宝钢EB    140.11  -0.25%  新华保险    59.18   0.20%   2.49    42.310  139.87  1.02%   
# 128014  永东转债    117.00  0.52%   永东股份    22.82   2.29%   4.02    20.460  111.53  4.90%   