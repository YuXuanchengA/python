

```python
from snownlp import SnowNLP

s = SnowNLP(u'这个东西真心很赞') #u存储为unicode格式

s.words #分词
```




    ['这个', '东西', '真心', '很', '赞']




```python
s.tags #词性标注
```




    <zip at 0xbec0508>




```python
list(s.tags) 
```




    [('这个', 'r'), ('东西', 'n'), ('真心', 'd'), ('很', 'd'), ('赞', 'Vg')]




```python
s.sentiments    #情感分析 越接近1表示正面情绪，越接近0表示负面情绪
```




    0.9769551298267365




```python
s.pinyin #转换为拼音
```




    ['zhe', 'ge', 'dong', 'xi', 'zhen', 'xin', 'hen', 'zan']




```python
s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')

s.han #繁体转简体
```




    '「繁体字」「繁体中文」的叫法在台湾亦很常见。'




```python
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
```




    ['语言', '自然', '计算机']




```python
s.summary(3) #前3句文本概括
```




    ['因而它是计算机科学的一部分',
     '自然语言处理是计算机科学领域与人工智能领域中的一个重要方向',
     '自然语言处理是一门融语言学、计算机科学、数学于一体的科学']




```python
s.sentences #分句（以逗号或句号为隔）
```




    ['自然语言处理是计算机科学领域与人工智能领域中的一个重要方向',
     '它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法',
     '自然语言处理是一门融语言学、计算机科学、数学于一体的科学',
     '因此',
     '这一领域的研究将涉及自然语言',
     '即人们日常使用的语言',
     '所以它与语言学的研究有着密切的联系',
     '但又有重要的区别',
     '自然语言处理并不是一般地研究自然语言',
     '而在于研制能有效地实现自然语言通信的计算机系统',
     '特别是其中的软件系统',
     '因而它是计算机科学的一部分']




```python
s = SnowNLP([[u'这篇', u'文章'],
             [u'那篇', u'论文'],
             [u'这个']])
s.tf #term frequency 单个词频统计
```




    [{'文章': 1, '这篇': 1}, {'论文': 1, '那篇': 1}, {'这个': 1}]




```python
s.idf #Inverse Document Frequency
```




    {'文章': 0.5108256237659907,
     '论文': 0.5108256237659907,
     '这个': 0.5108256237659907,
     '这篇': 0.5108256237659907,
     '那篇': 0.5108256237659907}




```python
s.sim([u'文章']) #计算相似度
```




    [0.4686473612532025, 0, 0]




```python
help(s.sim)
```

    Help on method sim in module snownlp:
    
    sim(doc) method of snownlp.SnowNLP instance
    
    
