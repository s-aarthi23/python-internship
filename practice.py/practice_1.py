numbers = [10,25,8,40,15,30]
temp = numbers[0]
for num in numbers:
    if num > temp:
        temp = num
print(temp,"is the largest number")  
total = 0    
for num in numbers: 
    sum = num + total
    total = sum  
print("The sum of the numbers is:", total)
average = total / len(numbers)
print("The average of the numbers is:", average)
temp1 = numbers[0]
for num in numbers:
    if num < temp1:
        temp1 = num
print(temp1,"is the smallest number")    