import random
def gameplay ():
    deck = ['AS','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS','AH','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH','AC','2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC','AD','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD']
    random.shuffle(deck);gamestart = True;trash = []
    pile0,pile1,pile2,pile3,pile4,pile5,pile6 = [],[],[],[],[],[],[]
    see0,see1,see2,see3,see4,see5,see6 = 1,1,1,1,1,1,1
    numup = [see0,see1,see2,see3,see4,see5,see6]
    piles = [pile0,pile1,pile2,pile3,pile4,pile5,pile6]
    pilespade,pileheart,pileclub,pilediamond = [],[],[],[]
    donepiles = [pilespade,pileheart,pileclub,pilediamond]
    print(type(piles[0]))
    for a in range(7):
        for b in range(a+1):
            card = deck[0]
            piles[a].append(card)
            del deck[0]
    while gamestart == True:
        print('Main piles')
        for a in range(7):
            if len(piles[a]) > 0:
                piletoprint = []
                for c in range(numup[a]):
                    piletoprint.append(piles[a][0])
                for b in range(numup[a],len(piles[a])):
                    piletoprint.append('-')
                print(' ,'.join(piletoprint))
            else:
                print('empty')
        print('Done piles')
        for a in range(4):
            if len(donepiles[a]) > 0:
                print(donepiles[a][0])
            else:
                print('empty')
        print('Trash')
        if len(trash) == 0:
            print('empty')
        else:
            print(trash[0])
        pilefrom = input('Choose the pile to move the card from (number 0-6, trash, or deck) ')
        nummoved = '0'
        if str.isdigit(pilefrom):
            nummoved = input('Choose the number of cards from that pile you wish to move ')
            pilefrom = int(pilefrom)
        if pilefrom == 'trash':
            movedcard = trash[0]
        if pilefrom == 'deck':
            movedcard = deck[0]
            del deck[0];trash.insert(0,movedcard);valid = True
        if str.isdigit(nummoved):
            nummoved = int(nummoved)
        try:
            if len(piles[pilefrom]) != 0:
                z = nummoved - 1
                movedcard = piles[pilefrom][z];print('Your bottom card is '+movedcard)
                cardlist = piles[pilefrom][:z]
        except TypeError:
            if pilefrom != 'deck' and pilefrom != 'trash':
                print('Invalid input. Please try again')
        try:
            if type(nummoved) == str or nummoved > len(piles[pilefrom]):
                print('Invalid number of cards moved. Please try again.')
        except TypeError:
            print('If not deck or trash, error occurred')
        print(type(pilefrom))
        if isinstance(pilefrom,int) or pilefrom == 'trash':
            pileto = input('Choose the pile to move the card to (number 0-6 or done) ')
        else:
            pileto = 'a'
        if str.isdigit(pileto):
            pileto = int(pileto)
        valid = False
        if pilefrom == 'trash' and isinstance(pileto,int):
            del trash[0];piles[pileto].insert(0,movedcard)
        if pilefrom == 'trash' and isinstance(pileto,str):
            del trash[0];donepiles[pileto].insert(0,movedcard)#FIX THIS. THIS IS TERRIBLE ON EVERY LEVEL
        try:
            if len(piles[pilefrom]) == 0 and valid == False:
                print('You are trying to move a card from an empty pile. Please try again.'); 
            elif pileto == 'done' and valid == False:
                if 'S' in movedcard:
                    pileto = 0
                elif 'H' in movedcard:
                    pileto = 1
                elif 'C' in movedcard:
                    pileto = 2
                elif 'D' in movedcard:
                    pileto = 3
                number = movedcard[0]
                if number in ['T','J','Q','K']:
                    q = ['T','J','Q','K'].index(number)
                    j = ['9','T','J','Q']
                    if j[q] in donepiles[pileto][0]:
                        donepiles[pileto].insert(0,movedcard);valid = True
                elif number == 'A' and len(donepiles[pileto]) == 0:
                       donepiles[pileto].append(movedcard);valid = True
                elif str.isdigit(number):
                       if str.isdigit(piles[pileto][0][0]) == False:
                           print('Illegal move. Please try again.')
                       elif (int(number)-1) == int(piles[pileto][0][0]):
                           donepiles[pileto].insert(0,movedcard);valid = True
            elif len(piles[pileto]) == 0 and movedcard[0] != 'K' and valid == False:
                print ('Invalid move. Please try again.')
            elif str.isdigit(pileto):
                if (movedcard[1] in ['S','C']) and (piles[pileto][0][1] in ['H','D']) or (movedcard[1] in ['H','D']) and (piles[pileto][0][1] in ['S','C']):
                    number = movedcard[0]
                    if number in ['T','J','Q','K']:
                       q = ['9','T','J','Q'].index(number)
                       j = ['T','J','Q','K']
                       if j[q] in piles[pileto][0]:
                           piles[pileto].insert(0,movedcard);valid = True
                elif number == 'K' and len(piles[pileto]) == 0:
                    piles[pileto].append(cardlist);valid == True
                elif number == 'A' and piles[pileto][0][0] == '2':
                    piles[pileto].insert(0,cardlist);valid = True
                elif str.isdigit(number):
                    if str.isdigit(piles[pileto][0][0]) == False:
                       print('Illegal move. Please try again.')
                    elif (int(number)+1) == int(piles[pileto][0][0]):
                       piles[pileto].insert(0,cardlist);valid = True
                elif (movedcard[1] == 'S' or movedcard[1] == 'C') and (piles[pileto][0][1] == 'H' or piles[pileto][0][1] == 'D'):
                    piles[pileto].insert(0,cardlist)
                    valid = True
            else:
                print('Invalid input. Please try again.')
        except TypeError:
            print('umm...')
        if pilefrom == 'deck' and valid == True:
            del deck[0]
        elif valid == True:
            del piles[pilefrom][0]
