#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'

import time
from selenium import webdriver # Doc: http://selenium-python.readthedocs.org/en/latest/index.html
from PIL import Image # Doc: http://pillow.readthedocs.org/

PNGPATH = '/tmp/'

def saveScreenshot():
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    url_zhengzhou = 'http://www.weather.com.cn/weather/101180101.shtml'
    driver.get(url_zhengzhou)
    
    timestyle = time.strftime('%m%d_%H%M%S')
    pngname = 'ZZ_7days_weather_{}.png'.format(timestyle)
    driver.get_screenshot_as_file(PNGPATH + pngname)

    # driver.close()
    # print(help(webdriver.Firefox().get_screenshot_as_png))
    print('successfully get {}'.format(pngname))

    # split picture
    im = Image.open(PNGPATH + pngname)
    box = (126, 266, 818, 684) # ROI(Region of Interest)  get from GIMP
    region = im.crop(box)
    ROI_name = 'ZZ_7days_weather_ROI_{}.png'.format(timestyle)
    region.save(PNGPATH + ROI_name)
    print('successfully get {}'.format(ROI_name))

    # remove ad
    im = Image.open(PNGPATH+ROI_name)
    xsize, ysize = im.size
    box = (153, 0, xsize, 39) # ad region, get from GIMP
    im.paste((255, 255, 255), box) # paint white color to ad region 
    im.save(PNGPATH+ROI_name)
    print('successfully remove ad. in {}'.format(ROI_name))

    pic7 =  '{}{}'.format(PNGPATH, ROI_name)
    ##################################################################

    # find element 8-15天
    element = driver.find_element_by_partial_link_text('8-15天')
    element.click()
    driver.implicitly_wait(30) # An implicit wait is to tell WebDriver to poll the DOM for a certain amount of time when trying to find an element or elements if they are not immediately available.

    pngname = 'ZZ_15days_weather_{}.png'.format(timestyle)
    driver.get_screenshot_as_file(PNGPATH + pngname)

    driver.close()
    # print(help(webdriver.Firefox().get_screenshot_as_png))
    print('successfully get {}'.format(pngname))

    # split picture
    im = Image.open(PNGPATH + pngname)
    box = (123, 260, 820, 802) # ROI(Region of Interest)  get from GIMP
    region = im.crop(box)
    ROI_name = 'ZZ_15days_weather_ROI_{}.png'.format(timestyle)
    region.save(PNGPATH + ROI_name)
    print('successfully get {}'.format(ROI_name))

    # remove ad
    im = Image.open(PNGPATH+ROI_name)
    xsize, ysize = im.size
    box = (653, 6, xsize, 43) # ad region, get from GIMP
    im.paste((255, 255, 255), box) # paint white color to ad region 
    im.save(PNGPATH+ROI_name)
    print('successfully remove ad. in {}'.format(ROI_name))
    
    pic15 =  '{}{}'.format(PNGPATH, ROI_name)

    return [pic7, pic15]

# saveScreenshot()
