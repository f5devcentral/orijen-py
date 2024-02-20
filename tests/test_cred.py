"""Cred classes tests"""
import pytest
from orijenpy import helper, apicred, svccred

class TestAPIcred:
    """Class used to test APIcred"""
    @pytest.fixture
    def this_apicred(self):
        """Method returns APIcred instance"""
        api = helper.test_session()
        return apicred(api)

    def test_list(self, this_apicred):
        """Method to test list()"""
        assert len(this_apicred.list()['items'])>0

    def test_get(self, this_apicred):
        """Method to test get()"""
        r = this_apicred.list()['items'][0]['name']
        assert isinstance(this_apicred.get(r), dict)

class TestSVCcred:
    """Class used to test SVCcred"""
    @pytest.fixture
    def this_svccred(self):
        """Method returns APIcred instance"""
        api = helper.test_session()
        return svccred(api)

    def test_list(self, this_svccred):
        """Method to test list()"""
        assert len(this_svccred.list()['items'])>0

