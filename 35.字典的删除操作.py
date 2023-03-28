# 删除：del
my_dict={'aaa':10,'bbb':20,'ccc':30}
del my_dict['aaa']
print(my_dict)

# 清空：clear
my_dict.clear()
print(my_dict)


# del 不但能够删除字典中的某个键值对
# 1.删除某个变量
a=10
print('a=',a)
del a
# print('a=',a)

# 2.删除列表中的元素
my_list=[1,2,3,4]
del my_list[0]
print(my_list)