# -*- coding:utf8 -*-

import numpy as np

# 按题目要求初始化三对角阵
n = 100                          # 矩阵维度
e = -4.0
d = 1.0
f = 1.0
matrix = np.zeros([n, n])       # 创建一个n行n列的零数组
b = np.zeros(n)
l = np.zeros(n)
r = np.zeros(n)
x = np.zeros(n)
y = np.zeros(n)
for i in range(n-1):            # 填充数组中的非零值
    matrix[i,i] = e
    matrix[i+1,i] = d
    matrix[i,i+1] = f
matrix[n-1,n-1] = e
for i in range(n):              # 填充b向量的值
    b[i] = -15.0
b[0] = -27.0
print "矩阵A："
print matrix

# LU分解
r[0] = e
for i in range(1,n):
    l[i] = d/r[i-1]
    r[i] = e - l[i]*f

# 解Ly=b（追过程）
y[0] = b[0]
for i in range(1,n):
    y[i] = b[i] - l[i]*y[i-1]

# 解Ux=y（赶过程）
x[n-1] = y[n-1]/r[n-1]
for i in range(n-2, -1, -1):
    x[i] = (y[i] - f*x[i+1])/r[i]

print "\n最终结果（解向量）："
print x