# 元祖：tuple
##########################################################################################
# 元祖可以从语法层面来限制数据的以外修改
# 元祖使用()定义

my_tuple =(10,20,30)
print(my_tuple[0])
# 注意：如果元祖只有一个元素，需在元素后加“,”
my_tuple=(10,)
print(my_tuple)

# 元祖嵌套
my_tuple=((1,2),(10,20))
print(my_tuple)

# # 元祖中的元素不能被修改
# my_tuple=(1,2,3)
# my_tuple[0]=100  # 报错，元祖不支持修改

# 遍历操作
for i in my_tuple:
    print(my_tuple)

# 查询
my_tuple=(1,2,3,4)
position=my_tuple.index(2)  # 2 表示具体值的查找
print(position)

# 元祖支持切片操作
my_tuple=(1,2,3,5,4)
print(my_tuple[1:])