import random
print ("Type 'hangman ()' in order to play. Please type in the two parentheses, but not the quotes.")
def hangamn ():
    print ("You have misspelled hangman. Please retype 'hangman ()'")
def hangman ():
    #Unused variables: i, w
    #Non-letter vars: c (incorrect guesses), f (str c), q (correct guesses), v (easy, etc.), x (word), z (input)
    #Important: u is letter for z
    y = 0    #controls letter y
    h = 0    #controls letter h
    e = 0    #controls letter e
    l = 0    #controls letter l
    g = 0    #controls letter g
    b = 0    #controls letter b
    p = 0    #controls letter p
    t = 0    #controls letter t
    n = 0    #controls letter n
    o = 0    #controls letter o
    a = 0    #controls letter a
    s = 0    #controls letter s
    m = 0    #controls letter m
    r = 0    #controls letter r
    k = 0    #controls letter k
    d = 0    #controls letter d
    j = 0    #controls letter j
    u = 0    #controls letter z
    q = 0    #variable for correct guesses
    c = 0    #variable for incorrect guesses
    x = random.randint (1,8)    #sets x to a random num. between 1 and 8
    list1 = ['hello', 'goodbye', 'python', 'apples', 'amtrak', 'bananas', 'pears','jazzed']    #Sets list1 to the 7 words
    print ("This is hangman.") #Explains the game
    print ('Type "quit" to quit')
    v = input ('Do you want easy, medium, or hard? ')
    while c == 0:
        if v == 'easy':
            c = 10    #if easy selected, sets guesses to 10
        else:
            if v == 'medium':
                c = 7
            else:
                if v == 'hard':
                    c = 5
                else:
                    if v == 'quit':
                        z = input ("Are you sure you want to quit? Retype 'quit' to quit. ")
                        if z == 'quit':
                            x = 0
                            q = 500
                            c = 1
                            print ('You have quit hangman.')
                        else:
                            v == input ('You have not quit hangman. Please insert a difficulty. ')
                    else:
                        v = input ('You have not typed in a valid difficulty. Please type in easy, medium, or hard. ')   
    if x == 1:    #runs the code if x = 1
        list2 = ['h','e','l','l','o']    #sets list2 to h,e,l,l,o
        q = 0   #sets q to 0
        print ('This word has 5 letters')    #prints that the word has 5 letters
        while q < 4:    #runs the code while q < 4
            z = input ('Please insert a letter ')    #asks to input a letter
            if z == 'h':    #runs code if h was typed in
                print ('Correct! H goes in the first letter spot.')    #Says that the letter is right
                h = 1 + h    #adds 1 to h
                if h == 1:    #tells the computer one more correct letter
                    q = q + 1
            else:
                if z == 'e':    #Same as above code
                    print ('Correct! E goes in the second letter spot.')
                    e = e + 1
                    if e == 1:
                        q = q + 1
                else:
                    if z == 'l':
                        print ('Correct! L goes in the third and fourth letter spots.')
                        l = l + 1
                        if l == 1:
                            q = q + 1
                    else:
                        if z == 'o':
                            print ('Correct! O goes in the fifth letter spot.')
                            o = o + 1
                            if o == 1:
                                q = q + 1
                        else:
                            if z == 'quit':    #quitters' code
                                z = input ('Are you sure you want to quit? Retype "quit" to quit ')    #double-checks if the usser wants to quit
                                if z == 'quit':    #runs next code if they want to quit
                                    q = 500        #sets q to 500 if they decide to quit
                                    print ('You have quit hangman.')    #notifies the user that they have quit
                            else:
                                if z == '':    #No letter typed in code
                                        print ('You need to type in a letter!')
                                else:
                                    if z == 'hello':
                                        print ('Correct! Hello is the word!')
                                        q = 100
                                    else:
                                        if len(z) > 1:    #runs code if more than 1 letter inserted
                                            print ('Please only insert 1 character!')
                                        else:
                                            if z == ('1') or z == ('2') or z == ('3') or z == ('4') or z == ('5') or z == ('6') or z == ('7') or z == ('8') or z == ('9') or z == ('0'): #runs code if number typed in
                                                print ('There are no numbers in this word.')
                                            else:
                                                c = c - 1    #Decreases the number of remaining incorrect guesses by 1
                                                f = str (c)    #Allows the comp. to print the number of incorrect guesses
                                                print ('Incorrect!')    #Tells the user the letter is incorrect
                                                print ('You have '+f+' incorrect answers remaining')    #Tells the user the # of inc. guesses left
                                                if c == 0:
                                                    q = 300    #sets q to 300 if they are out of guesses
                                                    print ("You have lost. The word was 'hello' Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")#user lose msg
            if q < 100:
                print ('Your word is:')
                if h > 0:           #says h if h has been typed, and a blank if it wasn't
                    print ('h')
                else:
                    print ('_')
                if e > 0:           #ditto
                    print ('e')
                else:
                    print ('_')
                if l > 0:
                    print ('l')
                    print ('l')
                else:
                    print ('_')
                    print ('_')
                if o > 0:
                    print ('o')
                else:
                    print ('_')
        if q < 300:
            print ("You Won! Thank you for playing hangman v. 3.5.3. Type 'hangman' () to play again")    #Tells the user they won if they won
    if x == 2:
        list2 = ['g','o','o','d','b','y','e']
        q = 0
        print ('This word has 7 letters')
        while q < 6:
            z = input ('Please insert a letter ')
            if z == 'g':
                print ('Correct! G goes in the first letter spot.')
                g = 1 + g
                if g == 1:
                    q = q + 1
            else:
                if z == 'o':
                    print ('Correct! O goes in the second and third letter spots.')
                    o = o + 1
                    if o == 1:
                        q = q + 1
                else:
                    if z == 'd':
                        print ('Correct! D goes in the fourth letter spot.')
                        d = d + 1
                        if d == 1:
                            q = q + 1
                    else:
                        if z == 'b':
                            print ('Correct! B goes in the fifth letter spot.')
                            b = b + 1
                            if b == 1:
                                q = q + 1
                        else:
                            if z == 'y':
                                print ('Correct! Y goes in the sixth letter spot.')
                                y = y + 1
                                if y == 1:
                                    q = q + 1
                            else:
                                if z == 'e':
                                    print ('Correct! E goes in the seventh letter spot')
                                    e = e + 1
                                    if e == 1:
                                        q = q + 1
                                else:
                                    if z == 'quit':
                                        z = input ('Are you sure you want to quit? Retype "quit" to quit ')
                                        if z == 'quit':
                                            q = 500
                                            print ('You have quit hangman.')
                                    else:
                                        if z == '':
                                            print ('You need to type in a letter!')
                                        else:
                                            if z == 'goodbye':
                                                print ("Correct! Goodbye is the word!")
                                                q = 100
                                            else:
                                                if len(z) > 1:
                                                    print ('Please only insert 1 character!')
                                                else:
                                                    if z == ('1') or z == ('2') or z == ('3') or z == ('4') or z == ('5') or z == ('6') or z == ('7') or z == ('8') or z == ('9') or z == ('0'):
                                                        print ('There are no numbers in this word.')
                                                    else:
                                                        c = c - 1
                                                        f = str (c)
                                                        print ('Incorrect!')
                                                        print ('You have '+f+' incorrect answers remaining')
                                                        if c == 0:
                                                            q = 300
                                                            print ("You have lost. The word was 'goodbye'. Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
            if q < 100:
                print ('Your word is:')
                if g > 0:
                    print ('g')
                else:
                    print ('_')
                if o > 0:
                    print ('o')
                    print ('o')
                else:
                    print ('_')
                    print ('_')
                if d > 0:
                    print ('d')
                else:
                    print ('_')
                if b > 0:
                    print ('b')
                else:
                    print ('_')
                if y > 0:
                    print ('y')
                else:
                    print ('_')
                if e > 0:
                    print ('e')
                else:
                    print ('_')
        if q < 300:
            print ("You Won! Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
    if x == 3:
        list2 = ['p','y','t','h','o','n']
        q = 0
        print ('This word has 6 letters')
        while q < 6:
            z = input ('Please insert a letter ')
            if z == 'p':
                print ('Correct! P goes in the first letter spot.')
                p = 1 + p
                if p == 1:
                    q = q + 1
            else:
                if z == 'y':
                    print ('Correct! Y goes in the second letter spot.')
                    y = y + 1
                    if y == 1:
                        q = q + 1
                else:
                    if z == 't':
                        print ('Correct! T goes in the third letter spot.')
                        t = t + 1
                        if t == 1:
                            q = q + 1
                    else:
                        if z == 'h':
                            print ('Correct! H goes in the fourth letter spot.')
                            h = h + 1
                            if h == 1:
                                q = q + 1
                        else:
                            if z == 'o':
                                print ('Correct! O goes in the fifth letter spot.')
                                o = o + 1
                                if o == 1:
                                    q = q + 1
                            else:
                                if z == 'n':
                                    print ('Correct! N goes in the sixth letter spot.')
                                    n = n + 1
                                    if n == 1:
                                        q = q + 1
                                else:
                                    if z == 'quit':
                                        z = input ('Are you sure you want to quit? Retype "quit" to quit ')
                                        if z == 'quit':
                                            q = 500
                                            print ('You have quit hangman.')
                                    else:
                                        if z == '':
                                            print ('You need to type in a letter!')
                                        else:
                                            if z == 'python':
                                                print ("Correct! Python is the word!")
                                                q = 100
                                            else:
                                                if len(z) > 1:
                                                    print ('Please only insert 1 character!')
                                                else:
                                                    if z == ('1') or z == ('2') or z == ('3') or z == ('4') or z == ('5') or z == ('6') or z == ('7') or z == ('8') or z == ('9') or z == ('0'):
                                                        print ('There are no numbers in this word.')
                                                    else:
                                                        c = c - 1
                                                        f = str (c)
                                                        print ('Incorrect!')
                                                        print ('You have '+f+' incorrect answers remaining')
                                                        if c == 0:
                                                            q = 300
                                                            print ("You have lost. The word was 'python'. Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
            if q < 100:
                print ('Your word is:')
                if p > 0:
                    print ('p')
                else:
                    print ('_')
                if y > 0:
                    print ('y')
                else:
                    print ('_')
                if t > 0:
                    print ('t')
                else:
                    print ('_')
                if h > 0:
                    print ('h')
                else:
                    print ('_')
                if o > 0:
                    print ('o')
                else:
                    print ('_')
                if n > 0:
                    print ('n')
                else:
                    print ('_')
        if q < 300:
            print ("You Won! Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
    if x == 4:
        list2 = ['a','p','p','l','e','s']
        q = 0
        print ('This word has 6 letters')
        while q < 5:
            z = input ('Please insert a letter ')
            if z == 'a':
                print ('Correct! A goes in the first letter spot.')
                a = 1 + a
                if a == 1:
                    q = q + 1
            else:
                if z == 'p':
                    print ('Correct! P goes in the second and third letter spots.')
                    p = p + 1
                    if p == 1:
                        q = q + 1
                else:
                    if z == 'l':
                        print ('Correct! L goes in the fourth letter spot.')
                        l = l + 1
                        if l == 1:
                            q = q + 1
                    else:
                        if z == 'e':
                            print ('Correct! E goes in the fifth letter spot.')
                            e = e + 1
                            if e == 1:
                                q = q + 1
                        else:
                            if z == 's':
                                print ('Correct! S goes in the sixth letter spot.')
                                s = s + 1
                                if s == 1:
                                    q = q + 1
                            else:
                                if z == 'quit':
                                    z = input ('Are you sure you want to quit? Retype "quit" to quit ')
                                    if z == 'quit':
                                        q = 500
                                        print ('You have quit hangman.')
                                else:
                                    if z == '':
                                        print ('You need to type in a letter!')
                                    else:
                                        if z == 'apples':
                                            print ("Correct! Apples is the word!")
                                            q = 100
                                        else:
                                            if len(z) > 1:
                                                print ('Please only insert 1 character!')
                                            else:
                                                if z == ('1') or z == ('2') or z == ('3') or z == ('4') or z == ('5') or z == ('6') or z == ('7') or z == ('8') or z == ('9') or z == ('0'):
                                                    print ('There are no numbers in this word.')
                                                else:
                                                    c = c - 1
                                                    f = str (c)
                                                    print ('Incorrect!')
                                                    print ('You have '+f+' incorrect answers remaining')
                                                    if c == 0:
                                                        q = 300
                                                        print ("You have lost. The word was 'apples'. Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
            if q < 100:
                print ('Your word is:')
                if a > 0:
                    print ('a')
                else:
                    print ('_')
                if p > 0:
                    print ('p')
                    print ('p')
                else:
                    print ('_')
                    print ('_')
                if l > 0:
                    print ('l')
                else:
                    print ('_')
                if e > 0:
                    print ('e')
                else:
                    print ('_')
                if s > 0:
                    print ('s')
                else:
                    print ('_')
        if q < 300:
            print ("You Won! Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
    if x == 5:
        list2 = ['a','m','t','r','a','k']
        q = 0
        print ('This word has 6 letters')
        while q < 5:
            z = input ('Please insert a letter ')
            if z == 'a':
                print ('Correct! A goes in the first and fifth letter spots.')
                a = 1 + a
                if a == 1:
                    q = q + 1
            else:
                if z == 'm':
                    print ('Correct! M goes in the second letter spot.')
                    m = m + 1
                    if m == 1:
                        q = q + 1
                else:
                    if z == 't':
                        print ('Correct! T goes in the third letter spot.')
                        t = t + 1
                        if t == 1:
                            q = q + 1
                    else:
                        if z == 'r':
                            print ('Correct! R goes in the fourth letter spot.')
                            r = r + 1
                            if r == 1:
                                q = q + 1
                        else:
                            if z == 'k':
                                print ('Correct! K goes in the sixth letter spot.')
                                k = k + 1
                                if k == 1:
                                    q = q + 1
                            else:
                                if z == 'quit':
                                    z = input ('Are you sure you want to quit? Retype "quit" to quit ')
                                    if z == 'quit':
                                        q = 500
                                        print ('You have quit hangman.')
                                else:
                                    if z == '':
                                        print ('You need to type in a letter!')
                                    else:
                                        if z == 'amtrak':
                                            print ("Correct! Amtrak is the word!")
                                            q = 100
                                        else:
                                            if len(z) > 1:
                                                print ('Please only insert 1 character!')
                                            else:
                                                if z == ('1') or z == ('2') or z == ('3') or z == ('4') or z == ('5') or z == ('6') or z == ('7') or z == ('8') or z == ('9') or z == ('0'):
                                                    print ('There are no numbers in this word.')
                                                else:
                                                    c = c - 1
                                                    f = str (c)
                                                    print ('Incorrect!')
                                                    print ('You have '+f+' incorrect answers remaining')
                                                    if c == 0:
                                                        q = 300
                                                        print ("You have lost. The word was 'amtrak'. Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
            if q < 100:
                print ('Your word is:')
                if a > 0:
                    print ('a')
                else:
                    print ('_')
                if m > 0:
                    print ('m')
                else:
                    print ('_')
                if t > 0:
                    print ('t')
                else:
                    print ('_')
                if r > 0:
                    print ('r')
                else:
                    print ('_')
                if a > 0:
                    print ('a')
                else:
                    print ('_')
                if k > 0:
                    print ('k')
                else:
                    print ('_')
        if q < 300:
            print ("You Won! Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
    if x == 6:
        list2 = ['b','a','n','a','n','a','s']
        q = 0
        print ('This word has 7 letters')
        while q < 4:
            z = input ('Please insert a letter ')
            if z == 'b':
                print ('Correct! B goes in the first letter spot.')
                b = 1 + b
                if b == 1:
                    q = q + 1
            else:
                if z == 'a':
                    print ('Correct! A goes in the second, fourth and sixth letter spots.')
                    a = a + 1
                    if a == 1:
                        q = q + 1
                else:
                    if z == 'n':
                        print ('Correct! N goes in the third and fifth letter spots.')
                        n = n + 1
                        if n == 1:
                            q = q + 1
                    else:
                        if z == 's':
                            print ('Correct! S goes in the seventh letter spot.')
                            s = s + 1
                            if s == 1:
                                q = q + 1
                        else:
                            if z == 'quit':
                                z = input ('Are you sure you want to quit? Retype "quit" to quit ')
                                if z == 'quit':
                                    q = 500
                                    print ('You have quit hangman.')
                            else:
                                if z == '':
                                    print ('You need to type in a letter!')
                                else:
                                    if z == 'bananas':
                                        print ("Correct! Bananas is the word!")
                                        q = 100
                                    else:
                                        if len(z) > 1:
                                            print ('Please only insert 1 character!')
                                        else:
                                            if z == ('1') or z == ('2') or z == ('3') or z == ('4') or z == ('5') or z == ('6') or z == ('7') or z == ('8') or z == ('9') or z == ('0'):
                                                print ('There are no numbers in this word.')
                                            else:
                                                c = c - 1
                                                f = str (c)
                                                print ('Incorrect!')
                                                print ('You have '+f+' incorrect answers remaining')
                                                if c == 0:
                                                    q = 300
                                                    print ("You have lost. The word was 'bananas'. Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
            if q < 100:
                print ('Your word is:')
                if b > 0:
                    print ('b')
                else:
                    print ('_')
                if a > 0:
                    print ('a')
                else:
                    print ('_')
                if n > 0:
                    print ('n')
                else:
                    print ('_')
                if a > 0:
                    print ('a')
                else:
                    print ('_')
                if n > 0:
                    print ('n')
                else:
                    print ('_')
                if a > 0:
                    print ('a')
                else:
                    print ('_')
                if s > 0:
                    print ('s')
                else:
                    print ('_')
        if q < 300:
            print ("You Won! Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
    if x == 7:
        list2 = ['p','e','a','r','s']
        q = 0
        print ('This word has 5 letters')
        while q < 5:
            z = input ('Please insert a letter ')
            if z == 'p':
                print ('Correct! P goes in the first letter spot.')
                p = p + 1
                if p == 1:
                    q = q + 1
            else:
                if z == 'e':
                    print ('Correct! E goes in the second letter spot.')
                    e = e + 1
                    if e == 1:
                        q = q + 1
                else:
                    if z == 'a':
                        print ('Correct! A goes in the third letter spot.')
                        a = a + 1
                        if a == 1:
                            q = q + 1
                    else:
                        if z == 'r':
                            print ('Correct! R goes in the fifth letter spot.')
                            r = r + 1
                            if r == 1:
                                q = q + 1
                        else:
                            if z == 's':
                                print ('Correct! S goes in the sixth letter spot.')
                                s = s + 1
                                if s == 1:
                                    q = q + 1
                            else:
                                if z == 'quit':
                                    z = input ('Are you sure you want to quit? Retype "quit" to quit ')
                                    if z == 'quit':
                                        q = 500
                                        print ('You have quit hangman.')
                                else:
                                    if z == '':
                                        print ('You need to type in a letter!')
                                    else:
                                        if z == 'pears':
                                            print ("Correct! Pears is the word!")
                                            q = 100
                                        else:
                                            if len(z) > 1:
                                                print ('Please only insert 1 character!')
                                            else:
                                                if z == ('1') or z == ('2') or z == ('3') or z == ('4') or z == ('5') or z == ('6') or z == ('7') or z == ('8') or z == ('9') or z == ('0'):
                                                    print ('There are no numbers in this word.')
                                                else:
                                                    c = c - 1
                                                    f = str (c)
                                                    print ('Incorrect!')
                                                    print ('You have '+f+' incorrect answers remaining')
                                                    if c == 0:
                                                        q = 300
                                                        print ("You have lost. The word was 'pears'. Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
            if q < 100:
                print ('Your word is:')
                if p > 0:
                    print ('p')
                else:
                    print ('_')
                if e > 0:
                    print ('e')
                else:
                    print ('_')
                if a > 0:
                    print ('a')
                else:
                    print ('_')
                if r > 0:
                    print ('r')
                else:
                    print ('_')
                if s > 0:
                    print ('s')
                else:
                    print ('_')
        if q < 300:
            print ("You Won! Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
    if x == 8:
        list2 = ['j','a','z','z','e','d']
        q = 0
        print ('This word has 6 letters')
        while q < 5:
            z = input ('Please insert a letter ')
            if z == 'j':
                print ('Correct! J goes in the first letter spot.')
                j = 1 + j
                if j == 1:
                    q = q + 1
            else:
                if z == 'a':
                    print ('Correct! A goes in the second spot.')
                    a = a + 1
                    if a == 1:
                        q = q + 1
                else:
                    if z == 'z':
                        print ('Correct! Z goes in the third and fourth letter spots.')
                        u = u + 1
                        if u == 1:
                            q = q + 1
                    else:
                        if z == 'e':
                            print ('Correct! E goes in the fifth letter spot.')
                            e = e + 1
                            if e == 1:
                                q = q + 1
                        else:
                            if z == 'd':
                                print ('Correct! D goes in the sixth letter spot.')
                                d = d + 1
                                if d == 1:
                                    q = q + 1
                            else:
                                if z == 'quit':
                                    z = input ('Are you sure you want to quit? Retype "quit" to quit ')
                                    if z == 'quit':
                                        q = 500
                                        print ('You have quit hangman.')
                                else:
                                    if z == '':
                                        print ('You need to type in a letter!')
                                    else:
                                        if z == 'jazzed':
                                            print ("Correct! Jazzed is the word!")
                                            q = 100
                                        else:
                                            if len(z) > 1:
                                                print ('Please only insert 1 character!')
                                            else:
                                                if z == ('1') or z == ('2') or z == ('3') or z == ('4') or z == ('5') or z == ('6') or z == ('7') or z == ('8') or z == ('9') or z == ('0'):
                                                    print ('There are no numbers in this word.')
                                                else:
                                                    c = c - 1
                                                    f = str (c)
                                                    print ('Incorrect!')
                                                    print ('You have '+f+' incorrect answers remaining')
                                                    if c == 0:
                                                        q = 300
                                                        print ("You have lost. The word was 'jazzed'. Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
            if q < 100:
                print ('Your word is:')
                if j > 0:
                    print ('j')
                else:
                    print ('_')
                if a > 0:
                    print ('a')
                else:
                    print ('_')
                if u > 0:
                    print ('z')
                    print ('z')
                else:
                    print ('_')
                    print ('_')
                if e > 0:
                    print ('e')
                else:
                    print ('_')
                if d > 0:
                    print ('d')
                else:
                    print ('_')
        if q < 300:
            print ("You Won! Thank you for playing hangman v. 3.5.3. Type 'hangman ()' to play again")
