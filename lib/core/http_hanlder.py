import os, sys
sys.path.append(os.getcwd())

import requests
import json
from urllib import parse
from lib.core.recursion import GetDictParam

SESSION = requests.Session()

class http_handler(GetDictParam):
    def __init__(self, request_bodys):
        self.session = SESSION
        self.body = request_bodys

    def make_request_template(self):
        """ Send http request
        """
        method = self.body.get('method')
        if method in ['get', 'GET']:
            temp = ('url', 'params', 'headers', 'cookies')
            body = self.list_for_key_to_dict(*temp, my_dict=self.body)
            if body.get('params'):
                if '&' in body.get('params') and '=' in body.get('params'):
                    body['params'] = dict(parse.parse_qsl(body['params']))
            return self.get(**body)
        
        if method in ['post', 'POST']:
            temp = ('url', 'data', 'json', 'headers', 'cookies')
            body = self.list_for_key_to_dict(*temp, my_dict=self.body)
            body = {key: value for key, value in body.items() if value is not None}
            return self.post(**body)

    def get(self, **kwargs):
        return self.session.get(**kwargs).json()

    def post(self, **kwargs):
        return self.session.post(**kwargs).json()
