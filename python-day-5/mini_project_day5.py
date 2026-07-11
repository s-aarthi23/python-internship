myfiles=open("student_notes.txt","w")
myfiles.write("Name:Aarthiswari\n")
myfiles.write("day5 of python learning was completed successfully")
myfiles.close()
myfiles=open("student_notes.txt","r")
print(myfiles.read())
myfiles.close()
with open("student_notes.txt","a") as myfiles:
    myfiles.write("\nI have learned about file handling in python") 
   
    