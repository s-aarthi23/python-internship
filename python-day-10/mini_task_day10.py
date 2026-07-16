Data={"Sasi":98,"Mani":85,"Sakthi":100,"Ram":60,"Karthik":90}
print(Data)

for name,marks in Data.items():
    if marks==max(Data.values()):
        print(name,marks)

Data=input("Enter the name: ")
count={}
for i in Data:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

key=input("Enter the key to check: ")
if key in Data:
    print("Key is found in the dictionary")
else:
    print("Key is not found in the dictionary")    

a={"s":1,"a":2,"p":7}
b={"b":0,"h":3,"a":4}
a.update(b)
print(a)  