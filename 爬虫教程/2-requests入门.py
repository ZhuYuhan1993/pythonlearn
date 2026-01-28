import requests

url = 'https://www.sogou.com/web?query=python'
resp = requests.get(url)
print(resp.text)
resp.close()