import os
os.chdir(r'C:\Users\Aakriti Vishnoi\Desktop')
file_path = os.path.join(os.environ.get('USERPROFILE'), 'ARPAN.txt')
print(file_path)