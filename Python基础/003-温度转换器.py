"""
项目3：温度转换器

### 基础要求
1. 支持摄氏度↔华氏度转换
2. 用户选择转换方向
3. 输入温度值，输出转换结果

### 完整要求
1. 支持三种单位（摄氏度、华氏度、开尔文）
2. 批量转换功能
3. 显示温度描述（寒冷/舒适/炎热）
4. 添加常用温度对照表

### 扩展要求
1. 实时获取天气温度并转换
2. 温度历史记录和趋势分析
3. 自定义温度单位
4. 语音播报功能

---

## 🎯 
"""
def basic_temp_converter():
    flag = int(input('请输入转换类型（1.摄氏度转华氏度，2.华氏度转摄氏度）：'))
    temp = float('请输入温度：')
    if flag == 1:
        new_temp = temp*1.8+32
        print(f'摄氏度：{temp},华氏度：{new_temp}')
    else:
        new_temp = (temp-32)/1.8
        print(f'华氏度：{temp},摄氏度：{new_temp}')

if __name__ == '__main__':
    basic_temp_converter()
