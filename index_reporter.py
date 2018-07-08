# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 07:21:32 2018

@author: morim
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import datetime

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

import functions as fs

FROM_ADDRESS = '{}'.format(input("Your Gmail adress:"))
MY_PASSWORD = '{}'.format(input("Your Password:"))
TO_ADDRESS = '{}'.format(input("Send to:"))


#BCC = 'receiver2@test.net'
SUBJECT = '今日の指標({})'.format(datetime.date.today())

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    #msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg

def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


#7時以降に送ること
def send_me():
    to_addr =TO_ADDRESS
    subject = SUBJECT

    body = "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}".format(
            fs.nikkei_stock_average(),
            fs.n_day_before(),
            fs.interest_rate(), 
            fs.exchange(), 
            fs.oil_price(), 
            fs.reit(), 
            fs.f_stock()
            )
    
    msg = create_message(FROM_ADDRESS, to_addr, subject, body)
    send(FROM_ADDRESS, to_addr, msg)
    print(body)

if __name__ == '__main__':
    
    send_me()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    