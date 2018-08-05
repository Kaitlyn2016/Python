#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Page(object):
    '''
    页面基础类，用于所有页面的继承
    '''
    '''
    通过__init__()方法初始化参数：浏览器驱动，URL地址，超时时长等。
    定义基本方法：open()打开BBS地址；find_element()和find_elements()分别用来定位单个和多个元素；创建script()方法可以更简便的调用Javascript代码。
    当然我们还可以对更多的webdriver方法进行重定义
    '''
    bbs_url = 'http://bbs.xiaomi.cn'
    url = '/'

    def __init__(self, selenium_driver, base_url=bbs_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent


    def _open(self, url):
        self.url = self.base_url + url
        self.driver.get(self.url)

    def open(self):
        self._open(self.url)

    def close(self):
        return self.driver.close()

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def get_title(self):
        return self.driver.title

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, new_handle):
        return self.driver.switch_to.window(new_handle)

    def scrpt(self, src):
        return self.driver.excute_script(src)
