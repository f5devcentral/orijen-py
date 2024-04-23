"""
Module for Site Methods
https://docs.cloud.f5.com/docs/api/site
"""
from datetime import datetime
from uplink import Consumer, QueryMap, Path, Body, json, get, post, put, delete # pylint: disable=unused-import
from orijenpy import helper

@helper.common_decorators
class Site(Consumer):
    """
    Class for Tenant Methods
    """
    def __init__(self, session):
        super().__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/config/namespaces/{namespace}/sites')
    def list(self, namespace: Path ='system'):
        """List Sites"""

    @get('/api/config/namespaces/{namespace}/sites{name}')
    def get(self, name: Path, namespace: Path ='system'):
        """Get a single Site"""

    @json
    @post('/api/config/namespaces/{namespace}/sites/{name}/upgrade_os')
    def upgrade_os(self, payload: Body, name: Path, namespace: Path ='system'):
        """
        Upgrade Site OS
        Use upgrade_payload() to build Body
        """

    @json
    @post('/api/config/namespaces/{namespace}/sites/{name}/upgrade_sw')
    def upgrade_sw(self, payload: Body, name: Path, namespace: Path ='system'):
        """
        Upgrade Site OS
        Use upgrade_payload() to build Body
        """

    @staticmethod
    def upgrade_payload(name: str, version: str, namespace: str = 'system') -> dict:
        """
        Payload for upgrade_*
        current_dw = "crt-20240329-2728"
        current_os = "9.2024.6" or "7.2009.45" (depending on RHEL vs. CentOS)
        """
        return {
            "name": name,
            "namespace": namespace,
            "version": version
        }