2. 创建ndarray
【问题描述】

创建一个长度为n的一维全为0的ndarray对象，然后让第m个元素等于1 

输入n,m并用空格隔开, 且n>=m



【输入形式】
【输出形式】
【样例输入】

10 5
【样例输出】

[[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]]


import numpy as np
n,m=map(int,input().split())

array=np.zeros([1,n],dtype=np.float)
array[0][m-1]=1
print(array)

