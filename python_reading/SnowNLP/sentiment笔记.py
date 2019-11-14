
# coding: utf-8

# ## sentiment情感分析
# 
# 判断一句话是积极态度还是消极态度
# 
# ## sentiment文件夹包含：
# 
# - neg.txt （存储消极/负样本，用于训练新模型）
# - pos.txt （存储积极/正样本，用于训练新模型）
# - sentiment.marshal （存储新模型）
# - sentiment.marshal.3
# 
# ## 调用了贝叶斯模型
# 
# 关于贝叶斯模型 https://blog.csdn.net/google19890102/article/details/80091502

# In[ ]:


#这是sentiment下的__init__.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import codecs

from .. import normal
from .. import seg #调用分词
from ..classification.bayes import Bayes #调用Bayes，在classification下

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),  #所用模型的路径，如果要利用新模型需要更换路径
                         'sentiment.marshal')  


class Sentiment(object): #面向对象编程的写法，创建Sentiment类，定义类的方法

    def __init__(self):
        self.classifier = Bayes() #使用Bayes模型

    def save(self, fname, iszip=True): 
        self.classifier.save(fname, iszip) #保存最终的模型

    def load(self, fname=data_path, iszip=True): 
        self.classifier.load(fname, iszip) #加载样本

    # 分词及过滤（去停用词）    
    def handle(self, doc):
        words = seg.seg(doc) #分词
        words = normal.filter_stop(words) #去停用词
        return words #返回结果

    def train(self, neg_docs, pos_docs):  #训练模型
        data = []  #列表
        for sent in neg_docs:
            data.append([self.handle(sent), 'neg']) #读入负样本，加neg标签
            # 例如[ [['A','B' ...],'neg'] ,  [['C','D' ...],‘neg’] ........]
        for sent in pos_docs:
            data.append([self.handle(sent), 'pos']) #读入正样本，加pos标签
        self.classifier.train(data) #调用Bayes模型的训练方法

    # 调用Bayes的classify方法
    def classify(self, sent):  
        ret, prob = self.classifier.classify(self.handle(sent))
        if ret == 'pos':
            return prob  #如果是pos返回概率值
        return 1-prob #如果是neg减1返回消极概率值


classifier = Sentiment()
classifier.load()


def train(neg_file, pos_file):
    # 打开正负样本文件
    neg = codecs.open(neg_file, 'r', 'utf-8').readlines() 
    pos = codecs.open(pos_file, 'r', 'utf-8').readlines()
    neg_docs = []
    pos_docs = []
    
    #遍历样本，加入列表
    for line in neg:
        neg_docs.append(line.rstrip("\r\n"))
    for line in pos:
        pos_docs.append(line.rstrip("\r\n"))
    global classifier
    classifier = Sentiment()
    classifier.train(neg_docs, pos_docs)  #训练


def save(fname, iszip=True):
    classifier.save(fname, iszip) #保存


def load(fname, iszip=True):
    classifier.load(fname, iszip) #加载样本


def classify(sent):
    return classifier.classify(sent) #分类

