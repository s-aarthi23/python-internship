def student_result(name,*marks):
    total = sum(marks)
    average = total / len(marks)
    print("Name:",name)
    print("Total:",total)
    print("Average:",average)
    if average >= 50:      
        print("Result:Pass")
    else:
        print("Result:Fail")    
student_result("Aarthi",80,75,90,85)