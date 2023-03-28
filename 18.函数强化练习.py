
# 1.编写一个函数用于计算从start 开始到 end 结束之间的所有数字的累加和
# 1.当函数执行到return 关键字时，就会马上终止函数执行；
# 2.函数中可以出现多个return，但是有且只有一个return会被执行；
# 3.return 后面可以不跟值，单独使用，return 等价于 return None
# 代码实现如下：
def leijiahe(start,end):
    # 判断start 和 end 是否都是数字类型
    is_int = isinstance(start,int)  # --isinstance 判断数据类型
    if not is_int:
        print('start 应该是一个数字！')
        return None
    is_int = isinstance(end,int)
    if not is_int:
        print('start 应该是一个数字！')
        return None
    if start > end:
        print('start 应该小于 end')
        return None
        i = start
    my_sum=0
    while i <=end:
        my_sum += i
        i += 1
    return  my_sum

# # 定义一个新的变量用于保存函数的返回结果
# ret = leijiahe(1,100)
# print('ret',ret)
#
# ret = leijiahe(10,90)
# print('ret',ret)
##########################################################################################
# # 2.编写一个函数根据传入的运算符，进行相应的 加减乘除 运算
#
# def my_caculator(a,b,operator):
#     if operator == '+':
#         ret = a + b
#     elif operator == '-':
#         ret = a - b
#     elif operator == '*':
#         ret = a * b
#     elif operator == '/':
#         ret = a / b
#     else:
#         print('您输入的操作符有误')
#         ret = None
#     return  ret
# ret = my_caculator(10,20,'+')
# print('ret:',ret)
#
# ret = my_caculator(50,20,'-')
# print('ret:',ret)
#
# ret = my_caculator(10,20,'*')
# print('ret:',ret)
#
# ret = my_caculator(10,20,'/')
# print('ret:',ret)
#
# ret = my_caculator(10,20,'%')
# print('ret:',ret)

##########################################################################################
# 调用函数时，既传递位置参数，又传递关键字参数时：位置参数一定要在关键字参数的前面
def my_add(num1,num2,num3,num4):
    result = num1 + num2 +num3 +num4
    return result
result = my_add(100,200,300,num4=20)  # 注意：num4=20 一定要在后面
print(result)


