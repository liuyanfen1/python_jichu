# # input_content=input('请输入您的尊姓大名:')
# # print(input_content)
# #
# # print('欢迎您 %s！'%input_content)
#
##########################################################################################
# # 举例：在控制台依次提示用户输入：姓名、公司、职位、电话、电子邮箱
# name=input('请输入姓名：')
# company=input('请输入公司：')
# title=input('请输入职位：')
# phone=input('请输入电话：')
# email=input('请输入电子邮箱：')
#
# # 打印邮件签名
# print('*'*50)  # 输入分隔符 **************************************************
# print(company)
# print('%s(%s)'%(name,title))
# print('电话:%s'%phone)
# print('邮箱:%s'%email)
# print('*'*50)  # 输入分隔符 **************************************************
#
#
# #  第一种：不换行
# print('我的名字是:',name,'我的公司是:',company,'我的职位是：',title,'我的电话是：',phone,'我的电子邮箱是:',email)
#
# # 第二种：换行
# print('*'*50)  # 输入分隔符 **************************************************
# print('姓名:',name)
# print('公司:',company)
# print('职位:',title)
# print('电话:',phone)
# print('电子邮箱:',email)

##########################################################################################
# ----使用 input 函数完成加法计算器程序
# 1.保存用户输入的两个值
# 对两个值进行加法运算，并且保存结果
# 直接输出打印结果
left_number=input('请输入第一个数字：')
right_number=input('请输入第二个数字：')

# 打印两个变量的数据类型
print(type(left_number),type(right_number))

# 数据类型不是想要的数据类型，则需要数据类型转换：将字符串类型转换为数字类型
left_number_int=int(left_number)
right_number_int=int(right_number)

# 进行加法计算
result=left_number_int+right_number_int

# 输出计算结果：方法一
print(result)
# 输出计算结果：方法二
print('%d+%d=%d'%(left_number_int,right_number_int,result))