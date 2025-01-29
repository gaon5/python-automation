from tools.handle_excel import read_excel
from tools.handle_path import excel_path
import pytest
from tools.handle_assert import response_assert
from tools.handle_api_request import api_request
from loguru import logger
from tools.handle_db_assert import db_assert


# step 1: get the list of all cases
case_all = read_excel(excel_path, "upload")

#step 2: execute test cases using pytest
@pytest.mark.parametrize("case", case_all)
def test_upload(case):

    resp = api_request(case)

    expected_result_str = case["Expected Result"]
    db_assert_str = case["Database Assertion"]

    response_assert(resp, expected_result_str)
    db_assert(db_assert_str)



