import pytest
from tools.handle_excel import read_excel
from tools.handle_path import excel_path
import requests
from tools.handle_assert import response_assert
import json
from tools.handle_api_request import api_request
from tools.handle_db_assert import db_assert

case_all = read_excel(excel_path, "search")
@pytest.mark.parametrize("case", case_all)
def test_search(case):
    resp = api_request(case)
    expected_result_str = case["Expected Result"]
    db_assert_str = case["Database Assertion"]

    print("expected_result:", expected_result_str)

    # resp = requests.request(method,url,headers=eval(header),json=eval(param))
    response_assert(resp, expected_result_str)
    db_assert(db_assert_str)

