import os
import shutil

path = "D:/course videos/"

names = os.listdir(path)

x = 1

previous_name = names[0]

for name in names:
    print(name[0:9])
    if(x == 1):
        dir_name = "Section " + name[3:5]
        if not os.path.exists(path+dir_name):
            os.makedirs(path+dir_name)

        shutil.move(path+name, path+dir_name)
        x = 2
        continue

    if(previous_name[:5] == name[:5]):
        dir_name = "Section " + name[3:5]
        shutil.move(path+name, path+dir_name)
    else:
        dir_name = "Section " + name[3:5]
        if not os.path.exists(path+dir_name):
            os.makedirs(path+dir_name)
        shutil.move(path+name, path+dir_name)
        print("Not same")
    previous_name = name
    x += 1
