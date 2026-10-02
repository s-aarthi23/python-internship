numbers = [12,45,7,89,23]
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_largest(numbers))