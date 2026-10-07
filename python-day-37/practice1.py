marks = [90,45,60,80,77]
average = sum(marks) / len(marks)
if average >= 90:
    grade = "A"
elif 75 <= average <= 89:
    grade = "B"
elif 50 <= average <= 74:
    grade = "C"
else:
    grade = "D"    
print("Grade:", grade)
