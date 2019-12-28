"""
9.3  继承
编写类时，并非总是要从空白开始，如果你要编写的类是另一个现成类的特殊版本，可使用
继承。
"""
"""
9.3.1  子类的方法 __init__()
"""


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has  " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# my_new_car = Car('AUDO', 'A4L', '2019')
# print(my_new_car.get_descriptive_name())


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)


# my_tesla = ElectricCar('tesla', 'model s', '2019')
# print(my_tesla.get_descriptive_name())
# my_tesla.update_odometer(906)
# my_tesla.read_odometer()
# my_tesla.increment_odometer(100)
# my_tesla.read_odometer()

"""
9.3.3 给子类定义属性和方法
"""


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        :param make:
        :param model:
        :param year:
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('This car has a' + str(self.battery_size) + '-kWh battery.')


# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

"""
9.3.4  重写父类的方法
对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写，为此，可在子类中 
定义一个这样的方法，即它与要重写的父类方法同名。
"""
"""
9.3.5 将实例用作属性
使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多，属性和方法清单以及文件都
越来越长，在这种情况下，可能需要将类的一部分作为一个独立的类提取出来，你可以将大型类
拆分成多个协同工作的小类
"""


class Battery():
    """一次模拟电动汽车的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""

        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += 'miles on a full charge.'
        print(message)


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化类的属性，再初始化电动汽车特有的属性
        :param make:
        :param model:
        :param year:
        """

        super().__init__(make, model, year)
        self.battery = Battery()


# my_tesla = ElectricCar('AMG', 'G63', '2020')
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

import collections
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is" + " " + language.title() + ".")



