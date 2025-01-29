from tools.handle_excel import read_excel
from tools.handle_path import excel_path
import requests
import pytest
import json
from jsonpath import jsonpath
from loguru import logger
from tools.handle_replace_variable import replace_variable
from data.envi_data import EnviVariable
from data.setting import my_db
from tools.handle_mysql import HandleMysql


def db_assert(db_assert_str):
    if db_assert_str is None:
        logger.info("This case doesn't need assertion.")
        return

    logger.info("===================Starting database assertion process==================")

    db_assert_str = replace_variable(db_assert_str)

    db_assert_dic = json.loads(db_assert_str)

    for k, v in db_assert_dic.items():
        sql_result_dic = HandleMysql(**my_db).query_data(k)
        if sql_result_dic is None:
            logger.info("There is no result retrieved from database.")
            return
        logger.info(f"The result from database: {sql_result_dic}")

        for i in sql_result_dic.values():
            actual_result = i
            logger.info(f"Actual Database result: {actual_result}")
            expected_result = v
            logger.info(f"Expected Database result: {expected_result}")
            try:
                assert actual_result == expected_result
                logger.info("Database assertion successful")
            except AssertionError as e:
                logger.error("Database assertion Failed")
                raise e


if __name__ == '__main__':
    db_assert_str = """{"select count(1) from tz_order where order_number = '1883380744534102016'":1,
"select is_payed from tz_order where order_number = '1883380744534102016'":1}"""
    db_assert(db_assert_str)







