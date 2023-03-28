my_list=[10,20,30,40]

# 列表是序列式容器，支持索引、切片
print(my_list[0],my_list[2])
print(my_list[:2])

# 列表的遍历
index=0
length=len(my_list)
while index<length:
    print(my_list[index])
    index +=1

# for 循环一般都用于容器中元素的遍历
# 先把10 赋给val，再把20 赋给val ，以此类推，直到全部赋完之后，循环结束
for val in my_list:
    print(val)

# 能否在for 循环中使用break 、continue？：能
##########################################################################################
# 遍历列表中的列表的元素（嵌套循环）
# while 循环
my_list=[[10,20,30],[100,200,300],[1000,2000,3000]]
i=0  # 外层列表
while i<len(my_list):
#     my_list[i]是什么类型
#     print(my_list)

    j=0  # 内层列表
    while j<len(my_list[i]):
        print(my_list[i][j])
        j +=1
    i +=1
########################
# for 循环
for o in my_list:
    for v in o:
        print(v)