def my_function(num):
    print('num:',num)

# 函数需要一个参数，调用的时候必须传递一个参数
my_function(20)
##########################################################################################
# 在给函数形参设置默认参数时，并不是会给所有参数都设置默认值
# 如果某一个位置形参设置了默认参数，那么该位置之后的所有参数都必须设置默认参数
def my_function(a,b=20,c=30):  # 错误示例：def my_function(a,b=20,c):
    return a+b+c

my_function(10)
my_function(10,100)
my_function(10,100,1000)