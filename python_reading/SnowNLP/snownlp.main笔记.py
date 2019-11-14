
# coding: utf-8

# In[1]:


from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞') #u存储为unicode格式

s.words #分词


# In[2]:


s.tags #词性标注


# In[4]:


list(s.tags) 


# In[3]:


s.sentiments    #情感分析 越接近1表示正面情绪，越接近0表示负面情绪


# In[5]:


s.pinyin #转换为拼音


# In[6]:


s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')

s.han #繁体转简体


# In[8]:


text = u'''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
'''

s = SnowNLP(text)

s.keywords(3) #提取3个关键词


# In[9]:


s.summary(3) #前3句文本概括


# In[10]:


s.sentences #分句（以逗号或句号为隔）


# In[11]:


s = SnowNLP([[u'这篇', u'文章'],
             [u'那篇', u'论文'],
             [u'这个']])
s.tf #term frequency 单个词频统计


# In[12]:


s.idf #Inverse Document Frequency


# In[13]:


s.sim([u'文章']) #计算相似度


# In[14]:


help(s.sim)

