from uplink import Consumer, Path, Body, json, get, post
from orijenpy import helper

'''
These classes are very similiar.
Maybe we could have a cred class that these inherit from?
'''
@helper.common_decorators
class APIcred(Consumer):
    def __init__(self, session):
        super(APIcred, self).__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/web/namespaces/{namespace}/api_credentials')
    def list(self, namespace: Path = 'system'):
        '''List all API Credentials'''
        pass

    @get('/api/web/namespaces/{namespace}/api_credentials/{name}')
    def get(self, name: Path, namespace: Path = 'system'):
        '''Get a single API Credential'''
        pass

    @json
    @post('/api/web/namespaces/{namespace}/api_credentials')
    def create(self, payload: Body, namespace: Path = 'system'):
        '''Create an API Credential'''
        pass

    @json
    @post('api/web/namespaces/{namespace}/renew/api_credentials')
    def renew(self, namespace: Path = 'system'):
        '''Renew an API Credential'''
        pass

    @json
    @post('/api/web/namespaces/{namespace}/revoke/api_credentials')
    def revoke(self, payload: Body, namespace: Path = 'system'):
        '''Revoke an API Credential'''
        pass

    @staticmethod
    def create_payload(name: str, expiration_days: int, namespace: str = 'system'):
        return {
            'spec': {
                'type': 'API_TOKEN'
            },
            'namespace': namespace,
            'name': name,
            'expiration_days': expiration_days
        }

    @staticmethod
    def renew_payload(name: str, expiration_days: int, namespace: str = 'system'):
        return {
            'expiration_days': expiration_days,
            'name': name,
            'namespace': namespace
        }

    @staticmethod
    def revoke_payload(name: str, namespace: str = 'system'):
        return {
            'name': name,
            'namespace': namespace
        }
    

@helper.common_decorators
class SVCcred(Consumer):
    def __init__(self, session):
        super(SVCcred, self).__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/web/namespaces/{namespace}/service_credentials')
    def list(self, namespace: Path = 'system'):
        '''List all Service Credentials'''
        pass

    @get('/api/web/namespaces/{namespace}/service_credentials/{name}')
    def get(self, name: Path, namespace: Path = 'system'):
        '''Get a single Service Credential'''
        pass

    @json
    @post('/api/web/namespaces/{namespace}/service_credentials')
    def create(self, payload: Body, namespace: Path = 'system'):
        '''Create an Service Credential'''
        pass

    @json
    @post('api/web/namespaces/{namespace}/renew/service_credentials')
    def renew(self, payload: Body, namespace: Path = 'system'):
        '''Renew a Service Credential'''
        pass

    @json
    @post('/api/web/namespaces/{namespace}/revoke/service_credentials')
    def revoke(self, payload: Body, namespace: Path = 'system'):
        '''Revoke a Service Credential'''
        pass

    @staticmethod
    def create_payload(name: str, namespace_roles: list, expiration_days: int, namespace: str = 'system'):
        return {
            'type':'SERVICE_API_TOKEN',
            'namespace': namespace,
            'name': name,
            'namespace_roles': namespace_roles,
            'expiration_days': expiration_days
        }

    @staticmethod
    def renew_payload(name: str, expiration_days: int, namespace: str = 'system'):
        return {
            'expiration_days': expiration_days,
            'name': name,
            'namespace': namespace
        }

    @staticmethod
    def revoke_payload(name: str, namespace: str = 'system'):
        return {
            'name': name,
            'namespace': namespace
        }