#!/usr/bin/env python
# coding=utf-8



from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        if self.images_or_none(driver,"login_01@auto.png",way_name='channel'):
            sleep(1)
            driver.click(1314,830)  # 切换登录
            sleep(1)
            driver.click(685,825)  # 确认登录
            log.info('授权登录')
        else:
            log.info('自动登录')
        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None

    def exitGame(self,driver):
        log.info('该渠道没有退出游戏')
        if self.wait_gone_images(driver, 'login_01@auto.png',way_name='channel'):
            log.info('退出游戏成功')
            return 'ok'
        else:
            return None