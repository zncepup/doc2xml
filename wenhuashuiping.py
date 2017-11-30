# -*- coding: utf-8 -*-
import re

def wenhua(file_str):
    a=re.findall('被告人.*?(大学|大专|中专|本科|高中|小学|初中|中学|文盲)',file_str)
    if len(a)!=0:
        return a[0]
    else:
        return 'unknown'

def status(file_str):
    a=re.findall('被告人.*?(人大代表|党员)',file_str)
    if len(a)!=0:
        return a[0]
    else:
        return '群众'
# aa='被告人。。党员'
# a=status(aa)
# print(a)
# print(type(a))


# with open('H:\weixianjiashi-henan\(2012-11-15) 于善国危险驾驶一案一审刑事判决书.txt',encoding='utf8') as f:
#     f=f.read()
#     f='出生于2017年5neigao被告人，结大专于月1日'
#     a=wenhuashuiping(f)
#
#
# print(a)