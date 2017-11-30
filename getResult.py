# -*- coding: utf-8 -*-
'''
Created on 2017年9月20日

@author: YZP
'''
import os,re,sys


num = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,}

def getSurveillans(con):
    con = preprocess(con)
    psl = "判处.*?管制(.*?[年月天])[；;。\s（(]"
    surveillans = re.findall(psl,con)
    
    if surveillans and len(surveillans[0]) < 10:
        sstime = surveillans[0].split('缓刑')[0]
        stime = getNum(sstime)
        probation = 0.0
        if '缓刑' in surveillans[0]:
            spro = surveillans[0].split('缓刑')[1]
            probation = getNum(spro)
        return surveillans[0],stime,probation
    else:
        return 'unknown',"unknown","unknown"

def getDentention(con):
    con = preprocess(con)
    #print con    
    pdt = "判处.*?拘役(.*?[年月天].*?)[；;。\s（(]"#
    dentention = (re.findall(pdt,con))
    
    #if dentention and len(dentention[0]) < 20:###
    if dentention:
        sdtime = dentention[0].split('缓刑')[0]
        dtime = getNum(sdtime)
        probation = 0.0
        if '缓刑' in dentention[0]:
           spro = dentention[0].split('缓刑')[1]
           probation = getNum(spro)         
        return dentention[0],dtime,probation
    else:
        return "unknown","unknown","unknown"

def getFixtedTerm(con):
    con = preprocess(con)
    #print con
    pft = "判处.*?有期徒?刑?(.*?[年月].*?)[；;。\s（(]"
    fixtedTerm = (re.findall(pft,con))
    
    if fixtedTerm:
        #print fixtedTerm[0]
        sftime = fixtedTerm[0].split('缓刑')[0]
        ftime = getNum(sftime)
        probation = 0.0
        if '缓刑' in fixtedTerm[0]:
            spro = fixtedTerm[0].split('缓刑')[1]
            probation = getNum(spro)        
        return fixtedTerm[0],ftime,probation
    else:
        return "unknown","unknown","unknown"
    
def getFine(con):
    con = preprocess(con)    
    pfine = "罚金?[人民币]*(.{5,10}?元)"
    fine = (re.findall(pfine,con))
    money = 0
    if fine:
        if '币' in fine[0]:
            money = fine[0].split('币')[1].split('元')[0]
        elif '金' in fine[0]:
            money = fine[0].split('金')[1].split('元')[0]
        else:
            money = fine[0].split('元')[0]    
        
        sw = sq = sb = ''
        if money.isdigit():
            money = int(money)
        else:
            if '万' in money:
                sw = money.split('万')[0]
                if '千' in money:
                    sq = money.split('万')[1].split('千')[0]
                    if '百' in money:
                        sb = money.split('千')[1].split('百')[0]
                elif '百' in money:
                    sb = money.split('万')[1].split('百')[0]
            elif '千' in money:
                sq = money.split('千')[0]
                if '百' in money:
                    sb = money.split('千')[1].split('百')[0]
            elif '百' in money:
                sb = money.split('百')[0]
        
            w = q = b = 0
            for n in num:
                if n == sw:
                    w = num[n]
                if n == sq:
                    q = num[n]
                if n == sb:
                    b = num[n]
            money = w*10000 + q*1000 + b*100
                
        return fine[0],money
    else:
        return "unknown",money

def preprocess(con):
    if '判决如下' in con:
        return con.split('判决如下')[-1].split("书记员")[0]
    elif '本院认为' in con:
        return con.split('本院认为')[-1].split("书记员")[0]
    else:
        return con.split("书记员")[0]

def getNum(time):
    syear = ''
    smonth = ''
    sday = ''
    if '年' in time:
        syear = time.split('年')[0]
        if '月' in time:
            smonth = time.split('年')[1].split('月')[0]
            if '天' in time:
                sday = time.split('月')[1].split('天')[0]
        elif '天' in time:
            sday = time.split('年')[1].split('天')[0]
    elif '月' in time:
        smonth = time.split('月')[0]
        if '天' in time:
            sday = time.split('月')[1].split('天')[0]
    elif '天' in time:
        sday = time.split('天')[0]
        
    year = 0
    month = 0
    day = 0
    for n in num:
        if n in syear:
            year = num[n]
        if '十一' in smonth:
            month = 11
        elif n in smonth:
            month = num[n]
            
        if '十五' in sday:
            day = 15
        elif '二十' in sday:
            day = 20
        elif '二十五' in sday:
            day = 25
        elif n in sday:
            day = num[n]
    time = year*12 + month + round(day/30.0,2)
    return time
    

if __name__ == "__main__":
    file_dir = "/media/zp/新加卷/weixianjiashi-all/"
    file_list = os.listdir(file_dir)
    os.chdir(file_dir)
    for index in range(len(file_list)):
        with open(file_list[index],'r') as f:
            con = f.read()
            #print con
#            print file_list[index],index
#             if getSurveillans(con) != 'unknown':
#                 #print file_list[index],index
#                 print getSurveillans(con)[0],getSurveillans(con)[1]
#             if getDentention(con) != 'unknown':
#                 #print file_list[index],n
#                 print (getDentention(con)[0],getDentention(con)[1],getDentention(con)[2])
#             if getFixtedTerm(con) != 'unknown':
#                 print (getFixtedTerm(con)[0],getFixtedTerm(con)[1],getFixtedTerm(con)[2])
#             if getFine(con)[0] != 'unknown':
#                 print (file_list[index],index)
#                 print (getFine(con)[0],getFine(con)[1])
