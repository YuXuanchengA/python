
## normal pinyin

- init__.py
- pinyin.py 汉字转拼音
- zh.py 繁体转简体
- pinyin.txt
- stopwords.txt


```python
from snownlp import SnowNLP
s = SnowNLP(u'这个东西真心很赞')
s.pinyin
```




    ['zhe', 'ge', 'dong', 'xi', 'zhen', 'xin', 'hen', 'zan']




```python
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

import codecs
class Trie(object):  #字典树

    def __init__(self):
        self.d = {}  #第一个方法：定义字典

    def insert(self, key, value): #在字典中插入键值对
        now = self.d
        for k in key:
            if not k in now:  #判断是否已经存在
                now[k] = {}
            now = now[k]
        now['value'] = value

    def find(self, text, start=0): #顺序查找（二叉树从根节点开始遍历）
        now = self.d
        n = len(text)
        ret = None
        pos = start
        while pos < n: #0~n
            if text[pos] in now:
                now = now[text[pos]]
            else:
                return ret  #没有找到则返回none
            if 'value' in now:
                ret = (text[start:pos+1], now['value'])
            pos += 1
        return ret

    def translate(self, text, with_not_found=True): #转换成对应的value
        n = len(text)
        pos = 0
        ret = [] #return列表
        while pos < n:
            now = self.d
            if text[pos] in now:
                tmp = self.find(text, pos)
                if tmp: #如果找到了
                    ret.append(tmp[1])
                    pos += len(tmp[0])
                    continue  
            if with_not_found: #如果没找到
                ret.append(text[pos])
            pos += 1
        return ret
    
    
tree = Trie()
tree.insert('你','ni')
tree.d
```




    {'你': {'value': 'ni'}}




```python
tree.insert('我','wo')
tree.d
```




    {'你': {'value': 'ni'}, '我': {'value': 'wo'}}




```python
tree.insert('他','ta')
tree.d
```




    {'他': {'value': 'ta'}, '你': {'value': 'ni'}, '我': {'value': 'wo'}}




```python
tree.find('你')
```




    ('你', 'ni')




```python
tree.find('他')
```




    ('他', 'ta')




```python
tree.translate('他它')
```




    ['ta', '它']




```python
# pinyin.py
# from __future__ import unicode_literals
# 
# import codecs #用于编码转换的模块
# 
# from ..utils.trie import Trie  #调用上上级目录下的utils的trie
# 
class PinYin(object):
    
    def __init__(self, fname):
        self.handle = Trie() #定义一个Trie对象
        fr = codecs.open(fname, 'r', 'utf-8')
        for line in fr:
            words = line.split() #split
            self.handle.insert(words[0], words[1:])
        fr.close()

    def get(self, text):
        ret = []
        for i in self.handle.translate(text):
            if isinstance(i, list) or isinstance(i, tuple): #isinstance是否为某种类型 ？
                ret = ret + i
            else:
                ret.append(i)
        return ret
    
    
hanzi = PinYin('test.txt')
hanzi.get('今天你')
```




    ['jin', 'tian', '你']




```python
#split()

a = '今天 天气不好' #split( ) 按照空格切分
b = a.split()
b
```




    ['今天', '天气不好']




```python
import re
import os

# stop_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
#                        'stopwords.txt')
# pinyin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
#                        'pinyin.txt')
# stop = set()
# fr = codecs.open(stop_path, 'r', 'utf-8')
# for word in fr:
#    stop.add(word.strip())
# fr.close()
pin = PinYin('pinyin.txt')
re_zh = re.compile('([\u4E00-\u9FA5]+)')


# def filter_stop(words):
#    return list(filter(lambda x: x not in stop, words))


# def zh2hans(sent):
#    return zh.transfer(sent)


def get_sentences(doc):
    line_break = re.compile('[\r\n]')
    delimiter = re.compile('[，。？！；]
    sentences = []
    for line in line_break.split(doc):
        line = line.strip()
        if not line:
            continue
        for sent in delimiter.split(line):
            sent = sent.strip()
            if not sent:
                continue
            sentences.append(sent)
    return sentences


def get_pinyin(sentence):
    ret = []
    for s in re_zh.split(sentence):
        s = s.strip()
        if not s:
            continue
        if re_zh.match(s):
            ret += pin.get(s)
        else:
            for word in s.split():
                word = word.strip()
                if word:
                    ret.append(word)
    return ret


get_pinyin('我不喜欢学编程')
```




    ['wo', 'bu', 'xi', 'huan', 'xue', 'bian', 'cheng']




```python
# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
str = "不喜欢学习"
print (str.strip( '不' )) 
```

    喜欢学习
    


```python
# -*- coding: utf-8 -*-
# from __future__ import print_function
# from __future__ import unicode_literals
# 
# from ..utils.trie import Trie

zh2hans = {               #定义字典
    '顯著': '显著',
    '土著': '土著',
    '印表機': '打印机',
    '說明檔案': '帮助文件',
    "瀋": "沈",
    "畫": "划",
    "鍾": "钟",
    "拿破崙": "拿破仑",
    "布殊": "布什",
    "布希": "布什",
    "柯林頓": "克林顿",
    "克林頓": "克林顿",
    "薩達姆": "萨达姆",
    "海珊": "萨达姆",
    "梵谷": "凡高",
    "大衛碧咸": "大卫·贝克汉姆",
    "米高奧雲": "迈克尔·欧文",
    "卡佩雅蒂": "珍妮弗·卡普里亚蒂",
    "沙芬": "马拉特·萨芬",
    "舒麥加": "迈克尔·舒马赫",
    "希特拉": "希特勒",
    "黛安娜": "戴安娜",
    "希拉": "赫拉",
}

handle = Trie()
for k, v in zh2hans.items(): #item返回键值对
    handle.insert(k, v)


def transfer(sentence):
    ret = handle.translate(sentence) #转换成value
    return ''.join(ret)

print(transfer('克林頓'))
```

    克林顿
    


```python
# stop_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
#                        'stopwords.txt')
# pinyin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
#                        'pinyin.txt')
# stop = set()
# fr = codecs.open(stop_path, 'r', 'utf-8')
# for word in fr:
#    stop.add(word.strip())
# fr.close()
# pin = PinYin('pinyin.txt')
# re_zh = re.compile('([\u4E00-\u9FA5]+)')


# def filter_stop(words):
#    return list(filter(lambda x: x not in stop, words))


def zh2hans(sent):
    return zh.transfer(sent)


def get_sentences(doc):
    line_break = re.compile('[\r\n]')
    delimiter = re.compile('[，。？！；]')
    sentences = []
    for line in line_break.split(doc):
        line = line.strip()
        if not line:
            continue
        for sent in delimiter.split(line):
            sent = sent.strip()
            if not sent:
                continue
            sentences.append(sent)
    return sentences


# def get_pinyin(sentence):
#     ret = []
#     for s in re_zh.split(sentence):
#         s = s.strip()
#         if not s:
#             continue
#         if re_zh.match(s):
#             ret += pin.get(s)
#         else:
#             for word in s.split():
#                 word = word.strip()
#                 if word:
#                     ret.append(word)
#     return ret

get_sentences('今天不想学习。明天也不想学习。') 
```




    ['今天不想学习', '明天也不想学习']


