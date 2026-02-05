"""
项目1：计算器
### 基础要求
1. 支持加减乘除四种运算
2. 用户输入两个数字和一个运算符
3. 输出计算结果
4. 处理除零错误
### 完整要求
1. 支持连续计算（使用上一次结果）
2. 支持小数运算
3. 添加清零功能
4. 添加退格功能
### 扩展要求
1. 支持括号运算
2. 支持幂运算、平方根
3. 添加历史记录功能
4. 开发GUI界面
---
## 🎯 
"""
def basic_calculator():
    operator = input('请输入运算符号：')
    a = int(input('请输入第一个数字'))
    b = int(input('请输入第二个数字'))
    if operator == '+':
        print('a + b = ',a + b)
    elif operator == '-':
        print('a - b = ',a - b)
    elif operator == '*':
        print('a * b = ',a * b)
    elif operator == '/':
        if b != 0:
            print('a / b = ',a / b)
        else:
            print('b = 0不能做分母')
    else:
        print('没有该操作')
def complete_calculator():
    return
def advanced_calculator():
    return
if __name__ == '__main__':
    basic_calculator()
    # complete_calculator()
    # advanced_calculator()