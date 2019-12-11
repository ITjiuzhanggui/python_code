"""
9.1 创建和使用类
"""


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """
        初始化属性name和age
        :param name:
        :param age:
        """
        self.name = name
        self.age = age

    def sit(self):
        """
        模拟小狗被命令时蹲下
        :return:
        """
        print(self.name.title() + 'is now sitting.')

    def roll_over(self):
        """
        模拟小狗被命令时打滚
        :return:
        """
        print(self.name.title() + 'rolled over！')


# my_dog = Dog('willie', 6)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + "years old.")
"""
2.  调用方法
"""
# my_dog.sit()
# my_dog.roll_over()

"""
3.  创建多个实例
"""
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + "years old.")
# my_dog.sit()
# my_dog.roll_over()
# print("\nYour dog's name is " + your_dog.name.title() + ".")
# print("Your dog is " + str(your_dog.age) + "years old.")
# your_dog.sit()
# your_dog.roll_over()

"""
9.2  使用类和实例
"""


# 编写一个表示汽车的类，他存储了有关汽车的信息，还有一个汇总这些信息的方法
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """
        初始化描述汽车的属性
        :param make:
        :param model:
        :param year:
        """
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """
        返回整洁的描述性信息
        :return:
        """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


# my_new_car = Car('audi', 'a4', '2019')
# print(my_new_car.get_descriptive_name())

"""
9.2.2  给属性指定默认值
"""


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """
        初始化描述汽车的属性
        :param make:
        :param model:
        :param year:
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 0

    def read_odometer(self):
        """
        打印一条指出汽车里程的消息
        :return:
        """
        print("This car has " + str(self.odometer_reding) + "miles on it.")


# my_new_car = Car('audi', 'a4', '2019')
# my_new_car.read_odometer()

