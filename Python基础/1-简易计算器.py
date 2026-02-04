"""
创建一个能进行基本计算的程序
要求：
用户可以选择要进行的操作（加、减、乘、除）
输入两个数字
输出计算结果
处理除零错误
可以连续计算或退出
扩展：
添加幂运算、平方根
支持括号（先乘除后加减）
"""
from logging import exception
import math
def calculator():
    calculate_flag = 1
    while calculate_flag:
        a = float(input('请输入第一个数'))
        b = float(input('请输入第二个数'))
        operator = input('请输入你想使用的运算符+、-、*、/、^、平方根')
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
        elif operator == '平方根':
            # print(math.pow(a,b))
            print(a**0.5)
            calculate_flag = 0
        else:
            print('没有匹配到指定的运算符')
        action = input('请指定下一步操作：1.继续运算,否则任意键退出')
        if action == '1':
            calculate_flag = 1

def advance_caculator():
#     用户输入一串算式，我能匹配出数字和字符并计算出结果
    str = input('请输入一串计算式')

if __name__ == '__main__':
    # calculator()
    advance_caculator()