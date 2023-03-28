# 具体功能需求如下:
# 1.员工信息: 编号、姓名、工资、性别
# 2.编号不允许修改,不允许重复.
# 3.功能实现:
#     3.1 新增员工信息
#     3.2 根据员工编号删除员工信息
#     3.3 根据员工编号修改员工信息
#     3.4 显示所有员工信息.
#     3.5退出员工管理系统

# 思路分析如下:
# 1.确定员工信息使用哪种容器来存储
# 2.搭建系统的业务框架
# 3.具体实现每个系统功能

# 元祖、字符串不能修改，字典不能重复

##############################################
# ------------------------存储所有员工信息----------------
employee={}
# ------------------------显示系统菜单--------------------
def show_menu():
    """1.显示系统菜单"""
    print('-'*30)
    print('员工管理系统 v1.0')
    print('1:添加员工信息')
    print('2:删除员工信息')
    print('3:修改员工信息')
    print('4:查询员工信息')
    print('5:退出员工管理系统')
    print('-' * 30)

# -------------------------添加员工信息----------------------
def add_new_employee():
    """添加员工信息"""
#     1.员工编号、员工姓名、员工性别、员工薪资
    employee_id=input('请输入员工编码：')
#        1.1 判断员工信息是否存在，如果存在，则拒绝添加，并提示：员工编号重复，添加失败
    all_employee_id=list(employee.keys())
    if employee_id in all_employee_id:
        print('员工编号重复，添加失败！')
        return
#        1.2 如果不重复，则进行下面的操作
    employee_name= input('请输入员工姓名：')
    employee_gender=input('请输入员工性别：')
    employee_salary=input('请输入员工薪资：')
#     2.将员工信息保存在字典中
#        2.1编号作为键，剩下薪资作为值
    employee_info={'name':employee_name,'gender':employee_gender,'salary':employee_salary}
#        2.2 '1001':{'name':xxx ,'age':xxx,'gender':xxx,'salary': xxx}
    employee[employee_id]=employee_info
    print('员工 %s 员工信息添加成功'% employee_id)



# -------------------------删除员工信息-------------------------

def del_employee():
    #     1.员工编号、员工姓名、员工性别、员工薪资
    employee_id = input('请输入员工编码：')
    #        1.1 判断员工信息是否存在，如果不存在，则拒绝添加删除失败，并提示：该员工不存在，删除失败
    all_employee_id = list(employee.keys())
    if employee_id not in all_employee_id:
        print('该员工 % s不存在，删除失败！' % employee_id)
        return
    #     1.2 如果员工存在，删除成功，并提示：删除成功
    del employee[employee_id]
    print('员工 %s 删除成功!'% employee_id)
#


# # -----------------------显示员工信息-------------------------
def show_all_employee():
    """显示员工信息"""

    for employee1 in employee.items():
        print('%s\t\t%s\t\t%s\t\ts' % (employee1[0],employee1[1]['name'],employee1[1]['gender'],employee1[1]['salary']))

# --------------------------修改员工信息------------------------
def update_employee():
    """修改员工信息"""
        # 1.员工编号、员工姓名、员工性别、员工薪资
    employee_id = input('请输入员工编码：')
        # 1.1 判断员工信息是否存在，如果不存在，错误提示：该员工不存在！，并且终止函数执行
    all_employee_id = list(employee.keys())
    print('该员工不存在！')
        # 1.2 如果存在，修改对应信息
        # 1.2.1 显示原来的信息，然后再修改
    new_employee_name=input('姓名是：%s 您要修改为：'% employee[employee_id]['name'])
    new_employee_gender=input('性别是：%s 您要修改为：'% employee[employee_id]['gender'])
    new_employee_salary = input('薪资是：%s 您要修改为：' % employee[employee_id]['salary'])
    # 如果用户直接回车不输入，则表示不更新
    if new_employee_name != []:
        employee[employee_id]['name']=new_employee_name
    if new_employee_gender != []:
        employee[employee_id]['gender'] = new_employee_gender
    if new_employee_salary !=[]:
        employee[employee_id]['salary'] = new_employee_salary
    print('员工编号为 % s 的员工信息修改成功' %employee_id)

# -------------------调用以上函数----------------
while True:
    # 1.显示系统菜单
    show_menu()
    # 2.获得用户输入的菜单编号
    user_operate = input('请输入您要操作的编号：')
    # 3.根据用户输入来判断做什么事情
    if user_operate == '1':
        add_new_employee()
        print(employee)
    elif user_operate == '2':
        del_employee()
        print(employee)

    elif user_operate == '3':
        update_employee()
        print(employee)

    elif user_operate == '4':
        show_all_employee()
        print(employee)
    elif user_operate == '5':
        print('欢迎再次使用本系统！')
        break
    else:
        print('您的输入有误，请重新输入！')



