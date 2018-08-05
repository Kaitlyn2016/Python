#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login


class LoginTest(myunit.MyTest):
    """社区登录测试"""

    def test_login1(self):
        """用户名、密码为空"""
        po = login(self.driver)
        po.user_login(username="", password="")
        self.assertEqual(po.login_blank_hint(), u"请输入帐号")
        function.screen_shot(self.driver, "user_pawd_empty.png")

    def test_login2(self):
        """用户名、密码错误"""
        character = random.choice('abcdefghijklmnopqrstuvweyz')
        username = "zhangsan"+character
        password = "123456"
        po = login(self.driver)
        po.user_login(username=username, password=password)
        self.assertEqual(po.login_error_hint(), u"用户名不正确")
        function.screen_shot(self.driver, "user_pawd_error.png")

    def test_login3(self):
        """用户名、密码正确"""
        username = "18610974468"
        password = "gwr892342269"
        po = login(self.driver)
        po.user_login(username=username, password=password)
        assert u"小米社区" in self.driver.page_source, u"页面源码中不存在该关键字！"
        function.screen_shot(self.driver, "user_pawd_correct.png")


if __name__ == '__main__':
    unittest.main()

