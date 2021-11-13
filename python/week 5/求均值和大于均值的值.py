# 【问题描述】

# 编写一个函数cacluate, 可以接收任意多个数, 返回的是一个元组.元组的第一个值为所有参数的平均值（均值保留一位小数）, 第二个值是大于平均值的所有值

# 【输入形式】
# 【输出形式】
# 【样例输入】

# Please input numbers,and press the Enter to end.(gap with  )

# 1,2,3,4,5


# 【样例输出】

# (3.0, [4, 5])



def calculate(*b):
    b = input(
        'Please input numbers,and press the Enter to end.(gap with ,)\n').split(',')
    sum = 0
    for i in range(len(b)):
        sum = sum+int(b[i])
    eva = sum/len(b)
    evas = round(eva, 1)
    ls = list()
    for j in range(len(b)):
        if eva < int(b[j]):
            ls.append(int(b[j]))
        else:
            continue
    return evas, ls


c = calculate()
print()
print(c)
