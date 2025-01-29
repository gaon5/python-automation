import allure
import requests
import json
from tools.handle_path import file_path
from loguru import logger
from tools.handle_extract_variable import extract_variable
from tools.handle_replace_variable import replace_variable
from tools.handle_mysql import HandleMysql
from data.setting import my_db
from data.envi_data import EnviVariable
from tools.handle_presql import extract_code

@allure.step("Handle api request")
def api_request(case, token=None, sql=None):
    method = case["Method"]
    url = case["URL"]
    param = case["Parameters"]
    header = case["Headers"]

    sql_extracted = case["Sql Extracted"]
    extract_code(sql_extracted)

    header = replace_variable(header)
    param = replace_variable(param)
    url = replace_variable(url)

    if header is not None:
        header = json.loads(header)
        if token is not None:
            header["Authorization"] = token
    if param is not None:
        param = json.loads(param)

    logger.info("---Request Info----")
    logger.info(f"Request header is: {header}")
    logger.info(f"Request body is: {param}")
    logger.info(f"Request method is: {method}")
    logger.info(f"Request url is: {url}")





    resp = None
    if method.lower() == "get":
        resp = requests.request(method, url, headers=header, params=param)
    elif method.lower() == "post":
        if header["Content-Type"] == "application/json":
            resp = requests.request(method, url, headers=header, json=param)
        elif header["Content-Type"] == "application/x-www-form-urlencoded":
            resp = requests.request(method, url, headers=header, data=param)
        elif header["Content-Type"] == "multipart/form-data":
            header.pop("Content-Type")
            file_name = param["filename"]
            param_file = {"file": open(file_path/file_name, mode="rb")}
            logger.info(f"File upload parameter: {param_file}")
            logger.info(f"Header of File upload: {header}")

            resp = requests.request(method, url, headers=header, files=param_file)
    elif method.lower() == "put":
        resp = requests.request(method, url, headers=header, json=param)

    logger.info("---Response---")
    if resp.text:
        logger.info(f"Response text: {resp.text}")
    if resp.status_code:
        logger.info(f"Response code: {resp.status_code}")


    extract_variable(resp, case["Variable Extracted"])

    return resp






