# 【问题描述】王老师刚刚完成了期末考的阅卷，为了方便学生查找成绩，请你帮他将成绩从小到大排个序吧。
# 【输入形式】n个同学的考试成绩
# 【输出形式】用数组存储且排好序的考试成绩。
# 【样例输入】
# 98 100 96.5 64 59 58 65 78 85
# 【样例输出】
# [ 58.   59.   64.   65.   78.   85.   96.5  98.  100. ]


import numpy as np
def main():
    arr = input("")
    a = [float(x) for x in arr.split()]
    a = np.array(a)
    print(np.sort(a))


if __name__ == '__main__':
    main()

