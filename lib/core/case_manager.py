import os, sys
sys.path.append(os.getcwd())

import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/').split('lib')[0]
CASE_PATH = ROOT_DIR + 'case/'

class CaseManager:
    def __init__(self, path = None) -> None:
        self.datas = {}
        self.path = path
        if not self.path:
            self.path = CASE_PATH

    def get_all_cases(self):
        return os.listdir(self.path)

    def read_case_json(self, file_name):
        """ Read all case.json file in case folder.

        Args:
            file_name (str): case file name

        Returns:
            Dict: decode json data
        """
        try:
            with open(self.path + file_name, encoding='utf-8') as file:
                return json.load(file)
        except Exception as err:
            print(err)

    def make_cases_info(self):
        """ Convert test case data to desired format.

        Returns:
            list: test case json data
        """
        all_case_enum = []
        for file in self.get_all_cases():
            class_name = file.split('.')[0]
            all_case_enum.append({class_name: self.read_case_json(file)})
        return all_case_enum

class CasesContainer:
    def __init__(self, body):
        self.body = body

    def __repr__(self) -> str:
        return 'CasesContainer<{}:{}>'.format(
            self.body.get('class_name'),
            self.body.get('methods_name')
        )
