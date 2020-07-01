#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: mason
# Date: 2014-10-23
# Purpose: 发送邮件

'''
发送邮件
Parameters：主题、接受者(多个用','分割)、抄送(多个用','分割)、内容(可以是文件)、附件(多个用','分割)
'''

__author__ = 'mason'

import email,sys,os
import smtplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage

SENDER = '****'
SMTPSERVER = '*******'
#RECEIVERS = ''
USERNAME = '*********'
APIKEY = '*********'

def sendMail(subject, receivers, cc, content, atts):
    msg = MIMEMultipart('related')
    msg['Subject'] = unicode(subject, "UTF-8")
    msg['From'] = SENDER
    msg['To'] = receivers
    if cc != '':
        msg['Cc'] = cc
    
    #邮件内容
    if os.path.isfile(content):
        if(content.split('.')[-1]=='html'):
            cont = MIMEText(open(content).read(),'html','utf-8')
        else:
            cont = MIMEText(open(content).read(),'plain','utf-8')
    else:
        cont = MIMEText(content, 'plain','utf-8')
    msg.attach(cont)
    
    #构造附件
    if atts != -1 and atts != '':
        for att in atts.split(','):
            os.path.isfile(att)
            name = os.path.basename(att)
            att = MIMEText(open(att).read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename=%s' % name.decode('utf-8').encode('gbk')
            msg.attach(att)
    smtp = smtplib.SMTP()
    smtp.connect(SMTPSERVER)
    smtp.login(USERNAME, APIKEY)
    for recev in receivers.split(','):
        smtp.sendmail(SENDER,recev, msg.as_string())
    if cc != '':
        for c in cc.split(','):
            smtp.sendmail(SENDER,c, msg.as_string())
    smtp.quit()

def main():
    print "start send mail[sendmail.py]"
    subject = sys.argv[1]
    receivers = sys.argv[2]
    #cc = sys.argv[3]
    leng = len(sys.argv)
    if leng == 3:
        cc = ""
        content = ""
        atts = -1
    elif leng == 4:
        print "The parameters is not currect!"
        sys.exit(0)
    elif leng == 5:
        cc = sys.argv[3]
        content = sys.argv[4]
        atts = -1
    elif leng == 6:
        cc = sys.argv[3]
        content = sys.argv[4]
        atts = sys.argv[5]
    sendMail(subject, receivers, cc, content, atts)
    print "finish send mail[sendmail.py]"

if __name__=='__main__':
    main()

