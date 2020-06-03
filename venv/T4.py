#-*- coding =utf-8 -*-
#@time: 20/06/02  21:32
#@AUTER: branch
#@File:  T4.py
#@Sofeware: PyCharm
import requests

params={"wd": "周杰伦", "ie": "utf-8"}
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
res = requests.get("https://www.baidu.com/s",params=params,headers=headers)

print(res.status_code)
print(res.request.url)