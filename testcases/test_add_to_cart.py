# print(resp.status_code)
import allure
import requests
from jsonpath import jsonpath
from tools.handle_path import excel_path
from tools.handle_excel import read_excel
import pytest
from tools.handle_api_request import api_request
from tools.handle_assert import response_assert
from tools.handle_extract_variable import extract_variable

case_all = read_excel(excel_path, "add to cart")
@allure.suite("add to cart")
@allure.title("{case[Test Case Title]}")
@pytest.mark.parametrize("case", case_all)
def test_add_to_cart(case):

    resp = api_request(case)

    expected_result_str = case["Expected Result"]

    print("expected_result:", expected_result_str)

    # resp = requests.request(method,url,headers=eval(header),json=eval(param))
    response_assert(resp, expected_result_str)


