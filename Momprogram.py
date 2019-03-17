import re, random
words = input("Type the words here: ")
wordlist = re.findall(r"\w+",words)
for w,x in enumerate(wordlist):
    x = list(x)
    random.shuffle(x)
    x = ''.join(x)
    wordlist[w] = x
random.shuffle(wordlist)
print(', '.join(wordlist))