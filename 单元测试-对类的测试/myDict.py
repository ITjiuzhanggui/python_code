class MyDict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        try:
            return self[item]

        except KeyError as e:
            raise AttributeError(r"dict not have the key")



