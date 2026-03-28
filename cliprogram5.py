import sys
argument = (sys.argv)
if len(argument) < 2:
    print('Wrong usage!! \n enter right command' )

command = (sys.argv)
if command[1].lower()  == ('add'):
    print('Added to task list')

elif command[1].lower() ==('list'):
    print('list added to task list')
else:
    print('Wrong command given !!')    


