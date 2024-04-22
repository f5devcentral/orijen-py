"""
Module for Registration Methods
https://docs.cloud.f5.com/docs/api/registration
"""
from datetime import datetime
from uplink import Consumer, QueryMap, Path, Body, json, get, post, put, delete # pylint: disable=unused-import
from orijenpy import helper

@helper.common_decorators
class Registration(Consumer):
    """
    Class for Tenant Methods
    """
    def __init__(self, session):
        super().__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/register/namespaces/{namespace}/registrations')
    def list(self, namespace: Path ='system'):
        """List Registrations"""

    @post('/api/register/namespaces/{namespace}/listregistrationsbystate')
    def list_by_state(self, payload: Body, namespace: Path ='system'):
        """List Registrations"""

    @get('/api/register/namespaces/{namespace}/registrations/{name}')
    def get(self, name: Path, namespace: Path ='system'):
        """Get a single Registration"""

    @post('/api/register/namespaces/{namespace}/registration/{name}/approve')
    def approve(self, payload: Body, name: Path, namespace: Path ='system'):
        """
        Approve a pending registration
        Use approve_payload() to build Body
        """

    @staticmethod
    def ls_by_state_payload(state: str = 'NEW', namespace: str = 'system') -> dict:
        """
        Payload for list_by_state
        """
        return {
            "namespace": namespace,
            "state": state
        }

    @staticmethod
    def approve_payload(name: str, passport: dict, state: str = 'APPROVED', namespace: str = 'system') -> dict: # pylint: disable=line-too-long
        """
        Payload for approve
        pass 'passport' dict from get()
        """
        return {
            "namespace": namespace,
            "name": name,
            "state": state,
            "passport" : passport
        }
    