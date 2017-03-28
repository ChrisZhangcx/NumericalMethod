# -*- coding:utf8 -*-

import numpy as np


# 根据指令选择不同的消元方法
def solveEquation(method):
    global matrix, n, e, d, x
    if method == 'sem':             # 选择高斯顺序消元法
        # 消元
        for k in range(0,n-1):
            for i in range(k+1,n):
                temp = matrix[i,k]/matrix[k,k]
                matrix[i,k] -= temp*matrix[k,k]
                b[i] -= temp*b[k]
                for j in range(k+1,n):
                    matrix[i,j] -= temp*matrix[k,j]
        # 回代
        x[n-1] = b[n-1]/matrix[n-1,n-1]
        for i in range(n-2,-1,-1):
            sum = 0
            for j in range(i+1,n):
                sum += matrix[i,j]*x[j]
            x[i] = (b[i] - sum)/matrix[i,i]
    elif method == 'mem':           # 选择列主元消去法
        # 消元
        for k in range(0,n-1):
            # 选主元
            r = k
            a = abs(matrix[k,k])
            for p in range(k+1,n):
                if abs(matrix[p,k]) > a:
                    r = p
                    a = abs(matrix[p,k])
            # 换行
            if r != k:
                for j in range(k, n):
                    matrix[k,j], matrix[r,j] = matrix[r,j], matrix[k,j]
                b[k], b[r] = b[r], b[k]
            # 消元
            for i in range(k+1,n):
                temp = matrix[i,k]/matrix[k,k]
                matrix[i,k] -= temp*matrix[k,k]
                b[i] -= temp*b[k]
                for j in range(k+1,n):
                    matrix[i,j] -= temp*matrix[k,j]
        # 回代
        x[n-1] = b[n-1]/matrix[n-1,n-1]
        for i in range(n-2,-1,-1):
            sum = 0
            for j in range(i+1,n):
                sum += matrix[i,j]*x[j]
            x[i] = (b[i] - sum)/matrix[i,i]
    else:
        return

# 按题目要求初始化方程组
n = 100                          # 矩阵维度
e = 3.0
d = 9.0
f = 1.0
matrix = np.zeros([n, n])       # 创建一个n行n列的零数组
b = np.zeros(n)
x = np.zeros(n)
for i in range(n-1):            # 填充数组中的非零值
    matrix[i,i] = e
    matrix[i+1,i] = d
    matrix[i,i+1] = f
matrix[n-1,n-1] = e
for i in range(n):              # 填充b向量的值
    b[i] = 13.0
b[0] = 4.0
b[n-1] = 12

print "矩阵A："
print matrix

# 采用顺序消元法
#solveEquation("sem")
# 采用列主元消去法
solveEquation("mem")
print "最终结果（解向量）："
print x