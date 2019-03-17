numin = input('Choose a number to start ')
numin = int(numin)
strintdict = {'0': 'zero', '1': 'one'}
while numin not in (18, 13):
    numstr = bin(numin)
    numstr = numstr[2:]
    magicstr = ''
    for x in numstr:
        magicstr += strintdict[x]
    lenstr = len(magicstr)
    print(lenstr)
    numin = lenstr