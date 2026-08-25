import os

file = __file__
print("Current Folder:",os.getcwd())
print("File Name:",os.path.basename(file))
print("Folder:",os.path.dirname(file))
print("File Extension:",os.path.splitext(file)[1])
print("File Exists:",os.path.isfile(file))
print("File Size:",os.path.getsize(file),"bytes")
print("Absolute Path:",os.path.abspath(file))