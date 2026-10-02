numbers = [12,7,18,25,30,41,50]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print("Even:", count)
print("Odd:", len(numbers) - count)