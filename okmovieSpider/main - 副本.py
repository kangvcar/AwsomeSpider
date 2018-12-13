#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree
import requests
import mysql.connector
import time

class movieInfo(object):
    '''define movieInfo Class to save movie info'''
    mid = None;
    mname = None;
    mimgurl = None;
    mscore = None;
    mdirector = None;
    mstar = None;
    mtype = None;
    marea = None;
    myear = None;
    msumary = None;
    mplayurl = None;

class okSpider(object):
    def __init__(self, url, sumpage):
        self.url = url
        self.sumpage = sumpage  # 爬取的页数
        self.pageurls = self.getIndexPages(self.url, self.sumpage)  # 获取总页数
        self.getMovieUrls = self.getMovieUrls(self.pageurls)    # 获取每部电影的详情页链接
        self.getMovieInfosItems = self.getMovieInfos(self.getMovieUrls)
        print(">>>>>> 正在写入数据库...")
        self.save2mysql(self.getMovieInfosItems)
        print(">>>>>> 成功写入数据库...")
        # for i in self.getMovieInfos:
        #     print(i.mid+"\t"+i.mname)

    def getIndexPages(self, url, sumpage):
        pageurls = list()
        ul = "-".join(url.split('-')[:-1])
        for page in range(1, sumpage+1):
            pageurls.append(ul + "-" + str(page) + ".html")
        return pageurls

    def getMovieUrls(self, pageurls):
        allurl = list()
        for i, pageurl in enumerate(pageurls):
            print("正在爬取第" + str(i+1) + "页")
            html = self.getSourceCode(pageurl)
            lis = html.xpath('//div[@class="xing_vb"]//ul/li')
            for ls in lis:
                urls = ls.xpath('//span[@class="xing_vb4"]/a/@href')
            for eachurl in urls:
                url = 'http://www.okzy.co' + eachurl
                allurl.append(url)
        return allurl

    def getMovieInfos(self, infourls):
        items = []
        for i, infourl in enumerate(infourls):
            try:
                item = movieInfo()
                html = self.getSourceCode(infourl)
                item.mid = infourl.split('-')[-1].split('.')[0]
                item.mname = html.xpath('//div[@class="vodInfo"]//h2')[0].text
                item.mimgurl = html.xpath('//img[@class="lazy"]/@src')[0]
                item.mscore = html.xpath('//div[@class="vodInfo"]//label')[0].text
                item.mdirector = html.xpath('//div[@class="vodinfobox"]/ul//li[2]//span')[0].text
                item.mstar = html.xpath('//div[@class="vodinfobox"]/ul//li[3]//span')[0].text
                item.mtype = html.xpath('//div[@class="vodinfobox"]/ul//li[4]//span')[0].text
                item.marea = html.xpath('//div[@class="vodinfobox"]/ul//li[5]//span')[0].text
                item.myear = html.xpath('//div[@class="vodinfobox"]/ul//li[7]//span')[0].text
                item.msumary = html.xpath('//div[@class="vodplayinfo"]//span')[0].text.strip()
                item.mplayurl = html.xpath('//*[@id="2"]/ul/li/text()')[0].split('$')[-1]
                items.append(item)
                # print(mid)
                # print(mname+"\t\t"+mdirector+"\t\t"+mstar+"\t\t"+mtype+"\t\t"+marea+"\t\t"+myear)
                # print(msumary)
                # print(mplayurl+"\n")
                print(">>> 已成功爬取电影："+item.mname+"("+item.mid+")")
                time.sleep(1)
                # if (i==1):
                #     break
            except Exception as e:
                continue
        return items

    def save2mysql(self, items):
        conn = mysql.connector.connect(user='root', password='root', database='okmovie')
        cursor = conn.cursor()
        for item in items:
            try:
                mid = item.mid.encode('utf-8')
                mname = item.mname.encode('utf-8')
                mimgurl = item.mimgurl.encode('utf-8')
                mscore = item.mscore.encode('utf-8')
                mdirector = item.mdirector.encode('utf-8')
                mstar = item.mstar.encode('utf-8')
                mtype = item.mtype.encode('utf-8')
                marea = item.marea.encode('utf-8')
                myear = item.myear.encode('utf-8')
                msumary = item.msumary.encode('utf-8')
                mplayurl = item.mplayurl.encode('utf-8')

                cursor.execute(
                    'INSERT INTO movie(mid, mname, mimgurl, mscore, mdirector, mstar, mtype, marea, myear, msumary, mplayurl) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    [mid, mname, mimgurl, mscore, mdirector, mstar, mtype, marea, myear, msumary, mplayurl])

                conn.commit()
            except Exception as e:
            	pass
				continue
				
        cursor.close()
        conn.close()

    def getSourceCode(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        try:
            html = etree.HTML(requests.get(url, headers=headers).text.encode('ISO-8859-1', "ignore").decode('utf-8', "ignore"))
        except Exception as e:
            return None
        else:
            return html
# ISO-8859-1
# ok = okSpider('http://www.okzy.co/?m=vod-type-id-1-pg-2.html', 1)
ok = okSpider('http://www.okzy.co/?m=vod-type-id-22-pg-1.html', 1)

# url = 'http://www.okzy.co/?m=vod-type-id-1-pg-1.html'
# url = 'http://www.okzy.co/?m=vod-detail-id-22396.html'
# print(requests.get(url).encoding)
# print("-".join(url.split('-')[:-1]))