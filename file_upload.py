
import requests
from tools.handle_path import file_path


# # 电商登录-- json格式数据
# url = "http://shop.lemonban.com:8107/login"
# meth = "post"
# header = {"Accept-Language":"zh","Content-Type":"application/json; charset=UTF-8"}
# param = {"principal":"lemon_py","credentials":"12345678","appType":3,"loginType":0}
#
# resp = requests.request(meth,url,headers=header,json=param)
# print(resp)
# print(resp.text)
# print(resp.json())
# print(resp.headers)
# print(resp.status_code)
#
# # ERP项目登录 -- form格式数据
# url = "	http://erp.lemonban.com/user/login"
# meth = "post"
# header = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
# param = {"loginame":"test123","password":"e10adc3949ba59abbe56e057f20f883e"}
# resp = requests.request(meth,url,headers=header,data=param) # data接受form数据
# print(resp)
# print(resp.text)
# print(resp.json())
# print(resp.headers)
# print(resp.status_code)

# 先执行登录接口 电商登录-- json格式数据
url = "http://shop.lemonban.com:8107/login"
meth = "post"
header = {"Accept-Language":"zh","Content-Type":"application/json; charset=UTF-8"}  # 一定要是字典的格式
param = {"principal":"lemon_py","credentials":"12345678","appType":3,"loginType":0}
resp = requests.request(meth,url,headers=header,json=param) # json接受
# print("登录的结果",resp.json()) # 得到的结果是 字典格式
# 通过字典取值 得到access_token 的值 --token
token = resp.json()["access_token"]
print(token)
#
# # 电商上传接口-- 二进制流格式数据
# url = "http://shop.lemonban.com:8107/p/file/upload"
# meth = "post"
# #  在上传接口的头部 带上这个token
# header = {"Accept-Language": "zh", "Authorization": "bearer " + token, "Content-Type": "multipart/form-data"}  # 一定要是字典的格式
# header.pop("Content-Type") #删除这个Content-Type头部
# # param_file = {"file":("python70.png",open("code.png",mode="rb"))}  # 按照格式写好文件参数
# file_name = "59kb.png"
# param_file = {"file": open(file_path/file_name, mode="rb")}
# resp = requests.request(meth, url, headers=header, files=param_file) # json接受
# # print(resp.text) #获取响应正文
# print(resp.json())   #如果响应结果是一个son格式的数据，可以通过json()方法转化为python的字典 就可以进行字典取值
