import sys
arguments = (sys.argv)
if len(arguments) < 2:
    print('Invalid input')
if arguments[1] == 'add':
     task = (sys.argv)
     with open('tasks.txt' ,'a') as file:
         file.write(task[2] + '\n')
     print('Task added: ' + task[2]) 
elif arguments[1] == 'list' :
 with open('tasks.txt', 'r') as file:
    tasks = file.readlines()
 for i , task in enumerate(tasks,1):
        print(i,task.strip())   
elif arguments[1] == 'delete':
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
    index = int(sys.argv[2]) - 1
    del tasks[index]
    with open('tasks.txt', 'w') as file:
        file.writelines(tasks)
elif arguments[1] == 'mark':
    with open('tasks.txt','r') as file:
        tasks = file.readlines()
    index = int(sys.argv[2]) - 1
    if index < 0 or index >= len(tasks):
        print('invald index number')
    else:
         tasks[index] = 'Done '  + tasks[index] 
         with open('tasks.txt','w') as file:
              file.writelines(tasks)
         print('Task marked as done')
elif arguments[1] == 'search':
    with open('tasks.txt', 'r') as file:
         tasks = file.readlines()
         keyword = input('What you want to search ? :')
         found = False
         for task in tasks:
             if keyword == task.strip():
                 found = True
         if found:
             print('Founded')
         else:
             print('Not founded')            
elif arguments[1] == 'update':
    with open('tasks.txt','r') as file:
        tasks = file.readlines()
        index = int(sys.argv[2]) - 1
        update_task = input('Whats the new task you want to enter? :') 
        tasks[index] = update_task + '\n'
    with open('tasks.txt','w') as file:
        file.writelines(tasks)
    print('Task has been updated')                       
else:
    print('Invalid task given')    
    