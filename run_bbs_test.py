#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, sys, unittest
from HTMLTestRunner import HTMLTestRunner
sys.path.append("./test_case")
sys.path.append("./models")
from models.function import send_email, find_new_file

test_dir = './test_case/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file_name = './report/html_report/' + now + ' result.html'
    fn = open(file_name, 'wb')
    runner = HTMLTestRunner(stream=fn, title='小米bbs论坛自动化测试报告', description='环境：windows7 浏览器：Chrome')
    runner.run(discover)
    fn.close()
    fnf = find_new_file('./report/html_report/')
    send_email(fnf)