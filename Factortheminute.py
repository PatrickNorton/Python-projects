import time; from sympy.ntheory import factorint
while True:
    clock = time.asctime().split(' ')
    factors = list(factorint(int(clock[3][0:2]+clock[3][3:5]+clock[3][6:8])).keys())
    factors = [str(q) for q in factors]
    if len(factors) == 1:
        print (clock[3], 'prime')
    else:
        print (clock[3],','.join(factors))
    y = int(clock[3][6:8])
    time.sleep(1-1/38-1/20+1/180)
