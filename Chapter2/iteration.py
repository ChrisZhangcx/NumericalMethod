# -*- coding:utf8 -*-

import numpy as np


# 判断是否达到停机条件
def isStop(x0, x1):
    varepsilon = 0.00001
    stop = 1
    for i in range(len(x0)):
        if abs(x0[i]-x1[i]) > varepsilon:
            stop = 0
            break
    return stop


# 根据命令执行不同的迭代方法
def solveEquation(method, isPrint=0):
    global N, L, D, U, b, A
    times = np.inf
    if method == 'jacobi':
        x = np.zeros(6)
        for i in range(N):
            # 迭代
            x_backup = x
            x = np.dot(np.dot(np.linalg.inv(D), (L+U)), x)+np.dot(np.linalg.inv(D), b)
            if isPrint == 1:
                print x
            # 判断是否到达停机条件
            if isStop(x, x_backup):
                times = i + 1
                break
    elif method == 'gauss':
        x = np.zeros(6)
        for i in range(N):
            # 迭代
            x_backup = x
            x = np.dot(np.dot(np.linalg.inv(D-L), U), x)+np.dot(np.linalg.inv(D-L), b)
            if isPrint == 1:
                print x
            # 判断是否到达停机条件
            if isStop(x, x_backup):
                times = i + 1
                break
    elif method == 'SOR':
        omega = [1.1, 1.2, 1.3]
        times = []
        # 分别计算\omega为三个值时的迭代次数
        for each in omega:
            x = np.zeros(6)
            for i in range(N):
                # 迭代一次
                x_backup = x
                x = np.dot(np.dot(np.linalg.inv(D-each*L), (1-each)*D+each*U), x)+\
                    np.dot(each*np.linalg.inv(D-each*L), b)
                if isPrint == 1:
                    print x
                # 判断是否到达停机条件
                if isStop(x, x_backup):
                    times.append(i+1)
                    break
    elif method == 'sdm':
        varepsilon = 0.00001
        x = np.zeros(6)
        for i in range(N):
            # 迭代一次
            r = b - np.dot(A, x)
            tau = np.dot(r.transpose(), r)/np.dot(np.dot(r.transpose(), A), r.transpose())
            x += np.dot(tau, r)
            if isPrint == 1:
                print x
            # 如果提前达到指定精度则退出
            if np.dot(r.transpose(), r) < varepsilon:
                times = i
                break
    else:
        return

    print "\nTo solve the problem by '", method, "': "
    print "Iteration times:", times
    print "Result:", x, "\n"


# 初始化方程组
A = [[4, -1, 0, -1, 0, 0],
     [-1, 4, -1, 0, -1, 0],
     [0, -1, 4, 0, 0, -1],
     [-1, 0, 0, 4, -1, 0],
     [0, -1, 0, -1, 4, -1],
     [0, 0, -1, 0, -1, 4]]
b = [0, 5, 0, 6, -2, 6]
A = np.array(A)
b = np.array(b)

# 对A进行LDU分割
L = np.zeros(A.shape)
D = np.zeros(A.shape)
U = np.zeros(A.shape)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if i == j:
            D[i,j] = A[i,j]
        elif i > j:
            L[i,j] = -A[i,j]
        else:
            U[i,j] = -A[i,j]
# 初始化第一次迭代的x向量均为0
x = np.zeros(A.shape[0])
N = 25

print '\nType solveEquation("jacobi/gauss/SOR/sdm") to solve the problem.'
print "If you want to print(x) in each step, add parameter '1' after the method you choose.\n"