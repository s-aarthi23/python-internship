import os
file = __file__
if os.path.exists(file):
    print(os.path.getsize(file),"bytes")
else:
    print("File not found")    