numbers = [10,25,8,40,15,30,7,12]
even_count = 0
for num in numbers:
    if num%2 == 0:
        print(num,"is an even number")
        even_count += 1
print("The count of even numbers is:", even_count)

odd_count = 0
for num in numbers: 
    if num%2 != 0:
        print(num,"is an odd number")
        odd_count += 1
print("The count of odd numbers is:", odd_count)
