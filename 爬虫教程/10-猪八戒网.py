'''
拿到页面源代码
提取和解析数据

'''
import requests
from lxml import etree
# url = 'https://www.zbj.com/fw/?k=saas'
# with requests.get(url) as resp:
#     # print(resp.text)
#     tree = etree.HTML(resp.text)
#     print(tree.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/span/text()'))
    # # 拿到每个服务商的div
    # divs = tree.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')
    # for div in divs:
    #     print(div.xpath('./div/div[3]/div[1]/span/text()'))

# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/span
import requests

url = 'https://www.zbj.com/fw/?k=saas'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

resp = requests.get(url, headers=headers)

# 保存页面内容查看
with open('zbj_page.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)

# 检查页面中是否有关键词
text = resp.text.lower()
keywords = ['¥', 'price', '商品', '服务', 'saas']
found_keywords = []

for keyword in keywords:
    if keyword in text:
        found_keywords.append(keyword)

print(f"在页面中找到的关键词: {found_keywords}")
print(f"页面大小: {len(resp.text)} 字符")

# 检查是否有常见的商品列表容器
if '<div class="product' in resp.text or '<div class="item' in resp.text:
    print("✓ 页面中有商品相关的div容器")
else:
    print("✗ 页面中没有找到商品相关的div容器")
