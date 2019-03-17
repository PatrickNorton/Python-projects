from random import randint
print("I'm thinking of a number between 1 and 10.")
x = input('Guess what it is! ')
y = randint(1,10)
if (int(x) == y)
    print ('Yay! You win!')
else:
    print("Nope!")
