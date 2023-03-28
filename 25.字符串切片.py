# 切片：slice
# 字符串提供了一种语法，用来获取字符串中的一个子串

user_email='liuyanfen@163.com'
# 切片语法：左闭右开
print(user_email[0:3])
print(user_email[0:6])
print(user_email[3:9])
# 获得容器中元素的个数
string_length=len(user_email)
print(user_email[10:string_length])
# 起始值不写，表示从0 开始
print(user_email[:9])
# 结束值不写，表示到最后
print(user_email[10:])
# 起始值和结束值都不写，只写冒号，表示从0 开始，到最后
print(user_email[:])

# 步长
print(user_email[0:9:1])  # 1 表示步长，从左向右取值，起始值小于结束值，等价于print(user_email[0:9])

print(user_email[0:9:2])  # 2 表示隔1个取值
print(user_email[0:9:3])  # 3 表示隔2个取值

# 了解：起始  结束  步长都可以为负数
print(user_email[-5:])  # 需考虑左闭右开

print(user_email[6:1:-1])  # -1 表示从右往左取，起始值大于结束值
# 字符串逆序
print(user_email[::-1])

# 例：找出邮箱的姓名和后缀
user_email='liuyanfen@163.com'
# 如果超找到，返回子串第一次出现的位置
position=user_email.find('@')
if position==-1:
    print('@不存在，邮箱不合法！')
else:
    user_name=user_email[:position]
    houzhui=user_email[position+1:]
    print('用户名是：',user_name)
    print('后缀是：',houzhui)