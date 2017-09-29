#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-29 19:02:49
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$
 
import smtplib
from email.mime.text import MIMEText
# 构造邮件
msg = MIMEText('hello, send by Python...123', 'plain', 'utf-8')
# 输入Email地址和口令:
from_addr = raw_input('From:')	#kangvcar123@163.com
password = raw_input('Password:')	#xxxxxxxx
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server:')	#smtp.163.com
# 输入收件人地址:
to_addr = raw_input('To:') 	##kangvcar123@163.com

server = smtplib.SMTP(smtp_server, 25) 	# SMTP协议默认端口是25
server.set_debuglevel(1)		#可以打印出和SMTP服务器交互的所有信息
server.login(from_addr, password) 	#登录SMTP服务器
server.sendmail(from_addr, to_addr, msg.as_string()) 	#发邮件
server.quit()
