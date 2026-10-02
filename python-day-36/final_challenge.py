numbers = [10,25,14,30,7,42,19]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even:", even)
print("Odd:", odd)