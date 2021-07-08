#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from tqdm import tqdm
import re
import jieba
import jieba.posseg as pseg
a=[]
with open('new_word_found_result.csv', 'r') as f:
    for line in f.readlines():
        a.append(line.strip('\n'))
def isjigou(single_word_string):
    pair_word_list = pseg.lcut(single_word_string)
    for eve_word, cixing in pair_word_list:
        if cixing == "nt":
            return 1
    return 0
c=['委','局','电视','新闻','院','日报','政府','厅','议会','基金会','视频','时报','晨报','快报','青年报','小组']
jigou=[]
for i in range(len(c)):
    for j in range(len(a)):
        if a[j].find(c[i]) == -1:
            continue
        b=a[j]
        jigou.append(b)
for d in range(len(a)):
        e=isjigou(a[d])
        if e==1:
                jigou.append(a[d])
jieguo=[]
for i in jigou:
    if not i in jigou:
        jieguo.append(i)
with open("./found_org.txt", 'w') as fw:
        for r in tqdm(jigou):
                fw.write(r+"\n") 
