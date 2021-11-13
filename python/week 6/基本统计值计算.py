# 【问题描述】

# 获取以逗号分隔的多个数据输入（输入为一行），计算基本统计值（平均值、标准差、中位数）‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# 除中位数外，其他输出保留小数点后两位。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# 请补充编程模板中代码完成

# #请在...补充一行或多行代码

# def getNum():       #获取用户不定长度的输入

#     ...



# def mean(numbers):  #计算平均值

#     ...

    

# def dev(numbers, mean): #计算标准差

#     ...



# def median(numbers):    #计算中位数

#     ...

    

# n =  getNum() #主体函数

# m =  mean(n)

# print("Average:{:.2f},Standard Deviation:{:.2f},Median:{}".format(...))

# 【输入形式】

# 【输出形式】

# 【样例输入】

# 1,3,6,9,2,5,1






def getNum():  # 获取用户不定长度的输入
    M = input().split(',')
    m = list(map(lambda x: float(x), M))
    return m


def mean(numbers):  # 计算平均值
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    ave = sum/len(numbers)
    return ave


def dev(numbers, mean):  # 计算标准差
    sum = 0
    for i in range(len(numbers)):
        sum += (numbers[i]-mean)**2
    sum = sum/(len(numbers)-1)
    #print(sum, end=',')
    SD = pow(sum, 0.5)
    # print(sum)
    return SD

# 判断一个数是整型还是浮点型并返回它的值


def judge(a):
    n1 = str(float(a))
    n2 = n1.split('.')
    if n2[1] == '0':
        return int(a)
    else:
        return a


def median(numbers):  # 计算中位数
    numbers.sort()
    if len(numbers) % 2 == 0:
        medi = (numbers[int(len(numbers)/2)] +
                numbers[int(len(numbers)/2)-1])*0.5
    else:
        medi = numbers[int((len(numbers)-1)/2)]
    c = judge(medi)
    return c

    # n是个列表
n = getNum()  # 主体函数
m = mean(n)
x = dev(n, m)
y = median(n)
# print("Average:{:.2f}".format(m))
# print("Average:{:.2f},Standard Deviation:{:.2f}".format(m, x))
print("Average:{:.2f},Standard Deviation:{:.2f},Median:{}".format(m, x, y))
