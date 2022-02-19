import os, sys
sys.path.append(os.getcwd())

from functools import wraps
from lib.core.recursion import GetDictParam
from lib.core.case_create import CreateCase
from lib.core.http_hanlder import http_handler

def test_case_runner(func):
    @wraps(func)
    def wrap(*args):
        """ Call http request function and make the result to dict.

        Returns:
            func: response result & test case assert. 
        """
        case_data = CreateCase()
        case_data.load()
        for item in iter(case_data):
            for _, value in item.items():
                if value == func.__name__:
                    client = http_handler(item.get('body'))
                    result = client.make_request_template()
                    return func(
                        *args,
                        response=result,
                        kwassert=item.get('body').get('assert')
                    )
    return wrap

def test_case_parse(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        response = kwargs.get('response')
        kwassert = kwargs.get('kwassert')
        tmp = tuple(kwassert.keys())
        result = GetDictParam.list_for_key_to_dict(*tmp, my_dict=response)

        exec_info = []
        for key, value in kwassert.items():
            exec_info.append([result[key], value])

        return func(*args, response=result, exec_text=exec_info)

    return wrap
