import json
import requests


class Client():

    def upload_info(self,node):
        requests.post(node ,data= json.dumps(self))#пост запрос з силкою на сервак







