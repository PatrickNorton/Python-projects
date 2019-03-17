import random
print('This is a word encrypter.')
password = input('Please type in the word which you wish to be encrypted.')
while 128 >= len(password):
    password.append(random.randint(1,9))
#Put in some complicated encryptor here
