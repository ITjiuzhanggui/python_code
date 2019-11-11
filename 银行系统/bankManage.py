"""
管理员类
名称：Admin
属性：name, passwd
方法：显示管理员欢迎界面，显示功能界面

银行卡
名称：Card
属性：id, balance
方法：生成卡号

取款机
名称：ATM
属性：
方法：开户，查询，取款，转账，存款，改密，锁定，解锁，补卡，销户

用户
名称：user
属性：姓名，身份证，电话号，银行卡
方法：
"""
import time, os
from .admin import Admin
import functions

# users = {}
def run():
