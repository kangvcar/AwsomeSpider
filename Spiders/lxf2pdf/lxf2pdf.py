#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : '2017/10/22'
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/

import urllib2
from lxml import html
from bs4 import BeautifulSoup
import pdfkit
import re
import os

class save2pdf(object):
	def __init__(self, url):
		self.url = url
		self.page_urls = self.get_page_urls(self.url)
		self.page_content_2_html = self.get_page_content_2_html(self.page_urls)
		self.html2pdf(self.page_content_2_html)
		
	def get_page_urls(self, url):
		page_urls_list = []
		soup = self.get_source_page(url)
		page_div = soup.find('div', attrs={'id': '001434446689867b27157e896e74d51a89c25cc8b43bdb3000'})
		page_a_urls = page_div.find_all('a')
		page_urls = []
		for page_a_url in page_a_urls:
			page_urls.append(page_a_url['href'])
		for page_url in page_urls:
			url = 'https://www.liaoxuefeng.com' + page_url
			page_urls_list.append(url)
		return page_urls_list
	
	def get_page_content_2_html(self, page_urls):
		filename_list = []
		for page, page_url in enumerate(page_urls):
			
			soup = self.get_source_page(page_url)
			page_title = soup.find('div', attrs={'class': 'x-content'}).h4
			# print page_title.get_text()
			page_content = soup.find('div', attrs={'class': 'x-wiki-content x-main-content'})
			page_content = str(page_content)
			img_src_complie = re.compile('src=\"/(.*?)/')
			page_content = img_src_complie.sub('src="https://www.liaoxuefeng.com/files/', page_content)
			filename = str(page) + '.html'
			with open(filename, 'w') as fp:
				fp.write(page_title.encode('utf-8'))
				fp.write(page_content)
			filename_list.append(filename)
			print u'正在写入第 ' + str(page + 1) + u' 个文件 ' + filename

		return filename_list
		
	def html2pdf(self, filename_list):
		options = {
			'page-size': 'Letter',
			'margin-top': '0.75in',
			'margin-right': '0.75in',
			'margin-bottom': '0.75in',
			'margin-left': '0.75in',
			'encoding': "UTF-8",
			'custom-header': [
				('Accept-Encoding', 'gzip')
			],
			'cookie': [
				('cookie-name1', 'cookie-value1'),
				('cookie-name2', 'cookie-value2'),
			],
			'outline-depth': 10,
		}
		pdfkit.from_file(filename_list, u'JavaScript.pdf',  options=options)
		
			
	def get_source_page(self, url):
		try:
			response = urllib2.urlopen(url).read()
			soup = BeautifulSoup(response, 'lxml')
		except:
			soup = None
		finally:
			return soup

# lxf2pdf = save2pdf('https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000')
# lxf2pdf = save2pdf('https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000')
lxf2pdf = save2pdf('https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000')
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000