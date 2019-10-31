class ATM(object):
    def __init__(self):
        self.account = '1'
        self.passwd = '1'
        self.money = 0
        self.isActive = True

    def atmInitView(self):
        print("==================================")
        print("        登陆(11)                   ")
        print("        关机(22)                   ")
        print("        提额(33)                   ")
        print("        改密(44)                   ")
        print("==================================")

    def welcomeView(self):
        print("==================================")
        print("       zxh is a good man          ")
        print("            插卡(111)              ")
        print("            开户(222)              ")
        print("            补卡(333)              ")
        print("            返回(444)              ")
        print("==================================")

    def optionsView(self, name, cardID):
        print("==================================")
        print("用户名%s  卡号:%s=" % (name, cardID))
        print("      查询(1)      转账(2)         ")
        print("      存款(3)      取款(4)         ")
        print("      改密(5)      注销(6)         ")
        print("      锁定(7)      解锁(8)         ")
        print("             退卡(9)               ")
        print("==================================")

        # 提额
        def addMoney(self, money):
            self.money += money
            if not self.isActive:
                self.isActive = True
