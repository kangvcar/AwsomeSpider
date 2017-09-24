# -*- coding: utf-8 -*-

import urllib
import urllib2

# 使用urllib2 获取网页源码方法一：
# url = 'http://www.baidu.com/'
# response = urllib2.urlopen(url)
# html = response.read()
# print html

# 使用urllib2 获取网页源码方法一：
# request = urllib2.Request('http://www.baidu.com')
# response = urllib2.urlopen(request)
# html = response.read()
# print html

# 使用POST方法并构造request传递data参数：
# values = {"username":"kangvcar", "password":"11111111111"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# html = response.read()
# print html

#使用GET方法传递数据
# values = {} 
# values['username'] = "kangvcar"
# values['password'] = "xxxxx"
# data = urllib.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?" + data
# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# print response.read()
# print "============"
# print geturl

# 在head中设置agent
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# values = {"username":"kangvcar", "password":"xxxxxxxxx"}
# headers = {'User-Agent': user_agent, 'Referer':'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'}
# data = urllib.urlencode(values)
# request = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(request)
# html = response.read()
# print html

#  HTTP Proxy代理的设置用法
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
# 	opener = urllib2.build_opener(proxy_handler)
# else:
# 	opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)

# Timeout 设置,urlopen()的第三个参数
# response = urllib2.urlopen('http://www.baidu.com', timeout=10)
# response = urllib2.urlopen('http://www.baidu.com', data, 10)

# 使用 HTTP 的 PUT 和 DELETE 方法
# import urllib2
# request = urllib2.Request(uri, data=data)
# request.get_method = lambda: 'PUT' 		# or 'DELETE'
# response = urllib2.urlopen(request)

# 使用 DebugLog
# httpHandler = urllib2.HTTPHandler(debuglevel=1)
# httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
# opener = urllib2.build_opener(httpHandler, httpsHandler)
# urllib2.install_opener(opener)
# response = urllib2.urlopen('http://www.baidu.com')

# URLError 的使用
# requset = urllib2.Request('http://www.xxxxx.com')
# try:
# 	urllib2.urlopen(requset)
# except urllib2.URLError, e:
# 	print e.reason

# HTTPError 的使用
# 100：继续 客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
# 101： 转换协议 在发送完这个响应最后的空行后，服务器将会切换到在 Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。
# 102：继续处理 由 WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。
# 200：请求成功 处理方式：获得响应的内容，进行处理
# 201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到 处理方式：爬虫中不会遇到
# 202：请求被接受，但处理尚未完成 处理方式：阻塞等待
# 204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。 处理方式：丢弃
# 300：该状态码不被 HTTP/1.0 的应用程序直接使用， 只是作为 3XX 类型回应的默认解释。存在多个可用的被请求资源。 处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
# 301：请求到的资源都会分配一个永久的 URL，这样就可以在将来通过该 URL 来访问此资源 处理方式：重定向到分配的 URL
# 302：请求到的资源在一个不同的 URL 处临时保存 处理方式：重定向到临时的 URL
# 304：请求的资源未更新 处理方式：丢弃
# 400：非法请求 处理方式：丢弃
# 401：未授权 处理方式：丢弃
# 403：禁止 处理方式：丢弃
# 404：没有找到 处理方式：丢弃
# 500：服务器内部错误 服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在**服务器端**的源代码出现错误时出现。
# 501：服务器无法识别 服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
# 502：错误网关 作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
# 503：服务出错 由于临时的**服务器**维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。
#### 3 开头的代号可以被处理，并且 100-299 范围的号码指示成功，所以你只能看到 400-599 的错误号码

# req = urllib2.Request('http://blog.csdn.net/cqcre')
# try:
# 	urllib2.urlopen(req)
# except urllib2.HTTPError, e:
# 	print e.code
# 	print e.reason


# req = urllib2.Request('http://blog.csdn.net/cqcre33')
# try:
# 	urllib2.urlopen(req)
# except urllib2.HTTPError, e:
# 	print e.code
# except urllib2.URLError, e:
# 	print e.reason
# else:
# 	print "OK"


# # 获取 Cookie 保存到变量
# import cookielib
# # 声明一个CookieJar对象实例来保存cookie
# cookie = cookielib.CookieJar()
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# # 此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# # 打印出了 cookie 中的值
# for item in cookie:
# 	print 'Name =' + item.name
# 	print 'Value =' + item.value

# # 保存 Cookie 到文件
# import cookielib
# # 设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib2.build_opener(handler)
# # 创建一个请求，原理同urllib2的urlopen
# response = opener.open('http://www.baidu.com')
# # 保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)

# # 从文件中获取 Cookie 并访问
# import cookielib
# # 创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()
# # 从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# # 创建请求的request
# req = urllib2.Request('http://www.baidu.com')
# # 利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print response.read()

# # 利用 cookie 模拟网站登录
# import urllib
# import urllib2
# import cookielib
# filename = 'cookie.txt'
# # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({
# 'stuid':'201200131012',
# 'pwd':'23342321'
# })
# # 登录教务系统的URL
# loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks\_login2.login'
# # 模拟登录，并把cookie保存到变量
# result = opener.open(loginUrl,postdata)
# # 保存cookie到cookie.txt中
# cookie.save(ignore_discard=True, ignore_expires=True)
# #利用cookie请求访问另一个网址，此网址是成绩查询网址
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print result.read()

# print '=============================================================='
# # -*- coding: utf-8 -*-
# #导入re模块
# import re
# # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
# pattern = re.compile(r'hello')
# # 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
# result1 = re.match(pattern,'hello')
# result2 = re.match(pattern,'helloo CQC!')
# result3 = re.match(pattern,'helo CQC!')
# result4 = re.match(pattern,'hello CQC!')

# #如果1匹配成功
# if result1:
# # 使用Match获得分组信息
# 	print result1.group()
# else:
# 	print '1匹配失败！'

# #如果2匹配成功
# if result2:
# # 使用Match获得分组信息
# 	print result2.group()
# 	# print result2.string
# 	# print result2.re
# 	# print result2.pos
# 	# print result2.endpos
# 	# print result2.lastindex
# 	# print result2.lastgroup
# else:
# 	print '2匹配失败！'

# #如果3匹配成功
# if result3:
# # 使用Match获得分组信息
# 	print result3.group()
# else:
# 	print '3匹配失败！'

# #如果4匹配成功
# if result4:
# # 使用Match获得分组信息
# 	print result4.group()
# else:
# 	print '4匹配失败！'

# print '=============================================================='
# #一个简单的match实例
# import re
# # 匹配如下内容：单词+空格+单词+任意字符
# m = re.match(r'(\w+) (\w+)(?P.*)', 'hello world!')
# print "m.string:", m.string				# m.string: hello world!
# print "m.re:", m.re 					# m.re:
# print "m.pos:", m.pos 					# m.pos: 0
# print "m.endpos:", m.endpos 			# m.endpos: 12
# print "m.lastindex:", m.lastindex		# m.lastindex: 3
# print "m.lastgroup:", m.lastgroup		# m.lastgroup: sign
# print "m.group():", m.group()	
# print "m.group(1,2):", m.group(1, 2)	# m.group(1,2): ('hello', 'world')
# print "m.groups():", m.groups()			# m.groups(): ('hello', 'world', '!')
# print "m.groupdict():", m.groupdict()	# m.groupdict(): {'sign': '!'}
# print "m.start(2):", m.start(2)			# m.start(2): 6
# print "m.end(2):", m.end(2)				# m.end(2): 11
# print "m.span(2):", m.span(2)			# m.span(2): (6, 11)
# print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')	# m.expand(r'\2 \1\3'): world hello!











