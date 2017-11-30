# -*- coding: utf-8 -*-
'''
Created on 2017年9月25日
@author: YZP
'''
import os,re,sys


def getArea(con):
    con = con.split("书记员")[0]
    pArea = "(.*?)[人 民]*法 ?院\s*\n"
    Area = (re.findall(pArea,con))
    #print trialResult[0]
    area = []
    province = Area[0][0:Area[0].find('省')+1].strip()
    if '市' in Area[0]:
        city = Area[0][Area[0].find('省')+1:Area[0].find('市')+1].strip()
        county = Area[0][Area[0].find('市')+1:Area[0].find('县')+1].strip()       
        district = Area[0][Area[0].find('市')+1:Area[0].find('区')+1].strip()
    else:
        city = ""
        county = Area[0][Area[0].find('省')+1:Area[0].find('县')+1].strip() 
        district = Area[0][Area[0].find('省')+1:Area[0].find('区')+1].strip()
    #print province,city,county,district
        
    if province:
        area.append(province)
    else:
        area.append(city)
    area.append(city)
    if county:
        area.append(county)
    else:
        area.append(district)

    return area

def getAwardID(con):
    con = con.split("书记员")[0]
    pAwardID = "([（(].*[）)].*号)\s*\n"
    AwardID = (re.findall(pAwardID,con))
    #print AwardID[0]
    if AwardID:
        return AwardID[0].strip()
    else:
        return 'unknown'

def getIndictmentID(con):
    con = con.split("书记员")[0]
    pIndictmentID = "[人民检察院|公诉机关]*以(.*号)起诉书[，,]?指控[，,]?被告人"
    IndictmentID = (re.findall(pIndictmentID,con))
    #print IndictmentID[0]
    if IndictmentID:
        return IndictmentID[0]
    else:
        return 'unknown'
    
def getJudge(con):
    con = con.split("书记员")[0]
    pJudge = "[　 \s]([代理|人民]*审[　 \s;]*判[　 \s;]*[员长][　 \s;]*.*)\s*" ##注意全角空格,方框形态的空格
    Judge = (re.findall(pJudge,con))
    #print Judge[0]
    if Judge:
        return Judge[0].strip()
    else:
        return 'unknown'
    
def getTrialTime(con):
    con = con.split("书记员")[0]
    pTime = "(二.*年.*月.*日)\s*\n"
    Time = (re.findall(pTime,con))
    #print Time[0].strip()
    if Time:
        return Time[0].strip()
    else:
        return 'unknown'

       
if __name__ == "__main__":
    file_dir = "/media/zp/新加卷/jiaotongzhaoshi-all/"
    file_list = os.listdir(file_dir)
    os.chdir(file_dir)
    for index in range(len(file_list)):
        with open('/media/zp/新加卷/jiaotongzhaoshi-all/(2009-06-03) 被告人张东伟犯交通肇事一案.txt') as f:
            con = f.read()
            #print con
            # print file_list[index],index
            print ('省',getArea(con)[0],'市',getArea(con)[1],'县',getArea(con)[2])
            # print getAwardID(con)
            # print getIndictmentID(con)
            # print getJudge(con)
            # print getTrialTime(con)
