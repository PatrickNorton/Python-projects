from itertools import product
rule0 = lambda current,moved,n: (moved.last().number == 13 and not current) or (current.top().suit,moved.last().suit) in product('sc','hd')
rule1 = lambda current,moved,n: moved is pile['deck'];rule2 = lambda current,moved,n: moved.last().suit == 'shdc'[n] and current.top().number+1 == moved.last().number
ruledict = [rule0,rule1,rule2]
class card:
    def __init__(self,number,suit,faceup):
        self.number = number;self.suit = suit;self.faceup = faceup
    def __str__(self):
        return str(self.number if self.number < 10 else 'tjqk'[self.number-10])+'♠♣♡♢'['schd'.index(self.suit)]
    def __eq__(self,other):
        return str(self) == str(other) if isinstance(other,card) else (self.number == other if isinstance(other,int) else self.suit == other)
    def __repr__(self):
        return str(self) if self.faceup else '--'
class decks:
    def __init__(self):
        self.stdpiles = [piles(0) for x in range(7)];self.discard = piles(1);self.donepiles = [piles(2,x) for x in range(4)];self.deck = decktype(self.discard)
        self.dict = {'deck':self.deck,'disc':self.discard,**{'schd'[x]:y for x,y in enumerate(self.donepiles)}};self.depth = max(x.len() for x in self.stdpiles)
    def __getitem__(self,index):
        return self.dict[index] if index in self.dict else self.stdpiles[int(index)-1]
    def __str__(self):
        return f""" s  c  h  d\n{' '.join(str(x[0]) if x else '--' for x in self.donepiles)}\n{self['disc'][0] if self['disc'] else '--'}\n{'  '.join('1234567')}
{chr(10).join(' '.join('  ' if len(self[x]) <= y else repr(self[x][y]) for x in range(7)) for y in range(self.depth))}"""
    def move(self,pilefrom,pileto,nummoved):
        if self[pilefrom].moverule(pilefrom):
            for x in range(nummoved):
                self[pilefrom].append(pileto[nummoved-x])
            return True
        return False
    def __contains__(self,other):
        return other in self.dict or str(other) in '1234567'
class piles:
    def __init__(self,ruleint,n = None):
        self.pile = [];self.rule = ruledict[ruleint];self.n = n
    def __getitem__(self,index):
        return self.pile[index]
    def __bool__(self):
        return bool(self.pile)
    def len(self):
        return len(self.pile)
    def moverule(self,movefrom):
        return self.rule(self,movefrom,self.n)
    def top(self):
        return self[0]
    def append(self,var):
        self.pile.insert(0,var)
class decktype(piles):
    def __init__(self,otherpile):
        self.pile = otherpile;self.rule = False;self.n = 3
    def __getitem__(self,index):
        return self.pile[-1]
    def moverule(self,movefrom):
        return False
    def top(self):
        return self[-1]
    def insert(self,var):
        self.pile.insert(-1,var)
pile = decks()
print('hi' if 'disc' in pile else 'bye')
def start():
    game = True
    while game:
        for x in pile.stdpiles:
            x.top().faceup = True if x else x.top().faceup
        print(pile);asker()
        if all(x.len() == 13 for x in pile.donepiles):
            game = False;print('You win!')
def asker():
    global pile;inputs,pileto = False,''
    while not inputs:
        try:
            pilefrom = input('Which pile do you want to move? ')
            cardcount = int(input('How many cards would you like to move? '))-1 if pilefrom in '1234567' else 0
            pileto = 'disc' if pilefrom == 'deck' else input('Where do you want to move these cards? ')
            if pile[pileto].moverule(pile[pilefrom]):
                pile.move(pile[pilefrom],pile[pileto],cardcount)
        except IndexError:
            if pilefrom == 'quit' or pileto == 'quit':
                quitter()
            print('Invalid input. Please try again.')
def quitter():
    pass
start()     