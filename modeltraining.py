#encoding=utf-8
from gensim.models import word2vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
f = open('word_split_result2.txt')

sentences=word2vec.Text8Corpus('word_split_result2.txt')
model=word2vec.Word2Vec(sentences,sg=1,vector_size=200,min_count=3,window=50,workers=5)
model.save("word2vec.model")
#y2=model.wv.similarity(u"湘西", u"湖南")
#print(y2)
content=[]

with open('cleaned_oov.csv', 'r') as f:
    for line in f.readlines():
        content.append(line.strip('\n'))
for a in content:
    print(a)
    for i in model.wv.most_similar(a,topn=20):
        print (i)
