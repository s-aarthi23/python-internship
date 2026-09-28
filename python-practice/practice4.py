numbers = [12,45,23,67,34,89,10]
search = int(input("Enter a number:"))
for num in numbers:
    if num == search:
        print("Found")
        break
else:
    print("Not Found")      