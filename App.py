#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'
'''此脚本需要在网速较好的情况下运行，否则会出现网页一直加载不完的情况'''

import time
from SendEmail import sendEmail
from Screenshot import Screenshot

try:
    text_body = 'weather' # ATTENTION: you must add the email's body, otherwise it CANNOT be sent out!
    subject = 'ZhengZhou weather for 7 days and 15 days later'
    ss = Screenshot()
    attachment = ss.saveScreenshot()
    sendEmail(subject=subject,text_body=text_body , attachment=attachment)
    # sendEmail(subject=subject,text_body=text_body)
except Exception as e:
    timestyle = time.strftime('%m%d_%H%M%S')
    logname = 'err_{}.log'.format(timestyle)
    print('err--->', str(e))
    with open(logname, 'w') as f:
        f.write(str(e))

