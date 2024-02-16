from uplink import Consumer, Path, Body, json, get, post
from orijenpy import helper


@helper.common_decorators
class User(Consumer):
    def __init__(self, session):
        super(User, self).__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/web/custom/namespaces/{namespace}/user_roles')
    def list(self, namespace: Path = 'system'):
        '''List all Users'''
        pass

    @json
    @post('/api/web/custom/namespaces/{namespace}/user_roles')
    def create(self, payload: Body, namespace: Path = 'system'):
        '''Create a User'''
        pass

    @json
    @post('/api/web/custom/namespaces/{namespace}/users/cascade_delete')
    def delete(self, payload: Body, namespace: Path = 'system'):
        '''Delete a User'''
        pass

    @staticmethod
    def create_payload(
            email: str,
            first_name: str, 
            last_name: str, 
            group_names: list = [],
            namespace_roles: list = [],
            idm_type: str = 'SSO',
            namespace: str = 'system'
        ):
        return {
            "email": email,
            "first_name": first_name,
            "group_names": group_names,
            "idm_type": idm_type,
            "last_name": last_name,
            "name": email,
            "namespace": namespace,
            "namespace_roles": namespace_roles,
            "type": "USER"
        }

    @staticmethod
    def delete_payload(email: str, namespace: str = 'system'):
        return {
            "email": email,
            "namespace": namespace
        }