# -*- coding: utf-8 -*-
'''
Created on 2017年10月11日
@author: YZP
'''
import os,re,sys



num = {'一':1,'二':2,'两':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,
       '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,
       '百':100,'千':1000,'万':10000,}

def getDeathNum(con):
    con1 = preprocess(con)
    #p = ur"([经|将|致|造|发].*?死亡?)[的重大交通事故|的严重事故|的严重后果]*"
    p = "([将|致|造|发].*?死亡?)"
    death1 = re.findall(p,con1)
#     for each in death:
#         print each
    if death1 and len(death1[0]) < 30:
        res = death1[0]
    else:
        death = re.findall(p,con)
        if death and len(death[0]) < 30:
            res = death[0]
        else:
            res = 'unknown'

    death_num = 0
    if res != 'unknown':
        for k in num:
            if k in res and k+'人' in res:
                death_num = num[k]
                break
            elif '致人死亡' in res:
                death_num = 1
                break
            elif '发生重大事故，致人重伤、死亡' in res:
                death_num = 0
                break
            else:
                death_num = len(res.split('、'))
                
        if '十' in res:###
            death_num = death_num + 10         
    else:
        death_num = 0
     
    return res,death_num

def getInjuredNum(con):
    con = preprocess(con)
    p1 = "([鉴|造|致].*?[重|受]伤)"
    p2 = "([造成|致]*.人?死亡?[，、]?.人?受?伤)"
    injured = re.findall(p1,con)
    if injured == None:
        injured = re.findall(p2,con)
#     for each in injured:
#         print each

    if injured and len(injured[0]) < 20:
        res = injured[0]
    else:
        res = 'unknown'
    #print res
    
    injured_num = 0
    if res != 'unknown':
        for k in num:
            if k in res and k+'人重伤' in res:
                injured_num = num[k]
                break
            elif k in res and k+'人受伤' in res:
                injured_num = num[k]
                break
            elif k in res and k+'余人受伤' in res:
                injured_num = num[k]
                break
            elif k in res and k+'伤' in res:
                injured_num = num[k]
                break
            elif '致人重伤' in res:
                injured_num = 1
                break
            elif '多人重伤' in res:
                injured_num = 3
                break
            else:
                injured_num = len(res.split('、'))
                
        if '十' in res:###
            injured_num = injured_num + 10      
    else:
        injured_num = 0
     
    return res,injured_num

def getDegreeOfPL(con):#
    con = con.split("书记员")[0]
    p = "[，；。](.{1,21}?车.{1,10}损[坏|害].{0,8}?)[。，；]"
    degree = re.findall(p,con)
#     for each in degree:
#         print each
    if degree:
        return degree[0]
    else:
        return 'unknown'
   
def getCompensation(con):######
    if '判决如下' in con:
        con = con.split('判决如下')[1].split('书记员')[0]
    elif '\n本院认为' in con:
        con = con.split('\n本院认为')[1].split('书记员')[0]
    else:
        con = con.split('书记员')[0]
        
    p1 = "[赔偿|支付]*.*?[人民币|经济损失]*.*?([\d \.一二三四五六七八九十百千万]{3,15}?元)"
    p2 = "[一二三四五六七八九十]、.*?[合|共|等].*?([\d \.一二三四五六七八九十百千万]{3,15}?元)"
    compensation = re.findall(p2,con)
    if len(compensation) == 0:
        compensation = re.findall(p1,con)

#     for each in compensation:
#         print each
    if compensation:
        if len(compensation) == 1:
            compensation[0] = compensation[0].replace(' ','')
            return compensation[0] +';'
        else:
            com_list = []
            for each in compensation:
                each = each.replace(' ','')
                if each not in com_list:
                    com_list.append(each)

            money = ''
            for each in com_list:
                money = money + each +';'
            return money
    else:
        return 'unknown'
    
def getUnderstanding(con):#
    con = con.replace(" ", "").split("书记员")[0]
    p = "本院.*?认为.*?谅解.*?如下"
    understanding = re.findall(p,con)
    #print understanding
    if understanding:
        return "yes"
    else:
        return 'no'

def getRes(con):
    con = con.replace(" ", "").split("书记员")[0]
    p = "[认定|认为]*.*?(被告人.*?[全部|主要|重要|次要|同等]责任?)"
    res = re.findall(p,con)
    #return res
    if res:
        if '全部责任' in res[0] or '全责' in res[0] or '全要责任' in res[0]:
            return '全部责任'
        elif '主要责任' in res[0] or '重要责任' in res[0]:
            return '主要责任'
        elif '次要责任' in res[0]:
            return '次要责任'
        elif '同等责任' in res[0]:
            return '同等责任'
    else:
        return 'unknown'
    
def getAbscond(con):
    con = con.replace(" ", "").split("书记员")[0]
    p = ".*?逃逸"
    abscond = re.findall(p,con)
    
    if abscond:
        return 'yes'
    else:
        return 'no'
    
def getAbscondDeath(con):
    con = con.replace(" ", "").split("书记员")[0]
    p = ".*?逃逸致人死亡"
    abs_death = re.findall(p,con)
    
    if abs_death:
        if '不存在' not in abs_death[-1]:
            return 'yes'
        else:
            return 'no'
    else:
        return 'no'

def preprocess(con):
    if '\n本院认为' in con and '判决如下' in con:
        return con.split('\n本院认为')[1].split('判决如下')[0]
    elif '\n本院认为' in con:
        return con.split('\n本院认为')[1].split('书记员')[0]
    elif '判决如下' in con:
        return con.split('判决如下')[0]
    else:
        return con.split('书记员')[0]
 
if __name__ == "__main__":
    file_dir = "/media/zp/新加卷/weixianjiashi-all/"
    #file_dir = "C:/Users/YZP/Desktop/交通肇事/交通肇事北京/".decode('utf-8')
    file_list = os.listdir(file_dir)
    os.chdir(file_dir)
    for index in range(len(file_list)):#
        with open(file_list[index],'r') as f:
            con = f.read()
            #print con
            print (file_list[index],index)
            print (getDeathNum(con)[0],getDeathNum(con)[1])
            print (getInjuredNum(con)[0],getInjuredNum(con)[1])
#             print getDegreeOfPL(con)
#             if getCompensation(con) != 'unknown':
#                 print file_list[index],index
#                 print getCompensation(con)
#             print getUnderstanding(con)
#             print getRes(con)
#              for each in getRes(con):
#                  print each
#             print getAbscond(con)
#             print getAbscondDeath(con)