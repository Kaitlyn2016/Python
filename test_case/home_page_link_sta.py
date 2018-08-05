#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, random, sys, time
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.base import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class HomePageLink(myunit.MyTest):
    """社区首页链接测试"""

    def test_recommended_topics(self):
        """主页所有推荐话题超链接”"""
        pg = Page(self.driver)
        pg.open()
        links_loc = (By.XPATH, "//div[@class='title']/a ")
        links = pg.find_elements(*links_loc)
        print("首页一共有%s个链接" % len(links))
        for i in range(len(links)):
            home_page_handle = pg.get_current_window_handle()
            link_title1 = links[i].text
            print( link_title1)
            links[i].click()
            time.sleep(1)
            all_handles = pg.get_window_handles()
            pg.switch_to_window(all_handles[1])
            time.sleep(1)
            link_title2 = pg.get_title()
            print(link_title2)
            try:
                self.assertIn( link_title1, link_title2)
                print("It's right ! ")
            except Exception as e:
                print("Failed !")
            pg.close()
            pg.switch_to_window(all_handles[0])
            time.sleep(1)

        def test_recommended_topics(self):
            """主页所有推荐话题超链接”"""
            pg = Page(self.driver)
            pg.open()
            links_loc = (By.XPATH, "//div[@class='title']/a ")
            links = pg.find_elements(*links_loc)
            print("首页一共有%s个链接" % len(links))
            for i in range(len(links)):
                home_page_handle = pg.get_current_window_handle()
                link_title1 = links[i].text
                print(link_title1)
                links[i].click()
                time.sleep(1)
                all_handles = pg.get_window_handles()
                pg.switch_to_window(all_handles[1])
                time.sleep(1)
                link_title2 = pg.get_title()
                print(link_title2)
                try:
                    self.assertIn(link_title1, link_title2)
                    print("It's right ! ")
                except Exception as e:
                    print("Failed !")
                pg.close()
                pg.switch_to_window(all_handles[0])
                time.sleep(1)

if __name__ == '__main__':
    unittest.main()

