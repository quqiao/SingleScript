#coding=utf-8

import os
from time import sleep,strftime
import re
import configure

def size(self):
    if configure.device_name == '':
        size = 'adb shell wm size'
    else:
        size = 'adb -s %s shell wm size' % configure.device_name
    a =  os.popen(size)
    for i in a:
        pass
    size =i.split(': ')
    size = size[1].split('x')
    size= [int(size[0]),int(size[1])] #size[0] 为width size[1] 为high
    return size
def swipe(self,driver,direction):
    if direction == 'up':
        return self.up_swipe(driver)
    elif direction == 'down':
        return self.down_swipe(driver)
    elif direction =='right':
        return self.right_swipe(driver)
    elif direction == 'left':
        return self.left_swipe(driver)
    else:
        print '没传滑动方向，不做滑动操作，up,down,right,left'
def up_swipe(self,driver):
    size = self.size()
    driver.swipe(size[0] /2, size[1] *0.8, size[0] /2, size[1] *0.2, steps=10)
    sleep(1)
def down_swipe(self,driver):
    size = self.size()
    driver.swipe(size[0] / 2, size[1] * 0.2, size[0] / 2, size[1] * 0.8, steps=10)
    sleep(1)
def right_swipe(self,driver):
    size = self.size()
    driver.swipe(size[0] *0.2, size[1] /2, size[0] *0.8, size[1] /2, steps=10)
    sleep(1)
def left_swipe(self,driver):
    size = self.size()
    driver.swipe(size[0] *0.8, size[1] /2, size[0] *0.2, size[1] /2, steps=10)
    sleep(1)
    
    
    
def get_name(self,name,way_name='game'):
    '''
    通过os.listdir 去获取文件夹所有截图，通过 re.match，获取所需要的截图名称
    :param name: 截图名称的前缀       如 name == 'pay_in'
    :param way_name: 区分游戏截图还是渠道截图
    :return: 返回一个有截图名称的list,如 ['pay_in_01','pay_in_02'......]
    '''
    if way_name == 'game':
        path = './/'+way_name+'/'+configure.game_name+'_images'
    else:
        path = './/' + way_name + '/' + configure.channel_name + '_images'
    a = os.listdir(os.getcwd() + os.sep + path)
    b = []
    name = '%s.*'%name
    for i in a:
        logo = re.match(name, i, re.M | re.I)
        if logo:
            logo=logo.group().split('.')   #截图名称格式一般是这样enter_game_01.1920x1080.png
            b.append(logo[0])             #分割后，获取的是 enter_game_01
    b = list(set(b)) #去重
    b = sorted(b)   #排序
    return b



def guide_exist(self,driver,name):
    '''
    判断目标图片是否存在,该方法主要判断 游戏引导第一个图片
    :param driver:
    :param name: 目标截图前缀
    :return: 目标图存在则返回非空，不存在则返回 None
    '''
    global image
    name = self.get_name(name)
    for x in xrange(10):
        print '第 %s 次寻找: %s' % (x + 1, name[0])
        image = self.images_or_none(driver, name[0] + '@auto.png')
        if image:
            print '引导图片存在，需要过引导: ' ,name[0] ,image
            break
        if x == 9:
            print '引导图片不存在，不需要过剧情: ',name[0],image
    return image

def pic_exist(self,driver,name,way_name):
    '''
    支付操作第三步，判断图片是否存在
    该方法,主要是判断,第三方支付界面的图片
    判断当前界面是相应的第三方支付界面
    :param driver:
    :param name: 目标图片
    :param way_name: 区分游戏和渠道截图的路径
    :return: 图片存在,返回非空，不存在 返回None
    '''
    name = name[0].replace('in_01', 'exist')
    name = self.get_name(name, way_name)
    for i in xrange(5):
        print strftime('%Y-%m-%d-%H-%M-%S') + '第 %s 次寻找: %s' % (i + 1, name[0])
        image = self.images_or_none(driver, name[0] + '@auto.png', way_name)
        if image:
            print(strftime('%Y-%m-%d-%H-%M-%S') + '--查找*******图片 %s 成功---图片信息 %s' % (name[0], image))
            return image
        if i == 4:
            return None
        
        
def game_click(self,driver,name):
    '''
    寻找和点击所有目标图片,如 目标图片是 guide_001 -----guide_100,只需 name 传入 'guide' 就会寻找和点击这些图片
    :param driver:
    :param name: 目标图片的前缀
    :return: 所有图片都找到和点击，返回一个非空，如果某张图片达到循环最大值都没找到，则返回 None
    '''
    name = self.get_name(name)
    for i in name:
        for x in xrange(10):
            print (strftime('%Y-%m-%d-%H-%M-%S')+'第 %s 次寻找: %s' %(x+1,i))
            image = self.images_or_none(driver,i+'@auto.png')
            if image:
                sleep(2)
                driver.click(image[0][0],image[0][1])
                #self.click_images(driver,i+'@auto.png')
                print (strftime('%Y-%m-%d-%H-%M-%S')+'--点击图片 %s 成功---图片信息 %s' %(i,image))
                break
            if x == 9:
                print '无法匹配到图片：', i
                return image
    return 'ok'

