def my_add(a,b):
    ret=a+b
    return ret  # 返回值

# 保存函数的返回结果
ret = my_add(10,20)
# 使用函数计算对的结果，进行下一步的计算
final_ret = ret + 100
# 输出最终结果
print('最终结果：',final_ret)

# 使用调试模式：debug
#     1.先加断点，
#     2.启动调试模式

# print 函数和 return 语句的区别
#   1.print 是一个函数，只是一个功能，return 是一个语句，和def、if类似；
#   2.print 会将数据打印到屏幕上，return 会将数据返回到程序中，给函数的调用者；
# 函数的返回值到底应该有没有？由需求决定
#
