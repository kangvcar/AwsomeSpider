#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-11 18:33:44
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : www.github.com/kangvcar
# @Version : $Id$

import random
import pdb

suiji = random.randint(1,10)
print '1111'
pdb.set_trace()
num = int(raw_input('请输入你猜的数字:'))
if num == suiji:
	print '恭喜你！猜对了！！！'
elif num > suiji:
	print '太大了'
else:
	print '太小了'

print 'the first homeworks'
