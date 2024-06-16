from py2neo import *
graph = Graph("http://localhost:7474",auth=("neo4j","123456789"))

#1.章节索引
all = ["HeJia","第一章集合与常用逻辑用语","第二章一元二次函数，方程和不等式","第三章函数的概念与性质，方程和不等式",
        "第四章指数函数与对数函数","第五章三角函数","第六章平面向量及其应用","第七章复数","第八章立体几何初步",
        "第九章统计","第十章概率","第十一章空间向量与立体几何","第十二章直线和圆的方程","第十三章圆锥曲线的方程",
        "第十四章数列","第十五章一元函数的导数及其应用","第十六章计数原理","第十七章随机变量及其分布","第十八章成对数据的统计分析"
]

#2.问答开始，询问用户学习章节
print('您好，我是高中数学领域知识图谱机器人，我叫小图!小图将帮您梳理学习高中数学所有的知识点!')
print('小图: 高中数学一共18个章节，请查看可视化知识图谱后，找到您想学习的章节并回复章节对应数字1-18\n')
#输入章节
inChapter = input('我的回答: ')
#函数int()将输入字符串转化为int类型，获得cypher查询
cyChapter = "MATCH(n:章节{text:"+"'"+all[int(inChapter)]+"'"+"})-->(m:知识点) RETURN m.text"
# 执行 cypher 语句，获得返回结果
chapter = graph.run(cyChapter)
#输出结果
print('\n小图: 【'+all[int(inChapter)]+'】有以下知识点,请回复您想学习的知识点：')
# 通过遍历的方式取出所有结果，即返回查询章节的所有知识点
for i in chapter:
    print(i)

#3.知识点问答，根据用户输入知识点输出题目
question1 = input('\n我的回答: ')
print("\n小图: 根据您所选知识点，为您提供了对应问题，快来解答吧!")
question2 = "MATCH(n:知识点{text:'" + question1 + "'})-->(m:题目) RETURN m.text"
question3 = graph.run(question2)
for i in question3:
    print(i)

#4.题目问答，根据用户输入获得答案
print("小图: 如果您已经做完了上述题目，请回复任意字符获取答案\n")
answer = input('我的回答: ')
answer2 = "MATCH(n:知识点{text:'" + question1 + "'})-[]->()-->(m:答案) RETURN m.text"
answer3 = graph.run(answer2)
print("\n小图: 答案如下，聪明的你一定做对了吧!")
for i in answer3:
    print(i)

#4.结束
print("\n小图: 相信你已经掌握了知识点【"+question1+"】快来学习下一个知识点吧!\n")