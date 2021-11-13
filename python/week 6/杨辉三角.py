# 杨辉三角形，也称帕斯卡三角，其定义为：顶端是 1,视为(row0).第1行(row1)(1&1)两个1,这两个1是由他们上头左右两数之和 (不在三角形内的数视为0).依此类推产生第2行(row2):0+1=1;1+1=2;1+0=1.第3行(row3):0+1=1;1+2=3; 2+1=3;1+0=1. 循此法可以产生以下诸行，如下图所示。
# 定义一个函数 ，传入正整数参数 M，输出 M 行的杨辉三角（为使格式美观，采用M行中最大数的位数 做为数据输出时的占位宽度和 数据间的间隔）。

# 【输入形式】

#  一个正整数，如：12 

# 【输出形式】

# 此时最大数的位数 为3  





def trigon(list, A_list, n):  # list总序列，alist每行序列
    blist = [1]
    if n > 0:
        for j in range(len(A_list)):
            if j < len(A_list) - 1:
                sum = A_list[j] + A_list[j+1]
                blist.append(sum)
        blist.append(1)
        list.append(blist)
        n -= 1
        trigon(list, blist, n)


if __name__ == "__main__":
    list1 = [1]  # 第一行
    list2 = [1, 1]  # 第二行
    n = int(input())
    list = []
    list.append(list1)
    list.append(list2)
    trigon(list, list2, n - 2)  # 计算出整个杨辉三角
    l = len(str(max(list[n-1])))
    for i in range(0, n):  # 输出n行
        j = 0
        while j < n-i:  # 打印每个数之间的间隔
            print(' '*l, end='')
            j += 1
        j = 0
        while j <= i:
            print(' '*(l-len(str(list[i][j]))), end='')  # 补位
            print(list[i][j], end='')
            print(' '*l, end='')
            j += 1
        print(end='\n')
