"""
ERP项目： 使用cookies鉴权

"""

import requests

session = requests.Session() # 会话的对象  使用的发送接口请求 会自动传递cookies

# ERP项目登录 -- form格式数据
url = "	http://erp.lemonban.com/user/login"
meth = "post"
param = {"loginame":"test123","password":"e10adc3949ba59abbe56e057f20f883e"}
resp = session.request(meth,url,data=param) # data接受form数据
# resp = requests.request(meth,url,data=param)
print(resp.json())

#添加角色的接口
url = "http://erp.lemonban.com/role/add"
method = "post"
data = {"info":'{"name":"22"}'}
resp = session.request(method,url,data=data)
# resp = requests.request(method,url,data=data)
print(resp.text)