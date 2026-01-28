from lxml import etree
tree = etree.parse("demo.html")
# result = tree.xpath("/html/body/ul/li/a/text()")
# result = tree.xpath("/html/body/ul/li[1]/a/text()")# xpath 从1开始数的
# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")# 根据标签属性筛选
# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")# 根据标签属性筛选
result = tree.xpath("/html/body/ol/li/a/@href")# 根据标签属性筛选
print(result)
ol_li_list = tree.xpath("/html/body/ol/li")
# print(ol_li_list)
for li in ol_li_list:
    # 从每个li中提取文字信息,现在是相对查找
    print(li.xpath('./a/text()'))
    # 拿a标签href的值 属性就是用@
    print(li.xpath('./a/@href'))
print(tree.xpath("/html/body/ul/li/a/@href"))