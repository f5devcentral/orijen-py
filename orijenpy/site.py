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