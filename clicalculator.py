import sys
command =(sys.argv)
a = int(command[2])
b = int(command[3])
if command[1] == 'add':
    print(a + b)
elif command[1] == 'subtract':
    print(a - b)
elif command[1] == 'multiply':
    print(a*b)
elif command == 'divide':
    print(a/b)
else:
    print('Invalid input')              
