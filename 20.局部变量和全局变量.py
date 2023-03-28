
# 全局变量：在函数外部定义的变量，全局指该变量在当前python 文件范围内是可见的，全局变量可以被当前python 文件内的所有函数直接使用；
# 局部变量：在函数内部定义的变量，该变量只能在定义的函数内部使用；
##########################################################################################
# 全局变量
g_val =100
def my_function1():
    print(g_val)

def my_function2():
    print(g_val)

my_function1()
my_function2()
##########################################################################################
# 局部变量

    # 定义全局变量
my_number =100

def my_function():
    # 定义局部变量
    my_number = 200
    print(my_number)  #打印局部变量的值

my_function()
print(my_number)  # 打印全局变量的值

##########################################################################################
# 就近原则
# 变量要先定义再使用
# 作用域：表示变量能够使用的范围（局部作用域和全局作用域）