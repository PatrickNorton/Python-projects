def opening(word):
    guesses = 0
    print('This is hangman. Please choose a mode.\nBeginner (20 wrong guesses)\nEasy (10)\nMedium (7)\nHard (5)\nType help for help')
    c = ['h', 'm', 'e', 0, 0, 0, 'b']
    while not guesses:
        b = input('What is your choice? ')
        if b == 'help':
            helpdesk()
        elif any(b.lower().startswith(str(x)) for x in c):
            guesses = int(((c.index(b.lower()[0]))*2.5+5))
            print(f"You have {guesses} incorrect guesses remaining.")
        else:
            print('You have not entered a valid gamemode. Please retry.')
    hangman(word, guesses, b)


def hangman(word, guesses, b):
    import string
    rightword, wrongword = [], []
    print(f"Your word is {len(word)} letters long")
    wordguessed = ['-' for x in word]
    while '-' in wordguessed and guesses:
        letter = input('Please guess a letter ').lower()
        if letter == 'quit' and input('Are you sure you want to quit? Retype "quit" to quit. ') == 'quit':
            print('You have quit the game.')
            break
        elif letter == 'help':
            helpdesk()
        elif letter == 'word':
            if input('Guess the word here: ') == word:
                wordguessed = list(word)
            else:
                print('Incorrect!')
                guesses = 0
        elif letter not in string.ascii_lowercase or len(letter) != 1:
            print('This is not a valid letter! Please retry.')
        elif letter in word and letter not in rightword:
            print(
                f"Correct! {letter} is in the word {word.count(letter)} {'times' if word.count(letter) > 1 else 'time'}.")
            rightword.append(letter)
            wordguessed = [x if x in rightword else '-' for x in word]
        elif letter in rightword or letter in wrongword:
            print('You have already guessed this letter.')
        else:
            wrongword.append(letter)
            guesses -= 1
            print(
                f"This letter is not in this word!\nYou have {guesses} incorrect guesses remaining!")
        if not b.lower().startswith('b'):
            print(open('hangmanart.txt').read().split(',')[10-guesses])
        if '-' in wordguessed:
            print(
                f"Your incorrect letters are: {','.join(wrongword)}\nYour word so far is: {''.join(wordguessed)}")
    if '-' not in wordguessed or not guesses:
        print(f"You {'lost' if not guesses else 'won'}! The word was {word}")


def helpdesk():
    print(open('hangmanhelp.txt').read())


def start():
    import random
    word = random.choice(open('hangmanwords.txt').readlines()).strip()
    opening(word)
    q = input('Would you like to play again? ')
    if q.lower().startswith('y'):
        start()
    else:
        print('Thank you for playing!')


start()