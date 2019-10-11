# """要求：从键盘输入身高，如果身高没有超过150cm，则进动物园不用买票，否则需要买票。"""
# gao = int(input("请输入身高："))
#
# if gao <= 150:
#     print("不用买票可以进入！")
#
# else:
#     print("超过150CM需要买票，才能进入！！！")


# """
# 情节描述：上公交车，并且可以有座位坐下
#
# 要求：输入公交卡当前的余额，只要超过2元，就可以上公交车；如果车上有空座位，就可以坐下。
# """

# seat = 0
# money = 2
# person = 1
#
# if money == 2:
#     print("可以上公交车！")
#
#     if seat > 0:
#         print("有座位可以坐下！")
#
#     else:
#         print("没有座位，你需要站着!")
#
#         if person == 0:
#             print("不需要让座，可以睡一觉了，开心!!!")
#
#         else:
#             print("有老人，看来的让座了")
#
# else:
#     print('你余额不足，无法上车')

# """跟媳妇承认错误，说一万遍 '媳妇儿，我错了' """

# i = 1
#
# while i <= 100:
#     print("第%d次，媳妇我错了!!!" % i)
#     i += 1

# i = 1
# while i < 5:
#     print("当前是第%d次执行循环" % i)
#     print("i=%d" % i)
#     i += 1

# i = 1
# sum = 0
#
# while i <= 1000:
#     sum = sum + i
#     i += 1
#
#     print("1~100的累计和为：%d" % sum)

# i = 1
# sum = 0
# while i <= 100:
#     if i % 2 == 0:
#         sum = sum + i
#     i+=1
#
#     print("1~100的累积和为:%d" % sum)

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*', end="")
#         j += 1
#
#     print("\n")
#     i += 1

# """break是立刻结束break所在的循环"""
# name = 'itheima'
# for x in name:
#     print('----')
#
#     if x == 'l':
#         break
#     print(x)
#
# else:
#     print('==for循环过程中，如果没有执行break退出，则执行本语句==')


# """continue 是用来结束本次循环，紧接着执行下一次的循环"""
# name = 'itheima'
# for x in name:
#     print('=====')
#
#     if x == 'h':
#         continue
#     print(x)
# else:
#     print('==while循环过程中，如果没有continue则执行==')


# namesList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']
#
# length = len(namesList)
#
# i = 0
#
# while i < length:
#     print(namesList[i])
#     i += 1


# """一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配"""
# import random
#
# # 定义一个列表来保存3个办公室
# offices = [[], [], []]
#
# # 定义一个列表用来存储8位老师的名字
# names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#
# i = 0
# for name in names:
#     index = random.randint(0, 2)
#     offices[index].append(name)
#
# i = 1
# for tempNmae in offices:
#     print('办公室%d的人数为:%d' % (i, len(tempNmae)))
#     i += 1
#     for name in tempNmae:
#         print('%s' % name, end='')
#     print("\n")
#     print("-" * 20)

# """遍历字典的key<键>"""
# dict = {'name': 'zhangsan', 'sex': 'm'}
# for key in dict.keys():
#     print(key)

# """遍历字典的value<值>"""
# dict = {'name': 'zhangsan', 'sex': 'm'}
#
# for value in dict.values():
#     print(value)

# """遍历字典的项<元素>"""
# dict = {'name': 'zhangsan', 'sex': 'm'}
# for item in dict.items():
#     print(item)

# """遍历字典key-valuea<键值对>"""
# dict = {'name': 'zhangsan', 'sex': 'm'}
# for key, value in dict.items():
#     print('key = %s,  value = %s' % (key, value))

# """
# 明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性
# 他先用计算机生成了N个1～1000之间的随机整数(N<=1000),N是用户输入>的，对于
# 其中重复的数字，只保留一个，把其余相同的数字去掉，不同的数对应着
# 不同的学生的学号，然后再把这些
# 数从小到大排序，按照排好的顺序去找同学做调查，请你协助明明完成“>去重”与排序工作
# """
# import random
#
# s = set([])
# for i in range(int(input('N:'))):
#     s.add(random.randint(1, 1000))
# print(s)
# print(sorted(s))
# print(len(s))

import os

# def creat_file(self, filename):
#     """
#     创建日志文件夹和日志文件
#     :return:
#     """
#     path = filename[0:filename.rfind('/')]
#     if not os.path.isdir(path):  # 无文件夹时创建
#         os.makedirs(path)
#
#     if not os.path.isfile(filename):  # 无文件时创建
#         fd = open(filename, mode='w', encoding='utf-8')
#         fd.close()
#
#     else:
#         pass


