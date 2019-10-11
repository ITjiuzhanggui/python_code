# age = 23
# message = "Happy " + str(age) + "rd Birthday!"
# print(message)
# print('Hello Python people!')
# user_0 = {'username': 'efermi',
#           'first': 'enrico',
#           'last': 'fermi',
#           }
# for key, value in user_0.items():
#     print('\nkey: ' + key)
#     print('\nvalue:' +value)

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     }
#
# }
# for username, user_info in users.items():
#     print("\nUsername: " + username)
#     full_name = user_info['first'] + " " + user_info['last']
#     location = user_info['location']
#
#     print("\tfull_name: " + full_name.title())
#     print("\tlocation: " + location.title())
#
# for username, user_info in users.items():
#     print("\nUsername: "+ username)
#     full_name = user_info['first'] + user_info['last']
#     location = user_info['location']


# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print("\n\tI have a " + animal_type + ".")
#     print("My" + animal_type + "'s name is" + pet_name.title() + ".")
#
#
# describe_pet(pet_name="willie")
# describe_pet(pet_name="xioahua")


# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# 让实参变成可选的
# def get_frmatted_name(first_name, last_name, middle_name=''):
#     """返回整洁的姓名"""
#     if last_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_frmatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_frmatted_name('john', 'lee', 'hooker')
# print(musician)


# 返回字典
# 函数可返回任何类型的值，包括列表和字典等较为复杂的数据结构。
# def build_person(frist_name, last_name, age=''):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first': frist_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# # 结合使用函数和while循环
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# # 这是一个无限循环
# while True:
#     print('\nPlease tell me your name:')
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(l_name, f_name)
#     print("\nHello, " + formatted_name + "!")


# break:结束循环
# continue:结束当前循环进入下一个循环

# 传递列表
# def greet_users(names):
#     """向列表中的每位用户都发出简单的问候"""
#     for name in names:
#         msg = "Hello, " + name.title() + '!'
#         print(msg)
#
#
# username = ['hannah', 'ty', 'margot']
# greet_users(ussername)

# 在函数中修改列表
# def greet_users(names):
#     """向列表中的每一位用户都发出简单的问候"""
#     for name in names:
#         msg = "Hello," + name.title() + "!"
#         print(msg)
#
#
# names = ['hannah', 'ty', 'margot']
# greet_users(names)


