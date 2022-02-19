import os, sys
sys.path.append(os.getcwd())

import json
from lib.core.case_manager import CaseManager, CasesContainer

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/').split('lib')[0]

HEADERS_TEMPLATE_PATH = ROOT_DIR + 'lib/template/header.txt'
CONTENT_TEMPLATE_PATH = ROOT_DIR + 'lib/template/content.txt'
TESTCASES_PATH = ROOT_DIR + 'lib/testcase/'
CASE_PATH = ROOT_DIR + 'case/'

class TestCaseLoader(CaseManager):
    __slots__ = 'tags'

    def __init__(self) -> None:
        super(TestCaseLoader, self).__init__()
        self.files = os.listdir(CASE_PATH)
        self.data = {}
        self.tags = self.make_cases_info()

    def __repr__(self) -> str:
        return json.dumps(self.tags)
