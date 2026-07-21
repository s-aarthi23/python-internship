try:
    a=open("filename.txt",'r')
except FileNotFoundError:
    print("The file does not exist")