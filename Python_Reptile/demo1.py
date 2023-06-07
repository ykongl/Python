import re
import urllib.request

from readConfig import get_all_for_sql

import pandas as pd
import requests

url = 'https://image.baidu.com/search/albumslist?tn=albumslist&word=%E4%BA%BA%E7%89%A9&album_tab=%E4%BA%BA%E7%89%A9' \
      '&rn=15&fr=searchindex_album'

response = requests.get(url)

images = re.findall(r'https://.*\.jpg', response.text)
x = 0
path = 'E:/mjy-workspace/python/Python_Reptile/resource/img'
for img in images:
    urllib.request.urlretrieve(img, '{}{}.jpg'.format(path, x))
    x = x + 1
