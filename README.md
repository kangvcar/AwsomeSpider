#pyproject

> 2017 python爬虫学习

## NumGame Folders
### -NumGame1.py
简单的猜数字的大小

### -NumGame2.py
多玩家猜数字游戏

### -NumGame5.py
游戏规则如下：<br>
主持人确定猜数字的范围和pk次数<br>
每位参赛者按顺序输入自己的名字<br>
主持人确定每次可以猜的次数（默认4次）<br>
开始比赛-每位参赛者按顺序猜一次，如果猜对加一分<br>
如果在规定次数大家都没有猜出来，打印出答案<br>
比赛结束后打印排行榜<br>

### -object.py
面向对象编程练习

### -Youdao-reptile.py
使用 urllib2 爬取有道翻译的源代码并写入Youdao.txt文件

## project Folders
> Scrapy 爬虫框架目录结构
```
project/
    scrapy.cfg 			#项目的配置文件
    project/ 			#该项目的python模块,之后您将在此加入代码
        __init__.py 	
        items.py 		#项目中的item文件
        pipelines.py 	#项目中的pipelines文件
        settings.py 	#项目的设置文件
        spiders/ 		#放置spider代码的目录
            __init__.py
            ...
```
### -project/spiders/suzhouSpider.py
爬取www.suzhou.tianqi.com 页面的六天天气,并写入result.txt文件

## Spiders Folders
> python 爬虫项目
### - Spiders/Spider_jisilu.py
使用 selenium 爬取www.jisilu.com 页面的部分数据并写入文件
### - Spiders/Spider_qiushibaike.py
爬取 www.qiushibaike.com 页面的段子，并实现回车查看段子，按Q退出
### - Spiders/Spider_SZtianqi.py
使用 BeautifulSoup 爬取 www.suzhou.tianqi.com 页面的数据，并用BeautifulSoup过滤

## training Folders
> 各爬虫工具模块的快速入门学习, 实例验证
### - training/Usage_BeautifulSoup.py
BeautifulSoup 快速入门，实例学习
### - training/Usage_BeautifulSoup_CSS_Select.py
CSS_Select => CSS选择器 快速入门，实例学习
### - training/Usage_BeautifulSoup_find_.py
BeautifulSoup 的 find_all 等函数 快速入门，实例学习
### - training/Usage_PyQuery.py
PyQuery 快速入门，实例学习
### - training/Usage_Requests.py
Requests 快速入门，实例学习
### - training/Usage_Selenium.py
Selenium 快速入门，实例学习
### - training/Usage_Urllib2.py
Urllib2 快速入门，实例学习
### - training/Usage_XPath.py
XPath 快速入门，实例学习

### Usage_pdb.txt
Pdb: The Python Debugger </br>
Python调试器 使用方法快速入门