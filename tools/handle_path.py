"""
这个是做路径处理的公共方法

# 路径处理针对日志文件  报错文件 用例excel文件等 是个公共的方法 -- 封装在tools工具下作为一个方法。
"""
from pathlib import Path

# 日志文件的路径处理 --因为单独放一个日志的路径管理 -- 代码分层管理思想
log_path = Path(__file__).absolute().parent.parent/"logs"/"Lmall_api.log"

# excel路径
excel_path = Path(__file__).absolute().parent.parent/"data"/"testcase_mall.xlsx"

file_path = Path(__file__).absolute().parent.parent/"data"

report_path = Path(__file__).absolute().parent.parent/"reports_allure"

if __name__ == '__main__':
    print(log_path)
    print(excel_path)
    print(file_path)