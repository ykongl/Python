import re
import urllib.request
import requests

import pandas as pd


def get_content(url, n):
    response = requests.get(url)

    context = re.findall(r'chapterContent:".*?"', response.text)

    path = 'E:/mjy-workspace/python/Python_Reptile/resource/'

    file = open(path + str(n) + ".txt", "w", encoding='gbk')

    for c in context:
        s = c.replace("chapterContent:", "")
        s = s.replace("\\u003Cp\\u003E", "")
        s = s.replace("\\r\\u003C\\u002Fp\\u003E", "")
        s = s.replace("\\u003C\\u002Fp\\u003E", "")
        s = s.replace('"', '')
        file.write(s)

    file.close()


def get_number(base_url):
    res = requests.get(base_url)
    number = re.findall("目录(.\\d*)", res.text)
    num = number[0].replace("(", "")
    for i in range(1, int(num)):
        get_content(base_url + str(i), i)


if __name__ == '__main__':
    get_number('https://book.qq.com/book-detail/46888796')
