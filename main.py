from flask import Flask, request
from client import Client
from data_node_1 import Data_Node1
from controlnode import ControlNode



app = Flask(__name__)


@app.route("/<phrase>", methods=['GET', 'POST'])
def server(phrase):
    a = ControlNode()
    if request.method == 'POST':    #обробка пост запросів
        for i in range(5):
            if a.amount_of_posts()[str(i)][2][0] == "":
                Client.upload_info(phrase,a.doing_posts(Data_Node1.adress,phrase))
            else:
                Client.upload_info(phrase,a.comparing_node())
                a.doing_posts(Data_Node1.adress,phrase)
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
        return text1 + "\n" + text2 + "\n" + text3 + "\n" + text4 + "\n" + text5     #контенація рядків з 5 нод


def start_local_server_on_port(port):
    app.run(port=port)

if __name__ == '__main__':
    start_local_server_on_port(5000)
