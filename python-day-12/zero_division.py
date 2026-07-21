a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
try:
    c=a//b
    print("The value is:",c)
except ZeroDivisionError:
    print("Zero division error")
        


  