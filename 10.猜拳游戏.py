
# 1.获取用户输入的石头（0）、剪刀（1）、布（2）

# 2.电脑产生的石头（0）、剪刀（1）、布（2）

# 3.判断胜负
##########################################################################################
# 代码实现如下：
# 导入 random 模块（工具箱）---import random随机数
import random

# 获取用户输入的拳头
user_quan=int(input('请出拳 石头（0）、剪刀（1）、布（2）：'))

# 获取电脑出拳,randint 用于产生一个范围的随机数
computer_quan=random.randint(0,2)
print(computer_quan)
# 判断胜负:玩家胜利的情况
if 0<=user_quan <=2 and 0<=computer_quan<=2:
    if user_quan == 0 and computer_quan == 1 \
            or user_quan == 1 and computer_quan == 2 \
            or user_quan == 2 and computer_quan == 0:
        print('您赢了！')
    # 平局
    elif user_quan == computer_quan:
        print('平局')
    else:
        print('您输了！')
else:
    print('您输入有误！')

