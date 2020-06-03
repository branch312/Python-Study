#-*- coding =utf-8 -*-
#@time: 20/05/21  16:32
#@AUTER: branch
#@File:  T2.py
#@Sofeware: PyCharm


import urllib.request
# reponse=urllib.request.urlopen("http://www.baidu.com")
# print(reponse.read().decode("utf_8"))

date=bytes()
reponse=urllib.request.urlopen("http://httpbin.org/post")
print(reponse.read())
