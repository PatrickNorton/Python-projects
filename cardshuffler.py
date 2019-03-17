import random
prevdecks = []
deck = ['AS','2S',
while currentdeck not in prevdecks[:-1]:
    currentdeck = random.shuffle(currentdeck)
    
with open('carddata','a+') as timesprevious:
    timesprevious.write('we\n')
    timesprevious.write('we\n')
    timesprevious.seek(0)
    print(timesprevious.read().splitlines())
    timesprevious.flush()
    timesprevious.close()
