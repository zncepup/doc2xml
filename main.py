import GetXml
import codecs
# -*- coding: utf-8 -*-
import searchkeyword
import os
import getResult
def file_name(file_dir):
    for root,dirs,files in os.walk(file_dir):
        return files

a=file_name(r'F:\jiaotongzhaoshi-all\jiaotongzhaoshi-all/')
i=0
for x in range(len(a)):
    i+=1
    j=0
    # try:
    #     f = r'/media/zp/新加卷/jiaotongzhaoshi-all/' + a[x]
    #     print(f, x)
    #     GetXml.getxml(f)
    #
    # except:
    #     continue
    f = r'F:\jiaotongzhaoshi-all\jiaotongzhaoshi-all/' + a[x]
    # f='F:\jiaotongzhaoshi-all\jiaotongzhaoshi-all/(2012-12-19) 被告人徐岗交通肇事一案.txt'
    # with codecs.open(f,'r','utf-8') as f:
    #     f=f.read()
    #     ped=searchkeyword.search(f,'pedigree.txt')
    #     if ped['前科']==1:
    #         print(ped['前科'])

    if x>-1:
        print(f, x)
        GetXml.getxml(f)


# with open(f) as ff:
        #     fff=ff.read()
        #     pedigree = fff.find('自asd')
        #     x=fff.find('危险品')
        #     if pedigree == -1 and x!=-1:
        #         print(fff)

