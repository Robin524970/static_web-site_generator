import os
import shutil
from copystatic import copy_all
from generate_page import *

   
def main():
    dest = "./public"
    src = "./static"
    
    if os.path.exists(dest):
        shutil.rmtree(dest)
        os.mkdir(dest)

    if os.path.exists("./static"):
        copy_all(src, dest)
    else:
        raise Exception("Static folder does not exist")
    
    generate_pages_recursive("./content/", "./template.html", "./public/")

main()
