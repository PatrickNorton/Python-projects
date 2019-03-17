class card:
    def __init__(self, number, suit):
        self.number = number+1
        self.suit = suit

    def __str__(self):
        return str(self.number if self.number < 10 else 'tjqk'[self.number-10])+'♠♣♡♢'['schd'.index(self.suit)]

    def __eq__(self, other):
        return self.number == other.number

    def __gt__(self, other):
        return self.number > other.number


deck = [card(x, y) for x in range(13) for y in 'schd']
from random import shuffle
shuffle(deck)
x = 0
counter = [26, 26]
decka = deck[:26]
deckb = deck[26:]


def compare():
    global decka, deckb, x, counter
    print(decka[0], deckb[0], len(decka), len(deckb))
    magicpile.extend((decka.pop(0), deckb.pop(0)))
    x += 1
    print(x)
    counter = [x-1 if x > 1 else 0 for x in counter]
    if not all(counter):
        shuffle([decka, deckb][counter.index(0)])
        counter[counter.index(0)] = len([decka, deckb][counter.index(0)])
    if magicpile[-2] > magicpile[-1]:
        decka.extend(magicpile)
    elif magicpile[-1] > magicpile[-2]:
        deckb.extend(magicpile)
    elif magicpile[-2] == magicpile[-1]:
        magicpile.extend((*decka[:3], *deckb[:3]))
        del decka[:3]
        del deckb[:3]
        counter = [x-3 if x > 3 else 1 for x in counter]
        if not (decka and deckb):
            decka.append(magicpile[-2])
            deckb.append(magicpile[-1])
            del magicpile[-2:]
        compare()
    else:
        print('Something aint right')


while decka and deckb:
    magicpile = []
    compare()
