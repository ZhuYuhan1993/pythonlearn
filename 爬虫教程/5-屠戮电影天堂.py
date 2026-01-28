import csv
import re

import requests
import time
def dytt():
    url = 'https://www.dytt8899.com'
    obj = re.compile(r'2026必看热片.*?<ul>.*?(?P<data>.*?)</ul>',re.S)
    obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
    obj3 = re.compile(r'<div class="title_all"><h1>(?P<name>.*?)</h1></div>.*?'
                      r'.*?<!--xunleiDownList Start-->.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<magnet>.*?)">magnet',re.S)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
    }
    child_href = []
    data = []
    with open('dytt.csv','w',encoding='utf-8-sig',newline='') as f:
        csvwriter = csv.writer(f)
        with requests.get(url,headers=headers) as r:
            r.encoding='gb2312'
            result = obj.finditer(r.text)#找到网页中ul标签框住的部分，这里只有一个地方满足条件
            for i in result:
                result1 = obj2.finditer(i.group('data'))#找到data下面的href
                for j in result1:
                    child_href.append(url+j.group('href'))
        # 爬取子页面中的下载链接
        for i in child_href:
            with requests.get(i,headers=headers) as rr:
                rr.encoding='gb2312'
                result2 = obj3.finditer(rr.text)
                for j in result2:
                    data.append([j.group('name'),j.group('magnet')])
            # time.sleep(1)
        csvwriter.writerows(data)


if __name__=='__main__':
    dytt()