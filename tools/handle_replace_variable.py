import re
from data.envi_data import EnviVariable
from loguru import logger
from tools.handle_generate_data import GenerateData


def replace_variable(str_data):
    if str_data is None:
        logger.info("data passed through is empty. no need for replacement.")
        return

    mark_list = re.findall("#(.*?)#", str_data)
    logger.info(f"the list of marks is {mark_list}")
    if mark_list:

        logger.info("------Start replacing-------")
        logger.info(f"The original data is {str_data}")

        for mark in mark_list:
            value = None
            if mark.endswith("()"):
                value = f"GenerateData().{mark}"
                value = eval(value)
                str_data = str_data.replace(f"#{mark}#", str(value))
                mark = mark[:-2]
                setattr(EnviVariable, mark, value)
                logger.info(f"Environment variables: {EnviVariable.__dict__}")
            elif hasattr(EnviVariable, mark):
                value = getattr(EnviVariable, mark)
                logger.info(f"The value for dynamic variable {mark} is {value}")
                str_data = str_data.replace(f"#{mark}#", str(value))
        logger.info(f"The data replaced with dynamic variable is {str_data}")

    else:
        logger.info("no data needs to be replaced.")
    return str_data

if __name__ == "__main__":
    class EnviVariable:
        prodId = 5069
        skuId = 5528


    str_data = '{"mobile":"#generate_unregistered_phone_num()#"}'
    replace_variable(str_data)

