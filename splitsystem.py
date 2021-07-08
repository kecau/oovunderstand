import jieba
from tqdm import tqdm
import emoji
import re
def remove_emoji(desstr, restr=''):
    try:
        str = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        str = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return str.sub(restr, desstr)
res=[]
a=[]
stopword=[]
file_userdict = 'common.txt'
jieba.load_userdict(file_userdict)
with open('1618051664.csv', 'r') as f:
        for line in tqdm(f.readlines()):
            res.append(line.strip('\n'))
with open('sto.txt', 'r') as f:
        for line in f.readlines():
            stopword.append(line.strip('\n'))
for i in tqdm(res):
    seg_list = jieba.cut(i)
    for word in seg_list:
        if word not in stopword:
            a.append(remove_emoji("".join(word)))
with open("./word_split_result2.txt", 'w') as fw:
        for r in a:
                fw.write(r+" ")#+"\t"+str(r[1])+"\n")
