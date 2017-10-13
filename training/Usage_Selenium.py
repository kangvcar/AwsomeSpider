#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-24 22:04:33
# @Author  : kangvcar (kangvcar@126.com)
# @Link    : http://www.github.com/kangvcar/
# @Version : $Id$

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


## 模拟提交提交搜索的功能，首先等页面加载完成，然后输入到搜索框文本，点击提交
# driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")

# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print driver.page_source


# print '========================================================='

# ## 测试用例
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # 测试用例是继承了 unittest.TestCase 类，继承这个类表明这是一个测试类。
# class PythonOrgSearch(unittest.TestCase):
# 	"""docstring for PythonOrgSearch"""
# 	# setUp方法是初始化的方法，这个方法会在每个测试类中自动调用。
# 	def setUp(self):
# 		self.driver = webdriver.Firefox()

# 	# 每一个测试方法命名都有规范，必须以 test 开头，会自动执行。
# 	def test_search_in_python_org(self):
# 		driver = self.driver
# 		driver.get("http://www.python.org")
# 		self.assertIn("Python", driver.title)
# 		elem = driver.find_element_by_name("q")
# 		elem.send_keys("pycon")
# 		elem.send_keys(Keys.RETURN)
# 		assert "No results found." not in driver.page_source

# 	# tearDown 方法会在每一个测试方法结束之后调用。
# 	#  close 方法相当于关闭了这个 TAB 选项卡，然而 quit 是退出了整个浏览器。
# 	def tearDown(self):
# 		self.driver.quit()

# if __name__ == '__main__':
# 	unittest.main()


# print '========================================================='

## 页面操作
# <input type="text" name="passwd" id="passwd-id" />
# 我们可以这样获取它
# element = driver.find_element_by_id("passwd-id")
# element = driver.find_element_by_name("passwd")
# element = driver.find_elements_by_tag_name("input")
# element = driver.find_element_by_xpath("//input[@id='passwd-id']")
# 获取了元素之后，下一步当然就是向文本输入内容了，可以利用下面的方法
# element.send_keys("some text")
# 同样你还可以利用 Keys 这个类来模拟点击某个按键。
# element.send_keys("and some", Keys.ARROW_DOWN)
# 用下面的方法来清除输入文本的内容。
# element.clear()

# print '========================================================='

## 填充表单
# 首先获取了第一个 select 元素，也就是下拉选项卡。然后轮流设置了 select 选项卡中的每一个 option 选项。
# 你可以看到，这并不是一个非常有效的方法。
# element = driver.find_element_by_xpath("//select[@name='name']")
# all_options = element.find_element_by_tag_name("options")
# for option in all_options:
# 	print "Value is: %s" % option.get_attribute("value")
# 	option.click()

# 其实 WebDriver 中提供了一个叫 Select 的方法，可以帮助我们完成这些事情。
# from selenium.webdriver.support.ui import Select
# select = Select(driver.find_element_by_name('name'))	#获取指定name的slelct
# select.select_by_index(index)	#根据索引来选择
# select.select_by_visible_text("text")	#根据文字来选择
# select.select_by_value(value)	#根据值来选择

# 取消全部选择怎么办呢？很简单
# select = Select(driver.find_element_by_id('id'))	#获取指定id的slelct
# select.deselect_all()		#取消全部选择

# 获取所有的已选选项
# select = Select(driver.find_element_by_xpath("xpath"))	#用xpath匹配select
# all_selected_options = select.all_selected_options	#.all_selected_options方法获取所有已选选项

# 获取所有可选选项
# options = select.options

# 如果你把表单都填好了，最后肯定要提交表单对吧
# driver.find_element_by_id("submit").click()

# print '========================================================='


##元素拖拽
# 要完成元素的拖拽，首先你需要指定被拖动的元素和拖动目标元素，然后利用 ActionChains 类来实现。
# source = driver.find_element_by_name("source")
# target = driver.find_element_by_name("target")
# from selenium.webdriver import ActionChains
# action_chains = ActionChains(driver)
# action_chains.drag_adn_drop(source, target).perform()

# print '========================================================='

## 页面切换
# 一个浏览器肯定会有很多窗口，所以我们肯定要有方法来实现窗口的切换。切换窗口的方法如下
#driver.switch_to_window("windowName")
# 另外你可以使用 window_handles 方法来获取每个窗口的操作对象。例如
#for handle in driver.window_handles:
#	driver.switch_to_window(handle)
# 另外切换 frame 的方法如下,这样焦点会切换到一个 name 为 child 的 frame 上。
#driver.switch_to_frame("frameName.0.child")

# print '========================================================='


## 弹窗处理
## 获取弹窗对象
# alert = driver.switch_to_alert()

# print '========================================================='

## 历史记录
# 操作页面的前进和后退功能
# driver.forward()
# driver.back()

# print '========================================================='

## Cookies处理
# 为页面添加 Cookies，用法如下
# Go to the correct domain
# driver.get("http://www.example.com")
# Now set the cookie. This one's valid for the entire domain
# cookie = {'name':'foo', 'value':'bar'}
# driver.add_cookie(cookie)

# 获取页面 Cookies，用法如下
# Go to the correct domain
# driver.get("http://www.example.com")
# Add now output all the available cookie for the currect URL
# driver.get_cookies()

# print '========================================================='

## 元素选取
# #单个元素选取							#多个元素选取
# find_element_by_id
# find_element_by_name 					find_elements_by_name
# find_element_by_xpath 				find_elements_by_xpath
# find_element_by_link_text 			find_elements_by_link_text
# find_element_by_partial_link_text 	find_elements_by_partial_link_text
# find_element_by_tag_name 				find_elements_by_tag_name
# find_element_by_class_name			find_elements_by_tag_name
# find_element_by_css_selector 			find_elements_by_css_selector

#另外还可以利用 By 类来确定哪种选择方式
# from selenium.webdriver.common.by import By
# driver.find_element(By.XPATH, '//button[text()="Some text"]')
# driver.find_elements(By.ID, 'dddd')
## By 类的一些属性如下
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

# print '========================================================='

## 页面等待
# Selenium 提供了两种等待方式，一种是隐式等待，一种是显式等待
# 显式等待(显式等待指定某个条件，然后设置最长等待时间。如果在这个时间还没有找到元素，那么便会抛出异常了。)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriver
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox()
# driver.get("http://somedomain/url_that_delays_loading")
# try:
# 	element = WebDriverWait(driver, 10).until(
# 		EC.presence_of_element_located((By.ID, "someid"))
# 	)
# finally:
# 	driver.quit()
## 下面是一些内置的等待条件，你可以直接调用这些条件，而不用自己写某些等待条件了。
# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable – it is Displayed and Enabled.
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present


# 隐式等待(隐式等待比较简单，就是简单地设置一个等待时间，单位为秒)
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver = implicitly_wait(10)
# driver.get("http://somedomain/url_that_delays_loading")
# myDynamicElement = driver.find_element_by_id("myDynamicElement")












