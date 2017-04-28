# -*- coding:utf8 -*-

# coder: 张成蹊, Latest Version: 2017-4-27

# f(x)=\frac{1}{1+25x^2}， |x|\leq 1，取等距节点n=5,n=10，用通用程序(1),(2),(3)
# 计算x=-0.95+ih处f(x)的近似值，并将结果与真实值相比较

from c4_16 import LagrangeInterpolation, NewtonForward, NewtonBackward
import numpy as np


# 计算函数：传入等距节点个数n与插值点x值，返回三个方法分别得到的y值
def calc(n, num):
    x = []
    y = []
    for i in range(n):
        x.append(-1 + i * 2.0/(n-1))
        y.append(1.0 / (1 + 25 * (x[i] ** 2)))
    x = np.array(x)
    y = np.array(y)
    # 计算真实值
    print "插值点：x=%f" % num
    print "真实插值结果为：%f" % float(1.0/(1+25*(num**2)))
    # 用Lagrange插值
    print "Lagrange插值结果：", LagrangeInterpolation(x,y,num)
    # 用Newton前插
    for i in range(len(x)):
        if x[i] < num and x[i+1] >= num:
            x1 = x[i:]
            y1 = y[i:]
            break
    t = (num-x1[0])/(2.0/(n-1))
    print "Newton前插结果：", NewtonForward(x1,y1,t)
    # 用Newton后插
    for i in range(len(x)):
        if x[i] <= num and x[i+1] > num:
            x2 = x[:i+2]
            y2 = y[:i+2]
            break
    t = (num-x2[len(x2)-1])/(2.0/(n-1))
    print "Newton后插结果", NewtonBackward(x2,y2,t)
    print ""



h = 0.1
# 取等距节点n=5
n = 5
print "\n\n当等距节点n=5时，输出下列结果"
for i in range(20):
    num = -0.95 + i*h
    calc(n,num)
n = 10
print "\n\n当等距节点n=10时，输出下列结果"
# 取等距节点n=10
for i in range(20):
    num = -0.95 + i*h
    calc(n,num)