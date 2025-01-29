from tools.handle_excel import read_excel
from tools.handle_path import excel_path
import requests
import pytest
import json
from jsonpath import jsonpath
from tools.handle_assert import response_assert
from tools.handle_api_request import api_request
from tools.handle_mysql import HandleMysql
from tools.handle_replace_variable import replace_variable
from tools.handle_db_assert import db_assert


# step 1: get the list of all cases
case_all = read_excel(excel_path, "register4")

@pytest.mark.parametrize("case", case_all)
def test_register(case):

    resp = api_request(case)

    expected_result_str = case["Expected Result"]
    db_assert_str = case["Database Assertion"]

    # resp = requests.request(method,url,headers=eval(header),json=eval(param))
    response_assert(resp, expected_result_str)
    db_assert(db_assert_str)



