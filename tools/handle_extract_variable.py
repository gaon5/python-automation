# 登录结果 --字典结果的数据 resp.json()
import json
from loguru import logger

from jsonpath import jsonpath
from data.envi_data import EnviVariable


def extract_variable(response, extracted_data_str):
    if extracted_data_str is None:
        logger.info("no data to be extracted.")
        return
    logger.info("-------Extracting variable starts------")
    extracted_data_dic = json.loads(extracted_data_str)
    logger.info(f"Data converted to dictionary: {extracted_data_dic}")
    for k, v in extracted_data_dic.items():
        result = None
        if v == "text":
            result = response.text
        elif v.startswith("$"):
            result = jsonpath(response.json(), v)[0]
        logger.info(f"data extracted from db is {result}")
        setattr(EnviVariable, k, result)
    logger.info(f"class property after extraction: {EnviVariable.__dict__}")

if __name__ == "__main__":
    response = {"access_token": "0efdce50-0e2f-4ed0-b4d1-944be5ab518a",
                "token_type": "bearer", "refresh_token": "4bfc3638-e7e4-4844-a83d-c0f8340bc146",
                "expires_in": 1295999,
                "pic": "http://mall.lemonban.com:8108/2023/09/b5a479b28d514aa59dfa55422b23a6f0.jpg",
                "userId": "46189bfd628e4a738f639017f1d9225d", "nickName": "lemon_auto", "enabled": True}
    extracted_data = '{"access_token":"$..access_token","token_type":"$..token_type"}'
    extract_variable(response, extracted_data)









