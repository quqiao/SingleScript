# coding=utf-8
#美图渠道SDK测试用例
from time import sleep, strftime
import public.methods as public
from public import logutils

log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        u'''渠道login'''
        if self.images_or_none(driver,'login_logo.1920x1080.png', way_name='channel'):
            self.click_images(driver, 'fastLogin.1920x1080.png', way_name='channel')
            if self.wait_gone_images(driver, 'login_logo.1920x1080.png', way_name='channel'):
                log.info('快速登录成功')
                return 'ok'
            else:
                log.info('快速登录失败')
                return None

    # def exitGame(self, driver):
    #     if self.images_or_none(driver, 'ucSDK_exitGame.1920x1080.png', way_name='channel'):
    #         self.click_images(driver, "ucSDK_exitGame.1920x1080.png", way_name='channel')
    #     if self.wait_gone_images(driver, 'ucSDK_exitGame.1920x1080.png', way_name='channel'):
    #         log.info('退出游戏成功')
    #         return 'ok'
    #     else:
    #         return None
