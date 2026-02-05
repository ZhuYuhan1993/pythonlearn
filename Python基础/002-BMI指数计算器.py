"""
项目2：BMI指数计算器
### 基础要求
1. 输入身高(米)和体重(千克)
2. 计算BMI值：体重/身高²
3. 输出BMI值和分类（偏瘦/正常/超重/肥胖）
### 完整要求
1. 支持多种单位输入（厘米、英尺英寸）
2. 显示理想体重范围
3. 给出具体的健康建议
4. 添加BMI标准说明
### 扩展要求
1. 添加历史记录功能
2. 绘制BMI变化趋势图
3. 集成其他健康指标（体脂率）
4. 开发移动端版本
---
## 🎯 
"""
def basic_bmi():
    height = float(input('请输入您的身高（m）：'))
    weight = float(input('请输入您的体重（kg）：'))
    bmi = weight / (height * height)
    print(f'您的BMI数值为：{bmi}')
    print('='*5,'世界卫生组织BMI分类标准','='*5)
    if bmi < 18.5:
        print('偏瘦')
    elif 18.5 <= bmi < 25:
        print('正常')
    elif 25 <= bmi < 30:
        print('超重')
    elif 30 <= bmi < 35:
        print('肥胖Ⅰ级')
    elif 35 <= bmi < 40:
        print('肥胖Ⅱ级')
    else:
        print('肥胖Ⅲ级')
    print('='*5,'中国特有的BMI分类标准','='*5)
    if bmi < 18.5:
        print('偏瘦')
    elif 18.5 <= bmi < 24:
        print('正常')
    elif 24 <= bmi < 28:
        print('超重')
    else:
        print('肥胖')

def complete_bmi():
    return
def advance_bmi():
    return
if __name__ == '__main__':
    basic_bmi()
    # complete_bmi()
    # advance_bmi()