def game_pay(self,driver,name):
    '''
    调起渠道支付界面的方法，先判断 activity,如果当前的activity是渠道支付界面的，则不再做操作,
    如果不是，则寻找和点击目标图片,目标图片不存在，则跳过，继续操作下一张图片.
    :param driver:
    :param name: m目标截图名称
    :return: 如果循环，达到最大次数，返回None
    '''
    name = self.get_name(name)
    for x in xrange(10):
        if self.get_view_info(driver) == self.get_channel():
            print unicode('已经进入到支付界面')
            return 'ok'
        else:
            for i in name:
                print (strftime('%Y-%m-%d-%H-%M-%S')+'寻找: %s' % (i))
                image = self.images_or_none(driver, i + '@auto.png')
                if image:
                    sleep(1)
                    driver.click(image[0][0], image[0][1])
                    print(strftime('%Y-%m-%d-%H-%M-%S') + '--点击图片 %s 成功---图片信息 %s' % (i, image))

        if x == 9:
            print unicode('进入支付界面失败')
            return None
        
        
        
        
def pay_in(self,driver,name,way_name='channel',direction=None):
    '''
    支付界面第一步操作,找到相应的支付方式
    :param driver:
    :param name:目标截图名称
    :param way_name: 区分游戏和渠道截图的路径
    :param direction: 如果图片，是否需要滑动操作，如需要则传入 'up' 'down' 'right' 'left',不需要就是None
    :return:
    '''
    name = self.get_name(name, way_name)
    for i in name:
        for x in xrange(5):
            print strftime('%Y-%m-%d-%H-%M-%S') + '第 %s 次寻找: %s' % (x + 1, i)
            image = self.images_or_none(driver, i + '@auto.png', way_name)
            if image:
                driver.click(image[0][0], image[0][1])
                print(strftime('%Y-%m-%d-%H-%M-%S') + '--点击图片 %s 成功---图片信息 %s' % (i, image))
                break
            else:
                self.swipe(driver, direction)

def pay_up(self,driver,way_name):
    '''
    支付界面第二步操作,找到发起支付的按钮，如‘立即支付’ '确认支付'
    :param driver:
    :param way_name: 区分游戏和渠道截图的路径
    :return:
    '''
    name = self.get_name('pay_up', way_name)
    for i in xrange(5):
        print strftime('%Y-%m-%d-%H-%M-%S') + '第 %s 次寻找: %s' % (i + 1, name[0])
        image = self.images_or_none(driver, name[0] + '@auto.png', way_name)
        if image:
            driver.click(image[0][0], image[0][1])
            print(strftime('%Y-%m-%d-%H-%M-%S') + '--点击图片 %s 成功---图片信息 %s' % (name[0], image))
            break

def pay_out(self,driver,name,way_name='channel'):
    '''
    支付操作第四部 退出支付界面,不能直接BACK键退出的，需要用图片退出才用该方法
    :param driver:
    :param name: 目标截图
    :param way_name: 区分游戏和渠道截图的路径
    :return:
    '''
    name = self.get_name(name, way_name)
    for i in name:
        for x in xrange(5):
            print strftime('%Y-%m-%d-%H-%M-%S') + '第 %s 次寻找: %s' % (x + 1, i)
            image = self.images_or_none(driver,i+'@auto.png',way_name)
            if image:
                driver.click(image[0][0], image[0][1])
                print(strftime('%Y-%m-%d-%H-%M-%S') + '--点击图片 %s 成功---图片信息 %s' % (i, image))
                break

def get_view_info(self,driver,act_or_package=1):
    '''
    获取当前界面的 packages,activity
    :param driver:
    :param act_or_package:  0 是package 1 是activity 2是 PID
    :return:
    '''
    sleep(2)
    return driver.current_app()[act_or_package]

def pay_exist_pic(self,driver,name,way_name='channel',direction=None):
    '''
    其实就是 pay_in pay_up 和 pic_exist 的调用。。。
    使用:判断是否进入到相应的第三方支付界面，通过 图片判断,
    :param driver:
    :param name: 目标图片
    :param way_name: 区分游戏和渠道截图的路径
    :param direction: 是否滑动
    :return:  pic_exist
    '''
    self.pay_in(driver,name,way_name,direction)
    self.pay_up(driver,way_name)
    return self.pic_exist(driver,name,way_name)

def pay_exist_act(self,driver,name,act_or_packages = 1,way_name='channel',direction=None):
    '''
    其实就是 pay_in pay_up 和 get_view_info 的调用。。。
    使用:判断是否进入到相应的第三方支付界面，通过 activitv或者 package 判断
    :param driver:
    :param name: 目标图片
    :param act_or_packages: 0 是package 1 是activity 2是 PID
    :param way_name: 区分游戏和渠道截图的路径
    :param direction: 是否滑动
    :return: get_view_info
    '''
    self.pay_in(driver,name,way_name,direction)
    self.pay_up(driver,way_name)
    sleep(10)
    return self.get_view_info(driver,act_or_packages)