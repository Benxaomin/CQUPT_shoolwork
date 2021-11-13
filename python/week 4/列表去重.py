# 【问题描述】输入一系列以逗号分隔的英文人名，其中包含重复的名字，请将其中重复的名字去掉，输出包含不重复人名的列表，名字出现顺序与输入顺序相同。【输入形式】

# 输入一系列以逗号分隔的英文人名，其中包含重复的名字，请将其中重复的名字去掉，输出包含不重复人名的列表，名字出现顺序与输入顺序相同。一系列以逗号分隔的英文人名

# 【输出形式】

# 包含不重复人名的列表，名字出现顺序与输入顺序相同
# 【样例输入】

# Calvin,bob,ada,McCord,Smith,Babbs,Calvin,Smith
# 【样例输出】

# ['Calvin', 'bob', 'ada', 'McCord', 'Smith', 'Babbs']



Name_list = input().split(',')
Name_set = set(Name_list)
Name_list2 = list(Name_set)

# 重新排序
Name_list2.sort(key=Name_list.index)
print(Name_list2)
