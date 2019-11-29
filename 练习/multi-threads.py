# ！/usr/bin/env python3
"""
demo1:
使用单线程执行循环
"""
# from time import sleep, ctime
#
#
# def loop0():
#     print("start loop 0 at:", ctime)
#     sleep(4)
#     print("loop 0 done at:", ctime)
#
#
# def loop1():
#     print("start loop1 at:", ctime)
#     sleep(2)
#     print("loop 1 done at:", ctime)
#
#
# def main():
#     print("starting at:", ctime)
#     loop0()
#     loop1()
#     print("all DONE at:", ctime)
#
#
# if __name__ == '__main__':
#     main()

"""
使用  thread模块
提供简单的多线程机制
"""

# import threading
# from time import sleep, ctime
#
# loops = [4, 2]
#
# def loop(nloop, nsec):
#     print("start loop:%S, at:%s" % (nloop, ctime()))
#     sleep(nsec)
#     print("loop:%s, done at:%s" % (nloop, ctime()))
#
#
# def main():
#     print("starting at:%s" % ctime())
#     threads = []
#     nloops = range(len(loops))
#
#     for i in nloops:
#
#
# if __name__ == '__main__':
#     main()

"""
使用可调用的类
"""
# import threading
# from time import sleep, ctime
#
# loops = [4, 2]
#
#
# class ThreadFunc(object):
#
#     def __init__(self, func, args, name=''):
#         self.name = name
#         self.func = func
#         self.args = args
#
#     def __call__(self):
#         self.func(*self.args)
#
#
# def loop(nloop, nsec):
#     print("start loop:%s, nloop at:" % (nloop, ctime()))
#     sleep(nsec)
#     print("loop:%S, done at:%s" % (nloop, ctime()))
#
#
# def main():
#     print("starting at:%s" % ctime())
#     threads = []
#     nloops = range(len(loops))
#
#     for i in nloops:  # create all threads
#         t = threading.Thread(
#             target=ThreadFunc(loop, (i, loop[i]),
#             loop.__name__))
#
#         threads.append(t)
#
#     for i in nloops:  # start all threads
#         threads[i].start()
#
#     for i in nloops:  # wait for completion
#         threads[i].join()
#     print("all DONE at:%s" % ctime())
#
#
# if __name__ == '__main__':
#     main()

    