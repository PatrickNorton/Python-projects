num1 = input('Input a number')
num2 = input('Input a second number')
operand = input('Input an operand')
num1 = int(num1)
num2 = int(num2)
if operand == '+':
    print(num1+num2)
elif operand == '-':
    print(num1-num2)
elif operand == '/':
    print(num1/num2)
elif operand == '*':
    print(num1*num2)
