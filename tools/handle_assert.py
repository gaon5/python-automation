from tools.handle_excel import read_excel
from tools.handle_path import excel_path
import requests
import pytest
import json
from jsonpath import jsonpath
from loguru import logger
from tools.handle_replace_variable import replace_variable


def response_assert(resp, expected_result_str):

    logger.info("Starting assertion process")
    if expected_result_str is None:
        logger.info("This case doesn't need assertion.")
        return
    expected_result_str = replace_variable(expected_result_str)
    expected_result_dic = json.loads(expected_result_str)

    for k, v in expected_result_dic.items():
        actual_result = None
        if k.startswith("$"):
            actual_result = jsonpath(resp.json(), k)[0]
            logger.info(f"Actual result: {actual_result}")
            logger.info(f"Expected result: {v}")
            try:
                assert actual_result == v
                logger.info("Assertion Successful")
            except AssertionError as e:
                logger.info("Assertion failed.")
                raise e
        elif k == "text":
            actual_result = resp.text
            logger.info(f"Actual result: {actual_result}")
            logger.info(f"Expected result: {v}")
            try:
                assert actual_result == v
                logger.info("Assertion Successful")
            except AssertionError as e:
                logger.info("Assertion failed.")
                raise e







