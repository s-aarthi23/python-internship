f=open("file.txt","r")
content=f.readlines()
print("Number of lines in the file:", len(content))
f.close()