import re

import requests


def get_number(base_url):
    res = requests.get(base_url)
    number = re.findall("目录(.\\d*)", res.text)
    num = number[0].replace("(", "")
    print(num)
    print(res.text)

    print(re.findall('title=".*?章"', res.text))


if __name__ == '__main__':
    get_number('https://book.qq.com/book-detail/46888796')
