from tenacity import retry, stop_after_attempt, wait_exponential
from requests.exceptions import HTTPError
import requests

retry_config = {
    'stop': stop_after_attempt(3),
    'wait': wait_exponential(multiplier=1, min=1, max=10),
    'retry_on_exception': lambda exc: isinstance(exc, HTTPError) and exc.response.status_code in [429, 503]
}

class XCSession:
    def __init__(self, base_url, api_token):
        self.base_url = base_url.rstrip('/')
        self.api_token = api_token
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Token {self.api_token}'})

    @retry(**retry_config)
    def get(self, path, params=None, **kwargs):
        url = f'{self.base_url}/{path.lstrip("/")}'
        response = self.session.get(url, params=params, **kwargs)
        response.raise_for_status()
        return response.json()

    @retry(**retry_config)
    def post(self, path, json=None, **kwargs):
        url = f'{self.base_url}/{path.lstrip("/")}'
        response = self.session.post(url, json=json, **kwargs)
        response.raise_for_status()
        return response.json()

    @retry(**retry_config)
    def put(self, path, json=None, **kwargs):
        url = f'{self.base_url}/{path.lstrip("/")}'
        response = self.session.put(url, json=json, **kwargs)
        response.raise_for_status()
        return response.json()

    @retry(**retry_config)
    def delete(self, path, **kwargs):
        url = f'{self.base_url}/{path.lstrip("/")}'
        response = self.session.delete(url, **kwargs)
        response.raise_for_status()
        return response.json()
