"""NS class tests"""
import pytest
from orijenpy import helper, ns

class TestNS:
    """Class used to test NS"""
    @pytest.fixture
    def this_ns(self):
        """Method returns NS instance"""
        api = helper.test_session()
        return ns(api)

    def test_list(self, this_ns):
        """Method to test list()"""
        assert len(this_ns.list()['items'])>0

    def test_get(self, this_ns):
        """Method to test get()"""
        r = this_ns.list()['items'][0]['name']
        assert isinstance(this_ns.get(r), dict)
