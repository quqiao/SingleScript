#!/usr/bin/env python
# coding=utf-8


from time import sleep, strftime,time
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        '''渠道login'''
        # self.click_images(driver,"login_01@auto.png",way_name='channel')
        # sleep(2)
        # self.click_exists(driver,"login_01@auto.png",way_name='channel')
        # sleep(2)
        # self.click_exists(driver,"login_01@auto.png",way_name='channel')
        # sleep(2)
        sleep(3)
        driver.click(50,50)  # 关闭按钮
        sleep(2)
        driver(index=3,className="android.widget.EditText").click()  # 点击输入框
        driver.clear_text() 
        driver.type('test%s'%time(),next=True)
        driver(index=1,className="android.widget.Button").click()
        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):   
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def fubiao(self, driver):
        sleep(2)
        driver.click(55,800)
        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def exitGame(self,driver):
        log.info('该渠道没有退出游戏功能')
        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None