# 首先创建一个列表，其中也包含一些要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # 拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # 模拟根据设计制作制作3D打印模型的过程
#     print('Printing model: ' + current_design)
#     completed_models.append(current_design)
# # 显示打印好的所有模型
# print("\nThe follwing modes have been printed: ")
# for completed_models in completed_models:
#     print(completed_models)
#
#
# def print_modles(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe follwing  models have been printed: ")
#     for completed_model in completed_models:
#         print(completed_models)
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_modles(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# def make_pizza(*toppings):
#     """打印顾客的所有配料"""
#     print("\nMaking a pizza with the following toppings: ")
#     for topping in toppings:
#         print("_ " + topping)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参
# python先匹配位置参数和关键字实参，再将余下的实参收集到最后一个形参中。

# def make_pizza(size, *toppings):
#     """概述要制作的比萨"""
#     print("\nMakeing a" + str(size) +
#           "_inch pizza with the following toppings: ")
#
#     for topping in toppings:
#         print("_ " + topping)
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.5.2 使用任意数量的关键字实参
# def build_profile(first, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户一切"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
#
# print(user_profile)


# dict = {'Google': 'wwww.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'wwww.taobao.com'}
#
# print('字典：%s' % dict.items())
#
# # 遍历字典列表
# for key, values in dict.items():
#     print(key, values)

# from test import pizza
#
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 函数编写指南，需要牢记：
# 应给函数指定描述名称，且在其中使用小写字母和下划线
# 描述性名称可帮助你和别人明白代码想要做什么。
# 给模块命名时也应遵循上述约定
# 每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式，
# 文档良好的函数让其它程序员只需要读文档字符串的描述就能够使用它：他们完全可以相信代码如描述
# 那样运行;只要知道函数的名称，需要的实参以及返回值的类型，就能在自己的程序中使用它
# 给形参指定默认值时，等号俩边不要有空格:
# 对于函数中的关键字实参，也应遵循这种约定；

# class Dog(object):
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         print(self.name.title() + "\t\nis now sitting. ")
#
#     def roll_over(self):
#         """模拟小狗命令时打滚"""
#         print(self.name.title() + "rolled over! ")
#
#
# s = Dog('willie', 6)
# your_dog = Dog('Lucy', 3)
# Dog.sit()
# Dog.roll_over(your_dog)
#
# print("My dog's name is " + your_dog.name.title() + ".")
# print("My dog is " + str(.age) + ' years old.')
# 根据类来创建对象被称为实例化;
# 这让你能够使用类的实例；


# class Car(object):
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 76
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + " " + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         将里程表读书设置为指定的值
#         禁止将里程往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """将里程表读数增加指定的量"""
#         self.odometer_reading += miles
#
#
# my_new_car = Car('audi', 'A4', 2016)
#
# print("\n\t" + my_new_car.get_descriptive_name())
# # my_new_car.read_odometer()
# # my_new_car.odometer_reading = 23  # 最简单的方式：通过实例直接访问它
# # my_new_car.read_odometer()
# my_new_car.update_odometer(79)  # 定义一个函数，让其自动更新里程
# my_new_car.read_odometer()
#
# my_used_car = Car('subaru', 'outback', 2013)
# print("\n\t" + my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23334)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)  # 通过方法对属性的值进行递增
# my_used_car.read_odometer()

# class Dog():
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self, name, age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟小狗被命令时蹲下"""
#         print(self.name.title() + " " + "is now sitting.")
#
#     def roll_over(self):
#         print(self.name.title() + "rolled over!")
#
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
#
# print("My dog's name is" + my_dog.name.title() + ".")
# print("My dos's name is " + your_dog.name.title() + " " + "it " + str(your_dog.age) + "years old. ")


# 根据类创建实例
# class Car():
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 8  # 给属性指定默认值
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + " " + self.make + " " + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """"打印一条指出汽车里程的消息"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     # 通过方法修改属性
#     # 添加逻辑：禁止任何人将里程表读数往回调
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         """将里程表读数增加指定的量"""
#         self.odometer_reading += miles
#
#
# class ElectricCar(Car):
#     """电动车的独特之处"""
#
#     def __init__(self, make, model, year):
#         """初始化父类的属性"""
#         super().__init__(make, model, year)
#         self.battery_size = 70
#
#     def desctibe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#         print('This car has a ' + str(self.battery_size) + "-KMh battery.")
#
#     def fill_gas_tank(self):
#         """电动车没有邮箱"""
#         print("This car doesn't need a gas tank!")
#
#
# class Batter():
#     """一次模拟电动汽车电瓶的简单尝试"""
#
#     def __init__(self, battery_size=70):
#         """初始化电瓶的属性"""
#         self.battery_size = battery_size
#         self.battery = Batter()
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息"""
#
#         print("This cat has a %s" % self.battery_size + "....")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# my_tesla.update_odometer(99999)
# print("\n\t" + my_tesla.get_descriptive_name())
# print(my_tesla.read_odometer())
# # print("\n\t" + str(my_tesla.desctibe_battery()))
#
# my_new_car = Car('audi', 'a6L', 2019)
# print(my_new_car.get_descriptive_name())
# print(my_new_car.read_odometer())
# # print(dir(ElectricCar)
# # 修改属性的值
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# # 通过方法修改属性
# my_new_car.update_odometer(56)
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(7)
# my_new_car.read_odometer()
#
#
# # 通过方法对属性的值进行递增
# my_new_car.increment_odometer(100)  # ^^^^^^
# my_tesla.increment_odometer(200)
# my_new_car.read_odometer()
# my_tesla.desctibe_battery()

# 继承
# 如果你要编写的类是另一个现成类的特殊版本，可使用继承
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；
# 原有的类称为父类，而新的类成为子类；
# 子类继承类其父类的所有属性和方法，同时还可以定义自己的属性和方法；

# Python标准库是一组模块，安装的Python都包含它。

# collections 中的OrderedDict类，

# from collections import OrderedDict
# favorite_languages = OrderedDict()
#
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
#
# for k, v in favorite_languages.items():
#     # if isinstance(v, (list,)):
#         # print(v[-1])
#     # if isinstance(v, dict):
#     #     # for k, v in v.items():
#     #     #     print(v)
#     #     print(v)
#     print(k.title() + "'s favorite languages is  " + v.title() + ".")


# file_name = 'test.txt'
# with open(file_name, 'r') as f:
#     lines = f.readlines()
#     str_1 = ''
#     for line in lines:
#         str_1 += line.rstrip()
#
# print(str_1[:5])
# print(len(str_1))


# while True:
#     first_number = input('\nFirst number:')
#     try:
#         if first_number == 'q':
#             break
#
#         second_number = input('\nSecond number:')
#         if second_number == 'q':
#             break
#
#         answer = int(first_number) / int(second_number)
#         print(answer)
#     except:
#         print('The result is wrong')


# import json
# numbers = [1, 2, 3, 4, 5]
# file_name = 'numbers.json'
#
#
# with open(file_name)as f:
#     numbers_1 = json.load(f)
# print(numbers_1)
# import json

# 10.4.2 保存和读取用户生成的数据

# username = input("What is your name: ")

# filename = 'numbers.json'
# try:
#     with open(filename)as f:
#         username = json.load(f)
#
# except FileNotFoundError:
#     username = input("What is your name:")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print("We'll remember you when you come back, " + username + "!")
#
# else:
#     print("Welcome back," + username + "!")


# import json
#
#
# def get_stored_username():
#     """如果存储了用户名，就获取它"""
#     filename = 'numbers.json'
#     try:
#         with open(filename)as f:
#             username = json.load(f)
#     except FileExistsError:
#         return None
#     else:
#         return username
#
#
# def greet_user():
#     """问候用户，并指出其名字"""
#     username = get_stored_username()
#     if username:
#         print("Welcome back," + username + "!")
#
#     else:
#         username = input("What is your name?")
#         filename = 'numbers.json'
#         with open(filename) as f:
#             json.dump(username,f)
#             print("We'll remember you when you come back," + username + "!")
#
#
# greet_user()


# import json
#
# filename = 'numbers.json'
# try:
#     with open(filename)as f:
#         username = json.load(f)
#
# except FileNotFoundError:
#     username = input("What is your name:")
#     with open(filename, 'w')as f:
#         json.dump(username, f)
#         print("\n" + "We'll remember you when you come back," + username + '!')
#
# else:
#     print("Welcome back," + username + "!")


# import json
#
#
# def greet_user():
#     filename = "numbers.json"
#
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name: ")
#         with open(filename, 'w')as f:
#             json.dump(username, f)
#             print("we'll remember you when you come back," + username + "!")
#     else:
#         print("Welcome back," + username + "!")
#
#
# greet_user()


# import json
#
# add_list = []
#
#
# def get_stored_username():
#     """如果存储了用户名，就获取它"""
#     filename = 'numbers.json'
#     try:
#         with open(filename)as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
#
#
# def get_new_name():
#     """提示用户输入用户名"""
#     username = input("What is your name:")
#     filename = "numbers.json"
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#     return username
#
#
# def greet_user():
#     """问候用户，并指出其名字"""
#     username = get_stored_username()
#     if username:
#         print("Welcome back," + username + "!")
#
#     else:
#         username = get_new_name()
#         print("We'll remember you when you come back," + username + "!")
#
#
# greet_user()


# from test.name_function import get_formatted_name
# print("Enter 'q' at any time to quit.")
#
# while True:
#     first = input("\nPlease give me a first name:")
#     if first == '/':
#         break
#     last = input("Please give me a last name:")
#     if last == '/':
#         break
#
#     formatted_name = get_formatted_name(first, last)
#     print("\tNeatly formatted name: " + formatted_name + ".")

# import pytest
# import unittest
# from test.name_function import get_formatted_name
#
#
# class NamesTestCase(unittest.TestCase):
#     """测试name_function.py"""
#
#     def test_first_last_name(self):
#         """能够正确地处理像janis joplin这样的姓名吗？"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         # print(formatted_name)
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
#
# unittest.main()




















