names = ["Aarthi","Priya","Divya"]
marks = [90,85,95]
for index, (name, mark) in enumerate(zip(names, marks)):
    print(index, name, mark)