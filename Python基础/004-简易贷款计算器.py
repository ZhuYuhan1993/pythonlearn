"""
项目4：简易贷款计算器
### 基础要求
1. 输入贷款总额、年利率、贷款年限
2. 计算月还款额（等额本息公式）
3. 显示总还款额和总利息
### 完整要求
1. 支持等额本金还款方式
2. 显示详细的还款计划表
3. 提前还款计算功能
4. 不同方案对比功能
### 扩展要求
1. 考虑LPR浮动利率
2. 生成还款计划图表
3. 导出计算结果到Excel
4. 集成银行利率API
---
## 🎯 
"""
def basic_loan_calculator():
    loan = float(input('请输入贷款总额：'))
    interest_rate = float(input('请输入年利率：'))
    years = float(input('请输入贷款年限：'))
    months = years * 12
    interest_rate_month = interest_rate / 12
    loan_month = loan*interest_rate_month*(1+interest_rate_month)**months/((1+interest_rate_month)**months-1)
    loan_total = loan_month*months
    interest_loan = loan_total-loan
    print('='*5,'等额本息还款方式','='*5)
    print(f'每月还款额:{loan_month}')
    print(f'还款总额:{loan_total}')
    print(f'总利息:{interest_loan}')

if __name__ == '__main__':
    basic_loan_calculator()
