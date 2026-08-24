import os
os.mkdir("OldFolder")
os.rename("OldFolder", "NewFolder")
print(os.listdir())