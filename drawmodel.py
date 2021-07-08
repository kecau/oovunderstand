import sys, os
from gensim.models import Word2Vec
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from matplotlib import pyplot
import tqdm as tqdm
model = Word2Vec.load('a.model')
words=[]
with open('SIMword.txt', 'r') as f:
    for line in f.readlines():
        words.append(line.strip('\n'))
# 基于2d PCA拟合数据
X = model.wv[model.wv.index_to_key]
pca = PCA(n_components=2)
result_pca = pca.fit_transform(X)
result = TSNE(n_components=2).fit_transform(result_pca)
# 可视化展示
pyplot.xticks([]) 
pyplot.yticks([]) 
pyplot.rcParams['font.sans-serif'] = ['Arial Unicode', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
pyplot.rcParams['font.size'] = 8  # 字体大小
pyplot.rcParams['axes.unicode_minus'] = False  # 正常显示负号
pyplot.figure(figsize=(20,20))
pyplot.scatter(result[:, 0], result[:, 1],color='#86C166')
#words = list(model.wv.index_to_key)

for i, word in enumerate(words):
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.savefig('耗子尾汁skip.eps',format='eps',dpi=600)


