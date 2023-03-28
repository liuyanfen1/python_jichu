my_dict={'aaa':10,'bbb':20,'ccc':30}
# # 默认只能遍历键
# for val in my_dict:
#     print(val)

# key 方法可以获得所有的键列表
key_list=my_dict.keys()
print(list(key_list))

# keys 方法可以获得所有的值列表
value_list=my_dict.values()
print(list(value_list))

# keys 方法可以获得所有的键值对列表，每一个键值对都是一个元祖

key_value_list=my_dict.items()
print(list(key_value_list))

for key_value in key_value_list:
    print(key_value)
    print('key',key_value[0],'value',key_value[1])

# 使用while 循环遍历字典
my_list=list(my_dict.items())
i=0
while i<len(my_list):
    print('key:',my_list[i][0],'value:',my_list[i][1])
    i +=1