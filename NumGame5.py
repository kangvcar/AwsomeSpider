#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-12 09:39:06
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

import random

namedict = {}
names = []
a = 0
kcNum = 1
lun = 1

def inputName(namestr):
    for i in namestr.split(','):
        namedict[i] = 0



pkNum = int(raw_input('请主持人确定PK次数:'))
sNum = int(raw_input('请主持人确定猜数字的范围最小值:'))
bNum = int(raw_input('请主持人确定猜数字的范围最大值:'))
kcNum = int(raw_input('请主持人确定每次可以猜的次数(默认4次):'))
namestring = raw_input('请每位参赛者按顺序输入自己的名字(用逗号,分割):')
inputName(namestring)

while pkNum > 0:

    suiji = random.randint(sNum, bNum)
    print '===第', lun, '轮==='
    for x in range(kcNum):
        print '===第', lun, '轮==>第', x + 1, '次'
        for j in namedict:
            print j, '玩家:'
            num = int(raw_input('your number is:'))
            if num == suiji:
                print 'you win!'
                a = 1
                namedict[j] = namedict[j] + 1
                suiji = random.randint(sNum, bNum)
                break
            elif num > suiji:
                print 'too big'
            else:
                print 'too small'
        if a == 0:
            print 'game over'
            print 'result number is:', suiji
            suiji = random.randint(sNum, bNum)
    pkNum = pkNum - 1
    if pkNum > 0:
        lun = lun + 1

print '-----------'
print '---score---'
print '-----------'
for key in namedict:
    print key,'猜对了',namedict[key],'次'