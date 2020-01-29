import json
import os
import re

import numpy as np
from gensim.models import word2vec
from sklearn.model_selection import train_test_split  # 将数据分为测试集和训练集
from sklearn.naive_bayes import MultinomialNB  # 朴素贝叶斯分类器
from sklearn.preprocessing.label import LabelEncoder  # 对标签进行数字化编码
from sklearn import metrics  # 检测训练精度

from sklearn.feature_extraction.text import TfidfTransformer  # tf-idf值
from sklearn.feature_extraction.text import CountVectorizer  # 词频矩阵
base_dir = r'C:\Users\surface\Desktop\nlp-sort'

spider_base = os.path.join(base_dir, r'spider/spiders')

# inp为输入语料, outp1为输出模型, outp2为vector格式的模型
inp = 'corpusSegDone_1.txt'
out_model = 'corpusSegDone_1.model'
out_vector = 'corpusSegDone_1.vector'

# 用numpy的add、divide方法形成全文词向量
def getVector_v4(cutWords, word2vec_model):
    i = 0
    index2word_set = set(word2vec_model.wv.index2word)
    article_vector = np.zeros((word2vec_model.layer1_size))
    for cutWord in cutWords:
        if cutWord in index2word_set:
            article_vector = np.add(article_vector, word2vec_model.wv[cutWord])
            i += 1
    cutWord_vector = np.divide(article_vector, i)
    return cutWord_vector

# 原文链接：https://www.cnblogs.com/always-fight/p/10159547.html

count = 0
dic = {}
X = []  # 单词
Y = []  # 标签

# 读取json文件（爬取的文本是英文，省去分词）
for label in os.listdir(spider_base):
    abs_path = os.path.join(spider_base, label)
    if os.path.isdir(abs_path):
        article_list = []
        for article_file in os.listdir(abs_path):
            label_path = os.path.join(abs_path, article_file)
            if article_file.endswith('.json') and os.path.isfile(label_path):
                with open(label_path, 'r', encoding='utf-8') as f:
                    json_file = json.load(f)
                    for k, v in json_file.items():
                        words = re.findall('[a-zA-Z0-9]+', v)
                article_list.append(words)
                X.append(words)
                Y.append(label)

        if article_list:
            dic[label] = article_list  # 字典 key标签 value文本

dic
encoder = LabelEncoder()
encoder.fit_transform(Y)

values = []
values.extend(dic.values())
all_sentences = []
for each_label in values:
    for each_article in each_label:
        all_sentences.append(' '.join(each_article))

# 装载语料
sentences = word2vec.Text8Corpus(all_sentences)

# 写入corpusSegDone_1.txt
with open(inp, 'w') as fin:
    fin.write('\n'.join(all_sentences))

try:
    word2vec.Word2Vec.load(out_model)
except:
    # 训练skip-gram模型
    model = word2vec.Word2Vec(sentences, size=50, window=5, min_count=5)

    # 保存模型
    model.save(out_model)
    # 保存词向量
    model.wv.save_word2vec_format(out_vector, binary=False)
# 参考
# 原文链接：https://blog.csdn.net/lilong117194/article/details/82849054
# model = word2vec.Word2Vec(sentences, min_count=3, size=50, window=5, workers=4)

# 获得词频的稀疏矩阵表示
words = CountVectorizer().fit_transform(all_sentences)
# 分割训练数据和测试数据
train_X, test_X, train_y, test_y = train_test_split(words, Y)
# 建立tf-idf词频权重矩阵
tfidf = TfidfTransformer().fit_transform(words)
# 对训练数据进行分类
clf = MultinomialNB(alpha=0.001).fit(train_X, train_y)

# 参考
# 原文链接：https://blog.csdn.net/cindy407/article/details/93789415
# 原文链接：https://blog.csdn.net/cindy407/article/details/93777413

# 预测分类结果
predicted = clf.predict(test_X)

print(predicted)
print("预测完毕!!!")

# 计算分类精度：
def metrics_result(actual, predict):
    print('精度:{0:.3f}'.format(metrics.precision_score(actual, predict, average='weighted')))
    print('召回:{0:0.3f}'.format(metrics.recall_score(actual, predict, average='weighted')))
    print('f1-score:{0:.3f}'.format(metrics.f1_score(actual, predict, average='weighted')))


metrics_result(test_y, predicted)