# def mkdir(path):
#     # 引入模块
#     import os
#     # 去除首位空格
#     path = path.strip()
#     # 去除尾部 \ 符号
#     path = path.rstrip(".")
#     # 判断路径是否存在
#     # 存在     True
#     # 不存在   False
#     isExists = os.path.exists(path)
#     # 判断结果
#     if not isExists:
#         # 如果不存在则创建目录
#         # 创建目录操作函数
#         os.makedirs(path)
#         print(path + ' 创建成功')
#         return True
#     else:
#         # 如果目录存在则不创建，并提示目录已存在
#         print(path + ' 目录已存在')
#         return False


# def create():
#     '''
#     根据本地时间创建新文件，如果已存在则不创建
#     '''
#
#     import time, os
#     t = time.strftime('%Y-%m-%d', time.localtime())  # 将指定格式的当前时间以字符串输出
#     suffix = ".txt"
#     newfile = t + suffix
#     if not os.path.exists(newfile):
#         f = open(newfile, 'w')
#         print(newfile)
#         f.close()
#         print(newfile + " created.")
#     else:
#         print(newfile + " already existed.")

# 全局变量和局部变量；
# import math
# import time
#
#
# def test01():
#     start = time.time()
#     for i in range(1000000):
#         math.sqrt(30)
#     end = time.time()
#     print('耗时-{0}'.format((end - start)))
#
#
# def test02():
#     b = math.sqrt
#     start = time.time()
#     for i in range(1000000):
#         b(30)
#     end = time.time()
#     print('耗时={0}'.format((end - start)))
#
#
# test01()
# test02()

"""
参数的传递：从实参到形参的赋值操作：
python中"一切皆对象"所有的赋值操作都是"引用的赋值"，所以，python中参数的传递都是"引用传递"，不是"值传递"，具体操作时分为俩类：

1.对"可变对象" 进行 "写操作"，直接作用与原对象本身；
2.对"不可变对象" 进行 "写操作"，会产生一个新的"对象空间"，并用新的值填充这块空间。（起到其它语言的"值传递"效果，但不是"值传递"）

可变对象有：
    字典，列表，集合，自定义的对象等
    
不可变对象有：
    数字，字符串，元组，function等
"""

"""
浅拷贝：不拷贝子对象的内容，只拷贝子对象的引用；
深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象；
"""

"""
缺省参数：在形参中，默认有值的参数，称之为缺省参数；
不定长参数：有时可能需要一个函数能处理比当初声明时更多的参数，这些参数叫做不定长参数，声明时不会命名；
"""

"""
装饰器：是一个闭包，把一个函数作为参数，然后返回一个替代版函数，本质上就是一个返回函数的函数，
"""

# 这组实例没有用原函数名
# def func():
#     print('hello word!')
#
#
# def wrapper(f):
#     def inner():
#         print('******')
#         f()
#
#     return inner
#
#
# d = wrapper(func)
# d()

# 这组实力用了原函数名
# def say(name, age):
#     return '%s is a goog man! he is %d' % (name, age)
#
#
# def wrapper(f):
#     def inner(name, age):
#         # 增加功能
#         if age <= 0:
#             age = 0
#
#         return f(name, age)
#
#     return inner
#
#
# say = wrapper(say) # 有了@之后就不写这句话了
# print(say('sunck', -18))

"""
 python 2.4之后 支持使用@将装饰器应用在函数上，只需要再函数定义前加上@装饰器的名称即可
"""

# def wrapper(f):
#     def inner(name, age):
#         # 增加功能
#         if age <= 0:
#             age = 0
#
#         return f(name, age)
#
#     return inner
#
#
# @wrapper
# def say(name, age):
#     return '%s is a goog man! he is %d' % (name, age)
#
#
# print(say('sunck', -18))

"""
通用装饰器
"""

# def wrapper(f):
#     def inner(*args, **kwargs):
#         # 在这增加功能
#         print('no zuo no die')
#         res = f(*args, **kwargs)
#         # 如果要修改原函数的返回值，在这修改
#         return res
#
#     return inner
#
#
# @wrapper
# def func(name, age):
#     return '%s is a goog man! he is %d' % (name, age)
#
#
# print(func('sange', 27))
#
#
# @wrapper
# def func2(fasfa, x=2, f=20):
#     print(fasfa)
#     print('*****' * 10)
#     return x  # ???
#     return f  # ???
#
#
# func2(111)


"""
装饰器传参，(有三层)
url:https://www.bilibili.com/video/av47451456/?p=42
装饰器：P42
"""


def wrapper(count):
    def deco(f):
        def inner(*args, **kwargs):
            for i in range(count):
                f(*args, **kwargs)

        return inner

    return deco


@wrapper(5)
def func():
    print('sunck is a good man')


func()
