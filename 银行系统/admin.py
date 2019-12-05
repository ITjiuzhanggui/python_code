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

    def checkAdminPasswd(self):
        n = 0
        while n <= 3:
            if n == 3:
                self.status = True
                print("输入超过3次，管理员被锁定，请联系大神张鑫慧")
                return -1
                passwd = input("请输入密码:")
                if passwd != self.__passwd:
                    print("密码输入错误，请重新输入")
                n += 1
            else:
                print("密码验证成功，请稍后")
                time.sleep(2)
                return 0


if __name__ == '__main__':
