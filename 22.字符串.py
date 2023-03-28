
# 字符串定义
#
my_str='hello'
      # 01234  --下标或者索引
# my_str="hello"
# my_str="""
#  你好啊
#  我很好
#  家人好吗？
#  """
# print(my_str)

# 遍历：不重复的访问容器中的每一个元素
# 索引支持正数索引，也支持负数索引
print(my_str[0])  # --0 是索引或者下标
print(my_str[-5])
print(my_str[-1])

# 1.while 循环方式进行遍历
i=0
while i<5:
    print(my_str[i],end='')
    i +=1
print()

# 2.for 循环方式进行遍历
for v in my_str:
    print(v,end='')

