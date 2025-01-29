import hashlib
import requests
import base64
#
# password = "123456"
# password_by = password.encode("utf8")
#
# passwd_md5 = hashlib.md5(password_by).hexdigest()
#
# passwd_b64 = base64.b64encode(password_by)
# passwd_b64_str = passwd_b64.decode("utf8")
#
#
#
# url = "http://erp.lemonban.com/user/login"
# header = {"Content-Type":"application/x-www-form-urlencoded"}
# param = {"loginame":"test123","password":passwd_md5}
# resp = requests.request(method="post",url=url,headers=header,data=param)
# print(resp.text)


# with open("angels-87kb.png", mode="rb") as f:
#     pic_data = f.read()
#     print(pic_data)
#
#     pic_b64 = base64.b64encode(pic_data)
#     pic_str = pic_b64.decode()


"""
步骤如下：【RSA一般都会结合base64编码一起使用的】
第一步：读取公钥信息内容
第二步：通过RSA导入公钥信息，并返回公钥对象
第三步： 基于公钥创建RSA加密器对象
第四步：通过RSA加密器对象进行加密（加密前数据转换为二进制格式）
第五步：需要先进行base64编码，才可以转化为字符串可用文本
第六步： 将二进制数据转化为文本

"""
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5



data = "12345" # 待加密的数据
data_bytes = data.encode("UTF8")  #转化为二进制数据

# 第一步：读取公钥信息内容
with open("rsa_public_key.pem") as f:
    public_key_str = f.read()
    # 第二步：通过RSA导入公钥信息，并返回公钥对象
    public_key = RSA.importKey(public_key_str)
    # 第三步： 基于公钥创建RSA加密器对象
    pk = PKCS1_v1_5.new(public_key)
    # 第四步：通过RSA加密器对象进行加密（加密前数据转换为二进制格式）
    rsa_data = pk.encrypt(data_bytes)  # 这个是二进制的数据
    # 第五步：需要先进行base64编码，才可以转化为字符串可用文本
    base64_data = base64.b64encode(rsa_data)
    # 第六步： 将二进制数据转化为文本
    print(base64_data.decode("UTF8"))