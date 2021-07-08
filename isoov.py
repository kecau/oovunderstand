#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pymysql
import requests
import json
import time, datetime
import urllib.request, urllib.parse, urllib.error
import ssl
import os
from urllib.parse import unquote
from bs4 import BeautifulSoup
from lxml import html
import xml.etree.ElementTree as ET
import pandas as pd
from tqdm import tqdm
content = []
newword=[]
errorwd=[]
etree = html.etree


with open('cleaned_oov.txt', 'r') as f:
    for line in f.readlines():
        content.append(line.strip('\n'))

b=0
for i in tqdm(content):
    response = requests.get('https://dict.baidu.com/s?wd='+i+'&from=poem')
    try:
        a=response.content.decode('utf-8')
        etree_html = etree.HTML(a)
        qz=etree_html.xpath('//*[@id="basicmean"]/text()')

    except:
        errorwd.append(i)
        qz=['词汇']
    d=len(qz)
    if d==0:
        newword.append(i)
for i in newword:
    print(i)