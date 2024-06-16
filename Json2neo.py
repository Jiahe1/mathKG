from py2neo import Graph, Node, Relationship
import json
#输入你的账号密码
graph = Graph("http://localhost:7474",auth=("neo4j","123456789"))
with open("总知识图谱4.0.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 解析数据并利用 Cypher 语句导入到 Neo4j
for item in data:
    annotations = item['annotations'][0]['result']  # 获取标注数据
    for annotation in annotations:

        # 创建节点
        if annotation['type'] == 'labels':
            label_node = Node(annotation['value']['labels'][0], text=annotation['value']['text'])
            graph.merge(label_node, annotation['value']['labels'][0], "text")

        # 创建关系
        elif annotation['type'] == 'relation':

            # 获取关系
            relation = annotation['labels'][0]

            # 定位起始节点
            from_id = annotation['from_id']
            from_value = [i['value'] for i in annotations if 'id' in i if i['id'] == from_id][0]
            head = from_value['text']
            label1 = from_value['labels'][0]

            # 定位终止节点
            to_id = annotation['to_id']
            to_value = [i['value'] for i in annotations if 'id' in i if i['id'] == to_id][0]
            tail = to_value['text']
            label2 = to_value['labels'][0]

            # 检查节点是否存在
            head_node = Node(label1, text=head)
            tail_node = Node(label2, text=tail)
            graph.merge(head_node, label1, "text")
            graph.merge(tail_node, label2, "text")

            # 创建关系
            relationship = Relationship(head_node, relation, tail_node)
            graph.merge(relationship)