#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-29 19:02:49
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$
 
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib

#函数_format_addr()用来格式化一个邮件地址
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((\
		Header(name, 'utf-8').encode(),\
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# 输入Email地址和口令:
from_addr = raw_input('From:')	#kangvcar123@163.com
password = raw_input('Password:')	#xxxxxxxx
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server:')	#smtp.163.com
# 输入收件人地址:
to_addr = raw_input('To:') 	##kangvcar123@163.com
# 构造邮件
msg = MIMEText('hello, send by Python...123', 'plain', 'utf-8')

msg['From'] = _format_addr(u'Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr(u'管理员<%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候······', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25) 	# SMTP协议默认端口是25
server.set_debuglevel(1)		#可以打印出和SMTP服务器交互的所有信息
server.login(from_addr, password) 	#登录SMTP服务器
server.sendmail(from_addr, to_addr, msg.as_string()) 	#发邮件
server.quit()
