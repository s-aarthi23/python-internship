names = ["Aarthi","Priya","Divya"]
marks1 = [90,75,88]
marks2 = [85,80,92]
for name,m1,m2 in zip(names,marks1,marks2):
    total = m1+m2
    print(name,"-",total)