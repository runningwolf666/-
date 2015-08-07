#!/usr/bin/env python3
#-*- coding:utf-8 -*-
请在Python3下运行此程序='Please run this program with Python3'

from envelopes import Envelope # Doc: http://tomekwojcik.github.io/envelopes/api/envelope.html

def sendEmail(subject, text_body=None, html_body=None, attachment=None):
    FROM_ADDR = 'xxxxx@163.com'
    PASSWD = 'xxxxx' # 客户端授权码 http://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2cda80145a1742516
    TO_ADDR = 'xxxxx@163.com'

    # From: https://pypi.python.org/pypi/Envelopes/0.4
    envelope = Envelope(

        from_addr=(FROM_ADDR, '163mail'),
        # to_addr = ['vtianqi666@163.com', 'vweather666@163.com'],
        to_addr = [TO_ADDR],
        subject=subject,
        text_body=text_body,
        html_body=html_body
        )
    # Parameters:    
    # to_addr – To address or list of To addresses
    # from_addr – From address
    # subject – message subject
    # html_body – optional HTML part of the message
    # text_body – optional plain text part of the message
    # cc_addr – optional single CC address or list of CC addresses
    # bcc_addr – optional single BCC address or list of BCC addresses
    # headers – optional dictionary of headers
    # charset – message charset


    # add_attachment(file_path, mimetype=None)
    #     Attaches a file located at file_path to the envelope. If mimetype is not specified an attempt to guess it is made. If nothing is guessed then application/octet-stream is used.

    # 既然有了type()来判断类型，为什么还有isinstance()呢？
    # 一个明显的区别是在判断子类。
    # type()不会认为子类是一种父类类型。
    # isinstance()会认为子类是一种父类类型。

    # about `is` and `==`: http://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is-in-python
    # is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.

    # about type() and isinstance(): http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python
    # isinstance caters for inheritance (an instance of a derived class is an instance of a base class, too), while checking for equality of type does not (it demands identity of types and rejects instances of subtypes, AKA subclasses).
    if attachment:
        if type(attachment) is str:
            envelope.add_attachment(attachment)
        elif type(attachment) in (list, tuple):
            for item in attachment:
                if item:
                    envelope.add_attachment(item)
        else:
            pass

    # Send the envelope using an ad-hoc connection...
    envelope.send('smtp.163.com', login=FROM_ADDR, password=PASSWD, tls=True)

    print('send mail done!')
