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
    size= [int(size[0]),int(size[1])] #size[0] Ϊwidth size[1] Ϊhigh
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
        print 'û���������򣬲�������������up,down,right,left'
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
    ͨ��os.listdir ȥ��ȡ�ļ������н�ͼ��ͨ�� re.match����ȡ����Ҫ�Ľ�ͼ����
    :param name: ��ͼ���Ƶ�ǰ׺       �� name == 'pay_in'
    :param way_name: ������Ϸ��ͼ����������ͼ
    :return: ����һ���н�ͼ���Ƶ�list,�� ['pay_in_01','pay_in_02'......]
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
            logo=logo.group().split('.')   #��ͼ���Ƹ�ʽһ��������enter_game_01.1920x1080.png
            b.append(logo[0])             #�ָ�󣬻�ȡ���� enter_game_01
    b = list(set(b)) #ȥ��
    b = sorted(b)   #����
    return b



def guide_exist(self,driver,name):
    '''
    �ж�Ŀ��ͼƬ�Ƿ����,�÷�����Ҫ�ж� ��Ϸ������һ��ͼƬ
    :param driver:
    :param name: Ŀ���ͼǰ׺
    :return: Ŀ��ͼ�����򷵻طǿգ��������򷵻� None
    '''
    global image
    name = self.get_name(name)
    for x in xrange(10):
        print '�� %s ��Ѱ��: %s' % (x + 1, name[0])
        image = self.images_or_none(driver, name[0] + '@auto.png')
        if image:
            print '����ͼƬ���ڣ���Ҫ������: ' ,name[0] ,image
            break
        if x == 9:
            print '����ͼƬ�����ڣ�����Ҫ������: ',name[0],image
    return image

def pic_exist(self,driver,name,way_name):
    '''
    ֧���������������ж�ͼƬ�Ƿ����
    �÷���,��Ҫ���ж�,������֧�������ͼƬ
    �жϵ�ǰ��������Ӧ�ĵ�����֧������
    :param driver:
    :param name: Ŀ��ͼƬ
    :param way_name: ������Ϸ��������ͼ��·��
    :return: ͼƬ����,���طǿգ������� ����None
    '''
    name = name[0].replace('in_01', 'exist')
    name = self.get_name(name, way_name)
    for i in xrange(5):
        print strftime('%Y-%m-%d-%H-%M-%S') + '�� %s ��Ѱ��: %s' % (i + 1, name[0])
        image = self.images_or_none(driver, name[0] + '@auto.png', way_name)
        if image:
            print(strftime('%Y-%m-%d-%H-%M-%S') + '--����*******ͼƬ %s �ɹ�---ͼƬ��Ϣ %s' % (name[0], image))
            return image
        if i == 4:
            return None
        
        
def game_click(self,driver,name):
    '''
    Ѱ�Һ͵������Ŀ��ͼƬ,�� Ŀ��ͼƬ�� guide_001 -----guide_100,ֻ�� name ���� 'guide' �ͻ�Ѱ�Һ͵����ЩͼƬ
    :param driver:
    :param name: Ŀ��ͼƬ��ǰ׺
    :return: ����ͼƬ���ҵ��͵��������һ���ǿգ����ĳ��ͼƬ�ﵽѭ�����ֵ��û�ҵ����򷵻� None
    '''
    name = self.get_name(name)
    for i in name:
        for x in xrange(10):
            print (strftime('%Y-%m-%d-%H-%M-%S')+'�� %s ��Ѱ��: %s' %(x+1,i))
            image = self.images_or_none(driver,i+'@auto.png')
            if image:
                sleep(2)
                driver.click(image[0][0],image[0][1])
                #self.click_images(driver,i+'@auto.png')
                print (strftime('%Y-%m-%d-%H-%M-%S')+'--���ͼƬ %s �ɹ�---ͼƬ��Ϣ %s' %(i,image))
                break
            if x == 9:
                print '�޷�ƥ�䵽ͼƬ��', i
                return image
    return 'ok'

def game_pay(self,driver,name):
    '''
    ��������֧������ķ��������ж� activity,�����ǰ��activity������֧������ģ�����������,
    ������ǣ���Ѱ�Һ͵��Ŀ��ͼƬ,Ŀ��ͼƬ�����ڣ�������������������һ��ͼƬ.
    :param driver:
    :param name: mĿ���ͼ����
    :return: ���ѭ�����ﵽ������������None
    '''
    name = self.get_name(name)
    for x in xrange(10):
        if self.get_view_info(driver) == self.get_channel():
            print unicode('�Ѿ����뵽֧������')
            return 'ok'
        else:
            for i in name:
                print (strftime('%Y-%m-%d-%H-%M-%S')+'Ѱ��: %s' % (i))
                image = self.images_or_none(driver, i + '@auto.png')
                if image:
                    sleep(1)
                    driver.click(image[0][0], image[0][1])
                    print(strftime('%Y-%m-%d-%H-%M-%S') + '--���ͼƬ %s �ɹ�---ͼƬ��Ϣ %s' % (i, image))

        if x == 9:
            print unicode('����֧������ʧ��')
            return None
        
        
        
        