def deckcheck (deck,trash):
    trash.insert(0,deck[0]);del deck[0]
    return (deck, trash)
def piletcheck(piles,pileto,pilefrom,nummoved,movedcard,cardlist):
    valid = False
    piles,pilefrom,nummoved,movedcard,cardlist,validb = pilefcheck(piles,pilefrom,nummoved,movedcard,cardlist,pileto)
    if len(piles[pileto]) == 0 and movedcard[0] == 'K':
        piles[pileto].append(movedcard);valida = True
    elif len(piles[pileto]) == 0:
        print('Invalid move. Please try again.')
    elif movedcard[0] in ['9','T','J','Q']:
        q = ['9','T','J','Q'].index(movedcard[0])
        j = ['T','J','Q','K']
        if j[q] in piles[pileto][0]:
            piles[pileto].insert(0,movedcard);valida = True
    elif str.isdigit(movedcard[0]):
        if str.isdigit(piles[pileto][0][0]) == False:
            print('Invalid move. Please try again.')
        elif int(movedcard[0])+1 == int(piles[pileto][0][0]):
            piles[pileto].insert(0,cardlist);valid = True   #MAKE CARDLIST VALID
    return piles,pileto,nummoved,movedcard,cardlist,valid
def piledcheck (donepiles,movedcard):
    pileto = ['S','H','C','D'].index(movedcard[1]);number = movedcard[0]
    if number in ['T','J','Q','K']:
        q = ['T','J','Q','K'].index(number)
        j = ['9','T','J','Q']
        if j[q] in donepiles[pileto][0]:
            donepiles[pileto].insert(0,movedcard);valid = True
        elif number == 'A' and len(donepiles[pileto]) == 0:
               donepiles[pileto].append(movedcard);valid = True
        elif str.isdigit(number):
            if str.isdigit(piles[pileto][0][0]) == False:
                print('Illegal move. Please try again.')
            elif (int(number)-1) == int(piles[pileto][0][0]):
                donepiles[pileto].insert(0,movedcard);valid = True
    return donepiles,movedcard,valid
def pilefcheck(piles,pilefrom,nummoved,movedcard,cardlist):
    if len(piles[pilefrom]) >= nummoved:
        piles,pileto,movedcard,cardlist,valid = piletcheck(piles,pileto,nummoved,movedcard,cardlist)
    else:
        print('Invalid move. Please try again.')
    if valid:
        piles[pileto].insert(0,cardlist);del piles[pilefrom][:nummoved]
def pilecheck (piles,pilefrom,pileto,nummoved,donepiles,trash,movedcard,cardlist):
    if type(pileto) == int:
        piletcheck(piles,pileto,nummoved,movedcard)
    elif pileto == 'done':
        piledcheck(donepiles,movedcard)
    if type(pilefrom) == int:
        pilefcheck(piles,pilefrom,nummoved,movedcard,cardlist)
    elif pilefrom == 'trash':
        piletcheck(trash,movedcard)
    return (piles,pilefrom,pileto,nummoved,donepiles,trash,movedcard,cardlist)
gameplay()
