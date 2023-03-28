#
# 查找：find
# user_email='liuyanfen@163.com'
# 1.找到字符串中 @ 的位置
# 2.获得字符串中的子串

user_email='liuyanfen@163.com'
# 如果超找到，返回子串第一次出现的位置
# 如果差找不到 @，返回-1
position=user_email.find('@')
if position==-1:
    print('@不存在，邮箱不合法！')
else:
    print('@的位置是：',position)

##########################################################################################
# 拆分：split -- 使用特别多

my_str='aa#bb#cc#dd'
ret = my_str.split('#')
print(ret)
print(ret[3])  # 3 表示第四个字符串

##########################################################################################
# 统计某个字符串出现的次数：count

# 例：邮箱校验 @ 出现的次数，大于1次 或者小于一次，则邮箱不合法
user_email='liuyanfen@163.com'
# 获得@ 字符串在user_email 中出现的次数
char_count=user_email.count('@')
if char_count >1 or char_count <1:
    print('您的邮箱不合法！')
else:
    result=user_email.split('@')
    print(result)