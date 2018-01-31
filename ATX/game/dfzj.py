#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)


class Game(public.Methods):
    def game_update(self,driver):
        sleep(5)
        driver.click(500,500)
        sleep(20)
        if self.wait_gone_images(driver,'guide_001@auto.png'):
            log.info('游戏更新成功')
            return 'ok'
        else:
            log.info('游戏更新失败')
            return None
        
    def game_pre(self,driver):
        self.click_images(driver,"game_pre_01@auto.png")
        self.click_images(driver,"game_pre_02@auto.png")
        if self.wait_gone_images(driver,'game_pre_02@auto.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def guide(self,driver):
        if self.images_or_none(driver,'guide_exist_01@auto.png'):
            '''创建战舰'''
            self.click_images(driver,"guide_001@auto.png")
            self.click_images(driver,"guide_002@auto.png")
            self.images_or_none(driver,"guide_exist_01@auto.png")#等待对话
            for i in range(15):
                driver.click(500,500)
                sleep(1)
            '''引导教学'''
            sleep(2)
            driver.swipe(310,863,310,750,steps=500) #前进
            sleep(6)
            self.images_or_none(driver,"guide_exist_01@auto.png")#等待对话
            for i in range(6):
                driver.click(500,500)
                sleep(1)
            sleep(2)
            '''向左转'''
            driver.swipe(1352,533,612,533,steps=100)#向左滑动
            self.images_or_none(driver,"guide_exist_01@auto.png")#等待对话
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(2)
            for i in range(2):
                driver.click(1761,930)#舰载火炮
                sleep(1)
            sleep(2)
            for i in range(3):
                driver.click(500,500)
                sleep(1)
            '''向右转'''
            sleep(2)
            driver.swipe(469,826,469,826,steps=1000)#向右转
            self.images_or_none(driver,"guide_exist_01@auto.png")#等待对话
            sleep(2)
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(2)
            driver.click(1800,496)#望眼镜
            sleep(3)
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(1)
            for i in range(6):
                driver.click(1761,930)#舰载火炮
                sleep(1)
            sleep(2)
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(2)
            driver.click(1800,496)#望眼镜
            sleep(2)
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(2)
            driver.click(1530,980)#舰载鱼雷
            sleep(2)
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(2)
            driver.click(1530,980)#舰载鱼雷
            sleep(8)
            for i in range(3):
                driver.click(500,500)
                sleep(1)
            '''向右转'''
            driver.swipe(639,530,1430,530,steps=100)#向右转
            sleep(2)
            for i in range(3):
                driver.click(500,500)
                sleep(1)
            sleep(1)
            for i in range(20):
                self.click_exists(driver,"guide_003@auto.png")
                sleep(1)
                if self.exist(driver,"guide_exist_01@auto.png"):
                    break
            sleep(1)
            for i in range(3):
                driver.click(500,500)
                sleep(1)
            '''引导完第一次战斗'''
            self.images_or_none(driver,"guide_exist_01@auto.png")#等待对话
            for i in range(15):
                driver.click(1800,975)
                sleep(1)
            sleep(10)
            for i in range(1000):
                self.click_exists(driver,"guide_003@auto.png")
                sleep(1)
                if self.exist(driver,"guide_exist_02@auto.png"):#等待战斗胜利
                    break        
            self.click_images(driver,"guide_exist_02@auto.png")
            '''武器强化'''
            sleep(2)
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(2)
            driver.click(774,102)#点击强化
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(3)
            driver.click(385,970)#武器图示
            sleep(3)
            driver.click(1685,720)#替换
            sleep(3)
            driver.click(1800,405)#替换2
            sleep(3)
            driver.click(39,40)#返回
            sleep(3)
            driver.click(1820,720)#升级
            sleep(3)
            driver.click(39,40)#返回
            sleep(3)
            driver.click(1788,975)#开始战斗
            '''战斗'''
            sleep(5)
            self.images_or_none(driver,"guide_exist_01@auto.png")#等待对话
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            for i in range(1000):
                self.click_exists(driver,"guide_003@auto.png")
                if self.exist(driver,"guide_exist_02@auto.png"):#等待战斗胜利
                    break
            sleep(2)
            driver.click(1850,22)#战斗结束后关闭
            '''任务'''
            for i in range(4):
                driver.click(500,500)
                sleep(1)
            sleep(3)
            driver.click(152,756)#任务
            sleep(3)
            driver.click(946,116)#成就任务
            sleep(3)
            driver.click(1763,272)#领取
            sleep(3)
            driver.click(39,40)#返回
            sleep(1)
            for i in range(3):
                driver.click(500,500)
                sleep(1)
            '''研发'''
            sleep(3)
            driver.click(610,100)#研发
            sleep(3)
            driver.click(80,1010)#舰种介绍
            sleep(1)
            for i in range(6):
                driver.click(500,500)
                sleep(2)
            sleep(3)
            driver.click(1835,138)#关闭
            sleep(3)
            driver.click(852,355)#可研发
            sleep(5)
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(3)
            driver.click(1238,175)#舰体
            for i in range(3):
                sleep(3)
                driver.click(1732,984)#研发
                sleep(3)
                driver.click(1610,455)#切换
            sleep(3)
            driver.click(1732,984)#研发
            sleep(3)
            driver.click(39,40)#返回
            sleep(3)
            driver.click(1820,856)#研发
            sleep(2)
            for i in range(2):
                driver.click(500,500)
                sleep(1)
            sleep(3)
            driver.click(39,40)#返回
            sleep(3)
            driver.click(39,40)#返回
            sleep(3)
            driver.click(566,970)#古鹰
        else:
            print "引导已完成"  
        if self.wait_gone_images(driver,'guide_022@auto.png'):
            log.info('引导成功')
            return 'ok'
        else:
            log.info('引导失败')
            return None
        
    def game_pay_pre(self,driver):
        self.click_images(driver,"game_pay_01@auto.png")
        if self.wait_gone_images(driver,'game_pay_01@auto.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def game_pay1(self,driver):
        self.click_images(driver,"game_pay_02@auto.png")
        if self.wait_gone_images(driver,'game_pay_02@auto.png'):
            log.info('进入游戏前准备成功')
            return 'ok'
        else:
            log.info('进入游戏前准备失败')
            return None
        
    def basicFunction(self,driver):
        self.click_images(driver,"BasicFunction_01@auto.png")
        self.click_images(driver,"BasicFunction_02@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_04@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_05@auto.png")
        self.click_images(driver,"BasicFunction_06@auto.png")
        self.click_images(driver,"BasicFunction_07@auto.png")
        self.click_images(driver,"BasicFunction_06@auto.png")
        self.click_images(driver,"BasicFunction_08@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_09@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_10@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_11@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_12@auto.png")
        self.click_images(driver,"BasicFunction_06@auto.png")
        self.click_images(driver,"BasicFunction_13@auto.png")
        self.click_images(driver,"BasicFunction_06@auto.png")
        self.click_images(driver,"BasicFunction_14@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_15@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_16@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_17@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_18@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        self.click_images(driver,"BasicFunction_19@auto.png")
        self.click_images(driver,"BasicFunction_03@auto.png")
        if self.wait_gone_images(driver, 'BasicFunction_03@auto.png'):
            return 'ok'
        else:
            return None

    '''战舰俱乐部'''   
    def live(self,driver):
        self.click_images(driver,"live_01@auto.png")
        self.click_images(driver,"live_02@auto.png")
        if self.wait_gone_images(driver, 'live_02@auto.png'):
            return 'ok'
        else:
            return None
    
    '''战舰社区'''   
    def gonglue(self,driver):
        self.click_images(driver,"gonglue_01@auto.png")
        self.click_images(driver,"gonglue_02@auto.png")
        self.click_images(driver,"gonglue_03@auto.png")
        self.click_images(driver,"gonglue_04@auto.png")
        self.click_images(driver,"gonglue_05@auto.png")
        if self.wait_gone_images(driver, 'gonglue_01@auto.png'):
            return 'ok'
        else:
            return None
        
    
    '''战舰赛事'''    
    def saishi(self,driver):
        self.click_images(driver,"saishi_01@auto.png")
        sleep(5)
        #driver(className="android.view.View",index=0).child(className="android.view.View",index=0).click() 
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=1).click() 
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=2).click() 
        #driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=3).click() 
        #driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.kp:id/uc_sdk_webviewtool_close_deufalt").click()
        self.click_images(driver,"saishi_02@auto.png")
        if self.wait_gone_images(driver, 'saishi_02@auto.png'):
            return 'ok'
        else:
            return None
       
    '''战舰邀请'''   
    def lingzuan(self,driver):
        self.click_images(driver,"lingzuan_04@auto.png")
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        #self.click_images(driver,"choujiang@auto.png")
        #self.click_images(driver,"lingzuian_04@auto.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=0).click() 
        #sleep(3)
        #driver(className="android.widget.LinearLayout",resourceId="com.tencent.mm:id/hf").click()
        self.click_images(driver,"lingzuan_02@auto.png")
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        #self.click_images(driver,"choujiang@auto.png")
        #self.click_images(driver,"lingzuian_05@auto.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=1).click() 
        self.click_images(driver,"lingzuan_02@auto.png")
        #sleep(2)
        #driver(className="android.widget.LinearLayout",resourceId="com.tencent.mm:id/hf").click()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        #self.click_images(driver,"choujiang@auto.png")
        #self.click_images(driver,"lingzuian_06@auto.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=2).click() 
        sleep(2)
        driver.press.back()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        self.click_images(driver,"lingzuan_01@auto.png")
        #sleep(2)
        #driver(className="android.widget.GridViewt",index=0).child(className="android.widget.LinearLayout",index=3).click() 
        sleep(3)
        driver.press.back()
        sleep(2)
        driver(className="android.view.View",description='每日成功分享（0/1）').click()
        #self.click_images(driver,"choujiang@auto.png")
        #self.click_images(driver,"lingzuian_07@auto.png")
        sleep(2)
        driver(className="android.widget.GridView",index=0).child(className="android.widget.LinearLayout",index=4).click()  
        sleep(2)
        driver.press.back()
        driver.press.back()
        sleep(1)
        driver(className="android.widget.TextView",text="不保存").click()
        #driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.nearme.gamecenter:id/uc_sdk_webviewtool_close_deufalt").click()
        self.click_images(driver,"lingzuan_03@auto.png")
        #self.click_images(driver,"basic_16@auto.png")
        if self.wait_gone_images(driver, 'lingzuan_03@auto.png'):
            return 'ok'
        else:
            return None
    
    '''战舰商城'''
    def store(self,driver):
        self.click_images(driver,"store_01@auto.png")
        sleep(5)
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=1).click()
        sleep(2)
        driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=2).click()
        #sleep(2)
        #driver(className="android.widget.ListView",index=0).child(className="android.view.View",index=3).click() 
        #sleep(2)
        #driver(className="android.widget.ImageView", resourceId="com.crisisfire.android.nearme.gamecenter:id/uc_sdk_webviewtool_close_deufalt").click()
        self.click_images(driver,"store_02@auto.png")
        if self.wait_gone_images(driver, 'store_02@auto.png'):
            return 'ok'
        else:
            return None
        
    def talking(self,driver):
        self.click_images(driver,"talking_01@auto.png")
        self.click_images(driver,"talking_02@auto.png")
        sleep(1)
        driver(className='android.widget.EditText',index=0).click()
        driver.type(u"毛泽东法轮功江泽民") 
        driver(className='android.widget.Button',index=1).click()
        self.click_images(driver,"talking_03@auto.png")
        self.click_images(driver,"talking_04@auto.png")

        if self.wait_gone_images(driver, 'talking_04@auto.png'):
            return 'ok'
        else:
            return None

    def setting(self,driver):
        self.click_images(driver,"setting_01@auto.png")
        sleep(1)
        driver.click(1170,115)
        if self.wait_gone_images(driver, 'setting_01@auto.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
        
        
    def exitgame(self,driver):
        self.click_images(driver,"exitgame_01@auto.png")
        if self.wait_gone_images(driver, 'exitgame_01@auto.png'):
            log.info('游戏中退出按钮')
            return 'ok'
        else:
            return None
        
        
        
        
        
        
        
        
        
            
        
        
    
        
        
        
            
            
        
