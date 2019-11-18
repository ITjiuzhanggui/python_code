"""
管理员类
名称：Admin
属性：name, passwd
方法：显示管理员欢迎界面，显示功能界面

银行卡
名称：Card
属性：id, balance
方法：生成卡号

取款机
名称：ATM
属性：
方法：开户，查询，取款，转账，存款，改密，锁定，解锁，补卡，销户

用户
名称：user
属性：姓名，身份证，电话号，银行卡
方法：
"""
import time, os
from .admin import Admin
import functions


# users = {}
def run():
    admin = functions.adminInit()
    users = functions.userInit()
    # print(users)

    if admin.adminView():
        functions.adminClose(admin)
        functions.userClose(users)
    return -1

    while True:
        admin.adminAction()
        value = input("请选择你要办理的业务:")

        if option == '1':
            pass

        elif option == '2':
            pass

        elif option == '3':
            pass

        elif option == '4':
            pass

        elif option == '5':
            pass

        elif option == '6':
            pass

        elif option == '7':
            pass

        elif option == '8':
            pass

        elif option == '9':
            pass

        elif option == '0':
            pass

        elif option == 'q':
            pass

        elif option == 'm':
            pass

        else:
            print("Fuck,你输入的根本理解不了，重新输入吧！")


if __name__ == '__main__':
    run()
