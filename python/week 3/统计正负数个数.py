# 【问题描述】从键盘输入非0整数，以输入0为输入结束标志，求平均值，统计正数负数个数
# 【输入形式】

#       每个整数一行。最后一行是0，表示输入结束。

# 【输出形式】

#      输出三行。

#      第一行是平均值。第二行是正数个数。第三行是负数个数。

# 【样例输入】

#                         1

#                         1

#                         1

#                         0


# 【样例输出】

#                         1

#                         3

#                         0
count=-1
zhengshu=0
num=0
fushu=0
while True:
    m=eval(input())
    count+=1
    #print(count,'次')
    if m>0:
        zhengshu+=1
        num+=m
    elif m<0:
        fushu+=1
        num+=m
    else:
        m==0
        break
#print('总数是',num)
ave = num/count
#print(type(ave))
print(ave)
print(zhengshu)
print(fushu)
