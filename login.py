import requests

print("这个是电信，如果你是移动，学号即为你的手机号，今日校园密码为空，六位密码正常输入")
username=input("输入你的学号")
stupasswd=input("输入你的今日校园密码")
password=input("输入你的六位密码")
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://10.10.10.52",
    "Pragma": "no-cache",
    "Referer": "http://10.10.10.52/eportal/index.jsp?wlanuserip=2f4d7723c7fd19b1049235d23ac312f9&wlanacname=5a85791c59bcedb6c5dc542474c4ecc7&ssid=&nasip=80b4f717eedd90b8eb2de8bfc5e1582c&snmpagentip=&mac=2c5c15c91ca8747902aff07f6b3f001e&t=wireless-v2&url=709db9dc9ce334aa02a9e1ee58ba6fcf3bc3349e947ead368bdd021b808fdbac30c65edaa96b0727&apmac=&nasid=5a85791c59bcedb6c5dc542474c4ecc7&vid=34326c36d2d214a7&port=507e3765dc813f4c&nasportid=5b9da5b08a53a5405fcca25f7e4ce1442a020aa74cfe06842ff842146c6784e9759a0ffcc014c9d7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
}
cookies = {
    "EPORTAL_AUTO_LAND": "",
    "EPORTAL_COOKIE_DOMAIN": "",
    "EPORTAL_COOKIE_USERNAME": username,
    "EPORTAL_COOKIE_PASSWORD": stupasswd,
    "EPORTAL_COOKIE_SAVEPASSWORD": "true",
    "EPORTAL_USER_GROUP": "null",
    "servicesJsonStr": f"{username}%40%25%25username%40%25%25%E7%94%B5%E4%BF%A1",
    "EPORTAL_COOKIE_SERVER": "%E7%94%B5%E4%BF%A1",
    "EPORTAL_COOKIE_SERVER_NAME": "%E7%94%B5%E4%BF%A1",
    "EPORTAL_COOKIE_OPERATORPWD": "470338",
    "JSESSIONID": "B3A8F2191A5236FCD78E661C1FFBA9F8"
}
url = "http://10.10.10.52/eportal/InterFace.do"
params = {
    "method": "login"
}
data = {
    "userId": username,
    "password": stupasswd,
    "service": "%E7%94%B5%E4%BF%A1",
    "queryString": "wlanuserip%3D2f4d7723c7fd19b1049235d23ac312f9%26wlanacname%3D5a85791c59bcedb6c5dc542474c4ecc7%26ssid%3D%26nasip%3D80b4f717eedd90b8eb2de8bfc5e1582c%26snmpagentip%3D%26mac%3D2c5c15c91ca8747902aff07f6b3f001e%26t%3Dwireless-v2%26url%3D709db9dc9ce334aa02a9e1ee58ba6fcf3bc3349e947ead368bdd021b808fdbac30c65edaa96b0727%26apmac%3D%26nasid%3D5a85791c59bcedb6c5dc542474c4ecc7%26vid%3D34326c36d2d214a7%26port%3D507e3765dc813f4c%26nasportid%3D5b9da5b08a53a5405fcca25f7e4ce1442a020aa74cfe06842ff842146c6784e9759a0ffcc014c9d7",
    "operatorPwd": password,
    "operatorUserId": "",
    "validcode": "",
    "passwordEncrypt": "false"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data, verify=False)

print(response.text)
res  = response.json()
if not res['message']:
    print('登录成功')
elif res['message'].find(username) != -1:
    print(f'账号{username}已经在线！')
else:
    print('登录失败')
