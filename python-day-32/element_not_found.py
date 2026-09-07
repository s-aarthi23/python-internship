numbers = [12,25,7,30,18]
target = 50
for i in range(len(numbers)):
    if numbers[i]==target:
        print("Element found at index:", i)
        break
else:
    print("Element not found")