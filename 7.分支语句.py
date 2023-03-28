# # -----if分支语句
# # 需求：如果a>b,进行加法计算，否则，进行减法计算
# a=10
# b=20
# # 代码如下：
# if a>b:
#     ret=a+b
# else:
#     ret=a-b
#     print('ret=%d'%ret)
##########################################################################################
# 练习需求：登陆（用户名+密码）
input_username=input('请输入您的用户名:')
input_password=input('请输入您的密码:')
# 正确的用户名密码
correct_username='admin'
correct_password='Abc123,,'

# 首先判断用户名是否正确
if input_username==correct_username:
    # 如果用户名正确，再判断密码是否正确
    if input_password==correct_password:
        print('欢迎%s登陆系统' % input_username)
    else:
        print('您的用户名或密码错误，请重新输入！')
else:
    print('您的用户名或密码错误，请重新输入！')

