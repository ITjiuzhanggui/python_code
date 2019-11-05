from Card.singleton import singletonFuncDeco


@singletonFuncDeco
class Bank(object):
    def __init__(self):
        self.usersDict = {}
