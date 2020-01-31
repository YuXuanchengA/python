
# coding: utf-8

# In[7]:


import jieba
import codecs

# 参考
# 原文链接：https://blog.csdn.net/oxuzhenyi/article/details/55511138

names = {} # 姓名字典
relationships = {} # 关系字典
lineNames = [] # 每段内人物关系

# 将人名存入列表
with codecs.open("persons.txt", "r", "utf-8") as f:
    persons = f.read().splitlines()
    
# 每段每个人物及出现次数
jieba.load_userdict("persons.txt")        # 载入自定义词典
with codecs.open("The_three_body_problem_full.txt", "r", "utf8") as f:
    for line in f.readlines():
        # 分词并返回该词词性
        name = jieba.cut(line)
        
        # 为新读入的一段添加人物名称列表
        lineNames.append([])
        for w in name:
            # 如果不在人名列表里，则不为人名
            if w not in persons:
                continue
                
            # 为当前段的环境增加一个人物
            lineNames[-1].append(w)
            
            if names.get(w) is None:
                names[w] = 0
                relationships[w] = {}
            # 该人物出现次数加 1
            names[w] += 1

            
# 计算每段中任意两个人物共同出现次数
for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            # 若两人尚未同时出现则新建项
            if relationships[name1].get(name2) is None:
                relationships[name1][name2]= 1
            else:
                # 两人共同出现次数加 1
                relationships[name1][name2] = relationships[name1][name2]+ 1

# output
with codecs.open("The_three_body_problem_relationship.txt", "a+", "utf-8") as f:
    f.write("人名1 人名2 紧密程度\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            f.write(name + " " + v + " " + str(w) + "\r\n")

