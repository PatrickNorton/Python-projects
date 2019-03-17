import random
def gameplay():
    numlist = ['1','2','3','4','5','6','7','8','9']
    oplist = ['+','-','*','/']
    solution = ['','','','','']
    a = random.randint(0,8)
    solution[0] = numlist.pop(a)
    game = True
    for x in range(1,3):
        a = random.randint(0,(len(oplist)-1))
        print('op',a,len(oplist))
        if oplist[a] == '/':
            a = random.randint(0,(len(numlist)-1))
            print('num',a,len(numlist))
            solution[2*x] = numlist.pop(a)
            if int(solution[2*x-2]) % int(solution[2*x]) != 0:
                a = random.randint(0,(len(oplist)-2))
            else:
                a = len(oplist)-1
            solution[2*x-1] = oplist.pop(a)
        else:
            solution[(2*x-1)] = oplist.pop(a)
            a = random.randint(0,(len(numlist)-1))
            print('num',a, len(numlist))
            solution[(2*x)] = numlist.pop(a)
    print(solution)
    number = ''.join(solution)
    number = int(eval(number))
    print(number)
    while game:
        guess = input('Input ')
        guess = guess.replace(' ','')
        if len(guess) == 5:
            list(guess)
            print(guess)
            outa = []
            outb = []
            for x in range(0,5):
                if guess[x] == solution[x]:
                    outa.append('\u25cf')
            for x in range(0,5):
                print(guess.count(guess[x]))
                if guess[x] in solution and guess.count(guess[x]) == 1:
                    outb.append('\u25cb')
                elif guess[x] in solution:
                    a = True
                    for y in range(0,5):
                        if guess[y] == solution[y]:
                            a = False
                    if a:
                        outb.append('\u25cb')
            print(' '.join(outa), ' '.join(outb))
            if len(outa) == 5:
                game = False
                print('You win!')
        else:
            print ('Error')
gameplay()
