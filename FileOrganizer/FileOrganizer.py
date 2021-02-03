import os
import shutil

path = input("Enter Path Name : ")

file_object = os.listdir(path)

for file in file_object:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    print(ext[0:])

    if ext == '':
        continue
    
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + file, path + '/' + ext)

    else:
        os.makedirs(path + '/' + ext)
        shutil.move(path + '/' + file, path + '/' + ext)