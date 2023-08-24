from flask import Flask, request
from client import Client
from data_node_1 import Data_Node1
from data_node_2 import Data_Node2
from data_node_3 import Data_Node3
from datanode4 import Data_Node4
from controlnode import ControlNode


app4 = Flask(__name__)

@app4.route("/<phrase>", methods=['GET', 'POST'])
def server(phrase):
    a = ControlNode()
    if request.method == 'POST':    #обробка пост запросів
        for i in range(5):
            if a.amount_of_posts()[str(i)][2][0] == "":
                Client.upload_info(phrase,a.doing_posts(Data_Node4.adress,phrase))
            else:
                Client.upload_info(phrase,(a.comparing_node()))
                a.doing_posts(Data_Node4.adress,phrase)
                break
    else:   #обробка гет запросів
        with open('datanode1.json', 'r') as f:
            text1 = f.read()
        with open('datanode2.json', 'r') as f:
            text2 = f.read()
        with open('datanode3.json', 'r') as f:
            text3 = f.read()
        with open('datanode4.json', 'r') as f:
            text4 = f.read()
        with open('datanode5.json', 'r') as f:
            text5 = f.read()
        return text1+"\n"+text2+"\n"+text3+"\n"+text4 +"\n"+text5      #контенація рядків з 2 нод

if __name__ == '__main__':
    app4.run(port=5003)