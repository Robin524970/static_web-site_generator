import os
import shutil

def copy_all(src, dest):
    directory_items = os.listdir(src)
    for item in directory_items:
        path_to = os.path.join(src, item)

        if os.path.isfile(path_to):
            print(shutil.copy(path_to, dest))
            
        if os.path.isdir(path_to):
            new_dest = os.path.join(dest, item)
            os.mkdir(new_dest)
            copy_all(path_to, new_dest)
 