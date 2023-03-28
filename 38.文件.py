# 文件读写
# 使用open 函数打开一个文件
fa=open('a.txt','w')
fb=open('b.txt','w')

# # 1.写入文件
my_content='hello world ! 第一次写入文件！'
fa.write(my_content)
print(my_content)

# 2.读取文件数据
fb=open('b.txt','r')
# read函数默认读取文件所有数据
my_content=fb.read()  # 括号内填数字，代表读取几个字符

print(my_content)

# # 关闭文件
# fa.close()
# fb.close()

def test01():
    """读方式打开文件"""
    f=open('a.txt','r')
    content = f.read()
    print(content)
    f.close()

#      w 模式默认是会覆盖文件中的数据
#      w 模式如果发现文件不存在，则会新建文件
def test02():
    """写方式打开文件"""
    f=open('a.txt','w')
    # write 函数一次写一行
    f.write('hello world ! 第一次写入文件！')
    # writelines 函数一次写多行，参数是一个列表，列表每一个元素都是一行数据，\n 换行
    f.writelines(['aaa\n','bbb\n','ccc\n'])
    f.close()

def test03():
    """a 方式打开文件"""
    f=open('a.txt','a')
    f.write('\n hello python')
    f.close()


#
# test01()
# test02()
# test03()
test04()