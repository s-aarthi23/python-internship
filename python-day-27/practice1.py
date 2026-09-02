def calculate_average(*numbers):
    total = sum(numbers)
    length = len(numbers)
    average = total / length 
    return average
print(calculate_average(10, 20, 30))