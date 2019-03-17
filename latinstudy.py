import random
def opendeck():
    a = input('Pick lesson (2 digits) ')
    b = ('fylj_'+a+'.txt')
    f = open(b)
    y = []
    wordlist = f.readlines()
    for x in range(0,len(wordlist)):
        wordlist[x] = wordlist[x].strip()
        if wordlist[x][0] == '#':
            y.append(x)
    for i in sorted(y, reverse = True):
        del wordlist[i]
    wordlist = [line.split(':') for line in wordlist]
    for x in range(0,len(wordlist)):
        wordlist[x] = [line.split(',',1) for line in wordlist[x]]
        for y in range(0, len(wordlist[x])):
            wordlist[x][y] = [line.strip() for line in wordlist[x][y]]
    deckrunthrough(wordlist)
def deckrunthrough(wordlist):
    random.shuffle(wordlist)
    for word in wordlist:
        l = input(word[0][0])
        try:
            l = input(word[0][1])
        except IndexError:
            l = input('\u2014')
        l = input(word[1][0])
    
opendeck()
