import requests
from orijenpy import helper, exception
import re
from urllib.parse import urlparse

class Session:
    def __init__(self, tenant_url=None, api_token=None, validate=True):
        self._tenant_url = self.validate_url(tenant_url)
        self._api_token = api_token
        self._session = requests.Session()
        self._session.headers.update({'Authorization': f'APIToken {self._api_token}'})
        if validate:
            self.whoami()

    def whoami(self) -> None:
        try:
            r = requests.get(self._tenant_url + '/api/web/custom/namespaces/system/whoami')
            r.raise_for_status()
            return
        except Exception as e:
            raise exception.OrijenXCException("Invalid Token")
        
    @staticmethod
    def validate_url(url) -> str:
        parsed_url = urlparse(url)
        if parsed_url.scheme and parsed_url.netloc:
            stripped_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path.rstrip('/')}"
            return stripped_url
        else:
            raise exception.OrijenXCException("Invalid Tenant URL")

'''
Could this be a base class of Consumer
that gets passed into the resource classes?
'''