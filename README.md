# 高中数学知识图谱，可视化，问答，neo4j
把Label Studio标注好实体关系的JSON文件导入neo4j，并且用Cypher实现简单问答功能。
# 该项目有298个实体和297个关系
# ![image](https://github.com/Jiahe1/neo4j-/assets/58599488/598bb41e-41a9-4521-8030-2a1557c221ea)
# 操作流程
### 1.下载要用的包 py2neo	2021.2.4	
 ```
 pip install py2neo
 ```
### 2.打开你的neo4j Desktop    
新建一个数据库，注意版本一定要是4.2.1  别的不行，因为py2neo已经很久没更新了，跟不上新版本
### 3.运行Json2neo.py     
注意填账号密码  这一步做完就可以在Neo4j Browser中可视化查看了，效果会是上图的样子
### 4.运行cypher.py
欢迎和我交流
