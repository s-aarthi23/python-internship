def count_even(*args):
    count = 0
    for num in args:
        if num%2 == 0:
            count = count + 1
    return count
print(count_even(10,15,20,23,30))