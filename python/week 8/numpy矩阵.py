# 1. numpy 矩阵
# 【问题描述】

# 在数组主对角线上创建一个值为1,2,3,4的4*4矩阵，图例如下：

# [[1. 0. 0. 0.]

#  [0. 2. 0. 0.]

#  [0. 0. 3. 0.]

#  [0. 0. 0. 4.]]

# 【输入形式】

# 4
# 【输出形式】

# [[1. 0. 0. 0.]

#  [0. 2. 0. 0.]

#  [0. 0. 3. 0.]

#  [0. 0. 0. 4.]]

# 【样例输入】
# 【样例输出】
# 【样例说明】
# 【评分标准】


import numpy as np
m = eval(input())
a = np.eye(m)
row, col = np.diag_indices_from(a)
a[row, col] = np.arange(0, m, 1)+1
print(a)



