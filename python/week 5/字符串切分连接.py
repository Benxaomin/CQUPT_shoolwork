# 【问题描述】

#  输入一个包含多个单词的英文句子，单词间以空格分隔，标点符号后跟一个空格。定义一个函数，功能是用指定的符号把单词连接起来。

# 【输入形式】

# 第一行输入一个英文句子‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# 第二行输入一个符号 

# 【输出形式】

# 用符号连接起来的单词

# 【样例输入】

# a string can be split on a delimiter.

# -


# 【样例输出】

# a-string-can-be-split-on-a-delimiter.


sent = input().split(" ")
m = input()
# print(sent())
ls = list()
for i in range(len(sent)):
    ls.append(sent[i])
    ls.append(m)
for j in range(len(ls)-1):
    print(ls[j], end="")
