#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 15:44:23
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

for i in xrange(10):
	for j in xrange(1, i+1):
		print j, '*', i, '=', i*j, '\t',
	print '\n'
#
print '========================================================='
#
for i in xrange(10):
	for j in xrange(1, 10-i):
		print j, '*', 9-i, '=', (9-i)*j, '\t',
	print '\n'
