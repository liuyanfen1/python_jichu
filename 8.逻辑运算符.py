
# and 和 or 用于连接多个条件，表示条件之间的关系
input_username=input('请输入用户名:')
input_password=input('请输入密码:')

if input_username=='admin' and input_password=='Abc123,,':
    print('欢迎%s登录系统'%input_username)
else:
    print('登录失败')

##########################################################################################
# and /or /not非0为真，0为假
# and：如果第一个条件为真，则第二个条件必须执行，直接返回第二个条件结果；如果第一个条件为假，则不需要检查第二个条件，返回第一个条件的结果
ret=1 and 0
print(ret)

# OR：若有第一个为真，则直接返回第一个条件的结果，不需要再执行第二个条件；若第一个条件为假，执行第二个条件，且返回第二个条件结果
ret=1 or 0
print(ret)

# not:对整体表达式取反
a=10
b=20

ret=not (a>b)
print(ret)
# 或者
ret=a>b
print(not ret)

##########################################################################################
# 如：
a=10
b=20
if a>b:
    ret=a
else:
    ret=b
# 简化写法：
ret=a>b and a or b
print(ret)

# 举例
a = 30
b = 20

if not (a>=b):
    print('正确')
else:
    print('错误')
