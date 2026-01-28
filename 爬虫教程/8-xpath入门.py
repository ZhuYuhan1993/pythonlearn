# xpath 是xml文档中搜索内容的一门语言
# html是xml的一个子集
from lxml import etree

xml = '''
<book>
    <id>1</id>
    <name>shaishd</name>
    <price>1.23</price>
    <nick>ooo</nick>
    <author>
        <nick id = '1'>asd</nick>
        <nick id = '2'>wer</nick>
        <nick class='ksd'>32</nick>
        <nick class="qwe">3333</nick>
        <div>
            <nick>qwerrtdf</nick>
        </div>
        <span>
            <nick>sdsfgg</nick>
            <div>
                <nick>yiot</nick>
            </div>
        </span>
    </author>
    <partner>
        <nick id='ppc'>ppc</nick>
        <nick id="ppbc">ppbc</nick>
    </partner>
</book>

'''
tree = etree.XML(xml) #
# result = tree.xpath('/book')#/表示层级关系，第一个/是根节点
# result = tree.xpath('/book/name')#
# result = tree.xpath('/book/name/text()')#找标签内文本
# result = tree.xpath('/book/author/nick/text()')#只能找下一级
# result = tree.xpath('/book//nick/text()')# //后代 找book下面所有的nick
result = tree.xpath('/book/author/*/nick/text()')# /*通配符*表示这个位置替换成任意标签都行


print(result)
