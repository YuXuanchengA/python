
项目介绍
=================

**项目名称：** 英文版mini Coh-Metrix

**项目功能：** 抽取给定文本特征：描述性特征（段落数、句子数、单词数、平均句长和平均单词音节长），词汇丰富度及文本可读性

**所有者：** 余煊铖

**代码说明：**  

+ 函数及功能

| 函数        |  功能   |
|:--------    |:--------|
| clearBlankLine & ContentFetch | 文本降噪：获取文本内容，去除文本空行 |
| DESPC & DESSC & DESWC & ASL & ASW | 返回文本段落数、句子数、单词数、平均句长和平均单词音节长 |
| LDTTRc & LDTTRa & LDMTLDa  | 返回文本实词ttr，全文ttr和MTLD词汇丰富度 |
| RDFRE & RDFKGL    | 返回The Flesch Reading Ease和Flesch-Kincaid Grade Level |

+ 用到的库

| 库        | 主要功能   | 具体说明   |
|:--------     |:--------|  :--------|
| re   | 处理正则表达式  | re.strip("\n")用于去除文本空行，计算段落数 |
| nltk    | 英文分词、分句及词性标注 | 无  |
| textstat    | 文本可读性计算包 | 多种文本可读性计算算法  |

+ 部分参考链接：  
http://141.225.41.245/cohmetrixhome/documentation_indices.html  
https://blog.csdn.net/weixin_38008864/article/details/102855031  
https://blog.csdn.net/qq_36652619/article/details/77253208

**存在的困难及问题：**  
+ 计算平均单词音节数时尝试了三种办法：使用nltk的语料库cmudict，但循环算法电脑跑不动；使用Readability库，同样没有跑动；最后选择用textstat库
+ Coh-Metrix官网上Readability只有三个指标，本项目实现了其中两种，其中RDL2（二语文本可读性）没有找到相关的计算公式和说明
+ Cohmatrix-Webtool无法打开，输出结果格式不确定
