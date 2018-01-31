#!/usr/bin/env python
# coding=utf-8
#快手渠道用例
from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self,driver):
        if self.images_or_none(driver, 'login_logo@auto.png', way_name='channel'):
            self.click_images(driver,'login_sureLogin@auto.png',way_name='channel')
        if self.wait_gone_images(driver, 'login_logo@auto.png', way_name='channel'):
            log.info('登录成功')
            return 'ok'
        else:
            log.info('登录失败')
            return None