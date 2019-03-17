def machine ():
    a,b,c,d,e,f,g,h,i = 1,1,1,1,1,1,1,1,1 #Values of the spaces at start (1 is empty, 2 is full)
    listin = [a,b,c,d,e,f,g,h,i]
    a00,a01,a02,a03,a04,a05,a06,a07,a08 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random() #Values of the multipliers for each list in the first layer
    lista0 = [a00,a01,a02,a03,a04,a05,a06,a07,a08]
    a10,a11,a12,a13,a14,a15,a16,a17,a18 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    lista1 = [a10,a11,a12,a13,a14,a15,a16,a17,a18]
    a20,a21,a22,a23,a24,a25,a26,a27,a28 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    lista2 = [a20,a21,a22,a23,a24,a25,a26,a27,a28]
    a30,a31,a32,a33,a34,a35,a36,a37,a38 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    lista3 = [a30,a31,a32,a33,a34,a35,a36,a37,a38]
    a40,a41,a42,a43,a44,a45,a46,a47,a48 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    lista4 = [a40,a41,a42,a43,a44,a45,a46,a47,a48]
    a50,a51,a52,a53,a54,a55,a56,a57,a58 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    lista5 = [a50,a51,a52,a53,a54,a55,a56,a57,a58]
    a60,a61,a62,a63,a64,a65,a66,a67,a68 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    lista6 = [a60,a61,a62,a63,a64,a65,a66,a67,a68]
    a70,a71,a72,a73,a74,a75,a76,a77,a78 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    lista7 = [a70,a71,a72,a73,a74,a75,a76,a77,a78]
    a80,a81,a82,a83,a84,a85,a86,a87,a88 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    lista8 = [a80,a81,a82,a83,a84,a85,a86,a87,a88]
    b00,b01,b02,b03,b04,b05,b06,b07,b08 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    listax = [lista0,lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8]
    listb0 = [b00,b01,b02,b03,b04,b05,b06,b07,b08]
    b10,b11,b12,b13,b14,b15,b16,b17,b18 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random() #Ditto for the second layer
    listb1 = [b10,b11,b12,b13,b14,b15,b16,b17,b18]
    b20,b21,b22,b23,b24,b25,b26,b27,b28 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    listb2 = [b20,b21,b22,b23,b24,b25,b26,b27,b28]
    b30,b31,b32,b33,b34,b35,b36,b37,b38 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    listb3 = [b30,b31,b32,b33,b34,b35,b36,b37,b38]
    b40,b41,b42,b43,b44,b45,b46,b47,b48 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    listb4 = [b40,b41,b42,b43,b44,b45,b46,b47,b48]
    b50,b51,b52,b53,b54,b55,b56,b57,b58 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    listb5 = [b50,b51,b52,b53,b54,b55,b56,b57,b58]
    b60,b61,b62,b63,b64,b65,b66,b67,b68 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    listb6 = [b60,b61,b62,b63,b64,b65,b66,b67,b68]
    b70,b71,b72,b73,b74,b75,b76,b77,b78 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    listb7 = [b70,b71,b72,b73,b74,b75,b76,b77,b78]
    b80,b81,b82,b83,b84,b85,b86,b87,b88 = 2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random(),2*random.random()
    listb8 = [b80,b81,b82,b83,b84,b85,b86,b87,b88]
    listbx = [listb0,listb1,listb2,listb3,listb4,listb5,listb6,listb7,listb8];x = 0
    while x < 1: #Number of training runs
        #Fix this bit so it runs multiple times per game
        lista = [0,0,0,0,0,0,0,0,0];listb = [0,0,0,0,0,0,0,0,0];global theSum;listay,listby = list(),list()
        for i in range(len(listax)):
            listay = list()
            for j in range(len(listax[i])):
                listaxx = list();listaxx.append(listax[i]*listin[i])
                listaxx=listaxx[0];sumlist(listaxx);listay.append(theSum)
            sumlist(listay);lista[i]=theSum;print (lista)
        print(lista)
        for i in range(len(listbx)):
            listby = list()
            for j in range(len(listbx[i])):
                listbxx = list();listbxx.append(listbx[i]*lista[i])
                listbxx=listbxx[0];sumlist(listbxx);listby.append(theSum)
            sumlist(listby);listb[i]=theSum;print (listb)
        while itemcheck == False:
            move = listb.index(max(listb))
            if 1 not in listin:
                #Tie codecheck here!
            elif listb[move] == 1:
                listb[move] += 1
                #Win codecheck here!
            else:
                listb[move] = 0
        x += 1
        print(lista)
def sumlist (listforsum):
    global theSum; theSum = 0
    for i in range(len(listforsum)):
        theSum += listforsum[i]
import random;machine()
