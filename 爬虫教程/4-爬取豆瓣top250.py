import re
import requests
import csv
import time
def doubantop250():
    a = [x*25 for x in range(0,9)]
    # print(a)
    obj = re.compile(r'<span class="title">(?P<name>.*?)</span>'
                     r'.*?<span class="rating_num" property="v:average">(?P<rate>.*?)</span>'
                     r'.*?<span>(?P<number>.*?)人评价</span>', re.S)
    data = []
    with open('top250.csv', 'w', newline='',encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        for i in a:
            url = f'https://movie.douban.com/top250?start={i}&filter='
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
            }
            with requests.get(url,headers=headers) as resp:
                ret = obj.finditer(resp.text)
                for i in ret:
                    temp = [i.group('name'), i.group('rate'), i.group('number')]
                    data.append(temp)
                print(data)
                csvwriter.writerows(data)
            time.sleep(1)

if __name__=='__main__':
    doubantop250()