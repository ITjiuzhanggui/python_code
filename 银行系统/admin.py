import time


class Admin():
    def __init__(self, name, passwd):
        self.name = name
        self.__passwd = passwd
        self.__status = False

    def adminView(self):
        for i in range(4):
            print("".center(60, "*"))
        s1 = "欢迎光临张氏银行"
        print(s1.center(60 - len(s1), "*"))

        for i in range(4):
            print("".center(60, "*"))

        if self.status:
            print("管理员被锁定，请联系大神")
            return -1
        name = input("请输入管理员用户名:")
        if name != self.name:
            print("用户名输入错误")
            return -1
        if self.checkAdminPasswd() != 0:
            return -1
        return 0

    def adminAction(self):
        print("""************************************************************
                ***************开户(1)****************销户(2)***************
                ***************查询(3)****************转账(4)***************
                ***************取款(5)****************存款(6)***************
                ***************锁定(7)****************解锁(8)***************
                ***************改密(9)****************补卡(0)***************
                ************************退出 系统(q)************************
                ************************************************************
        """)


if __name__ == '__main__':

