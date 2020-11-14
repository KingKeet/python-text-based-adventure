class NamedList:
    def __init__(self, names, values):
        assert(len(names) == len(values))
        self.names = names
        self.values = values

    def get(self, name):
        return self.values[self.names.index(name)]
