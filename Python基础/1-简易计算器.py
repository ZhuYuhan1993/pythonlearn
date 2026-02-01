"""
创建一个能进行基本计算的程序
要求：
1. 让用户输入两个数字
2. 计算这两个数字的和、差、积、商
3. 注意：input()得到的是字符串，需要转换
"""
from logging import exception
import math
def calculator():
    calculate_flag = 1
    while calculate_flag:
        a,b = input('请输入两个数字，用空格隔开').split()
        a = int(a)
        b = int(b)
        operator = input('请输入你想使用的运算符+、-、*、/、^、')
        if operator == '+':
            print(a+b)
            calculate_flag = 0
        elif operator == '-':
            print(a-b)
            calculate_flag = 0
        elif operator == '*':
            print(a*b)
            calculate_flag = 0
        elif operator == '/':
            if b!=0:
                print(a/b)
                calculate_flag = 0
            else:
                print('b为0，不能作分母')
                calculate_flag = 0
        elif operator == '^':
            # print(math.pow(a,b))
            print(a**b)
            calculate_flag = 0

        else:
            print('没有匹配到指定的运算符')
        action = input('请指定下一步操作：1.继续运算,否则任意键退出')
        if action == '1':
            calculate_flag = 1

if __name__ == '__main__':
    calculator()