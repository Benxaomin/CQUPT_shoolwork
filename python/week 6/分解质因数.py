# 【问题描述】

# 输入一个正整数n，把数字n分解成不能再分解因子的乘法，比如：8=2*2*2， 10 = 2*5，而不是 8 = 2 * 4 这种可以再分解的。
# 【输入形式】

# 输入一个正整数n
# 【输出形式】

# 输出包含所有因子的列表
# 【样例输入】

# 12
# 【样例输出】

# [2, 2, 3]



def FengJie(n):
    lt = []
    while n != 1:
        for i in range(2, int(n+1)):
            if n % i == 0:
                lt.append(i)
                n = n/i
                break
    print(lt)


m = eval(input())
FengJie(m)
