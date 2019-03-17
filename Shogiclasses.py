import os
import sys
cpath = sys.path[0]


class piece:
    """The class for each chess piece. Contains type, color, and list of possible moves"""

    def __init__(self, ptype, color):
        self.PTYPE = ptype
        self.COLOR = color
        self.MOVES = piecedict[ptype]
        self.prom = False if self.PTYPE.upper() in piecedict.keys() else None

    def __str__(self):
        return self.PTYPE+self.COLOR

    def __eq__(self, other):
        return (self.PTYPE, self.COLOR) == (other.PTYPE, other.COLOR)

    def __bool__(self):
        return not isinstance(self, nopiece)

    def promote(self):
        self.PTYPE = self.PTYPE.upper()
        self.MOVES = piecedict[self.PTYPE]
        self.prom = True


class nopiece(piece):
    """The instance of a piece for an empty square"""

    def __init__(self):
        super().__init__('-', '-')


class coord:
    """The class of xy coordinates"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tup = (x, y)

    def __eq__(self, other):
        return self.tup == other.tup

    def __iter__(self):
        yield from self.tup

    def __add__(self, other):
        return coord(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return coord(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return coord(self.x*other.x, self.y*other.y)


class board:
    """The class of the shogi board"""

    def __init__(self):
        with open(os.path.join(cpath, 'shogiboard.txt')) as boardtxt:
            shogiboard = [x for x in boardtxt.readlines()]
            shogiboard = [x.strip().split() for x in shogiboard]
        self.PIECES = {}
        for (x, y) in self.it():
            if shogiboard[y][x]:
                piecel = list(shogiboard[y][x])
                self.PIECES[(x, y)] = piece(*piecel)

    def __str__(self):
        return f"  {'  '.join(b)}\n{chr(10).join(f'{a[v]} {chr(32).join(x)}' for v,x in enumerate(self))}"

    def __iter__(self):
        yield from [[str(self[x, y]) for x in range(9)] for y in range(9)]

    def __getitem__(self, coords):
        return self.PIECES[tuple(coords)] if tuple(coords) in self.PIECES.keys() else nopiece()

    def it(self):
        yield from [(x, y) for x in range(9) for y in range(9)]

    def move(self, current, new):
        if self[new].COLOR != '-':
            self.capture(new)
        self.PIECES[tuple(new)] = self.PIECES.pop(tuple(current))

    def capture(self, new):
        global captlist
        piece = self[new]
        piece.PTYPE = piece.PTYPE.lower()
        piece.MOVES = piecedict[piece.PTYPE]
        captlist['wb'.index(turn)].append(self[new])
        self[new].COLOR = turn
        piece.prom = False if piece.prom else piece.prom
        del self.PIECES[new]


class turntype:
    """The class of the turn. Used for transforming 'wb' to numbers and back again"""

    def __init__(self, turnnum):
        self.int = turnnum
        self.name = 'wb'[self.int]
        self.other = 'bw'[self.int]

    def __str__(self):
        return self.name

    def __int__(self):
        return self.int


def promoter(theboard, new):
    """Tests conditions for piece promotion"""
    return new.y in [[0, 1, 2], [8, 7, 6]][int(turn)] and theboard[new].prom is not None and not theboard[new].prom


with open(os.path.join(cpath, 'shogimoves.txt')) as movestxt:
    movestxt = movestxt.readlines()
    for x in movestxt:
        x = x.split(', ')
        x = [y.strip() for y in x]
    piecedict = {x[0]: x[1] for x in movestxt}
captlist = [[], []]
board = board()
a, b = 'abcdefghi', '987654321'
turn = turntype(0)
