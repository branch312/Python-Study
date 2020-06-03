#-*- coding =utf-8 -*-
#@time: 20/06/02  22:22
#@AUTER: branch
#@File:  T5.py
#@Sofeware: PyCharm
import requests

if __name__ == '__main__':
    target = "http://fanyi.baidu.com/"
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    print(req.text)