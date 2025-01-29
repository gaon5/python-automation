"""
allure使用在pytest.main()里家参数：
* 运行用例的时候就会自动生成结果文件： 使用pytest运行的参数：加一个参数：--alluredir=相对于run.py所在目录rootdir的目录
* 在当前目录下就会生成一个reports目录下的allure目录，然后结果文件都生成在里面。
   -json文件给allure看的 我们不需要看 看不懂。
* 这些只是结果文件，还没有生成报告，接下来要allure来解析这些结果文件 生成allure的报告 --HTML页面给人看的
  - allure serve 解析json文件  生成HTML页面给人看的报告
* 使用allure命令生成报告：
    * cmd里或者terminal里，跳转到rootdir目录；==cd 切换目录
    * 运行命令： allure serve allure_report=== serve后面跟的是自己定义的结果文件的目录，相对于你目前所在位置；
    * "--clean-alluredir"  清楚历史执行json'文件记录。 --一般都会加上。

最后执行自动化测试都会结合Jenkins进行持续集成测试-就不需要allure serve 生成；

测试报告两种报错：
1、产品缺陷： product defects -- 产品项目的bug，开发修复的
2、用例缺陷： test defects -- 用例脚本本身bug，自动化测试框架搭建者修复 -优化自动化框架的

"""
import pytest
from tools.handle_path import report_path
from loguru import logger
from tools.handle_path import log_path

logger.add(sink=log_path,
           encoding="utf8",
           level="INFO",
           rotation='10kb',
           retention=6)

pytest.main(["-v","-s",f"--alluredir={report_path}"
                ,"--clean-alluredir"])

# allure serve .\reports_allure\
