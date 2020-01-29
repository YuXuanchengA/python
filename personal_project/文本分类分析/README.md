项目介绍
=================

**项目名称：** 可可英语新闻文本分类

**项目简介：** 对于可可英语网爬虫爬取结果的文章，进行文本分类。要求拿出60%的数据进行训练，40%的数据进行测试。  

**所有人：** 余煊铖

**数据训练和测试所使用的主要工具：**  

|  模块   | 说明  |
|  ----  | ----  |
| gensim  | 使用word2vec模型训练词向量 |
| sklearn  | 机器学习方法，主要使用了贝叶斯分类方法 |  

一些参考链接
``` python
https://blog.csdn.net/cindy407/article/details/93789415  
https://blog.csdn.net/cindy407/article/details/93777413 
https://blog.csdn.net/lilong117194/article/details/82849054  
https://www.cnblogs.com/always-fight/p/10159547.html 
https://www.jianshu.com/p/6ada34655862 
```

**数据准备：**   

http://www.kekenet.com/read/  
经济
http://www.kekenet.com/read/news/economy/  
娱乐
http://www.kekenet.com/read/news/entertainment/  
校园
http://www.kekenet.com/read/news/Economics/  
科技
http://www.kekenet.com/read/news/keji/

爬取数据使用的是Scrapy框架  
``` python
scrapy.cfg：项目的配置文件
mySpider/：项目的Python模块，将会从这里引用代码
myspider/items.py：项目的目标文件
myspider/piplines.py：项目的管道文件
myspider/settingd.py：项目的设置文件
myspider/spiders/：存储爬取代码目录
```

数据库使用的是mysql  
在spider/spiders/piplines里面配置，默认配置是
``` python
HOSTNAME = 'localhost'
PORT = ''
DATABASE = 'nlp'
USER = 'root'
PASSWORD = ''
```

一些参考链接
``` python
SQLAlchemy: https://www.liaoxuefeng.com/wiki/897692888725344/955081460091040  
Middlewares: https://blog.csdn.net/weixin_30764771/article/details/95004989  
Settings: https://blog.csdn.net/weixin_30894389/article/details/95004944  
```
