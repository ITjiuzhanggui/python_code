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
