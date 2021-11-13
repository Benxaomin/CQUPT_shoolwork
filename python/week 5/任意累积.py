# 【问题描述】

# 计算任意个输入数字的乘积。

# 【输入形式】
# 【输出形式】
# 【样例输入】

# 输入："1,2,3,4"

# 【样例输出】

# 输出："24"

m=input().split(',')
sum=1
for i in range(len(m)):
	sum=sum*int(m[i])
print(sum)
