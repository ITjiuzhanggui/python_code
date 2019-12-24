# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents)
# path = r"C:\Users\xinhuizx\python_cod\练习.txt"
# with open(r"C:\Users\xinhuizx\python_cod\练习.txt", 'r', encoding='utf-8')as file_object:
#     contents = file_object.read()
#     print(contents)

"""逐行读取"""
# filename = r'C:\Users\xinhuizx\python_cod\练习.txt'
#
# with open(filename)as f:
#     for line in f:
#         print(line.rstrip())


# file_name = 'pi_str_test.txt'
#
# with open(file_name, 'w+', encoding='utf-8') as f:
#     f.write('I love you Audi')


"""
10.4.1  存储数据
使用json.dump()和json.load()
"""
# import json
#
# number = [122, 222, 322, 422, 522, 1122, 722, ]
#
# file_name = 'numbers.json'
# with open(file_name, 'a+')as f:
#     json.dump(number, f)


# 读取json文件中的数据
# import json
#
# file_name = 'numbers.json'
# with open(file_name, 'r')as f:
#     numbers = json.load(f)
# print(numbers)

# import json
#
# username = input('What is your name? ')
# file_name = 'username.json'
# with open(file_name, 'a')as f:
#     json.dump(username, f)
#     print(username)

# import json
#
# filename = 'username.json'
# try:
#     with open(filename)as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input('What is your name? ')
#     with open(filename, 'w')as f:
#         json.dump(username, f)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")


"""
10.4.3  重构
"""
# import json
#
#
# def greet_user():
#     """
#     问候用户，并指出其名字
#     :return:
#     """
#     filename = 'username.json'
#     try:
#         with open(filename)as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input('What is your name? ')
#         with open(filename, 'w')as f:
#             json.dump(username, f)
#             print("We'll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")
#
#
# greet_user()

# import json
#
#
# def get_stored_username():
#     """如果存储了用户名，就获取它"""
#     filename = 'username.json'
#     try:
#         with open(filename)as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         return None
#
#     else:
#         return username
#
#
# def greet_user():
#     """问候用户，并指出其名字"""
#     username = get_stored_username()
#     if username:
#         print("Welcome back, " + username + "!")
#     else:
#         username = input("What is your name？ ")
#         filename = 'username.json'
#         with open(filename, 'w')as f:
#             json.dump(username, f)
#             print("We'll remember you when you come back, " + username + "!")
#
#
# greet_user()


"""
最终版本
"""
import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename)as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w')as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()


