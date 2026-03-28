num1 = float(input('enter num 1:'))
op = input('enter operator:')
num2 = float(input('Enter your num 2:'))
if op == '+':
   print(num1 + num2)
elif op == '-':
    print(num1 - num2)    
elif op == '/':    
     print(num1 / num2)
elif op == '*':
     print(num1 * num2)
else:
    print('Invalid operator')      