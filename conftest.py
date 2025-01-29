"""
夹具共享conftest文件
- 不用导包 可以直接使用conftest里的夹具 自动发现夹具；

conftest.py的作用范围： conftest.py所在文件夹下面的所有用例。一般放在根目录下 或者testcases目录下都可以。
    * 也有可能在同一个项目中不同的目录下创建conftest.py文件 这也是可以的；那么也是在它目录下生效；
    * 超出了范围就会报错：E fixture 'class_setup_teardown' not found

习惯： 把conftest写在根目录下。 根目录下所有用例都可以共享夹具。

思考： 多个conftest都有夹具 优先用哪个？ -- 就近原则
当用例的模块也有夹具和conftest优先会用哪个夹具？
* 名字不一样，按照名字区分
* 名字一样，就近原则，优先用自己的夹具。
    * 1) 如果用例所在的测试文件中 找fixture，找到了就用
    * 2）如果1）中没有找到，就去当前文件所在目录下conftest.py找，找到了就用
    * 3）如果2）中没有找到，就去【当前文件所在目录的上一级目录】下contest.py找，找到了就用
    * 4）一直找到rootdir下面截止，没有找到 就报错。

"""
import pytest
import requests
from jsonpath import jsonpath


@pytest.fixture()  # 这个夹具类级别的夹具
def login_fixture():

    method = "post"
    url = "http://shop.lemonban.com:8107/login"
    param = {"principal": "lemon_py", "credentials": "12345678", "appType": 3, "loginType":0}
    resp = requests.request(method, url, json=param)
    access_token = jsonpath(resp.json(), "$..access_token")[0]
    token_type = jsonpath(resp.json(), "$..token_type")[0]
    token = token_type + access_token
    # headers = {'Authorization': token, 'Accept-Language': 'zh'}
    yield token
