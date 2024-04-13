import os
import shutil
from_dir="c:/Users/SARAF/Downloads"
to_dir="c:/Users/SARAF/OneDrive/Desktop/Document_Files"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file1 in list_of_files:
    name,extension = os.path.splitext(file1)
    print(name)
    print(extension)
