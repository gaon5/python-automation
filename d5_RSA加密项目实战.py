"""
前程贷：lemon_v3 ，token和加密处理

timestamp+token+sign鉴权，
其中sign= RSA(token前50位+时间戳)

1、先登录接口，获取结果
{"code":0,"msg":"OK",
"data":{"id":6,"leave_amount":7697887.48,"mobile_phone":"13323231111",
"reg_name":"黑长直6","reg_time":"2023-02-14 13:34:46.0","type":1,
"token_info":{"token_type":"Bearer","expires_in":"2024-09-18 21:05:34",
"token":"eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjYsImV4cCI6MTcyNjY2NDczNH0.4H42c3VT_fCMDfd3fr9LdNt1o5bQrnrA71pAibVZ9lDaYRp014OHer_n0sy1qA4SMyDP4Modv7g8YLJRpqMrSg"}},
"copyright":"Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"}

2、充值接口
 - 头部要拼接token信息
 - member_id:动态获取用户登录后的用户id 也要从登录结果里提取。
 - timestamp: 时间戳，值为当前秒级时间戳
 - sign: RSA(token前50位+时间戳)

"""
import time

import requests
from jsonpath import jsonpath
from tools.handle_encrypt_rsa import encrypt_rsa


# 第一步：先登录，获取token信息
url = "http://api.lemonban.com:8788/futureloan/member/login"
header = {"X-Lemonban-Media-Type":"lemonban.v3","Content-Type":"application/json"}
param = {"mobile_phone": "13323231111","pwd": "12345678"}
resp = requests.request(method="post",url=url,json=param,headers=header)
print(resp.text)
# 第二步：提取token信息
token = jsonpath(resp.json(),"$..token")[0]
menber_id =jsonpath(resp.json(),"$..id")[0]
print(token,menber_id)

# 获取时间戳
ts = int(time.time())

#sign: RSA(token前50位+时间戳)
 # token前50位
token_sub = token[0:50]
print(token_sub)
# token前50位+时间戳
data = token_sub+str(ts)
# data = f"{token_sub}{ts}"
print(data)
# RSA(token前50位+时间戳)
sign = encrypt_rsa(data,"rsa_public_key.pem")
print(sign)

# 第三步： 发送充值接口请求
url = 'http://api.lemonban.com:8788/futureloan/member/recharge'
header = {"X-Lemonban-Media-Type":"lemonban.v3","Content-Type":"application/json",
          "Authorization":f"Bearer {token}"}
param = {"member_id": menber_id,"amount": 1000.0,"timestamp": ts,"sign": sign}
resp = requests.request(method="post",url=url,json=param,headers=header)
print(resp.text)
