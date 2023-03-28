#
# # 1.简易版的员工管理系统
# # 1.1接收用户输入
# # 1.2
# #   输入1：展示所有员工
# #   输入2：新增一个员工信息
# #   输入3：修改一个员工信息
# #   输入4：删除一个员工信息
# #   输入5：退出系统
# ##########################################################################################
# # 代码实现如下：
#
# print('欢迎使用员工管理系统v1.0')
# # 显示系统菜单
# print('*'*10 + '操作菜单' +'*'*10)
# print('1.显示所有员工信息')
# print('2.新增一个员工信息')
# print('3.修改一个员工信息')
# print('4.删除一个员工信息')
# print('5.退出系统')
# # 保存用户输入操作
# user_operation = int(input('请输入操作编码：'))
# while 1<= user_operation<=5:  # 或者也可写 while True：  --True 代表是否满足下面if 条件
#     if user_operation == 1:
#         print('name', 'age', 'sex')
#         print('刘', '19', '女')
#         print('肖', '30', '男')
#         print('芬', '31', '女')
#     elif user_operation == 2:
#         name = input('请输入员工姓名：')
#         age = input('清晰呼入员工年龄：')
#         sex = input('请输入员工性别：')
#         print('新员工 %s 新增成功' % name)
#     elif user_operation == 3:
#         name = input('请输入您要修改的员工姓名：')
#         print('员工 %s 信息修改成功！' % name)
#     elif user_operation == 4:
#         name = input('请输入您要修改的员工姓名：')
#         print('员工 %s 信息删除成功！' % name)
#     elif user_operation == 5:
#         name = input('退出系统')
#         print('再见')
#         break
#         user_operation += 1
# else:
#     print('操作有误！')


##########################################################################################
# 2.猜拳游戏
# 代码实现如下：
# 导入 random 模块（工具箱）---随机数
import random
# 判断胜负:玩家胜利的情况
while True:
    # 获取用户输入的拳头
    user_quan = int(input('请出拳 石头（0）、剪刀（1）、布（2）：'))
    if user_quan == 3:
        print('退出游戏！')
        break
    if user_quan >=4 or user_quan <0:
        print('您输入有误！')
        continue
    # 获取电脑出拳,randint 用于产生一个范围的随机数
    computer_quan = random.randint(0, 2)
    print(computer_quan)
    if 0<=user_quan <=2 and 0<=computer_quan<=2:
        if (user_quan == 0 and computer_quan == 1 )\
            or (user_quan == 1 and computer_quan == 2) \
            or (user_quan == 2 and computer_quan == 0):
            print('您赢了！')
    # 平局
    elif user_quan == computer_quan:
        print('平局!')
    else:
        print('您输了！')

