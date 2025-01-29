from faker import Faker
from tools.handle_mysql import HandleMysql
from data.setting import my_db
from data.envi_data import EnviVariable
from loguru import logger

class GenerateData:

    def generate_unregistered_phone_num(self):
        fk = Faker(locale="zh_CN")
        while True:
            phone_number = fk.phone_number()
            sql = f"SELECT user_phone FROM `tz_sms_log` WHERE user_phone = {phone_number} ORDER BY rec_date desc;"
            result = HandleMysql(**my_db).query_data(sql)
            if result is None:
                logger.info(f"Unregistered phone number: {phone_number}")
                return phone_number

    def generate_unregistered_user_name(self):
        fk = Faker(locale="zh_CN")
        while True:
            # user_name = fk.user_name()
            user_name = fk.pystr(min_chars=4, max_chars=6)
            sql = f"SELECT user_name FROM `tz_user` WHERE user_name = '{user_name}';"
            result = HandleMysql(**my_db).query_data(sql)
            if result is None:
                logger.info(f"Unregistered user name: {user_name}")
                return user_name
if __name__ == '__main__':

    GenerateData().generate_unregistered_user_name()
    # GenerateData().generate_unregistered_phone_num()



