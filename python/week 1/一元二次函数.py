#【问题描述】一元二次方程：ax2+bx+c=0 （a ╪ 0）
#【输入形式】输入a、b和c的值（有理数）
# 【输出形式】输出x的两个值，或者No（即没有有理数的解）
# 【样例输入】1 2.5 3
# 【样例输出】No
# 【样例输入】1 -2 1
# 【样例输出】1.00 1.00
# 【样例输出说明】输出的两个解保留两位小数，大的在前
from math import *
a,b,c = map(float,input().split())
'''b=float(input("b"))
c=float(input("c"))'''
if b**2-4*a*c < 0:
    print("No")
else:
    x1=(-b+sqrt(b**2-4*a*c))/2*a
    x2=(-b-sqrt(b**2-4*a*c))/2*a
    if x1>x2:
        print("{:.2f} {:.2f}".format(x1,x2))
    else:
        print("{:.2f} {:.2f}".format(x2,x1))
