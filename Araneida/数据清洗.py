# -- coding: utf-8 --
import requests
from lxml import etree
import json
import re
import openpyxl


        # 目标url
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/"

        # 伪装请求头
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36 '
        }
        # 发出get请求
response = requests.get(url, headers=headers).text
time_in = re.findall('"mapLastUpdatedTime":"(.*?)"', response)[0]
time_out = re.findall('"foreignLastUpdatedTime":"(.*?)"', response)[0]
html = etree.HTML(response)
# 解析数据
result = html.xpath('//script[@type="application/json"]/text()')
result = result[0]
result = json.loads(result)
print(result['component'][0]['caseList'])














