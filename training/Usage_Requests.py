#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-24 21:21:04
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

## 安装
# pip install requests

import requests

r = requests.get('http://cuiqingcai.com')
# print type(r)			#返回结果的类型
# print r.status_code	#返回结果的状态码
# print r.encoding		#返回结果的编码方式
# print r.text			#返回结果的源代码
# print r.cookies		#返回结果的Cookies

## 基本请求
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/head')
# r = requests.options('http://httpbin.org/get')

## 基本GET请求
# r = requests.get('http://httpbin.org/get')
# 如果想要加参数，可以利用 params 参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print r.url

# 如果想添加 headers，可以传 headers 参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# headers = {'content-type': 'application/json'}
# r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
# print r.url

## 基本POST请求
# 传参方法可以利用 data 这个参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print r.text

# 传JSON格式的数据过去，所以我们可以用 json.dumps() 方法把表单数据序列化
# import json
# url = 'http://httpbin.org/post'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
# print r.text

# 如果想要上传文件，那么直接用 file 参数即可
# 新建一个 a.txt 的文件，内容写上 Hello World!
# url = 'http://httpbin.org/post'
# files = {'file': open('test.txt', 'rb')}
# r = requests.post(url, files=files)
# print r.text

# requests 是支持流式上传的，这允许你发送大的数据流或文件而无需先把它们读入内存。
# 要使用流式上传，仅需为你的请求体提供一个类文件对象即可
# with open('massive-body') as f:
#     requests.post('http://some.url/streamed', data=f)


## Cookies
# 如果一个响应中包含了cookie，那么我们可以利用 cookies 变量来拿到
# url = 'http://www.baidu.com'
# r = requests.get(url)
# print r.cookies
# print r.cookies['example_cookie_name']

# 用 cookies 变量来向服务器发送 cookies 信息
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# print r.text


## 超时配置
# requests.get('http://github.com', timeout=0.001)


## 会话对象
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")
# print(r.text)

# 既然会话是一个全局的变量，那么我们肯定可以用来全局的配置了
# s = requests.Session()
# s.headers.update({'x-test': 'true'})
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print r.text


## SSL证书验证
# r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
# print r.text

# r = requests.get('https://github.com', verify=True)
# print r.text


## 代理
# proxies = {
#   "https": "http://41.118.132.69:4433"
# }
# r = requests.post("http://httpbin.org/post", proxies=proxies)
# print r.text