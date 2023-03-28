# 1.普通输出变量
my_number1=100
my_number2=100
my_number3=100
print(my_number1,my_number2,my_number3)  # 函数中的逗号用来隔开多个参数
# 换行符：\n a
print('aaa',end='')
print('bbb',end='#')
print('ccc')
print('ddd')
##########################################################################################
# 2.格式化输出：%s -- s表示string  %d – d 表示digit   %f – f表示float  %% -- 输出%
name='刘艳芬'
age=30
salary=15000.87
my_fomat='我的名字是%s,我的年龄是%d,我的工资是%f.'%(name,age,salary)
print(my_fomat)
print('游戏胜率：%d'%87)  # 第一种

print('我的名字是',name,'我的年龄是',age,'我的工资是',salary,'我的游戏胜率是',87)  # 第二种