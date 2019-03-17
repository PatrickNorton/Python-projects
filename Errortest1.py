print("This is a calculator.")
val1 = input("Please type in the first value for calculation.")
val2 = input("Please type in the second value.")
operand = input("Please type in the operation. (+,-,*,/)'
if operand == '+':
    output = val1+val2
elif operand == '-':
    output = val1-val2
elif operand == '*':
    output = val1*val2
elif operand == '/':
    output = val1/val2
print('Your answer is'+str(output))
