import os
import shutil
folder = r'C:\Users\Aakriti Vishnoi\Downloads'
for file in os.listdir(folder):
    if file.endswith('.exe') and file !='python.exe':
     os.makedirs(os.path.join(folder,'Extensions'),exist_ok=True)
     source = os.path.join(folder,file)
     destination = os.path.join(folder,'Extensions',file)
     shutil.move(source,destination)
    if file.endswith('.jpg'):
         os.makedirs(os.path.join(folder,'Images'),exist_ok=True)
         source = os.path.join(folder,file)
         destination = os.path.join(folder,'Images',file)
         shutil.move(source,destination)
    if file.endswith('.txt'):
         os.makedirs(os.path.join(folder,'Text documents'),exist_ok=True)
         source = os.path.join(folder,file)
         destination = os.path.join(folder,'Text documents',file)
         shutil.move(source,destination)
    if file.endswith('.pdf'): 
         os.makedirs(os.path.join(folder,'Pdfs'),exist_ok=True)
         source = os.path.join(folder,file)
         destination = os.path.join(folder,'Pdfs',file)
         shutil.move(source,destination)       
    if file.endswith('.mp3'):
         os.makedirs(os.path.join(folder,'Songs'),exist_ok=True)
         source = os.path.join(folder,file)
         destination = os.path.join(folder,'Songs',file)
         shutil.move(source,destination)