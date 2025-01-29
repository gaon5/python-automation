import requests
from jsonpath import jsonpath
from tools.handle_path import excel_path
from tools.handle_excel import read_excel

case_all = read_excel(excel_path, "order flow")

# 1. Login

json = {"principal":"lemon_py","credentials":"12345678","appType":3,"loginType":0}
url = 'http://shop.lemonban.com:8107/login'
res = requests.request('post', url, json=json)
print("The result of Login is", res.json())
access_token = jsonpath(res.json(), "$..access_token")[0]
print(access_token)
token_type = jsonpath(res.json(), "$..token_type")[0]
print(token_type)
headers = {'Authorization': token_type + access_token, 'Accept-Language': 'zh'}

# 2. Search

url = 'http://shop.lemonban.com:8107/search/searchProdPage'
param = {"prodName": "精华液"}
res = requests.request("get", url, params=param)
print("The result of Search is", res.json())
prodId = jsonpath(res.json(), "$..prodId")[0]


# 3. Product detailed page
url = 'http://shop.lemonban.com:8107/prod/prodInfo'
param = {"prodId": prodId}
res = requests.request("get", url, params=param)
print("The result of detailed product info is", res.json())
skuId = jsonpath(res.json(), "$..skuId")[0]

# 4. add to cart
json = {
 "basketId":0,
 "count":1,
 "prodId":prodId,
 "shopId":1,
 "skuId":skuId
 }
url = 'http://shop.lemonban.com:8107/p/shopCart/changeItem'
res = requests.request("post", url, headers=headers, json=json)
print("The result of adding to cart is", res.text)

# 5. check cart - get basketId
url = 'http://shop.lemonban.com:8107/p/shopCart/info' 
json = []
res = requests.request("post", url, headers=headers, json=json)
print("The result of check cart info is", res.json())
basketId = jsonpath(res.json(), "$..basketId")[0]
print("basketId is", basketId)

# 6. Calculate products
url = 'http://shop.lemonban.com:8107/p/order/confirm'
json = {"addrId": 0,
"basketIds": [basketId],
"couponIds": [],
"isScorePay": 0,
"userChangeCoupon": 0,
 "userUseScore": 0
 }
res = requests.request("post", url, headers=headers, json=json)
print("The result of calculate products is", res.json())

# 7. Submit order
url = 'http://shop.lemonban.com:8107/p/order/submit'
json = {"addrId": 0,
"basketIds": [basketId],
"couponIds": [],
"isScorePay": 0,
"userChangeCoupon": 0,
 "userUseScore": 0
 }
res = requests.request("post", url, headers=headers, json=json)
print("The result of order submitted is", res.json())



