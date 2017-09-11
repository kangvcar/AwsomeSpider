#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-06 21:42:30
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : www.github.com/kangvcar
# @Version : $Id$

import os
import random
namedict = {}
a = 0
go = 1
while go == 1:
        name = raw_input("please input your name:")
        if not (name in namedict):
                namedict[name] = 0
        suiji = random.randint(1,100)
        print suiji
        for i in range(4):
                num = int(raw_input("your number is:"))
                if num == suiji:
                        print("you win!")
                        a = 1
                        if name in namedict:
                        	namedict[name] = namedict[name] + 1
                                break
                elif num > suiji:
                        print("too big")
                else:
                        print("too small")
        #namedict[name] = a
        if a == 0:
                print 'game over'
        print "go on? Yes=1  No=0"
        go = int(raw_input("please input you choice(1/0):"))
print '---------------'
print '-----score-----'
print '---------------'
for key in namedict:
        print key,'====>',namedict[key]






