import json

class Data_Node2():
    adress = 'http://127.0.0.1:5001/'

    def read(self):
        with open('datanode2.json', 'r') as f:
            text = f.read("%s\n"%json.load(self))
            return text

    def upload_info(self):
        with open('datanode2.json', 'a') as f:
            f.write("%s\n"%json.dumps(self))