class NamedList:
    def __init__(self, title, names, values):
        assert(len(names) == len(values))
        self.title = title
        self.names = names
        self.values = values

    def get(self, name):
        return self.values[self.names.index(name)]

    def add(self, name, value):
        self.names.append(name)
        self.values.append(value)
        return 1

    def to_string(self):
        return self.title
