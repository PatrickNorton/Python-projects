class card:
    def __init__(self, number, suit, faceup):
        self.number = number
        self.suit = suit
        self.faceup = faceup

    def __str__(self):
        return str(self.number if self.number < 10 else 'tjqk'[self.number-10])+'♠♣♡♢'['schd'.index(self.suit)]


import random
import itertools
deck = [card(*x, False) for x in itertools.product(range(1, 14), 'schd')]
random.shuffle(deck)
discard = []
piles = [[deck[x*(x-1)//2+y] for y in range(x)] for x in range(1, 8)]
del deck[:28]
endpiles = [[] for x in range(4)]


def start():
    game = True
    while game:
        for x in range(7):
            if piles[x]:
                piles[x][0].faceup = True
        print(
            f" {'  '.join('schd')}\n{' '.join(str(endpiles[x][0]) if endpiles[x] else '--' for x in range(4))}")
        print(
            f"discard {discard[0] if discard else '--'}{' DECK EMPTY' if not deck else ''}\n {'  '.join('1234567')}")
        print('\n'.join(' '.join('  ' if len(piles[x]) <= y else (str(
            piles[x][y]) if piles[x][y].faceup else '--') for x in range(7)) for y in range(max(len(x) for x in piles))))
        asker()
        if all(len(x) == 13 for x in endpiles):
            game = False
            print('You win!')


def asker():
    global deck, piles, endpiles, discard
    inputs, pileto = False, ''
    from copy import deepcopy
    while not inputs:
        try:
            pilefrom = input('Which pile do you want to move? ')
            pilefrom = pilefrom if pilefrom in [
                'disc', 'deck'] else int(pilefrom)-1
            cardcount = int(input('How many cards would you like to move? ')
                            )-1 if not isinstance(pilefrom, str) else 0
            if pilefrom == 'deck':
                discard.insert(0, deck[0])
                del deck[0]
                inputs = True
                if not deck:
                    discard.reverse()
                    deck = deepcopy(discard)
                    discard = []
                    discard.append(deck.pop())
            elif pilefrom == 'disc' or ((pilefrom in range(7) and cardcount < len(piles[pilefrom])) and piles[pilefrom][cardcount].faceup):
                pileto = input('Where would you like to move this? ')
                pileto = pileto if pileto in 'schd' or pileto in [
                    'quit', 'disc'] else int(pileto)-1
                inputs = movecheck(pilefrom, cardcount, pileto)
            elif pilefrom == 'quit' and quitter():
                break
            if pileto == 'quit' and quitter():
                break
            if not inputs:
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please try again.')


def movecheck(pilefrom, cardcount, pileto):
    cardcount = 0 if str(pileto) in 'schd' else cardcount
    bottomcard = piles[pilefrom][cardcount] if isinstance(
        pilefrom, int) else discard[0]
    if pileto == 'quit':
        return True
    elif str(pileto) in 'schd' and (bottomcard.suit == pileto and (bottomcard.number == 1 or endpiles['schd'.index(pileto)][0].number == bottomcard.number-1)):
        endpiles['schd'.index(pileto)].insert(0, bottomcard)
        if isinstance(pilefrom, int):
            del piles[pilefrom][0]
            return True
        else:
            del discard[0]
            return True
    elif (bottomcard.number == 13 and not piles[pileto]) or (piles[pileto][0].number == bottomcard.number+1 and (piles[pileto][0].suit, bottomcard.suit) in itertools.product('sc', 'hd')):
        if pilefrom == 'disc':
            if str(pileto) in 'schd':
                endpiles['schd'.index(pileto)].insert(0, discard[0])
                del discard[0]
                return True
            else:
                piles[pileto].insert(0, discard[0])
                del discard[0]
                return True
        else:
            for x in range(cardcount+1):
                piles[pileto].insert(x, piles[pilefrom][x])
            del piles[pilefrom][:cardcount+1]
            return True
    return False


def quitter():
    return input('Would you like to quit? Type quit to quit').startswith('q')


start()
