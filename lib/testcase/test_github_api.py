import os, sys
sys.path.append(os.getcwd())

import pytest
from lib.core import wraps

class TestGithubApi:
    """TestGithubApi"""

    def setup(self):
        """ setup function """

    def teardown(self):
        """ tearDown function """

    @wraps.test_case_runner
    @wraps.test_case_parse
    def test_some_endpoint_success(self, *args, **kwargs):
        """ Test github endpoint api """
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        for assert_vale in kwargs.get('exec_text'):
            assert assert_vale[0] == assert_vale[1]

    @wraps.test_case_runner
    @wraps.test_case_parse
    def test_some_endpoint_fail(self, *args, **kwargs):
        """ Test github endpoint api """
        response = kwargs.get('response')
        print("Response :", response)
        print("AssertInfo: ", kwargs.get('exec_text'))
        for assert_vale in kwargs.get('exec_text'):
            assert assert_vale[0] == assert_vale[1]

