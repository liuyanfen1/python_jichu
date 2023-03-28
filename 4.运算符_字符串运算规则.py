# 字符串运算规则
# 字符串只支持加法、乘法，
my_str1 = ' hello '
my_str2 = ' world '
ret = my_str1 + my_str2
print(ret)  # 加法

my_str1 = ' hello '
ret = my_str1 * 3
print(ret)  # 乘法

# 不支持减法、除法等
my_str1 = ' hello '
my_str2 = ' world '
ret = my_str1 - my_str2
print(ret) # 错误的例子(减法)

my_str1 = ' hello '
ret = my_str1 / 3
print(ret) # 错误的例子(减法)

# 字符串不支持与数字相加
my_number = 3
my_str3 = 'hello'
ret2 = my_number + my_str3
print(ret2)  # 错误的例子