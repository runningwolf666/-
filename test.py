#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'

from SendEmail import sendEmail
import time

try:
    text_body = '...' # ATTENTION: you must add email's body, otherwise it CAN'T be send out!
    subject = 'subject'
    attachment = ['/tmp/abc.png', '/tmp/abc.png']
    sendEmail(subject=subject,text_body=text_body , attachment=attachment)
    # sendEmail(subject=subject,text_body=text_body)
except Exception as e:
    timestyle = time.strftime('%m%d_%H%M%S')
    logname = 'err_{}.log'.format(timestyle)
    with open(logname, 'w') as f:
        f.write(str(e))
