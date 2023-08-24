import json

class Data_Node3():
    adress = "http://127.0.0.1:5002/"

    def read(self):
        with open('datanode3.json', 'r') as f:
            text = f.read(json.load(f))
            return text

    def upload_info(self):
        with open('datanode3.json', 'a') as f:
            f.write("%s\n"%json.dumps(self))
