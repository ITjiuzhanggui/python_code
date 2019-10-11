"""一组用于表示电动汽车独特之处的类"""
from test.car import Car, Battery


class ElectricCar(Car):
    """模拟电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动车汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()