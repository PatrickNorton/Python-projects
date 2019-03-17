class matchbox:
    def __init__(self, array):
        from itertools import chain
        self.positions = {
            x: (0 if not isinstance(y, nopiece) else y) for x, y in enumerate(array)}
        self.matchlist = list(
            chain(*[[x for z in range(y)] for x, y in enumerate(self.positions)]))

    def __getitem__(self, index): return self.positions[index]

    def __setitem__(self, index, var): self[index] = var

    def __iter__(self): yield from self.positions

    def __str__(self): return ' '.join(self)

    def nextmove(self):
        from random import choice
        return choice(self.matchlist)

    def change(self, space, ldw):
        self[space] += [-1, 1, 3][ldw+1]


class bot:
    def __init__(self, turnno):
        self.matchboxes = {}
        from itertools import chain
        from sympy.utilities.iterables import multiset_permutations as permutations
        if not turnno:
            for x in range(5):
                boardpieces = list(
                    chain([[piece('X'), piece('O')] for k in range(x)]))
                for _ in range(9-2*x):
                    boardpieces.append(nopiece())
                for y in permutations(boardpieces):
                    print(y)
                    self[y] = matchbox(y)
        else:
            for x in range(4):
                boardpieces = list(
                    chain([[piece('X'), piece('O')] for k in range(x)]))
                boardpieces.append(piece('X'))
                for _ in range(9-2*x):
                    boardpieces.append(nopiece())
                for y in permutations(boardpieces):
                    print('hi')
                    self[y] = matchbox(y)

    def __getattr__(self, array):
        print(type(array))
        return self.matchboxes[list(array)]

    def __setattr__(self, array, equals):
        self[array] == equals

    def choose(self, board):
        return self[list(board)].nextmove()


class piece:
    def __init__(self, color):
        self.color = color

    def __str__(self): return self.color

    def __eq__(self, other): return self.color == other.color


class nopiece(piece):
    def __init__(self):
        super().__init__('-')

    def __eq__(self, other): return isinstance(other, nopiece)


class board:
    def __init__(self):
        self.values = [nopiece() for x in range(9)]

    def __str__(self):
        return '\n'.join(' '.join(self[3*x:3*x+3]) for x in range(3))

    def __getitem__(self, index): return self.values[index]

    def __iter__(self): yield from self.values

    def __setitem__(self, index, value): self[index] = value


botlist = [bot(0), bot(1)]
theboard = board()
outcome = 0
moveslist = []


def gameplay():
    global turn, moveslist
    game = True
    while game:
        for turn in (0, 1):
            currentbot = botlist[turn]
            movedvar = currentbot.choose(board)
            theboard[movedvar] = piece('XO'[turn])
            moveslist.append([turn, list(board), movedvar])
            print(board)
            if endcheck():
                outcome = [1, -1][turn]
            if nopiece() not in theboard or outcome:
                game = False
                outcome = 0
                break


def endcheck():
    win = False
    for x in range(4):
        if theboard[4] == theboard[x] == theboard[8-x] == turn:
            win = True
            break
    else:
        for x in range(4):
            wincom = [[0, 1, 2], [0, 3, 6], [2, 5, 8], [6, 7, 8]][x]
            if all(theboard[x] == theboard[wincom[0]] == turn for x in wincom):
                win = True
                break
    return win


def aifixer():
    for var in moveslist:
        botlist[var[0]][var[1]].change(var[2], outcome*[1, -1][var[0]])
