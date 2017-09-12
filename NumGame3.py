#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 09:39:06
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import os
import random

namedict = {}   #定义namedict字典，用于存储用户和对应的猜对次数
names = []
a = 0           #初始化变量a
pkNum = 1          #初始化变量go

def inputName(namestr):
	for i in namestr.split(','):
		namedict[i] = 0


while pkNum > 0:  #判断是否继续玩
	print '请主持人确定猜数字的范围和pk次数'
	sNum = int(raw_input('请主持人确定猜数字的范围最小值:'))
	bNum = int(raw_input('请主持人确定猜数字的范围最大值:'))
	pkNum = int(raw_input('请主持人确定PK次数:'))
	suiji = random.randint(sNum,bNum)           #生成随机数并赋值suiji
	namestring = raw_input('请每位参赛者按顺序输入自己的名字(用逗号,分割):')
	inputName(namestring)
	kcNum = int(raw_input('请主持人确定每次可以猜的次数(默认4次):'))
    for x in range(kcNum):
    	for j in namedict:
    		print j		#打印玩家名
            num = int(raw_input("your number is:")) #读取并赋值用户输入的数字num
            if num == suiji:        #判断num 是否等于 suiji
                print("you win!")
                a = 1           #赋值a,使得循环外的判断不成立
                if j in namedict:    #判断玩家是否在字典namedict内
                	namedict[j] = namedict[j] + 1    #如果猜对了就加1
                    break   #结束并跳出循环
            elif num > suiji:
                print("too big")
            else:
                print("too small")
    if a == 0:              #判断玩家是否猜对了
        print 'game over'                
		print 'result Number is:',suiji
    pkNum = pkNum - 1
        
print '---------------'
print '-----score-----'
print '---------------'
for key in namedict:    #迭代循环字典
        print key,'====>',namedict[key]
