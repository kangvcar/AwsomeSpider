#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-03 10:53:26
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/

import aiohttp
import asyncio

# async def fetch(session, url):
# 	async with session.get(url) as response:
# 		return await response.get_encoding()
#
# async def main():
# 	async with aiohttp.ClientSession() as session:
# 		html = await fetch(session, 'http://www.baidu.com')
# 		print(html)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# async def main():
# 	async with aiohttp.ClientSession() as session:
# 		async with session.get('http://www.okzy.co') as resp:
# 			print(resp.status)
# 			print(await resp.text())

# async def main():
# 	async with aiohttp.ClientSession() as session:
# 		async with session.get('https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2288864780.jpg') as resp:
# 			with open('fimg.jpg', 'wb') as fd:
# 				while True:
# 					chunk = await resp.content.read(20)
# 					if not chunk:
# 						break
# 					fd.write(chunk)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())