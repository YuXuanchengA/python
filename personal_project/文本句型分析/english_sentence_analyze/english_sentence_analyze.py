
# coding: utf-8

# In[67]:


import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import nltk

# 分句
def sents_tokenize(content):
    sent_tokenize_list = sent_tokenize(content)
    return sent_tokenize_list

def sents_analyze(sents):
    sents_pattern = []
    i = 0
    for sent in sents:
        i += 1
        # 分词
        words = sent.lower() #全部转换为小写
        words = word_tokenize(words)
        word_l = []
        for w in words:
            word_l.append(w)
        #print(word_l)
        # 词性标注
        # pos = nltk.pos_tag(words)
        # 判断
        
        #compound sentence or complex sentence
        if ('because' in word_l):
            sents_pattern.append('原因状语从句')
        elif ('and' in word_l) or ('or' in word_l ) or ('but' in word_l):
            sents_pattern.append('并列句')
        elif ('if' in word_l) or ('unless' in word_l):
            sents_pattern.append('条件状语从句')
        elif ('though' in word_l) or ('although' in word_l):
            sents_pattern.append('让步状语从句')
        elif word_l[-1] == '!' :
            sents_pattern.append('感叹句')
        elif word_l[-1] == '?' :
            sents_pattern.append('疑问句')
            
        # 其他
        else:
            sents_pattern.append('陈述句')
        
        if i == 5000:
            break
    return sents_pattern
            
#main
with open('Pullman, Philip - His Dark Materials, Book 2.txt', 'r', encoding='utf-8') as f:
    content = f.read().replace('\n', '')
    # 去除对话引号，不影响判断
    content = content.replace('"', '')
    
sents = sents_tokenize(content)
patterns = sents_analyze(sents)
with open('Pullman, Philip - His Dark Materials, Book 2_analyze.txt', 'w', encoding='utf-8') as f:
    for pattern, sent in zip(patterns,sents):
        f.write('{}\t{}\n'.format(pattern, sent))


# In[68]:


# 准确率判断
import random
test = []
test_pattern = []
test_sent = []

for i in range(200) :
    num = random.randint(0,4999) # 闭区间
    if(num not in test):
        test.append(num)
        test_pattern.append(patterns[num])
        test_sent.append(sents[num])

# 将抽取的200个句子存入文件            
with open('measurement_english.txt', 'w', encoding='utf-8') as f: 
    for pattern, sent in zip(test_pattern,test_sent):
        f.write('{}\t{}\n'.format(pattern, sent))


# In[ ]:


# 人工判断准确率
# 错误个数：并列句：23；感叹句：1
# 准确率：76%

