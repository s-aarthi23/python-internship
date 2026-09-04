names = ["Aarthi","Priya","Divya"]
marks1 = [90,75,88]
marks2 = [85,80,92]
for index,(name,m1,m2) in enumerate(zip(names,marks1,marks2)):
    total = m1+m2
    average = total/2
    print(index,name)
    print("Total:",total)
    print("Average:",average)
    print()