# # from six import add_metaclass
# # from abc import ABCMeta, abstractclassmethod, abstractmethod
#
#
# # @add_metaclass(ABCMeta)
# class Car(object):
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 8
#
#     # @abstractmethod
#     def get_descriptive_name(self):
#         """返回整洁的描述信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#         # pass
#
#     # @abstractmethod
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#         def update_odometer(self, mileage):
#             """将里程表读数设置为指定的值"""
#             self.odometer_reading = mileage
#         # pass
#
#     def update_odometer(self, mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         # if mileage >= self.odometer_reading:
#         #     self.odometer_reading = mileage
#
#         # else:
#         #     print("You can't roll back an odometer!")
#
#         self.odometer_reading = mileage \
#             if mileage >= self.odometer_reading \
#             else print(
#                 "You can't roll back an odometer!"
#             )
#
#     def increment_odometer(self, miles):
#         """将历程表读数增加指定的量"""
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """初始化父类的属性"""
#         super().__init__(make, model, year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print("This car has a %s" % self.battery_size + "-KWh battery.")
#
#     def get_range(self):
#         """打印一条消息，指出电瓶的续航里程"""
#         if self.battery_size == 70:
#             range = 240
#
#         elif self.battery_size == 85:
#             range = 270
#
#         message = "This car can go approximately %s" % range
#         message += " miles on a full charge."
#         print(message)
#
#
# my_new_car = Car('audi', 'a4', 2016)
# my_tesla = ElectricCar('teals', 'model s', 2019)
#
# print(my_new_car.get_descriptive_name())
# # my_new_car.odometer_reading = 23  # 直接修改属性的值
# my_new_car.update_odometer(10)  # 通过方法修改属性的值
# my_new_car.read_odometer()
# my_new_car.increment_odometer(1)
# my_new_car.read_odometer()
#
# # 电动车的执行
# # print("\n\n" + my_tesla.get_descriptive_name())
# # print(my_tesla.describe_battery())
# my_tesla.get_descriptive_name()
# my_tesla.read_odometer()
#
# my_tesla.battery_size = 85
# my_tesla.describe_battery()
# my_tesla.get_range()
