'''
encoding:   -*- coding: utf-8 -*-
@Time           :  2024/10/7 17:17
@Project_Name   :  SendEmail
@Author         :  lhw
@File_Name      :  uniTest.py

功能描述

实现步骤

'''
from src.lhw_send_email import SendEmail
from email.header import Header


fromEmailAddress = '扶摇-lhw <1959415641@qq.com>'
password = 'vrpphqonlthjbcea'
destination = ['2704316524@qq.com']
subject = '扶摇团队->lhw-send-email 0.1.2版本'
content = '附件功能测试'
att_paths = ['D:/code/All_Learning/Python/Tecent/uniTest.py']

# with open('D:/code/All_Learning/Python/Tecent/uniTest.py', 'r', encoding='utf-8') as f:
#     print(f.read())
s = SendEmail(fromEmailAddress=fromEmailAddress, password=password,
              destination=destination, subject=subject,
              content=content, isAtt=True, att_paths=att_paths)

s.send()
