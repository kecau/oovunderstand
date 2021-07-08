import re
import json
import requests
import tqdm as tqdm
import json
import jieba
from tqdm import tqdm
import emoji
import re
from gensim.models import word2vec
from sklearn.decomposition import PCA
from matplotlib import pyplot

# 基于 m.weibo.cn 抓取少量数据，无需登陆验证
url_template = "https://m.weibo.cn/api/container/getIndex?type=wb&queryVal={}&containerid=100103type=2%26q%3D{}&page={}"
herders={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML,like GeCKO) Chrome/46.0.2454.85 Safari/537.36 115Broswer/6.0.4',
    'Referer':'https://m.weibo.cn',
    'Connection':'keep-alive'}

def clean_text(text):
    """清除文本中的标签等信息"""
    dr = re.compile(r'(<)[^>]+>', re.S)
    dd = dr.sub('', text)
    dr = re.compile(r'#[^#]+#', re.S)
    dd = dr.sub('', dd)
    dr = re.compile(r'@[^ ]+ ', re.S)
    dd = dr.sub('', dd)
    return dd.strip()


def fetch_data(query_val, page_id):
    """抓取关键词某一页的数据"""
    resp = requests.get(url_template.format(query_val, query_val, page_id),headers=herders)
    card_group = json.loads(resp.text)['data']['cards'][0]['card_group']
    print('url：', resp.url, ' --- 条数:', len(card_group))

    mblogs = []  # 保存处理过的微博
    for card in card_group:
        mblog = card['mblog']
        blog = {'mid': mblog['id'],  # 微博id
                'text': clean_text(mblog['text']),  # 文本
                #'userid': str(mblog['user']['id']),  # 用户id
                #'username': mblog['user']['screen_name'],  # 用户名
                #'reposts_count': mblog['reposts_count'],  # 转发
               # 'comments_count': mblog['comments_count'],  # 评论
               # 'attitudes_count': mblog['attitudes_count']  # 点赞
                }
        mblogs.append(blog)
    return mblogs


def remove_duplication(mblogs):
    """根据微博的id对微博进行去重"""
    mid_set = {mblogs[0]['mid']}
    new_blogs = []
    for blog in mblogs[1:]:
        if blog['mid'] not in mid_set:
            new_blogs.append(blog)
            mid_set.add(blog['mid'])
    return new_blogs


def fetch_pages(query_val, page_num):
    """抓取关键词多页的数据"""
    mblogs = []
    for page_id in range(1 + page_num + 1):
        try:
            mblogs.extend(fetch_data(query_val, page_id))
        except Exception as e:
            print(e)

    print("去重前：", len(mblogs))
    mblogs = remove_duplication(mblogs)
    print("去重后：", len(mblogs))

    # 保存到 result.json 文件中
    fp = open('result_{}.json'.format(query_val), 'w', encoding='utf-8')
    json.dump(mblogs, fp, ensure_ascii=False, indent=4)
    print("已保存至 result_{}.json".format(query_val))
def remove_emoji(desstr, restr=''):
    try:
        str = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        str = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return str.sub(restr, desstr)



if __name__ == '__main__':
    word1=input()
    fetch_pages(word1, 50)
    res=[]
    f=open('result_'+word1+'是什么.json',encoding='utf-8')
    data=json.load(f)
    for dict_data in data:
        res.append(dict_data['text'])
    with open("test2.txt","a") as f:
        f.write(word1)
    a=[]
    stopword=[]
    file_userdict = 'test2.txt'
    #file_userdict = 'common.txt'
    jieba.load_userdict(file_userdict)
    with open('sto.txt', 'r') as f:
        for line in f.readlines():
            stopword.append(line.strip('\n'))
    for i in tqdm(res):
        seg_list = jieba.cut(i)
        for word in seg_list:
            if word not in stopword:
                a.append(remove_emoji("".join(word)))
        with open("./test.txt", 'w') as fw:
            for r in a:
                fw.write(r+" ")#+"\t"+str(r[1])+"\n")

    sentences=word2vec.Text8Corpus('test.txt')
    model=word2vec.Word2Vec(sentences,sg=0,vector_size=200,min_count=3,window=50,workers=5)
    model.save("a.model")
#y2=model.wv.similarity(u"湘西", u"湖南")
#print(y2)
    for i in model.wv.most_similar(word1,topn=20):
        print (i)

