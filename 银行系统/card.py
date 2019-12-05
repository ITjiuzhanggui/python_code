import random

class Card():
    def __init__(self, id, balance):
        self._id = id
        self._balance = balance
        self.status = False

    @property

