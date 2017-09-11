#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-06 21:42:30
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : www.github.com/kangvcar
# @Version : $Id$

import os
import random   #导入随机数模块
namedict = {}   #定义namedict字典，用于存储用户和对应的猜对次数
a = 0           #初始化变量a
go = 1          #初始化变量go
while go == 1:  #判断是否继续玩
        name = raw_input("please input your name:")     #读取并赋值玩家名name
        if not (name in namedict):              #判断玩家是否在字典namedict内
                namedict[name] = 0              #不在则赋值初始值0
        suiji = random.randint(1,100)           #生成随机数并赋值suiji
        #print suiji                            #用于测试，打印随机数
        for i in range(4):                      #循环4次
                num = int(raw_input("your number is:")) #读取并赋值用户输入的数字num
                if num == suiji:        #判断num 是否等于 suiji
                        print("you win!")
                        a = 1           #赋值a,使得循环外的判断不成立
                        if name in namedict:    #判断玩家是否在字典namedict内
                        	namedict[name] = namedict[name] + 1    #如果猜对了就加1
                                break   #结束并跳出循环
                elif num > suiji:
                        print("too big")
                else:
                        print("too small")
        #namedict[name] = a
        if a == 0:              #判断我那家是否猜对了
                print 'game over'
        print "go on? Yes=1  No=0"
        go = int(raw_input("please input you choice(1/0):"))    #读取并赋值给go，用于判断是否继续
print '---------------'
print '-----score-----'
print '---------------'
for key in namedict:    #迭代循环字典
        print key,'====>',namedict[key]






