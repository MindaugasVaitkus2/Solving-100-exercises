# Please download the attached ZIP file and extract its files in a folder. Then, write a script that counts and prints out the number of .py files in that folder.
import glob
import os

path = r'../inputs&outputs/files/'
py_files = len(glob.glob(os.path.join(path, "*.py")))
print (py_files)
