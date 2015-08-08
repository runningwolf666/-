#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'

import time
import os
import sys
from selenium import webdriver # Doc: http://selenium-python.readthedocs.org/en/latest/index.html
from PIL import Image # Doc: http://pillow.readthedocs.org/


class Screenshot:
    '''get screenshot'''
    def __init__(self):
        PNGPATH = self.setPicPath()

    def saveScreenshot(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        
        url_zhengzhou = 'http://www.weather.com.cn/weather/101180101.shtml'
        driver.get(url_zhengzhou)
        
        timestyle = time.strftime('%m%d_%H%M%S')
        pngname = 'ZZ_7days_weather_{}.png'.format(timestyle)
        rawpic7 = os.path.join(PNGPATH, pngname)
        driver.get_screenshot_as_file(rawpic7)

        # driver.close()
        # print(help(webdriver.Firefox().get_screenshot_as_png))
        print('successfully get {}'.format(pngname))

        # split picture
        im = Image.open(rawpic7)
        box = (126, 266, 818, 684) # ROI(Region of Interest)  get from GIMP
        region = im.crop(box)
        ROI_name = 'ZZ_7days_weather_ROI_{}.png'.format(timestyle)
        ROI_pic7 = os.path.join(PNGPATH, ROI_name)
        region.save(ROI_pic7)
        print('successfully get {}'.format(ROI_name))

        # remove ad
        im = Image.open(ROI_pic7)
        xsize, ysize = im.size
        box = (153, 0, xsize, 39) # ad region, get from GIMP
        im.paste((255, 255, 255), box) # paint white color to ad region 
        im.save(ROI_pic7)
        print('successfully remove ad. in {}'.format(ROI_name))

        ##################################################################

        # find element 8-15天
        element = driver.find_element_by_partial_link_text('8-15天')
        element.click()
        driver.implicitly_wait(30) # An implicit wait is to tell WebDriver to poll the DOM for a certain amount of time when trying to find an element or elements if they are not immediately available.

        pngname = 'ZZ_15days_weather_{}.png'.format(timestyle)
        rawpic15 = os.path.join(PNGPATH, pngname)
        driver.get_screenshot_as_file(rawpic15)

        driver.close()
        # print(help(webdriver.Firefox().get_screenshot_as_png))
        print('successfully get {}'.format(pngname))

        # split picture
        im = Image.open(rawpic15)
        box = (123, 260, 820, 802) # ROI(Region of Interest)  get from GIMP
        region = im.crop(box)
        ROI_name = 'ZZ_15days_weather_ROI_{}.png'.format(timestyle)
        ROI_pic15 = os.path.join(PNGPATH, ROI_name)
        region.save(ROI_pic15)
        print('successfully get {}'.format(ROI_name))

        # remove ad
        im = Image.open(ROI_pic15)
        xsize, ysize = im.size
        box = (653, 6, xsize, 43) # ad region, get from GIMP
        im.paste((255, 255, 255), box) # paint white color to ad region 
        im.save(ROI_pic15)
        print('successfully remove ad. in {}'.format(ROI_name))
        
        return [ROI_pic7, ROI_pic15]


    def setPicPath(self):
        # linux or Mac
        if sys.platform.startswith('linux') or sys.platform == 'darwin':
            currpath =  '/tmp'
        # windows
        elif sys.platform.startswith('win'):
            currpath = os.getcwd()
        else:
            raise PlatformError
        
        DIR_NAME = 'pic'
        picpath = os.path.join(currpath, DIR_NAME)
        if not os.path.exists(picpath):
            os.makedirs(picpath)
        return picpath


class PlatformError(Exception):
    """platform error"""
    pass

