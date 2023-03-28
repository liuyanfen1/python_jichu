
my_list=[10,20,30,40]
# index 用于根据值查询，如果查询失败，则会报错
# position = my_list.index(20)
# print(position)
#
# position = my_list.index(60)  # 60 不在列表中，报错
# print(position)
#
# 根据位置修改值
old_value=30
new_value=200
if  old_value in my_list:
    # 查找到值为 old_value 的位置
    position = my_list.index(old_value)
    # 根据位置修改值
    my_list[position]=new_value
print(my_list)

##########################################################################################
# extend 将一个列表中的所有元素追加到当前列表的尾部（合并列表）
my_list2=['aaa','bbb','ccc']
my_list.extend(my_list2)
print(my_list)
