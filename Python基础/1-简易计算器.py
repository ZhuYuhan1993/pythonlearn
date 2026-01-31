"""
创建一个能进行基本计算的程序
要求：
1. 让用户输入两个数字
2. 计算这两个数字的和、差、积、商
3. 注意：input()得到的是字符串，需要转换
"""
from logging import exception

try:
    a,b = input('输入两个数字:').split()
except Exception as e:
    print(f"报错：{e}")
print(f'a+b:{int(a)+int(b)}')
print(f'a-b:{int(a)-int(b)}')
print(f'a*b:{int(a)*int(b)}')
if b!=0:
    print(f'a/b:{int(a)/int(b)}')
else:
    print(f'b为0')