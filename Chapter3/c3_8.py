# -*- coding:utf8 -*-

# coder: 张成蹊, Latest Version: 2017-4-27

# 用乘幂法（子程序（1））求下列矩阵的按模最大特征值及特征向量

import numpy as np


# 编写规范化乘幂法的计算函数
# 输入：numpy.darray类型矩阵，迭代次数（如不设置则默认迭代20次）
# 返回：矩阵的按模最大特征值，以及矩阵的特征向量
def calcValueVector(matrix, iterations=20):
    # 设初始特征向量值均为1
    m, n = matrix.shape
    x = np.transpose(np.ones([1, m]))
    for i in range(iterations):
        # 找到max(abs(x))
        x0 = -np.inf
        for each in x:
            if abs(each)>x0:
                x0 = abs(each)
        y = x/x0
        x = np.dot(matrix, y)
    # 找到最后的max(abs(x))
    x0 = -np.inf
    for each in x:
        if abs(each) > x0:
            x0 = abs(each)
    return x0, y


# 创建对应矩阵
A1 = [[49.0/8, -131.0/8, -43.0/4],
      [11.0/8, -17.0/8, -9.0/8],
      [-1.0/2, 7.0/2, 3]]
A2 = [[7,3,2],
      [3,4,-1],
      [-2,-1,3]]
A1 = np.array(A1)
A2 = np.array(A2)

print "矩阵", A1
print A1
value, vector = calcValueVector(A1, 41)
print "矩阵按模的最大特征值：", value
print "矩阵的特征向量：", vector, "\n"

print "矩阵", A2
print A2
value, vector = calcValueVector(A2, 41)
print "矩阵按模的最大特征值：", value
print "矩阵的特征向量：", vector, "\n"
