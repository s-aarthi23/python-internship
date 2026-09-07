numbers = [5,10,15,20,25,30,35,40]
target = 25
low = 0
high = len(numbers) - 1
while low<=high:
    mid = (low+high)//2
    if numbers[mid] == target:
        print("Element found at index:", mid)
        break
    elif numbers[mid]<target:
        low = mid+1
    else:
        high = mid-1 
           