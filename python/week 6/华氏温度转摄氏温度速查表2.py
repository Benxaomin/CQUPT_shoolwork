# 已知华氏温度转换摄氏温度的计算公式：C=5×(F−32)/9，其中：C表示摄氏温度，F表示华氏温度。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# 编写函数F2C(f)将华氏温度转换为摄氏温度，读入两个华氏温度值f1和f2，打印范围在f1~f2内，每次增加两个华氏温度刻度的速查表。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# 注意：如果f1>f2，则直接打印error。

# 【输入形式】

# 输入为一行，为两个不小于32的正整数f1和f2，表示两个华氏温度。两个数之间用逗号隔开，形如f1,f2。

# 【输出形式】

# 如果f1>f2，输出error。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# 如果f1<=f2，则输出华氏转摄氏的温度转换速查表，速查表可能有多行，每行一个温度转换对，形如f1 : c1，其中c1保留小数点两位。速查表以2华氏度为刻度。


# 【样例输入1】

# 86,44

# 【样例输出1】

# error

# 【样例输入2】

# 44,47

# 【样例输出2】

# 44 : 6.67

# 46 : 7.78
def F2C(f1, f2):
    if f1 > f2:
        print('error')
    elif f1 <= f2:
        for i in range(int(f1), int(f2)+1, 2):
            C = 5*(i-32)/9
            print('{:.0f} : {:.2f}'.format(i, C))


f1 = input().split(',')
F2C(f1[0], f1[1])
