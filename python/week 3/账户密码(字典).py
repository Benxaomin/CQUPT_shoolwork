# 问题描述】

# 模拟某系统用户登录过程‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# 用户登陆系统时需要首先输入账号，如果账号不存在，输出“Wrong User”并结束程序；账号正确时，再输入密码，验证账号密码与已给定的账号密码是否一致，如果一致，输出“Success”，否则输出“Fail”以及剩余尝试次数。总尝试次数为3次，如果3次均输入错误，输出“Login Denied”。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# 给定账户及密码如下：

# 账号 密码 

# aaa 123456 

# bbb 888888 

# ccc 333333 

# 字典可设为：

# 字典可设为：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬

# dic={"aaa":["123456",10000],"bbb":["888888",5000],"ccc":["333333",3000]}

# 【输入形式】

# 在两行中分别用户名和密码
# 【输出形式】

# 参考测试用例
# 【样例输入】

# ttt
# 【样例输出】
# 【样例说明】

# Wrong User
import sys
dic={"aaa":"123456","bbb":"888888","ccc":"333333"}

log_error_count = 0

username=input()
if username not in dic.keys():
    print('Wrong User')
    exit()
while True:       
    if username in dic.keys():
        password=input()
        if password == dic[username]:
            print('Success')
            sys.exit()
        else:
            log_error_count+=1
            #print(log_error_count)
            if log_error_count<=2:
                print('Fail,'+str(3-log_error_count)+' Times Left')
                
            else:
                print('Login Denied')
                sys.exit()
        

# print(dic)
# a=dic.keys()
# print(a)
# b=dic.values()
# print(b)
