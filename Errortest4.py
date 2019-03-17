def opening():
    a = True;global guesses
    print('This is hangman. Please choose a mode.\nBeginner (20 wrong guesses)(b)\nEasy (10)(e)\nMedium (7)(m)\nHard (5)(h)');c = ['h','m','e',a,a,a,'b']
    while a == True:
        b = input ('What is your choice? ')
        if b == 'help':
            helpdesk()
        elif b in c:
            guesses = int(((c.index(b))*2.5+5));print('You have '+str(guesses)+' incorrect guesses remaining.')
        else:
            print('You have not entered a valid gamemode. Please retry.')
def hangman(word,guesses):
    correct = 0;joiner = '';joiner2 = ',';rightword = [];wrongword = []; wordguessed = []; h = open('hangmanletters.txt'); validletters = h.read().split(',')
    for a in range (0,len(word)-1):
        wordguessed.append ('-')
    while correct < (len(word)-1) and guesses > 0:
        print('Your word is '+str(len(word)-1)+' letters long');letter = input('Please guess a letter ')
        if letter == 'quit':
            z = input('Are you sure you want to quit? Retype "quit" to quit. ')
            if z == 'quit':
                correct = len(word);print ('You have quit the game.')
        elif letter == 'help':
            helpdesk()
        elif letter in word and letter not in rightword and letter != '':
            print ('Correct! '+letter+' is in the word '+str(word.count(letter))+' time(s).')
            correct += word.count (letter);places = word.index (letter); places = [x for x, char in enumerate(word) if char == letter];rightword.append(letter)
            for d in range (0,(len(places))):
                wordguessed [places[d]] = (letter)
        elif letter in word and letter in rightword or letter in wrongword and letter != '':
            print ('You have already guessed this letter.')
        elif letter not in validletters:
            print ('This is not a valid letter! Please retry.')
        else:
            print ('This letter is not in this word!');wrongword.append (letter);guesses -= 1;print ('You have '+str(guesses)+' incorrect guesses remaining!')
        if correct <= (len(word))-1:
            print ('Your incorrect letters are: '+joiner2.join(wrongword));print ('Your word so far is: '+joiner.join(wordguessed))
    if correct == (len (word))-1:
        print ('You won!')
    elif guesses == 0:
        print ('You lost! The word was '+word)
def helpdesk ():
    with open('hangmanhelp.txt') as g:
        helpfile = g.read();print (helpfile)
def start ():
    import random; global guesses; f = open('hangmanwords.txt');wordlist = f.readlines();x = random.randint (0,len(wordlist)-1);word = wordlist[x];wordlist = [];opening();hangman(word,guesses);q = input ('Would you like to play again? (y/n) ')
    if q == 'y':
        start()
    else:
        print ('Thank you for playing!')
start ()
