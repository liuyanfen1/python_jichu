# 需求：一个学校，有3个办公室，现在有8个老师等待工位的分配，请编写程序，完成随机的分配
# 思路：

import random

# 定义学校和办公室
school =[[],[],[]]


def create_teachers():
    """"创建老师列表"""
# 定能够以列表保存老师
    teacher_list=[]
    index=1
    while index<=8:
    # 创建老师的名字
        teacher_name='老师'+str(index)
    # 将老师放进列表中
        teacher_list.append(teacher_name)
        index +=1
    return teacher_list

teacher_list=create_teachers()
print(teacher_list)

# # 函数调用多次，每次返回一个新的变量
# teacher_list=create_teachers()
# print(id(teacher_list))
# teacher_list2=create_teachers()
# print(id(teacher_list2))

# 分配老师
for teacher in teacher_list:
     # 产生一个办公室编号的随机数
     office_number=random.randint(0,2)
     # 给老师随机分配办公室
     school[office_number].append(teacher)

# 查看各办公室老师
for office in school:
    for person in office:
        print(person,end=' ')
    print()
