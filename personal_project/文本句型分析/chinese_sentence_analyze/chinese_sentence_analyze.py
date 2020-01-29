
# coding: utf-8

# In[21]:


import re
import jieba
import jieba.posseg as pseg
import nltk

# 分句
# 参考链接：https://blog.csdn.net/zhuzuwei/article/details/80487032

def sents_tokenize(content):
    sentences = re.split('(。|！|\!|\.|？|\?)', content)  # 保留分割符
    new_sents = []
    for i in range(int(len(sentences)/2)):
        sent = sentences[2*i] + sentences[2*i+1]
        new_sents.append(sent)
    return new_sents

def sents_analyze(sents):
    sents_pattern = []
    i = 0
    for sent in sents:
        i += 1
        words = jieba.lcut(sent) # 返回列表
        # print(words)
        if words[-1] == '！':
            sents_pattern.append('感叹句')
        elif words[-1] == '？':
            sents_pattern.append('疑问句')
        elif '是' in words:
            sents_pattern.append('是字句')    
        elif '把' in words:
            sents_pattern.append('把字句')
        elif '被' in words:
            sents_pattern.append('被字句')
        else:
            sents_pattern.append('陈述句')
    
        if i == 5000:
            break
    return sents_pattern
            
#main
with open('The_three_body_problem_full.txt', 'r', encoding='utf-8') as f:
    content = f.read().replace('\n', '')
    # 去除对话引号，不影响判断
    content = content.replace('“', '')
    content = content.replace('”', '')
    
sents = sents_tokenize(content)
patterns = sents_analyze(sents)
with open('The_three_body_problem_analyze.txt', 'w', encoding='utf-8') as f:
    for pattern, sent in zip(patterns,sents):
        f.write('{}\t{}\n'.format(pattern, sent))


# In[34]:


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
with open('measurement_chinese.txt', 'w', encoding='utf-8') as f: 
    for pattern, sent in zip(test_pattern,test_sent):
        f.write('{}\t{}\n'.format(pattern, sent))


# In[ ]:


# 人工判断准确率
# 错误个数：把字句：1；是字句：7；被字句：2
# 准确率：95%

