import json

class Data_Node1():
    adress = 'http://127.0.0.1:5000/'

    def read(self):
        with open('datanode1.json', 'r') as f:
            text = f.read(json.load(f))
            return text

    def upload_info(self):
        with open('datanode1.json', 'a') as f:
            f.write("%s\n"%json.dumps(self))



