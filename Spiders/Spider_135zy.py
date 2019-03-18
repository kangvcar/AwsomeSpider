#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-3-17 19:25:26
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/

from lxml import etree
import requests
import pymysql.cursors
import threading

class movieInfo(object):
    '''define movieInfo Class to save movie info'''
    mId = None  # 影片ID
    mName = None    # 影片名
    mCover = None  # 影片封面
    mScore = None   # 影片评分
    mDirector = None    # 影片导演
    mStar = None    # 影片演员
    mType = None    # 影片类型
    mArea = None    # 影片地区
    mYear = None    # 影片上映年份
    mSumary = None  # 影片介绍
    mPlayUrl_m3u8 = None    # 影片播放链接，m3u8格式
    mPlayUrl_mp4 = None     # 影片播放链接，mp4格式

class zySpider(object):
    def __init__(self, sumPage, type):
        self.typedict = {'电影': 1, '连续剧': 2, '综艺': 2, '动漫': 4, '伦理片': 18, '美女热舞写真': 19, 'VIP视频秀': 20, '纪录片': 22,
                         '街拍美女': 23}
        self.type = type  # 设定爬取影片的类型，[电影，连续剧，综艺，动漫，伦理片，美女热舞，VIP视频秀，纪录片，街拍美女]
        if self.type in self.typedict:
            self.startUrl = 'http://www.135zy.vip/?m=vod-type-id-' + str(self.typedict[self.type])  # 爬虫起始页
        self.sumPage = sumPage      # 爬取的影片列表页的总页数
        self.pageUrls = self.getpageUrls(self.startUrl, self.sumPage)     # 生成所有影片列表页的链接
        self.movieUrls = self.getMovieUrls(self.pageUrls)   # 获取所有影片详情页的链接
        self.movieInfoItems = self.getMovieInfoItems(self.movieUrls)    # 获取所有影片详情信息
        self.save2mysql(self.movieInfoItems)    # 把所有影片信息写入数据库
        # print(self.MovieUrls)

    def getpageUrls(self, startUrl, sumPage):
        '''生成所有影片列表页的Url'''
        pageUrlsList = []
        for i in range(1, sumPage+1):
            pageUrl = startUrl + '-pg-' + str(i) + '.html'
            # print(pageUrl)
            pageUrlsList.append(pageUrl)
        return pageUrlsList

    def getMovieUrls(self, pageUrls):
        '''获取所有影片详情页的链接'''
        MovieUrlsList = []
        for i, pageurl in enumerate(pageUrls):
            print('正在爬取第'+str(i+1)+'页数据...')
            html = self.getSourceCode(pageurl)
            lis = html.xpath('//div[@class="xing_vb"]//ul/li')
            for ls in lis:
                urls = ls.xpath('//span[@class="xing_vb4"]/a/@href')
            for eachurl in urls:
                url = 'http://www.135zy.vip' + eachurl
                MovieUrlsList.append(url)
        return MovieUrlsList

    def getMovieDetail(self, detailUrl):
        '''获取一部影片的详情信息'''
        item = movieInfo()
        html = self.getSourceCode(detailUrl)
        item.mId = detailUrl.split('-')[-1].split('.')[0]
        item.mName = html.xpath('//div[@class="vodInfo"]//h2')[0].text
        item.mScore = html.xpath('//div[@class="vodInfo"]//label')[0].text
        # item.mScore = ' '
        item.mDirector = html.xpath('//div[@class="vodinfobox"]/ul//li[2]//span')[0].text + ' '
        # item.mDirector = ' '
        item.mStar = html.xpath('//div[@class="vodinfobox"]/ul//li[3]//span')[0].text + ' '
        # item.mStar = ' '
        item.mType = html.xpath('//div[@class="vodinfobox"]/ul//li[4]//span')[0].text
        item.mArea = html.xpath('//div[@class="vodinfobox"]/ul//li[5]//span')[0].text + ' '
        item.mYear = html.xpath('//div[@class="vodinfobox"]/ul//li[7]//span')[0].text
        item.mCover = html.xpath('//img[@class="lazy"]/@src')[0]
        item.mSumary = html.xpath('//*[@class="vodplayinfo"][1]//text()')[0][:200] + '...'
        # item.mSumary = ' '
        item.mPlayUrl_mp4 = html.xpath('//*[@class="vodplayinfo"][last()]//ul[1]/li/input/@value')[0]
        item.mPlayUrl_m3u8 = html.xpath('//*[@class="vodplayinfo"][last()]//ul[2]/li/input/@value')[0]
        # print(">>> 已成功爬取电影：" + item.mName + "(" + item.mId + ")")
        return item

    def getMovieInfoItems(self, movieUrls):
        '''获取所有影片详情信息'''
        items = []
        for i, infourl in enumerate(movieUrls):
            try:
                item = self.getMovieDetail(infourl)
                # t = threading.Thread(target=self.getMovieDetail, args=(infourl,))
                # t.start()
                # t.join()
                items.append(item)
                print(">>> 已成功爬取电影：" + str(i+1) + '.' + item.mName + "(" + item.mId + ")")
            except Exception as e:
                continue
            # if i>5:
            #     break
        return items

    def save2mysql(self, items):
        '''把爬取结果写入数据库'''
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='okmovie3',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `movie` (`mId`, `mName`, `mCover`, `mScore`,`mDirector`,`mStar`,`mType`,`mArea`,`mYear`,`mSumary`,`mPlayUrl_m3u8`,`mPlayUrl_mp4`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                for item in items:
                    try:
                        mId = item.mId
                        mName = item.mName.encode('utf-8')
                        mCover = item.mCover.encode('utf-8')
                        mScore = item.mScore
                        mDirector = item.mDirector.encode('utf-8')
                        mStar = item.mStar.encode('utf-8')
                        mType = item.mType.encode('utf-8')
                        mArea = item.mArea.encode('utf-8')
                        mYear = item.mYear.encode('utf-8')
                        mSumary = item.mSumary.encode('utf-8')
                        mPlayUrl_mp4 = item.mPlayUrl_mp4.encode('utf-8')
                        mPlayUrl_m3u8 = item.mPlayUrl_m3u8.encode('utf-8')
                        cursor.execute(sql, (mId, mName,mCover,mScore,mDirector,mStar,mType,mArea,mYear,mSumary,mPlayUrl_mp4,mPlayUrl_m3u8))
                    except Exception as e:
                        print('写入失败：'+mName)
                        continue

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print('>>>Finish. 写入数据库完成！')
        finally:
            connection.close()

    def getSourceCode(self, url):
        '''获取网页状态码'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        try:
            html = etree.HTML(requests.get(url, headers=headers, timeout=2).text.encode(
                'ISO-8859-1', "ignore").decode('utf-8', "ignore"))
        except Exception as e:
            return None
        else:
            return html

# Arg1: 指定爬取的页数
# Arg2: 指定爬取影片类型
# [电影，连续剧，综艺，动漫，伦理片，美女热舞写真，VIP视频秀，纪录片，街拍美女]
Spider = zySpider(2, '电影')
