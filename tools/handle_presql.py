import json
from tools.handle_mysql import HandleMysql
from data.envi_data import EnviVariable
from data.setting import my_db
from loguru import logger
import re
from tools.handle_replace_variable import replace_variable


def extract_code(sql_data):
    if sql_data is None:
        logger.info("No sql to be extracted")
        return
    logger.info("-------Presql processing------")
    sql_extracted = json.loads(sql_data)
    for k, v in sql_extracted.items():
        mark_list = re.findall("#(.*?)#", v)
        if mark_list:
            v = replace_variable(v)

        sql_result = HandleMysql(**my_db).query_data(v)
        if sql_result is None:
            logger.info("no data extracted from database")
            return
        logger.info(f"Result from database: {sql_result}")
        for i, j in sql_result.items():
            setattr(EnviVariable, i, j)
            logger.info(f"Environment variables: {EnviVariable.__dict__}")

if __name__ == "__main__":
    sql_extracted = """{"mobile_code":
"select mobile_code  from tz_sms_log where user_phone='15368201528' order by rec_date desc limit 1;"}"""
    extract_code(sql_extracted)









