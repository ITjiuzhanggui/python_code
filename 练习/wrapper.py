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


# """
# 装饰器传参，(有三层)
# url:https://www.bilibili.com/video/av47451456/?p=42
# 装饰器：P42
# """
#
#
# def wrapper(count):
#     def deco(f):
#         def inner(*args, **kwargs):
#             for i in range(count):
#                 f(*args, **kwargs)
#
#         return inner
#
#     return deco
#
#
# @wrapper(5)
# def func():
#     print('sunck is a good man')
#
#
# func()


# """
# 装饰器：重试(retry)
# """
#
#
# def retry(count=3, wait=0, exceptions=(Exception,)):
#     import time
#
#     def wrapper(f):
#         def inner(*args, **kwargs):
#             for i in range(count):
#                 try:
#                     res = f(*args, **kwargs)
#
#                 except exceptions as e:
#                     time.sleep(wait)
#                     continue
#                 else:
#                     return res
#
#         return inner
#
#     return wrapper

# 函数实现生成器
"""
如果说推导的算法比较复杂，用列表生成式或for循环无法实现的时候可以选择使用函数生成器；
(yield)

如果想让一个函数变为生成器函数，只需将函数的return改为yield.

变成generator函数，在每次调用next()的时候，遇到yield语句返回，如果再次执行next(),
会从上次返回的yield语句处继续执行
"""


# 生成器(斐波那契数列)
def fib(count):
    index = 0
    x, y = 0, 1
    while index < count:
        yield y
        x, y = y, x + y
        index += 1
    return 'sunck is a good man'


g = fib(6)
# for循环遍历generator时，拿不到generator的return的返回值；
# 如果想拿返回值，必须捕获StopIteration错误,返回值包含在错误对象的value属性
# 中
# for i in g:
#     print(i)
while 1:
    try:
        ret = next(g)
        print(ret)
    except StopIteration as e:
        print('返回值：', e.value)
        break
