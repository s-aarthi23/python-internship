numbers = [10,25,8,40,25,15,30,8,12,40]
seen =[]
duplicates = []
for num in numbers:
    if num not in duplicates and num in seen:
        duplicates.append(num)
    else:
        seen.append(num)
print("The duplicate numbers are:", duplicates)