import time
from Card.bank import Bank


class ATM(object):
    def __init__(self):
        self.account = '1'
        self.passwd = '1'
        self.money = 0
        self.isActive = True

    def atmInitView(self):
        """开机画面"""
        print("=====================================")
        print("=           系统开机界面             =")
        print("=            登陆(11)               =")
        print("=            关机(22)               =")
        print("=            提额(33)               =")
        print("=            改密(44)               =")
        print("=====================================")

    def welcomeView(self):
        """欢迎界面"""
        print("=====================================")
        print("=       zxh is a good man          =")
        print("=            插卡(111)              =")
        print("=            开户(222)              =")
        print("=            补卡(333)              =")
        print("=            返回(444)              =")
        print("=====================================")

    def optionsView(self, name, cardID):
        print("====================================")
        print("用户名%s  卡号:%s=" % (name, cardID))
        print("=      查询(1)      转账(2)          =")
        print("=      存款(3)      取款(4)          =")
        print("=      改密(5)      注销(6)          =")
        print("=      锁定(7)      解锁(8)          =")
        print("=             退卡(9)                =")
        print("=====================================")

    def checkPasswd(self):
        """(11)登陆校验逻辑"""
        account = input("请输入系统账号:")
        passwd = input("请输入系统密码:")
        if account != self.account or passwd != self.passwd:
            print("账号密码错误！")
            return 1
        else:
            print("系统设置成功，正在启动......")
            return 0

        time.sleep(2)

    def shutDown(self):
        """
        关机(22)
        应该是将数据持久化存储
        """
        print("正在保存数据......")

    def addMoney(self, money):
        """提额"""
        money = int(input("请输入提额额度:"))
        self.money += money
        if not self.isActive:
            self.isActive = True

    def changeAtmPasswd(self):
        """改密"""
        passwd = input("请输入原始密码:")
        if passwd != self.passwd:
            print("密码错误，修改失败!")
            return
        passwd1 = input("请输入新密码:")
        passwd2 = input("请输验证密码:")

        if passwd1 != passwd2:
            print("俩次密码不同，修改失败")

        else:
            self.passwd = passwd1
            print("系统密码修改成功")

        time.sleep(2)

    def createCard(self):
        """开户"""
        idCard = input("请输入您的身份证号:")
        # 验证是否存在该用户
