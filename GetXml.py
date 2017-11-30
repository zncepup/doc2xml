import myxml
import wenhuashuiping
import birthdandage
import searchkeyword
import os.path
import getInfo,getResult
import getHarm
import find_alcohol_concentration
def getxml(file_name):
    with open(file_name,'r',encoding='utf8') as f:
        f=f.read()
        ff = getResult.preprocess(f)
    _,fname=os.path.split(file_name)
    generator=myxml.XMLGenerator(fname.split('.')[0]+'.xml')

    trial=generator.createNode('Trial')
    generator.addNode(trial)
    #文档信息
    # 文档信息

    trialInfo = generator.createNode("TrialInfo")
    generator.addNode(trialInfo, trial)
    # 判决书文号
    awardID = generator.createNode("AwardID")
    generator.addNode(awardID, trialInfo)
    # 起诉书文号
    indictmentID = generator.createNode("IndictmentID")
    generator.addNode(indictmentID, trialInfo)
    # 地区：省/市/县（区）
    area = generator.createNode("Area")
    generator.addNode(area, trialInfo)
    province = generator.createNode("Province")
    generator.addNode(province, area)
    city = generator.createNode("City")
    generator.addNode(city, area)
    countyDistrict = generator.createNode("CountyDistrict")
    generator.addNode(countyDistrict, area)
    # 审判时间
    trialTime = generator.createNode("TrialTime")
    generator.addNode(trialTime, trialInfo)
    # 审判员
    judge = generator.createNode("Judge")
    generator.addNode(judge, trialInfo)

    #主体（被告人）
    node_defendant=generator.createNode('Defendant')
    node_status=generator.createNode('Status')
    node_educationalbackground=generator.createNode('EducationalBackground')
    node_age=generator.createNode('IncidentAge')
    node_birthday=generator.createNode('Birthday')
    node_pedigree=generator.createNode('Pedigree')
    node_attitude=generator.createNode('Attitude')
    generator.addNode(node_defendant,trial)
    generator.addNode(node_status,node_defendant)
    generator.addNode(node_educationalbackground,node_defendant)
    generator.addNode(node_age,node_defendant)
    generator.addNode(node_birthday,node_defendant)
    generator.addNode(node_pedigree,node_defendant)
    generator.addNode(node_attitude,node_defendant)
    #身份
    status=wenhuashuiping.status(f)
    generator.setNodeValue(node_status,status)
    #学历
    educationalbackground=wenhuashuiping.wenhua(f)
    generator.setNodeValue(node_educationalbackground,educationalbackground)
    #年龄,生日
    ageandbirth=birthdandage.birthandage(f)
    generator.setNodeValue(node_age,str(ageandbirth['案发年龄']))
    birthday=str(ageandbirth['年'])+'-'+str(ageandbirth['月'])+'-'+str(ageandbirth['日'])
    generator.setNodeValue(node_birthday,birthday)
    generator.setNodeAttr(node_age,'remarks','0=null')
    generator.setNodeAttr(node_birthday, 'remarks', '0=null')
    #前科累犯
    pedigree=searchkeyword.search(f,'pedigree.txt')
    generator.setNodeAttr(node_pedigree,'前科',str(pedigree['前科']))
    generator.setNodeAttr(node_pedigree, '累犯', str(pedigree['累犯']))
    #态度

    attitude=searchkeyword.search(ff,'attitude.txt')
    generator.setNodeAttr(node_attitude,'自首',str(attitude['自首']))
    generator.setNodeAttr(node_attitude, '坦白', str(attitude['坦白']))
    generator.setNodeAttr(node_attitude, '立功', str(attitude['立功']))
    generator.setNodeAttr(node_attitude, '认罪', str(attitude['认罪']))
    generator.setNodeAttr(node_attitude, '悔罪', str(attitude['悔罪']))


    #客观方面
    node_objectiveaspects=generator.createNode('ObjectiveAspects')
    node_vehicle=generator.createNode('Vehicle')
    node_road=generator.createNode('Road')
    node_plot=generator.createNode('Plot')
    node_raeing=generator.createNode('Reaing')
    node_drunkdriving=generator.createNode('DrunkDriving')
    node_alcohol = generator.createNode('Alcohol')
    node_overspeed=generator.createNode('OverSpeed')
    node_overload=generator.createNode('OverLoad')
    node_dangerouscargo=generator.createNode('DangerousCargo')
    generator.addNode(node_objectiveaspects,trial)
    generator.addNode(node_vehicle,node_objectiveaspects)
    generator.addNode(node_road,node_objectiveaspects)
    generator.addNode(node_plot,node_objectiveaspects)
    generator.addNode(node_raeing,node_plot)
    generator.addNode(node_drunkdriving,node_plot)
    generator.addNode(node_alcohol, node_plot)
    generator.addNode(node_overspeed,node_plot)
    generator.addNode(node_overload,node_plot)
    generator.addNode(node_dangerouscargo,node_plot)

    #车类型
    vehicle=searchkeyword.search(f,'che.txt')
    generator.setNodeAttr(node_vehicle,'客车',str(vehicle['客车']))
    generator.setNodeAttr(node_vehicle, '货车', str(vehicle['货车']))
    generator.setNodeAttr(node_vehicle, '摩托车', str(vehicle['摩托车']))
    generator.setNodeAttr(node_vehicle, '轿车', str(vehicle['轿车']))
    generator.setNodeAttr(node_vehicle , '电动车-机动', str(vehicle['电动车（机动）']))
    generator.setNodeAttr(node_vehicle , '其他机动车辆', str(vehicle['其他机动车辆']))
    generator.setNodeAttr(node_vehicle , '非机动车', str(vehicle['非机动车']))
    generator.setNodeAttr(node_vehicle, '报废车', str(vehicle['报废车']))
    generator.setNodeAttr(node_vehicle, '套牌车', str(vehicle['套牌车']))
    generator.setNodeAttr(node_plot, '无证驾驶', str(vehicle['无证驾驶']))
    generator.setNodeAttr(node_plot, '无牌驾驶', str(vehicle['无牌驾驶']))



    #道路类型

    #情节
    #追逐竞驶
    #醉驾酒驾
    drunk=searchkeyword.search(f,'drunk.txt')
    generator.setNodeAttr(node_drunkdriving,'酒驾',str(drunk['酒驾']))
    alcohol=find_alcohol_concentration.findWordInFile(f)
    generator.setNodeAttr(node_alcohol,'酒精含量',str(alcohol))
    #超速超载
    over=searchkeyword.search(f,'overloadspeed.txt')
    generator.setNodeValue(node_overspeed,str(over['超速']))
    generator.setNodeValue(node_overload,str(over['超载']))
    #危险品运输


    # 审判结果
    trialResult = generator.createNode("TrialResult")
    generator.addNode(trialResult, trial)
    # 主刑
    principalPenalty = generator.createNode("PrincipalPenalty")
    generator.addNode(principalPenalty, trialResult)
    surveillans = generator.createNode("Surveillans")  # 管制
    generator.addNode(surveillans, principalPenalty)
    surveillansDuration = generator.createNode("SurveillansDuration")
    generator.addNode(surveillansDuration, surveillans)
    dentention = generator.createNode("Dentention")  # 拘役
    generator.addNode(dentention, principalPenalty)
    dententionDuration = generator.createNode("DententionDuration")
    generator.addNode(dententionDuration, dentention)
    fixtedTerm = generator.createNode("FixtedTerm")  # 有期徒刑
    generator.addNode(fixtedTerm, principalPenalty)
    fixtedTermDuration = generator.createNode("FixtedTermDuration")
    generator.addNode(fixtedTermDuration, fixtedTerm)
    unfixtedTerm = generator.createNode("UnfixtedTerm")  # 无期徒刑
    generator.addNode(unfixtedTerm, principalPenalty)
    death = generator.createNode("Death")  # 死刑/死缓
    generator.addNode(death, principalPenalty)
    deathDuration = generator.createNode("deathDuration")
    generator.addNode(deathDuration, death)
    lifeImprisonment = generator.createNode("LifeImprisonment")  # 终身监禁
    generator.addNode(lifeImprisonment, principalPenalty)
    # 附加刑
    accessionPunishment = generator.createNode("AccessionPunishment")
    generator.addNode(accessionPunishment, trialResult)
    fine = generator.createNode("Fine")  # 罚金
    generator.addNode(fine, accessionPunishment)
    amount = generator.createNode("Amount")  # 罚金数额
    generator.addNode(amount, fine)
    confiscationOfProperty = generator.createNode("ConfiscationOfProperty")  # 没收财产
    generator.addNode(confiscationOfProperty, accessionPunishment)
    deprivalOfPoliticalRight = generator.createNode("DeprivalOfPoliticalRight")  # 剥夺政治权利
    generator.addNode(deprivalOfPoliticalRight, accessionPunishment)
    deportation = generator.createNode("Deportation")  # 驱逐出境
    generator.addNode(deportation, accessionPunishment)
    captureIllegalProperty = generator.createNode("CaptureIllegalProperty")  # 收缴非法财产
    generator.addNode(captureIllegalProperty, accessionPunishment)

    #yzp

    con=f
    Area = getInfo.getArea(con)
    generator.setNodeValue(province, Area[0])
    generator.setNodeValue(city, Area[1])
    generator.setNodeValue(countyDistrict, Area[2])

    AwardID = getInfo.getAwardID(con)
    generator.setNodeValue(awardID, AwardID)

    IndictmentID = getInfo.getIndictmentID(con)
    generator.setNodeValue(indictmentID, IndictmentID)

    Judge = getInfo.getJudge(con)
    generator.setNodeValue(judge, Judge)

    TrialTime = getInfo.getTrialTime(con)
    generator.setNodeValue(trialTime, TrialTime)

    _,time,huanqi = getResult.getDentention(con)
    punish=str(time)+'/'+str(huanqi)
    generator.setNodeValue(dententionDuration, punish)  ##
    _,fine = getResult.getFine(con)
    generator.setNodeValue(amount, str(fine))

    _,fixd_time,huanqi_fixd=getResult.getFixtedTerm(con)
    fixd=str(fixd_time)+'/'+str(huanqi_fixd)
    generator.setNodeValue(fixtedTermDuration,fixd)

    _,surve_time,huanqi_surve=getResult.getSurveillans(con)
    surve=str(surve_time)+'/'+str(huanqi_surve)
    generator.setNodeValue(surveillansDuration,surve)



    # 危害结果
    harmfulConse = generator.createNode("HarmfulConsequences")
    generator.addNode(harmfulConse, trial)
    # 人员伤亡
    casualties = generator.createNode("Casualties")
    generator.addNode(casualties, harmfulConse)
    deathNum = generator.createNode("DeathNum")  # 死亡人数
    generator.addNode(deathNum, casualties)
    injuredNum = generator.createNode("InjuredNum")  # 重伤人数
    generator.addNode(injuredNum, casualties)
    # 财产损失
    propertyLosses = generator.createNode("PropertyLosses")
    generator.addNode(propertyLosses, harmfulConse)
    degreeOfPropertyLosses = generator.createNode("DegreeOfPropertyLosses")  # 财产损失程度
    generator.addNode(degreeOfPropertyLosses, propertyLosses)
    amountOfCompensation = generator.createNode("AmountOfCompensation")  # 赔偿数额
    generator.addNode(amountOfCompensation, propertyLosses)
    victimUnderstanding = generator.createNode("VictimUnderstanding")  # 被害人谅解
    generator.addNode(victimUnderstanding, propertyLosses)
    # 责任认定
    confirmationOfRes = generator.createNode("confirmationOfResponsibility")
    generator.addNode(confirmationOfRes, harmfulConse)
    # 逃逸
    abscond = generator.createNode("Abscond")
    generator.addNode(abscond, harmfulConse)
    # 逃逸致人死亡
    deathCausedByAbscond = generator.createNode("DeathCausedByAbscond")
    generator.addNode(deathCausedByAbscond, harmfulConse)

    # 死亡人数
    _,DeathNum = getHarm.getDeathNum(con)
    generator.setNodeValue(deathNum, str(DeathNum))
    # 重伤人数
    _,InjuredNum = getHarm.getInjuredNum(con)
    generator.setNodeValue(injuredNum, str(InjuredNum))
    # 财产损失程度
    DegreeOfPropertyLosses = getHarm.getDegreeOfPL(con)
    generator.setNodeValue(degreeOfPropertyLosses, DegreeOfPropertyLosses)
    # 赔偿数额
    AmountOfCompensation = getHarm.getCompensation(con)
    generator.setNodeValue(amountOfCompensation, AmountOfCompensation)
    # 被害人谅解
    VictimUnderstanding = getHarm.getUnderstanding(con)
    generator.setNodeValue(victimUnderstanding, VictimUnderstanding)
    # 责任认定
    ConfirmationOfRes = getHarm.getRes(con)

    generator.setNodeValue(confirmationOfRes, str(ConfirmationOfRes))
    # 逃逸
    Abscond = getHarm.getAbscond(con)
    generator.setNodeValue(abscond, Abscond)
    # 逃逸致人死亡
    DeathCausedByAbscond = getHarm.getAbscondDeath(con)
    generator.setNodeValue(deathCausedByAbscond, DeathCausedByAbscond)



    # generator.setNodeValue(node_city,'shanghai')
    # generator.setNodeAttr(node_city,'a','2222')
    generator.genXml()
# getxml('H:\weixianjiashi-henan\(2015-06-25) 张某某危险驾驶一案一审刑事判决书.txt')

if __name__ == '__main__':
    getxml('/media/zp/新加卷/jiaotongzhaoshi-all/(2009-06-04) 赵京强交通肇事一案.txt')