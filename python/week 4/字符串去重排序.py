# 【问题描述】输入一个非空字符串，去除重复的字符后，从小到大排序输出为一个新字符串。

# 【输入形式】一个非空字符串

# 【输出形式】去重排序后的字符串

# 【样例输入】zzzxbcdfebd

# 【样例输出】bcdefxz




# 元素去重可以考虑集合的元素不可重复性
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 把输入字符串去重
m = input()
n = set(m)
a = list(n)
# 将字符串变成ASCII码进行冒泡排序
b = list()
for letter in a:
    asc = ord(letter)
    b.append(asc)
result = BubbleSort(b)
# 将排好序的ASCII码换回字符串按顺序打印
c = list()
for j in result:
    ch = chr(j)
    print(ch, end='')
