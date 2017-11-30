# -*- coding: utf-8 -*-
import re
from collections import OrderedDict as dict
def birthandage(file_str):
    dictionary={'年':0,'月':0,'日':0,'案发年龄':0}
    # dictionary=dict({'年':0,'月':0,'日':0,'案发年龄':0})
    age1=re.compile('被告.*?(\d{1,})岁')
    age=re.findall(age1,file_str)
    birthday=re.findall('出生于(\d{1,})年(\d{1,})月(\d{1,})日',file_str)
    # print(list(birthday[0])[1])
    # print(type(birthday[0]))
    num=0
    if len(age) != 0:
        # print(age)
        dictionary['案发年龄'] = int(age[0])
        num += 1
    if len(birthday)==1:
        dictionary['年']=int(list(birthday[0])[0])
        dictionary['月'] = int(list(birthday[0])[1])
        dictionary['日'] = int(list(birthday[0])[2])
        num+=3
    else:
        year=re.findall('被告.*?[^于]([1,2]\d{3})年',file_str)
        month = re.findall('被告.*?[^于][1,2]\d{3}年(\d{1,})月', file_str)
        day = re.findall('被告.*?[^于][1,2]\d{3}年\d{1,}月(\d{1,})日', file_str)
        day_1=re.findall('被告.*?[^于][1,2]\d{3}年\d{1,}月(\d{1,})',file_str)

        # print(year,month,day)
        if len(year)!=0:
            dictionary['年']=int(year[0])
            num += 1
        if len(month) != 0:
            dictionary['月'] = int(month[0])
            num += 1
        if len(day) != 0:
            dictionary['日'] = int(day[0])
            num += 1
        if len(day)==0 and len(day_1)!=0:
            dictionary['日'] = int(day_1[0])
            num += 1
    return dictionary





# (?:(?!于).)*?
#
# with open('H:\文书\危险驾驶-来自file/2015-06-26 刘×危险驾驶罪一审刑事判决书.txt',encoding='utf8') as f:
#     f=f.read()
#
# a=birthandage(f)
# print(a)