def pay_in(self,driver,name,way_name='channel',direction=None):
    '''
    ֧�������һ������,�ҵ���Ӧ��֧����ʽ
    :param driver:
    :param name:Ŀ���ͼ����
    :param way_name: ������Ϸ��������ͼ��·��
    :param direction: ���ͼƬ���Ƿ���Ҫ��������������Ҫ���� 'up' 'down' 'right' 'left',����Ҫ����None
    :return:
    '''
    name = self.get_name(name, way_name)
    for i in name:
        for x in xrange(5):
            print strftime('%Y-%m-%d-%H-%M-%S') + '�� %s ��Ѱ��: %s' % (x + 1, i)
            image = self.images_or_none(driver, i + '@auto.png', way_name)
            if image:
                driver.click(image[0][0], image[0][1])
                print(strftime('%Y-%m-%d-%H-%M-%S') + '--���ͼƬ %s �ɹ�---ͼƬ��Ϣ %s' % (i, image))
                break
            else:
                self.swipe(driver, direction)

def pay_up(self,driver,way_name):
    '''
    ֧������ڶ�������,�ҵ�����֧���İ�ť���确����֧���� 'ȷ��֧��'
    :param driver:
    :param way_name: ������Ϸ��������ͼ��·��
    :return:
    '''
    name = self.get_name('pay_up', way_name)
    for i in xrange(5):
        print strftime('%Y-%m-%d-%H-%M-%S') + '�� %s ��Ѱ��: %s' % (i + 1, name[0])
        image = self.images_or_none(driver, name[0] + '@auto.png', way_name)
        if image:
            driver.click(image[0][0], image[0][1])
            print(strftime('%Y-%m-%d-%H-%M-%S') + '--���ͼƬ %s �ɹ�---ͼƬ��Ϣ %s' % (name[0], image))
            break

def pay_out(self,driver,name,way_name='channel'):
    '''
    ֧���������Ĳ� �˳�֧������,����ֱ��BACK���˳��ģ���Ҫ��ͼƬ�˳����ø÷���
    :param driver:
    :param name: Ŀ���ͼ
    :param way_name: ������Ϸ��������ͼ��·��
    :return:
    '''
    name = self.get_name(name, way_name)
    for i in name:
        for x in xrange(5):
            print strftime('%Y-%m-%d-%H-%M-%S') + '�� %s ��Ѱ��: %s' % (x + 1, i)
            image = self.images_or_none(driver,i+'@auto.png',way_name)
            if image:
                driver.click(image[0][0], image[0][1])
                print(strftime('%Y-%m-%d-%H-%M-%S') + '--���ͼƬ %s �ɹ�---ͼƬ��Ϣ %s' % (i, image))
                break

def get_view_info(self,driver,act_or_package=1):
    '''
    ��ȡ��ǰ����� packages,activity
    :param driver:
    :param act_or_package:  0 ��package 1 ��activity 2�� PID
    :return:
    '''
    sleep(2)
    return driver.current_app()[act_or_package]

def pay_exist_pic(self,driver,name,way_name='channel',direction=None):
    '''
    ��ʵ���� pay_in pay_up �� pic_exist �ĵ��á�����
    ʹ��:�ж��Ƿ���뵽��Ӧ�ĵ�����֧�����棬ͨ�� ͼƬ�ж�,
    :param driver:
    :param name: Ŀ��ͼƬ
    :param way_name: ������Ϸ��������ͼ��·��
    :param direction: �Ƿ񻬶�
    :return:  pic_exist
    '''
    self.pay_in(driver,name,way_name,direction)
    self.pay_up(driver,way_name)
    return self.pic_exist(driver,name,way_name)

def pay_exist_act(self,driver,name,act_or_packages = 1,way_name='channel',direction=None):
    '''
    ��ʵ���� pay_in pay_up �� get_view_info �ĵ��á�����
    ʹ��:�ж��Ƿ���뵽��Ӧ�ĵ�����֧�����棬ͨ�� activitv���� package �ж�
    :param driver:
    :param name: Ŀ��ͼƬ
    :param act_or_packages: 0 ��package 1 ��activity 2�� PID
    :param way_name: ������Ϸ��������ͼ��·��
    :param direction: �Ƿ񻬶�
    :return: get_view_info
    '''
    self.pay_in(driver,name,way_name,direction)
    self.pay_up(driver,way_name)
    sleep(10)
    return self.get_view_info(driver,act_or_packages)