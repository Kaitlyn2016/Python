#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#  截图函数
def screen_shot(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 这样写是为了让项目具有可移植性
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split("/test_case")[0]
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)

#  定义发送邮件函数
def send_email(file_new):
    fn = open(file_new, "rb")  # file_new是查找到的最新的测试报告的路径
    mail_body = fn.read()
    fn.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')  # MIMRText是python中一个支持html格式邮件的类，msg是MIMEText的一个实例化对象
    msg['Subject'] = Header('自动化测试报告', 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("gaowanru2016@126.com", "gao3901012")
    smtp.sendmail("gaowanru2016@126.com", "892342269@qq.com", msg.as_string())
    smtp.quit()
    print(" 邮件已成功发送！ ")


#  查找测试报告目录，找到最新的测试报告
def find_new_file(html_report):  # html_report是存放测试报告的目录路径
    lists = os.listdir(html_report)
    lists.sort(key=lambda fn: os.path.getmtime(html_report+'\\'+fn))
    file_new = os.path.join(html_report, lists[-1])
    return file_new


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    screen_shot(driver, "baidu.png")
    driver.quit()