import re
s = '我的电话是：10010， your电话是_10086'
lst = re.findall('.',s) # 匹配除换行符意外的任意字符
print(lst)
lst = re.findall('\w',s) # 匹配数字字母下划线
print(lst)
lst = re.findall('\d',s) # 匹配数字
print(lst)
lst = re.findall('\s',s) # 匹配任意的空白符
print(lst)

# 大写就是反着的意思
lst = re.findall('\W',s) # 匹配非数字字母下划线
print(lst)
lst = re.findall('\D',s) # 匹配非数字
print(lst)
lst = re.findall('\S',s) # 匹配非空白符
print(lst)

lst = re.findall('[abcdefg0123456789]',s)# 匹配中括号里面的字符组,取范围可以这么写[a-zA-Z0-9_]
print(lst)

a = 'a15675374478'
a1 = re.findall('^\d',a) #^ $分别是匹配字符的开始和结尾，做校验的时候比较常用
print(a1) #开头不是数字所以匹配不到

# 正则里面的量词
# * 0次或者多次
lst = re.findall('\d*',s)
print(lst)
# + 1次或者多次
lst = re.findall('\d+',s)
print(lst)
# ？0次或者1次
lst = re.findall('\d?',s)
print(lst)
# {n}重复n次
lst = re.findall('\d{2}',s) #匹配出连着2个数字的结果
print(lst)
# {n,} 重复n次或者更多次
lst = re.findall('\d{2,}',s)
print(lst)
#{n,m} 重复n次到m次
lst = re.findall('\d{2,3}',s)
print(lst)

#贪婪匹配和惰性匹配
# .* 贪婪匹配
# .*？惰性匹配
s1 = '玩儿吃鸡游戏，晚上一起上游戏，干嘛呢？打游戏啊'
lst = re.findall('玩儿.*游戏',s1)
print(lst)
lst = re.findall('玩儿.*?游戏',s1)
print(lst)

s = '我的电话是：10010， your电话是_10086'
lst = re.findall(r'\d+',s)# 加r防止系统将\当成转义
print(lst)
#finditer 返回迭代器，效率比列表高
it = re.finditer(r'\d+',s)
for i in it:
    print(i.group())

# search 返回的结果是match对象，那数据需要group ，找到一个结果就返回
se = re.search(r'\d+',s)
print(se.group())

# match
# se = re.match(r'\d+',s)
# print(se.group())#没匹配到，会报错

#预加载正则表达式
obj = re.compile(r'\d+')
ret = obj.finditer(s)
for i in ret:
    print(i.group())

l = '''
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>zhang</span></div>
<div class='jolin'><span id='3'>wang</span></div>
<div class='sylar'><span id='4'>zihu</span></div>
<div class='tory'><span id='5'>asd</span></div>
'''
obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<name>.*?)</span></div>",re.S)
ret = obj.finditer(l)
namelist = []
for i in ret:
    namelist.append(i.group('name'))
    print(i.group('name'))
print(namelist)