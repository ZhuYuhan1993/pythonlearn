def temp_converter():
    a = int(input('请输入转换类型：1.摄氏转华氏,2.华氏转摄氏：'))
    temp = float(input('输入温度：'))
    if a == 1:
        b = temp*1.8+32
        print(f'华氏温度为：{b}')
    elif a==2:
        b = (temp-32)/1.8
        print(f'摄氏温度为：{b}')
    else:
        print('未指定正确的转换类型')

if __name__ == '__main__':
    temp_converter()