#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-15 19:14:54
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import urllib2
import requests
from lxml import html
import os
import time
import random
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

class get_babehub_pic(object):
	def __init__(self, url):
		print self.get_current_time() + u' 爬虫开始...'
		self.url = url
		self.to_addr = 'kangvcar123@163.com'
		# self.to_addr = '15119523504@163.com'
		# self.to_addr = '919497370@qq.com'
		# self.to_addr = '806215829@qq.com'
		# self.to_addr = '15875458822@163.com'
		print self.get_current_time() + u' 正在爬取' + self.url + u'站点...'
		# 获取总页数
		self.sum_pages = self.get_sum_page(self.url)
		# 获取所有页面的url
		self.all_page_urls = self.get_all_page_urls(self.sum_pages)
		# 获取所有图集的url,返回的是一个tuple,包含两个元素
		self.all_album_and_video_urls = self.get_all_album_and_video_urls(self.all_page_urls)
		# 所有图集urls, dict
		self.all_album_urls = self.all_album_and_video_urls[0]
		# 所有视频urls, dict
		self.all_video_urls = self.all_album_and_video_urls[1]
		# 下载所有图片并保存到以图集名称命名的文件夹
		self.download_album_to_dir = self.get_download_album_to_dir(self.all_album_urls)
		print self.get_current_time() + u' 已载所有图片并保存到以图集名称命名的文件夹...'
		# 下载所有视频并保存到以图集名称命名的文件夹
		# self.download_video_to_dir = self.get_download_video_to_dir(self.all_video_urls)
		# print self.get_current_time() + u' 已载所有视频并保存到以视频标题名称命名的文件夹...'
		#######################################################################
		# 获取所有图片的src
		# self.all_album_pic_srcs = self.get_all_album_pic_srcs(self.all_album_urls)
		# 获取所有webm格式视频的src
		# self.all_video_webm_srcs = self.get_all_video_webm_srcs('http://www.babehub.com/video-archive/page/1')
		# 发送所有图片或者视频的src到邮箱
		# self.send_email_as_src(self.all_album_pic_srcs)
		# headers 在下载视频的函数get_download_video_to_dir()里可能会需要
		# self.headers = {
		# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
		# 	'Accept-Encoding': 'gzip, deflate',			# 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		# 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		# 	'Accept-Language': 'zh-CN,zh;q=0.8'
		# }
		
	def get_sum_page(self, url):
		'''获取总页数...'''
		print self.get_current_time() + u' 正在获取总页数...'
		sum_pages = 1
		print self.get_current_time() + u' 总共获取' + str(sum_pages) + u'页...'
		return sum_pages
	
	def get_all_page_urls(self, sum_pages):
		'''根据总页数，获取所有页面的url...'''
		print self.get_current_time() + u' 正在根据总页数，获取所有页面的url...'
		all_page_urls_list = []
		ul = self.url.split('/')
		for page in range(1, int(sum_pages) + 1):
			ul[-1] = str(page)
			url = '/'.join(ul)
			all_page_urls_list.append(url)
		print self.get_current_time() + u' 总共获取' + str(len(all_page_urls_list)) + u'个页面的url...'
		return all_page_urls_list
		
	def get_all_album_and_video_urls(self, all_page_urls):
		'''获取所有图集的url...'''
		print self.get_current_time() + u' 正在获取所有图集和视频的url...'
		all_album_urls_dict = {}	#存储图集title和url
		all_video_urls_dict = {}	#存储视频title和url
		for page_url in all_page_urls:
			try:
				selector = self.get_source_page(page_url)
			except:
				continue
			album_li_tags = selector.xpath('//article[@id="content"]/ul//li[not(@class)]')
			video_li_tags = selector.xpath('//article[@id="content"]/ul//li[@class="vid"]')
			for album_li_tag in album_li_tags:		#匹配图集urls
				try:
					album_title = album_li_tag.xpath('./a/span/text()')[0]
					album_url = album_li_tag.xpath('./a/@href')[0]
				except:
					continue
				else:
					all_album_urls_dict[album_title] = album_url
			for video_li_tag in video_li_tags:		#匹配视频urls
				try:
					video_title = video_li_tag.xpath('./a/span/text()')[0]
					video_url = video_li_tag.xpath('./a/@href')[0]
				except:
					continue
				else:
					all_video_urls_dict[video_title] = video_url
		print self.get_current_time() + u' 总共获取' + str(len(all_album_urls_dict)) + u'个图集的url...'
		print self.get_current_time() + u' 总共获取' + str(len(all_video_urls_dict)) + u'个视频的url...'
		return all_album_urls_dict, all_video_urls_dict		#返回的是tuple
	
	# 注意：传入的all_album_urls 为dict字典
	def get_download_album_to_dir(self, all_album_urls):
		'''下载所有图片并保存到以图集名称命名的文件夹...'''
		print self.get_current_time() + u' 正在下载所有图片并保存到以图集名称命名的文件夹...'
		a = 0
		for album_title, album_url in all_album_urls.items():
			a += 1
			album_dir_name = self.mk_dir(album_title)
			try:
				selector = self.get_source_page(album_url)
				album_pic_srcs = selector.xpath('//article[@id="content"]//ul[1]//li/a/@href')
			except:
				continue
			else:
				try:
					for pic_num, album_pic_src in enumerate(album_pic_srcs):
						filename = album_dir_name + '/' +  str(pic_num + 1) + '.jpg'
						with open(filename, 'wb') as fp:
							fp.write(urllib2.urlopen(album_pic_src).read())
				except:
					print self.get_current_time() + u' 下载图集 <' + album_dir_name + u'> 失败!!!'
					continue
			print self.get_current_time() + u' 下载图集' + str(a) + u' <' + album_dir_name + u'> 成功...'
	
	def get_download_video_to_dir(self, all_video_urls):
		'''下载所有视频并保存到以视频名称命名的文件夹...'''
		print self.get_current_time() + u' 下载所有视频并保存到以视频名称命名的文件夹...'
		a = 0
		for video_title, video_url in all_video_urls.items():
			a += 1
			video_dir_name = self.mk_dir(video_title)
			# if status == 'fail':
			# 	print self.get_current_time() + ' ' + video_title + u'视频目录已存在,已跳过下载该视频...'
			# 	continue
			try:
				selector = self.get_source_page(video_url)
				video_src = selector.xpath('//article[@id="content"]//video/source[position()=2]/@src')[0]
			except:
				continue
			else:
				try:
					video_name = video_dir_name + '/' + str(a) + '.webm'
					print self.get_current_time() + u' 正在下载视频 ' + video_name + u'...'
					# video_response = requests.get(video_src, headers=self.headers)
					video_response = requests.get(video_src)
					video_data = video_response.content
					if video_data:
						with open(video_name, 'wb') as vf:
							vf.write(video_data)
				except:
					print self.get_current_time() + ' ' + video_name + u' 视频' + str(a) + u'下载失败！！！！'
				else:
					print self.get_current_time() + u' 已下载视频 ' + str(a) + video_name + u'到本地...'
	
	def get_all_album_pic_srcs(self, all_album_urls):
		'''获取所有图片的src...'''
		print self.get_current_time() + u' 正在获取所有图片src...'
		all_album_pic_srcs = []
		a = 0
		for album_title, album_url in all_album_urls.items():
			a += 1
			selector = self.get_source_page(album_url)
			album_pic_srcs = selector.xpath('//article[@id="content"]//ul[1]//li/a/@href')
			for album_pic_src in album_pic_srcs:
				all_album_pic_srcs.append(album_pic_src)
			print self.get_current_time() + u' 正在获取图集' + str(a) + u'<' + album_title + u'>所有图片src...'
		print self.get_current_time() + u' 已获取所有图片src...'
		return all_album_pic_srcs
	
	def get_all_video_webm_srcs(self, video_page_url):
		'''获取所有webm视频src...'''
		print self.get_current_time() + u' 正在获取所有视频src...'
		################获取视频页的urls开始##############################
		all_video_page_urls_list = []
		video_sum_page = 4
		ul = video_page_url.split('/')
		for page in range(4, int(video_sum_page) + 1):
			ul[-1] = str(page)
			video_page_url = '/'.join(ul)
			all_video_page_urls_list.append(video_page_url)
		print self.get_current_time() + u' 总共获取到' + str(video_sum_page) + u'页视频资源...'
		################获取视频页的urls结束##############################
		################获取视频页所有视频入口的urls开始####################
		all_video_urls_list = []
		for page_num, video_url in enumerate(all_video_page_urls_list):
			print self.get_current_time() + u'正在爬取第' + str(page_num + 1) + u'页的视频资源...'
			selector = self.get_source_page(video_url)
			video_urls = selector.xpath('//article[@id="content"]/ul//li/a/@href')
			for video_url in video_urls:
				all_video_urls_list.append(video_url)
			print self.get_current_time() + u'已爬取第' + str(page_num + 1) + u'页的视频资源...'
		################获取视频页所有视频入口的urls开始####################
		################获取所有视频的webm格式的src开始####################
		all_video_srcs_list = []
		for p, video_url in enumerate(all_video_urls_list):
			print self.get_current_time() + u'正在爬取第' + str(p + 1) + u'个的视频资源src...'
			selector = self.get_source_page(video_url)
			# video_src = selector.xpath('//article[@id="content"]/video//source[last()]/@src')[0]	#webm格式
			video_src = selector.xpath('//article[@id="content"]/video//source[1]/@src')[0]			#MP4格式
			all_video_srcs_list.append(video_src)
		print self.get_current_time() + u' 总共获取到' + str(len(all_video_srcs_list)) + u'个视频资源src...'
		################获取所有视频的webm格式的src结束####################
		print self.get_current_time() + u' 已获取所有视频src资源...'
		return all_video_srcs_list
	
	def send_email_as_src(self, pic_or_src_list):
		'''使用电子邮件发送数据'''
		print self.get_current_time() + u'正在发送内容至邮箱 ...'
		# 函数_format_addr()用来格式化一个邮件地址
		def _format_addr(s):
			name, addr = parseaddr(s)
			return formataddr((
				Header(name, 'utf-8').encode(),
				addr.encode('utf-8') if isinstance(addr, unicode) else addr))
		
		# Email地址和口令:
		from_addr = 'kangvcar1234@163.com'
		password = 'pyproject1234'
		# SMTP服务器地址:
		smtp_server = 'smtp.163.com'
		# 收件人地址:
		to_addr = self.to_addr
		# 构造邮件
		sum_src = len(pic_or_src_list)
		msgtext = "\n".join(pic_or_src_list)
		msg = MIMEText(msgtext, 'plain', 'utf-8')
		msg['From'] = _format_addr(u'我的Python学习资源<%s>' % from_addr)
		msg['To'] = _format_addr(u'管理员<%s>' % to_addr)
		msg['Subject'] = Header(u'我的Python学习资源, 总共有%s个学习资源...' % sum_src, 'utf-8').encode()
		
		server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
		# server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
		# server.set_debuglevel(1)		#可以打印出和SMTP服务器交互的所有信息
		server.login(from_addr, password)  # 登录SMTP服务器
		server.sendmail(from_addr, to_addr, msg.as_string())  # 发邮件
		server.quit()
		print self.get_current_time() + u'内容已发送至邮箱, 请查收...'
	
	
	def mk_dir(self, dirname):
		'''创建文件夹'''
		path = dirname
		if os.path.exists(path):
			path = dirname + str(random.randint(1,5000))
		os.mkdir(path)
		print self.get_current_time() + u' 成功创建文件夹' + path + u'...'
		return path
	
	def get_current_time(self):
		'''获取当前时间'''
		at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		return at
	
	def get_source_page(self, url):
		try:
			response = urllib2.urlopen(url).read()
			selector = html.fromstring(response)
		except:
			selector = None
		finally:
			return selector
	
babehub = get_babehub_pic('http://www.babehub.com/page/1')
#http://www.babehub.com/page/1