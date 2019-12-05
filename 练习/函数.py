"""
8.1.1  向函数传递信息 （实参和形参）
"""


def greet_user(username):
    """
    显示简单的问候语
    :param username:
    :return:
    """
    print('Hello, ' + username.title() + '!')


# greet_user('jesse')

"""
8.2.1  位置实参
你调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参，为止，
最简单的关联方式是基于实参的顺序，这种关联方式被称为位置实参。
"""


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print('\nI have a  ' + animal_type + ".")
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')


# describe_pet('hamster', 'harry')

"""
8.2.2  关键字实参
关键字实参是传递给函数的名称-值对；
你直接在实参中将名称和值关联起来；
"""


def describe_pet(animal_type, pet_name):
    print('\nI have a  ' + animal_type + ".")
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')


# describe_pet(animal_type='hamster', pet_name='harry')

"""
默认值
编写函数时，可给每个形参指定默认值。
"""


def describe_pet(pet_name, animal_type='dog'):
    print('\nI have a ' + animal_type + ".")
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')


# describe_pet(pet_name='willie')

"""
8.3 返回值
"""


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name


musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
"""
8.3.2  让实参变成可选的
"""


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

"""
8.3.3  返回字典
"""


def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')


# print(musician)

# 扩展

def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

"""
8.3.4  结合使用函数和while循环
"""


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# 这是一个无限循环！
# while True:
#     print('\nPlease tell me your name:')
#     f_name = input("First name: ")
#     l_name = input("last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print('\nHello ' + formatted_name + '!')

"""
8.5.1  结合使用位置实参和任意数量实参
"""

# def make_pizza(size, *toppings):
#     """
#     概述要制作的披萨
#     :param size:
#     :param toppings:
#     :return:
#     """
#     print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
8.5.2  使用任意数量的关键字实参
"""


def build_profile(first, last, **user_info):
    """
    创建一个字典，其中包含我们知道的有关用户的一切
    :param first:
    :param last:
    :param user_info:
    :return:
    """

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstrin', location='princeton', field='physics')
# print(user_profile)
