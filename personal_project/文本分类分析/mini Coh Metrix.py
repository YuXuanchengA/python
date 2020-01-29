
# coding: utf-8

# In[21]:


# Coh-Metrix

import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
#from nltk.corpus import cmudict
import nltk
import textstat

# 去掉文本空行，避免段落计算干扰
def clearBlankLine(fname):
    f1 = open(fname, 'r', encoding='utf-8') # 要去掉空行的文件 
    f2 = open('textclear.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    for line in f1.readlines():
        if line == '\n':
            line = line.strip("\n")
        f2.write(line)
    f1.close()
    f2.close()

def ContentFetch():
    with open('textclear.txt', 'r', encoding = 'utf-8')as f:
        content = f.read()
    f.close()
    return content

# Descriptive
# Number of paragraphs (DESPC) 
def DESPC(content):
    PC = 0
    for i in content:
        if i == '\n':
            PC += 1
    
    # 最后一段默认没有换行符
    return PC + 1 
      
# Number of sentences (DESSC) 
def DESSC(content):
    sents = sent_tokenize(content)
    SC = 0
    for i in sents:
        SC += 1
    return SC

# Number of words (DESWC)
def DESWC(content):
    words = word_tokenize(content)
    
    #不统计英文标点
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    tokens = [word for word in words if word not in english_punctuations]
    return tokens

# Lexical Diversity 
# Type-token ratio: LDTTRc 实词类符/形符比
def LDTTRc(tokens):
    tokens_c = []
    types_c = []
    #词性标注
    tokens_tagged = nltk.pos_tag(tokens)
    for gram in tokens_tagged:
        if gram[1] == "RP": # PR为虚词
            continue
        else: 
            tokens_c.append(gram)
            # 类符
            if gram not in types_c:
                types_c.append(gram)
    TTRc = len(types_c)/len(tokens_c)*100
    return TTRc

# Type-token ratio: LDTTRa 所有单词类符/形符比 
# TTR=类符/形符*100
def LDTTRa(tokens,word_number):
    tokens_number = word_number
    types = [] # 类符
    for gram in tokens:
        if gram not in types:
            types.append(gram)
    TTRa = len(types)/tokens_number*100
    return TTRa

# LDMTLDa: MTLD lexcical diversity measure for all words.
# 参考链接：https://blog.csdn.net/qq_36652619/article/details/77253208
def LDMTLDa(tokens):
    # 判断list要够长，否则当前ttr的值没有效果
    if len(tokens) < 50:
        return -1
    # 先得到一个type的list
    types = []
    factors = 0.0
    now_ttr = 1.0 # 当前ttr为1.0
    ttr_standard = 0.72 # 标准ttr为0.72
    tokens_number = 0
    types_number = 0
    for gram in tokens:
        gram = gram.lower() # 全部转换为小写，用于计算类符
        tokens_number+=1
        
        # 计算类符
        if gram not in types:
            types_number+=1
            types.append(gram) 
        now_ttr = types_number*1.0/tokens_number
        
        # 如果ttr < 0.72，在这里断开，前面两个词就是一个词串，一个词串factors+1
        if now_ttr < ttr_standard:
            factors+=1.0
            now_ttr = 1.0
            tokens_number = 0
            types_number = 0
            types = []
    RS = now_ttr
    # print now_ttr
    IFS = (1-RS)*1.0/0.28
    IFS+=factors
    if IFS != 0:
        return len(tokens)/IFS
    
# Readability
# ASL(Average Sentence Length)
def ASL(sent_number,word_number):
    ASL = word_number/sent_number
    return ASL

# ASW(Average number of syllables per word) 平均音节数/词
# 参考链接：https://blog.csdn.net/weixin_38008864/article/details/102855031
def ASW(content,word_number):
    SW_number = textstat.syllable_count(content)
    ASW = SW_number/word_number
    return ASW

# Flesch Reading Ease: RDFRE
# 206.835 - (1.015 x ASL) - (84.6 x ASW)
def RDFRE(ASL,ASW):
    RDFRE = 206.835 - (1.015*ASL) - (84.6*ASW)
    return RDFRE
    #r = Readability(content)
    #fk = r.flesch_kincaid()
    #return fk.ease

# Flesch_Kincaid Grade Level: RDFKGL
# READFKGL = (.39 x ASL) + (11.8 x ASW) - 15.59
def RDFKGL(ASL,ASW):
    RDFKGL = (.39*ASL)+(11.8*ASW)-15.59
    return RDFKGL
    #r = Readability(content)
    #fk = r.flesch_kincaid()
    #return fk.grade_level

# RDL2
# 没有找到相关的计算公式

#main
clearBlankLine('test.txt')

text = ContentFetch()
para_number = DESPC(text)
sent_number = DESSC(text)
tokens = DESWC(text)
word_number = len(tokens)
ASL = ASL(sent_number,word_number)
ASW  = ASW(text,word_number)

print("Descriptive:")
print('文本段落数:',para_number)
print('文本句子数:',sent_number)
print('文本单词数:',word_number)
print('平均句长：',ASL)
print('平均单词音节长：',ASW)

print("Lexical Diversity:")
TTRc = LDTTRc(tokens)
print('实词类符/形符比:',TTRc)
TTRa = LDTTRa(tokens,word_number)
print('全文类符/形符比:',TTRa)
MTLD  = LDMTLDa(tokens)
print('MTLD词汇丰富度:',MTLD)

print("Readability:")
RDFRE = RDFRE(ASL,ASW)
RDFKGL = RDFKGL(ASL,ASW)
print("The Flesch Reading Ease: " ,RDFRE)
print("Flesch-Kincaid Grade Level: " ,RDFKGL)

