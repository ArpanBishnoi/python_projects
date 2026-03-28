import os
os.chdir(r"C:\Users\Aakriti Vishnoi\Desktop")
for dirpath, dirname, filename in os.walk(r"C:\Users\Aakriti Vishnoi\Desktop"):
 print('Current path: ',  dirpath)
 print('Directories:',  dirname)
 print('Files:' , filename)
 print()