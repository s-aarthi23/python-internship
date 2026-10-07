marks = [90,45,60,80,77]
average = sum(marks) / len(marks)
if average >= 50:
    print("Pass")   
else:
    print("Fail")
print("Average marks:", average)
print("Highest marks:", max(marks)) 
print("Lowest marks:", min(marks))
        