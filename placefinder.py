import jieba.posseg as pseg
from tqdm import tqdm
a=[]
place=[]
with open('new_word_found_result.csv', 'r') as f:
    for line in f.readlines():
        a.append(line.strip('\n'))
with open('place.txt', 'r') as f:
    for line in f.readlines():
        place.append(line.strip('\n'))
jieguo=[]
for i in range(len(place)):
    for j in range(len(a)):
        if a[j].find(place[i]) == -1:
            continue
        b=a[j]
        jieguo.append(b)
with open("./found_place.txt", 'w') as fw:
        for r in tqdm(jieguo):
                fw.write(r+"\n") 