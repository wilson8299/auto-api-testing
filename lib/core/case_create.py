import json
import os, sys
sys.path.append(os.getcwd())

import lib.config.config as config

class FileMeta():
    def __init__(self):
        self.header = None
        self.content = None

    def __enter__(self):
        self.header = open(config.HEADERS_TEMPLATE_PATH, encoding='utf-8')
        self.content =  open(config.CONTENT_TEMPLATE_PATH, encoding='utf-8')
        self.head = self.header.read()
        self.cont = self.content.read()
        return self

    def make_testcase_py(self, class_name, func_name, desc):
        """ Change template.txt to python file.

        Args:
            class_name (str): test class name
            func_name (str): test function name
            desc (str): test function description
        """

        filepath = config.TESTCASES_PATH + class_name + '.py'
        if not os.path.exists(filepath):
            with open(filepath, 'w', encoding='utf-8') as file:
                class_name = class_name.title().replace('_', '')
                file.write(self.head.format(class_name, class_name))
        
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(self.cont.format(func_name, desc))

    def generating_template(self):
        """ Get test case json data through config.TestCaseLoader.
            Returns a generator object.
        """
        tags = json.loads(repr(config.TestCaseLoader()))
        for item in tags:
            for class_name, body in item.items():
                for func_name, body in body.items():
                        yield config.CasesContainer({
                            'class_name': class_name,
                            'methods_name': func_name,
                            'desc': body.get('desc'),
                            'body': body
                        }), self.make_testcase_py

    def __exit__(self, exc_type, exc_value, traceback):
        self.header.close()
        self.content.close()
        del self.head
        del self.cont

class CreateCase:
    def __init__(self) -> None:
        self.data = []

    def create(self):
        """ Call generating_template & make_testcase_py function 
        """
        with FileMeta() as file:
            for item in file.generating_template():
                obj, func = item
                func(
                    obj.body['class_name'],
                    obj.body['methods_name'],
                    obj.body['desc']
                )

    def load(self):
        with FileMeta() as file:
            for item in file.generating_template():
                obj, _ = item
                self.data.append(obj.body)

    def __iter__(self):
        return iter(self.data)

    def __call__(self):
        return next(self.data)

    def __repr__(self) -> str:
        return json.dumps(self.data)
