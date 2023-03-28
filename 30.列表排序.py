
# 需求：创建一个包含10个随机数的列表

# 导入随机数模块
import  random
my_list=[]
i=0
while i<10:
    # 产生随机数
    random_number=random.randint(1,100)
    # 将随机数插入列表中
    my_list.append(random_number)
    i+=1
print(my_list)

# 对列表中的元素进行排序 ：sort
# 默认从小到大排序：升序
my_list.sort()
print(my_list)
# 将sort 函数的reverse 默认值改成True 可实现从大到小排序
my_list.sort(reverse=True)
print(my_list)
# 逆序，此处的reverse 是函数
my_list.reverse()
print(my_list)