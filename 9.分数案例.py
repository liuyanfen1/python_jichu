
# 根据分数显示档位

# 1.获取输入的分数

# 2.将分数从字符串类型转换成数字类型

# 3.根据分数分档
#     3.1  90-100  A档
#     3.2  80-90  B档
#     3.3 70-80  C档
#     3.4 60-70  D档
#     3.5 60 以下  E档

# 获取输入的分数：方式一
# score=int(input('请输入分数：'))  # 或者score=float(input('请输入分数：'))
# if score>=90 and score <=100:
#     print('你太棒了！')
# elif score>=80 and score <90:
#     print('优秀！')
# elif score>=70 and score <80:
#     print('良好！')
# elif score>=60 and score <70:
#     print('及格！')
# elif score >100 or score <0:
#     print('输入错误！')
# else:
#     print('继续加油哦！')

# 获取输入的分数：方式二
score=int(input('请输入分数：'))  # 或者score=float(input('请输入分数：'))
if score >=0 and score <=100:
    if score >= 90 and score <= 100:
        print('你太棒了！')
    elif score >= 80 and score < 90:
        print('优秀！')
    elif score >= 70 and score < 80:
        print('良好！')
    elif score >= 60 and score < 70:
        print('及格！')
    else:
        print('继续加油哦！')
else :
    print('输入错误！')