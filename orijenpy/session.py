import requests
from orijenpy import helper

class Session:
    def __init__(self, tenant_url=None, api_token=None):
        self._tenant_url = helper.validate_url(tenant_url)
        self._api_token = api_token
        self._session = requests.Session()
        self._session.headers.update({'Authorization': f'APIToken {self._api_token}'})

'''
Could this be a base class of Consumer
that gets passed into the resource classes?
'''