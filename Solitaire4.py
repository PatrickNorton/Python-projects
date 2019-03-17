from itertools import product


class card:
    def __init__(self, suit, number):
        self.SUIT = suit
        self.NUMBER = number
        self.faceup = faceup

    def __str__(self):
        if self.number < 10:
            toreturn = str(self.NUMBER)
        else:
            toreturn = 'tjqk'[self.NUMBER-10]
        return toreturn+self.SUIT

    def __eq__(self, other):
        if isinstance(other, card):
            return str(self) == str(other)
        elif isinstance(other, int):
            return self.NUMBER == other
        elif isinstance(other, str):
            return self.SUIT == other
        else:
            return False

    def __repr__(self):
        return str(self) if self.faceup else '--'


class decks:
    def __init__(self):
        self.STDPILES = [piles() for x in range(7)]
        self.DONEPILES = [donepile(x) for x in range(4)]
        self.DECK = deck()
        self.DICT = {
            'deck': self.DECK,
            'disc': self.DECK[-1],
            **{'♠♣♡♢'[x]: y for x, y in enumerate(self.DONEPILES)}
        }
        self.DEPTH = max(len(x) for x in self.STDPILES)

    def __getitem__(self, index):
        if index in self.DICT:
            return self.DICT[index]
        else:
            return self.STDPILES[int(index)]

    def __str__(self):
        tostr = ""
        tostr += 's  c  h  d\n'
        for x in self.DONEPILES:
            tostr.append(str(x))
        tostr += f'\nDiscard: {self.DISCARD}\n'
        tostr += '  '.join('0123456')
        for x in range(self.DEPTH):
            line = ''
            for pile in self.STDPILES:
                try:
                    line += repr(pile[x])
                except IndexError:
                    line += '  '
                line += ' '
            line += '\n'
            tostr += line
        return tostr

    def __contains__(self, other):
        return other in self.dict or other in range(7)

    def move(self, pilefrom, pileto, nummoved):
        if self[pilefrom].moveoff(nummoved):
            movedpile = self[pilefrom].remove(nummoved)
            if self[pileto].moveon(movedpile):
                self[pileto].add(movedpile)
                return True
        return False


class basepile:
    def __init__(self):
        self.PILE = []

    def __getitem__(self, index): return self.PILE[index]

    def __len__(self): return len(self.PILE)

    def __bool__(self): return bool(self.PILE)

    def moveoff(self, other): return False

    def moveon(self, other): return False


class piles(basepile):
    def moveoff(self, num): return self[num].faceup()

    def moveon(self, pile):
        bottomcard = pile[-1]
        if not self:
            return bottomcard.NUMBER == 13
        return (self[0].suit, bottomcard.suit) in product('sc, hd')

    def remove(self, num):
        var = self[:num]
        del self.PILE[:num]
        return var

    def add(self, pile):
        pile.extend(self.PILE)
        self.PILE = pile


class deck(basepile):
    def flip(self):
        self.PILE += [self.PILE.pop()]

    def 
