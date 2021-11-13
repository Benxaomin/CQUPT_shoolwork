# 【问题描述】

# 编写程序， 输入一个大于 2 的自然数， 然后输出小于该数字的所有素数组成的列表。
# 【输入形式】
# 【输出形式】
# 【样例输入】

# 7

# 【样例输出】

# [2, 3, 5]

# 【样例说明】
# 【评分标准】



m = eval(input())
a = []
for i in range(2, m):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(i)
print(a)
