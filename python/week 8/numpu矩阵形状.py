# 【问题描述】给定长度为12的列表a，输出其形状，如果能改变其形状为n*m，则输出改变后的数组，否则输出NO。
# 【输入形式】整数n和m
# 【输出形式】若满足n*m=12，输出数组，否则输出"NO"。
# 【样例输入】
# 1 12
# 【样例输出】
# [[ 1  2  3  4  5  6  7  8  9 10 11 12]]
# 【样例说明】
# 【评分标准】



import numpy as np


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n, m = input().split()
    n = int(n)
    m = int(m)
    a = np.array(a)
    if n*m==12:
        b=a.reshape(n,m)
        print(b)
    else:
        print('NO')


if __name__ == '__main__':
    main()

