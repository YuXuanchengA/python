
# SnowNLP处理中文文本

###如何使用
- 导入snownlp模块
- 创建snownlp对象（方法：s = SnowNLP(u'text')，u'转成unicode编码）

###snownlp features
- 分词 s.words
- 词性标注 s.tags
- 情感分析 s.sentiments（返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪）
- 转换为拼音 s.pinyin
- 繁体转简体 s.han
- 提取关键词 s.keywords(3) #*提取3个关键词*
- 文本概括 s.summary
- 分句 s.sentences
- 统计单个词频 s.tf（term frequency）
- 在单个词频基础上加权重 s.idf（自动过滤一些常见的词，比如“的”，这个权重叫做"逆文档频率"（Inverse Document Frequency，缩写为IDF），它的大小与一个词的常见程度成反比。）
- 计算文本相似度 s.sim

# setup.py

- 下载源码：**python setup.py install**
- 在线安装：安装pip后直接**pip install snownlp**

###subprocess模块
- os.system：以控制台的形式运行程序。<br />
- subprocess：涉及到进行进程间通信时需要用到。（并不是很明白）

###python打包工具setuptools和distutils
**distutils**：python标准库的一部分，这个库的目的是为开发者提供一种**方便的打包方式**， 同时为使用者提供**方便的安装方式**。当我们开发了自己的模块之后，使用distutils的setup.py打包。

from distutils.core import setup<br />
setup(<br />
name=" ", #*要打包的包名*<br />
version=" ", #*版本信息*<br />
...<br />
) #*建立setup文件*<br />
python setup sdist #*执行打包命令*

**setuptools**：setuptools是distutils的增强版。

from setuptools import setup<br />
之后操作与distutils类似

# test.py

- normal.get_sentences() 分句
- seg.seg() 分词
- normal.filter_stop() 过滤提取高频词
- textrank.TextRank() 概括文本信息提取摘要
- rank.top_index(n) 提取前n句

# 关于训练

### 分词，词性标注，情感分析都需要用到训练模型

- .train 训练新模型
- .save 保存训练好的模型

# 源码

## - sentiment

### sentiment情感分析

判断一句话是积极态度还是消极态度，训练新模型→保存新模型→

### sentiment文件夹包含：

- neg.txt （存储消极/负样本，用于训练新模型）
- pos.txt （存储积极/正样本，用于训练新模型）
- sentiment.marshal （存储新模型）
- sentiment.marshal.3

### 调用了贝叶斯模型

关于贝叶斯模型 https://blog.csdn.net/google19890102/article/details/80091502
