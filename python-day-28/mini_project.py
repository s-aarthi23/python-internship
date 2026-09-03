numbers = [5,12,8,20,3,15]
doubled = list(map(lambda x: x*2,numbers))
even = list(filter(lambda x: x%2==0,numbers))
greater = list(filter(lambda x : x>10 , numbers))
print("Original:",numbers)
print("Doubled:",doubled)
print("Even Numbers:",even)
print("Greater than 10:",greater)