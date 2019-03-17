class machine:
    def __init__(self):
        self.layers = [layer(x, y) for x, y in enumerate([42, 10, 10, 10, 7])]

    def __getitem__(self, index): return self.layers[index]

    def outputs(self): return list(self.layers[-1])


class layer:
    def __init__(self, layerno, nodeno):
        self.nodelist = [node(layerno) if layerno else node(
            layerno, 0) for x in range(nodeno)]

    def __getitem__(self, index):
        return self.nodelist[index]


class node:
    def __init__(self, layerno, value=None):
        self.links = [(0, x)
                      for x in machine[layerno-1]] if value is None else None
        self.value = sum(x[0]*int(x[1])
                         for x in self.links) if self.links else value

    def __int__(self): return self.value

    def __getitem__(self, index):
        return self.links[index] if self.links else None


class board:
    def __init__(self):
        self.pieces = {(x, y): nopiece() for x in range(7) for y in range(6)}

    def __getitem__(self, index): return self.pieces[index[0], index[1]]

    def move(self, index):
        self[index, min(x for x in range(6) if self[index, x])]


class piece:
    def __init__(self, number):
        self.number = number
        self.color = 'RB'[number]

    def __bool__(self):
        return not isinstance(self, nopiece)


class nopiece(piece):
    def __init__(self):
        self.number = 0
        self.color = '-'


machine = machine()
