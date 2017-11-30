import numpy as np
from collections import OrderedDict as dict
def substrinlist(str,list):
    for x in list:
        index=str.find(x)
        if index!=-1:
            return 1
    return 0



def search(doc,che):
    # with open(file,'r',encoding='utf8') as f:
    #     doc=f.read()
    with open(che,'r',encoding='utf8') as f:
        vocab_che=f.read()
        voca=vocab_che.split("///")
    zhonglei=[]
    bool=np.zeros([len(voca)],dtype=np.int)
    for x in range(len(voca)):
        a1=voca[x].split()
        zhonglei.append(a1[0])
        bool[x]=substrinlist(doc,a1[1:])
    dictionary=dict(zip(zhonglei,bool))
    # print(zhonglei,bool)
    return dictionary
# a=cheliang('H:\weixianjiashi-henan\(2015-06-25) 张某某危险驾驶一案一审刑事判决书.txt','che.txt')
# print(a)

