class User(object):
    def __init__(self, name, cardID, phone):
        self.name = name
        self.cardId = cardID
        self.phone = phone
        self.cardsDict = {}
