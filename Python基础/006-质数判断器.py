"""
项目6：质数判断器
### 基础要求
1. 输入一个正整数
2. 判断是否为质数
3. 输出判断结果
### 完整要求
1. 判断指定范围内的所有质数
2. 计算质数的数量
3. 显示质因数分解结果
4. 性能优化（使用开方优化）
### 扩展要求
1. 大数质数测试（Miller-Rabin算法）
2. 寻找第n个质数
3. 质数分布可视化
4. 质数应用（RSA加密演示）
---
## 🎯 
"""
def isPrime():
    n = int(input('请输入一个正整数：'))
    if n<=1:
        print('不是质数')
        return
    elif n<=3:
        print('是质数')
        return
    elif n%2==0 or n%3==0:
        print('不是质数')
        return
    else:
        for i in range(5,int(n**0.5)+1,6):
            if n%i==0 or n%(i+2)==0:
                print('不是质数')
                return
        print('是质数')
        return
if __name__=='__main__':
    isPrime()