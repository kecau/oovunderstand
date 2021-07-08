#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import jieba.posseg as pseg
from tqdm import tqdm
a=[]
cou=[]
with open('new_word_found_result.csv', 'r') as f:
    for line in f.readlines():
        a.append(line.strip('\n'))
with open('Chinese_Names_Corpus.txt', 'r') as f:
    for line in f.readlines():
        cou.append(line.strip('\n'))
def isname(single_word_string):
    pair_word_list = pseg.lcut(single_word_string)
    for eve_word, cixing in pair_word_list:
        if cixing == "nr":
            return 1
    return 0

renm=[]
for d in range(len(a)):
        e=isname(a[d])
        if e==1:
                renm.append(a[d])

qx=['女士','男士','人员','某']
for i in range(len(qx)):
    for j in range(len(a)):
        if a[j].find(qx[i]) == -1:
            continue
        b=a[j]
        renm.append(b)
for v in tqdm(range(len(cou))):
    for j in range(len(a)):
        if a[j].find(cou[i]) == -1:
            continue
        b=a[j]
        renm.append(b)
jieguo=[]
for i in renm:
    if not i in jieguo:
        jieguo.append(i)
with open("./found_name.txt", 'w') as fw:
        for r in tqdm(jieguo):
                fw.write(r+"\n") 