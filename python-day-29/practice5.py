names = ["Aarthi","Priya","Divya","Kavi"]
marks = [90,75,88,95]
for index,(name,mark) in enumerate(zip(names,marks)):
    print(index,name,mark)