"""
人：User
属性：姓名，身份证号码，电话号，卡(多张卡 {卡号：卡对象......})
卡：插卡，输入信息

卡：Card
属性：卡号，密码，余额，是否正常
行为：

提款机：ATM
属性：系统账号，系统密码，余额，是否正常
行为：
系统开机界面，欢迎界面，功能操作界面，修改系统密码，提额，开户，查询，存款，取款，转账，改密，锁定，解锁，注销，补卡，退出

银行(单例)：Bank
属性：用户字典({身份证号：用户对象......})
行为：

"""
import time

from Card.atm import ATM
from Card.bank import Bank
from Card.card import Card
from Card.user import User

# 创建银行对象
BANK = Bank()
atmMachine = ATM()
atmMachine.money = 10000


def main():
    while True:
        # 展示开机界面
        atmMachine.atmInitView()
        # 接受操作
        optionStr = input("请输入操作:")

        # 操作匹配
        if optionStr == '11':
            """登陆"""
            res = atmMachine.checkPasswd()
            if not res:
                """循环进入欢迎界面"""
                time.sleep(2)
                welcome()

        elif optionStr == '22':
            """关机"""
            atmMachine.shutDown()
            break

        elif optionStr == '33':
            """提额"""
            atmMachine.addMoney()

        elif optionStr == '44':
            """改密"""
            atmMachine.changeAtmPasswd()

        time.sleep(2)


def welcome():
    while True:
        atmMachine.welcomeView()
        # 等待操作
        optionStr = input("请输入操作:")

        # 操作匹配
        if optionStr == '111':
            """插卡"""
            res = atmMachine.checkPasswd()
            if not res:
                """循环进入欢迎界面"""
                time.sleep(2)
                welcome()

        elif optionStr == '222':
            """开户"""
            pass

        elif optionStr == '333':
            """补卡"""
            pass

        elif optionStr == '444':
            """返回"""
            print("返回开机界面")
            break

        time.sleep(2)


if __name__ == '__main__':
    main()
