# 字典：dict

# my_dict={k1:v1,k2:v2}

def test01():
    """1.字典定义"""

    my_dict={'name1':'liu','name2':'yan','name3':'fen',102:100}
    print(my_dict['name1'])  # 通过关键字查询
    print(my_dict[102])
    my_dict['name1']='xiao'
    print(my_dict)

test01()  # 只有调用了才能打印出来

##########################################################################################
# def test02():
#     """2.字典不支持索引，也不支持切片"""
#
#     my_dict={'name1':'liu','name2':'yan','name3':'fen',102:100}
#     print(my_dict[0])
#     print(my_dict[1:])

# test02()  # 此函数会报错

##########################################################################################
def test03():
    """3.获取字典的值"""

    my_dict={'name1':'liu','name2':'yan','name3':'fen',102:100}
    print(my_dict['name1'])
    # print(my_dict['name11'])  # 如果键不存在，会报错，程序终止
#     使用get 方法,如果键不存在，默认返回 None，程序不会终止
    print(my_dict.get('name12'))
test03()

def test04():
    """4.添加和修改元素"""

    my_dict={'name1':'liu','name2':'yan','name3':'fen',102:100}
    # 如果key不存在，则是新增元素
    my_dict['score']=99
    # 如果key存在，则是修改元素
    my_dict['name1']='xiao'
    print(my_dict)
test04()