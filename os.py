import os
from datetime import datetime
os.chdir(r'C:\Users\Aakriti Vishnoi\Desktop')
time = (os.stat('arpan_vishnoi').st_mtime)
print(datetime.fromtimestamp(time))
