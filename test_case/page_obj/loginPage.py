#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class login(Page):
    """
    用户登录页面
    """
    url = '/'

    # Action
    bbs_login_button_loc = (By.XPATH, "//*[@id='login']/a[1]")

    def bbs_login(self):
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.ID, "username")
    login_password_loc = (By.ID, "pwd")
    login_button_loc = (By.ID, "login-button")

    #  登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #  登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #  定义统一登录入口
    def user_login(self, username='username', password='password'):
        """获取的用户名密码登录"""
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    login_error_hint_loc = (By.XPATH, "//*[@id='login-main-form']/div/div[4]/div/span")
    login_blank_hint_loc = (By.XPATH, "//*[@id='login-main-form']/div/div[4]/div/span")

    #  用户名密码错误提示文字内容
    def login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text

    #  用户名密码为空时提示文字内容
    def login_blank_hint(self):
        return self.find_element(*self.login_blank_hint_loc).text



