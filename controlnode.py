from data_node_1 import Data_Node1
from data_node_2 import Data_Node2
from data_node_3 import Data_Node3
from datanode4 import Data_Node4
from datanode5 import Data_Node5
import json

class ControlNode:


    def amount_of_posts(self):
        with open("sw_templates.json", "r") as f:
            text = json.load(f)
        return text

    def doing_posts(self,node,phrase):
        text = self.amount_of_posts()
        for i in range(5):                  #Обробка 1 пост запроса для створення відомості про перегружені сервери та вільні
            if text[str(i)][0][0] == node:
                if text[str(i)][2][0] == "":
                    result = []
                    with open("sw_templates.json", "w") as f:
                        result = text
                        result[str(i)][2].insert(0,"node_in_use")
                        result[str(i)][2].pop()
                        json.dump(result, f)
                        return node
            else:
                if text[str(i)][2][0] == "":
                    with open("sw_templates.json", "w") as f:
                        result = text
                        result[str(i)][2].insert(0,"free_node")
                        result[str(i)][2].pop()
                        json.dump(result, f)

        data_node_list = [Data_Node1, Data_Node2, Data_Node3, Data_Node4, Data_Node5]
        for i in range(5):
            if text[str(i)][2][0] == "node_in_use":
                with open("sw_templates.json", "w") as f:
                    result = text
                    result[str(i)][1].insert(0,result[str(i)][1][0] +1)
                    result[str(i)][1].pop()
                    result[str(5)] = result[str(5)]+1
                    json.dump(result,f)
                    for j in range(len(data_node_list)):
                        if i == j:
                            data_node_list[j].upload_info(phrase)



    def comparing_node(self):
        text = self.amount_of_posts()
        downloaded_of_nodes = []
        for i in range(5):
            downloaded_of_nodes.append(text[str(i)][1][0])
        free_node_number = min(downloaded_of_nodes)
        loaded_node = max(downloaded_of_nodes)
        for i in range(5):
            if text[str(i)][1][0] == free_node_number:
                free_node = i
        if text["5"] > 50:
            for i in range(5):
                if text[str(i)][2][0] == "node_in_use":
                    with open("sw_templates.json", "w") as f:
                        result = text
                        result[str(i)][2].insert(0, "free_node")
                        result[str(i)][2].pop()
                        json.dump(result, f)
                    return text[str(i)][0][0]
                if i == free_node:
                    with open("sw_templates.json", "w") as f:
                        result = text
                        result["5"] = 0
                        result[str(i)][2].insert(0, "node_in_use")
                        result[str(i)][2].pop()
                        json.dump(result, f)
                    return text[str(i)][0][0]
        else:
            for i in range(5):
                if text[str(i)][2][0] == "node_in_use":
                    return text[str(i)][0][0]

