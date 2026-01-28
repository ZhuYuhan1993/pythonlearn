'''
https://hksclz.com/groceries/index
用bs4爬2024年一月份的菜价
'''
from bs4 import BeautifulSoup
import requests
import csv
import time
def getprice():
    data = []
    url_set = []
    number = list(range(1,21))
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
    }
    for i in number:
        datestr = f'2026-01-{i:02d}'
        child_url = f'https://hksclz.com/groceries/index?date={datestr}'
        url_set.append(child_url)
    for url in url_set:
        with requests.get(url,headers=headers) as r:
            soup = BeautifulSoup(r.text,'html.parser')
            tables = soup.find_all('table')
            # print(len(table[0].find_all('tr')))
            for table in tables:
                trs = table.find_all('tr')
                for tr in trs:
                    tds = tr.find_all('td')
                    if(len(tds)!=0):
                        date = tds[0].text
                        name = tds[1].text
                        price = tds[2].text
                        data.append([date,name,price])
        print('爬取完一个')
        time.sleep(1)


    with open('price.csv', 'w', newline='', encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(data)
if __name__=='__main__':
    getprice()