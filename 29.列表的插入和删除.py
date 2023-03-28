
# 创建一个空列表
my_list=[]

# append 追加，在尾部插入元素
my_list.append(10)
my_list.append(20)
my_list.append(30)

# insert 可以在指定位置插入
my_list.insert(0,100)  # 0 表示元素位置
print(my_list)
my_list.insert(2,200)
print(my_list)

# 删除元素：值删除、位置删除
# pop 方法用于位置删除，默认删除最后一个元素，如果指定了位置，删除该位置元素
my_list.pop()  # 不填，则删除最后一个元素
print(my_list)
my_list.pop(0)  # 0 表示元素位置，删除指定位置元素
print(my_list)

# remove 值删除：默认删除第一次出现的值
my_list.remove(20)  # 10 表示具体值
print(my_list)
my_list.append(20)
print(my_list)
my_list.remove(20)
print(my_list)

# 清空:清除所有元素
my_list.clear()
print(my_list)
print('列表长度',len(my_list))