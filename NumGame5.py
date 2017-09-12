#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 09:39:06
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import random   #导入随机数模块

namedict = {}   #定义字典namedict用于存储玩家名和猜对的次数
names = []      #定义列表names用于存储多个玩家名

kcNum = 4
lun = 1

def inputName(namestr):     #切割names列表，并把所有玩家写入namedict字典
    for i in namestr.split(','):
        namedict[i] = 0

def pScore():       #打印排行榜函数
    print '-----------'
    print '---score---'
    print '-----------'
    for key in namedict:
        print key, '猜对了', namedict[key], '次'

pkNum = int(raw_input('请主持人确定PK次数:'))
sNum = int(raw_input('请主持人确定猜数字的范围最小值:'))
bNum = int(raw_input('请主持人确定猜数字的范围最大值:'))
kcNum = int(raw_input('请主持人确定每次可以猜的次数(默认4次):'))
namestring = raw_input('请每位参赛者按顺序输入自己的名字(用逗号,分割):') #读取字符串namestring
inputName(namestring)

while pkNum > 0:    #判断PK次数是否大于0
    suiji = random.randint(sNum, bNum)  #生成随机数
    print '===第', lun, '轮==='
    for x in range(kcNum):  #循环可猜的次数
        print '===第', lun, '轮==>第', x + 1, '次'
        for j in namedict:  #循环显示玩家名
            a = 0
            print j, '玩家:'
            num = int(raw_input('your number is:')) #读取玩家猜的数字
            if num == suiji:
                print 'you win!'
                a = 1
                namedict[j] = namedict[j] + 1   #在namedict字典对应的玩家值加1
                suiji = random.randint(sNum, bNum)  #重新生成随机数
                break   #结束循环
            elif num > suiji:
                print 'too big'
            else:
                print 'too small'
        if a == 0:  #判断是否所有玩家都没有猜对
            print '===>game over<==='
            print '===>result number is:', suiji
            suiji = random.randint(sNum, bNum)  #重新生成随机数
    pkNum = pkNum - 1   #pk次数减1
    if pkNum > 0:
        lun = lun + 1

pScore()    #调用打印排行榜函数