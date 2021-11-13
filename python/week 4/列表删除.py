# 【问题描述】

# 输入一个1-100之间的正整数 n, 以 n 为随机数种子随机生成一个不大于 n 的正整数 m 。 生成一个包含元素为 1，2，3……n 的列表 ls，在列表 ls 中删除值为 m 的整数倍的元素，在两行中输出原始列表和删除 m 倍数后的列表。
# 【输入形式】

# 输入一个1-100之间的正整数 n
# 【输出形式】

# 两行，每行一个列表



import random

n = int(input())
random.seed(n)
m = random.randint(1, n)
# print(m)

ls = list(range(1, n+1))
ls2 = ls.copy()
print(ls2)

k = n//m
# print(k)
a = list(range(1, k+1))
# print(a[0],a[1])
for i in range(k):
    index = (a[i]*m)-(i+1)
    ls.pop(index)
print(ls)
