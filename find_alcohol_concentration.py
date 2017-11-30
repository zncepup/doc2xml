# coding=utf-8
import codecs
import sys
import os
import re

# pattern = re.compile(r'\d+[.]{0,1}\d+mg/\d+ml', re.I|re.M)
# pattern = re.compile(r'[0-9]+([.]{0,1}[0-9]+){0,1}mg[/,／,∕]100m[1,l]', re.I|re.M)
pattern = re.compile(r'[0-9]+([.]{0,1}[0-9]+){0,1}mg.{1}100m.{1}', re.I | re.M)


def getListFiles(path):
    ret = []
    for root, dirs, files in os.walk(path):
        for filespath in files:
            ret.append(os.path.join(root, filespath))
    return ret


def findWordInFile(filename):

    match = pattern.search(filename)
    if match:
        # print(filename + "\t" + match.group())
        return match.group()
    return 'unknown'


if __name__ == '__main__':
    ret = getListFiles("/media/zp/新加卷/weixianjiashi-all")
    for each in ret:
        print(findWordInFile(each))
