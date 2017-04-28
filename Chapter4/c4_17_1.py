# -*- coding:utf8 -*-

# coder: 张成蹊, Latest Version: 2017-4-27

# 已知f(x)=ln(x), [a,b]=[1,2]，取h=0.1, xi=1+ih,i=0,1,...,10，
# 用通用程序(1),(2),(3)计算ln1.54及ln1.98的近似值

from c4_16 import LagrangeInterpolation, NewtonForward, NewtonBackward
from math import log
import numpy as np

h = 0.1
# 构造Lagrange插值基础数据
x = []
y = []
for i in range(11):
    x.append(1+i*h)
    y.append(log(1+i*h))
x = np.array(x)
y = np.array(y)
# 构造Newton前插基础数据
x11 = x[5:]             # 前插1.54
y11 = y[5:]
t11 = (1.54-x11[0])/h
x12 = x[9:]
y12 = y[9:]
t12 = (1.98-x12[0])/h
# 构造Newton后插基础数据
x21 = x[:7]
y21 = y[:7]
t21 = (1.54-x21[len(x21)-1])/h
x22 = x                 # 后插1.98
y22 = y
t22 = (1.98-x22[len(x22)-1])/h


print "Ln1.54与Ln1.98的真实值："
print "Ln1.54=", log(1.54)
print "Ln1.98=", log(1.98)
print ""

print "使用通用程序1（Lagrange插值公式）计算近似值"
print "Ln1.54=", LagrangeInterpolation(x, y, 1.54)
print "Ln1.98=", LagrangeInterpolation(x, y, 1.98)
print ""

print "使用通用程序2（Newton前插公式）计算近似值"
print "Ln1.54=", NewtonForward(x11, y11, t11)
print "Ln1.98=", NewtonForward(x12, y12, t12)
print ""

print "使用通用程序3（Newton后插公式）计算近似值"
print "Ln1.54=", NewtonBackward(x21, y21, t21)
print "Ln1.98=", NewtonBackward(x22, y22, t22)
