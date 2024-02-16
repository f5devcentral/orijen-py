from uplink import Consumer, Path, Body, json, get, post
from orijenpy import helper


@helper.common_decorators
class NS(Consumer):
    def __init__(self, session):
        super(NS, self).__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/web/namespaces')
    def list(self):
        '''List all Namespaces'''
        pass

    @get('/api/web/namespaces/{name}')
    def get(self, name: Path):
        '''Get a single Namespace'''

    @json
    @post('/api/web/namespaces')
    def create(self, payload: Body):
        '''Create a Namespace'''

    @json
    @post('/api/web/namespaces/{name}/cascade_delete')
    def delete(self, name: Path):
        '''Cascade delete a namespace'''
        payload = {
            'name': name
        }
        return payload
   
    @staticmethod
    def create_payload(name: str, description: str):
        return {
            'metadata': {
                'annotations': {},
                'description': description,
                'disable': False,
                'labels': {},
                'name': name,
                'namespace': ''
            },
            'spec': {}
        }