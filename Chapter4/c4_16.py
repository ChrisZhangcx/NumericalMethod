# -*- coding:utf8 -*-

# coder: 张成蹊, Latest Version: 2017-4-27

# 编写n次：Lagrange插值计算公式、Newton前插与后插计算公式

import numpy as np
from math import factorial


# Lagrange插值计算公式
# 传入：n+1个x值与对应的n+1个y值(用于构造插值多项式)；要计算的x值（用于计算插值结果）
# 返回：插值结果
def LagrangeInterpolation(x, y, num):
    n = x.shape[0]
    n -= 1
    # 构造n次插值多项式
    result = 0
    for i in range(n):      # 计算第i个插值项
        result1 = 1     # 分子
        result2 = 1     # 分母
        for j in range(n):
            if j != i:
                result1 *= (num-x[j])
                result2 *= (x[i]-x[j])
        result += result1*1.0/result2*y[i]
    return result


# Newton前插公式
# 输入：n+1个x值与对应的n+1个y值（用于构造前向差分表与插值多项式），t值（从第1个x开始往后的x所在系数
# 输出：插值结果
def NewtonForward(x, y, t):
    n = x.shape[0]
    n -= 1
    # 维护一个行列为n+1*n+1的向前差分表
    table = np.zeros([n+1, n+1])   # 用0初始化
    for i in range(n+1):
        table[i,0] = y[i]
    for i in range(1,n+1):
        for j in range(n+1-i):
            table[j,i] = table[j+1,i-1] - table[j,i-1]
    # 根据向前差分表进行插值
    result = 0
    for i in range(n+1):        # 计算每一项的结果
        if i == 0:
            result += table[0,0]
        else:
            tmpResult = 1
            for j in range(i):
                tmpResult *= (t - j)
            tmpResult /= factorial(i)
            result += tmpResult*table[0,i]
    return result



# Newton后插公式
# 输入输出值同上
def NewtonBackward(x, y, t):
    n = x.shape[0]
    n -= 1
    # 维护一个行列为n+1*n+1的向后差分表
    table = np.zeros([n+1, n+1])
    for i in range(n+1):
        table[i,0] = y[n-i]
    for i in range(1,n+1):
        for j in range(n+1-i):
            table[j,i] = table[j,i-1] - table[j+1,i-1]
    # 根据向后差分表进行插值
    result = 0
    for i in range(n+1):        # 计算每一项的结果
        if i == 0:
            result += table[0,0]
        else:
            tmpResult = 1
            for j in range(i):
                tmpResult *= (t + j)
            tmpResult /= factorial(i)
            result += tmpResult*table[0,i]
    return result