#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host='smtp.126.com'  #设置服务器
mail_user='*****@126.com'    #用户名
mail_pass='****'   #口令 
 
 
sender = '***@126.com'
receivers = ['****@qq.com' ,'****@qq.com.cn'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = '***@126.com'
message['To'] = '***;***'
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print( "邮件发送成功")
except Exception as e:
    print('sendemail failed next is the reason')
    print(e)
