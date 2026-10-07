marks = [90,45,60,80,77]
pass_count = 0
fail_count = 0
for mark in marks:
    if mark>=50:
        pass_count += 1
        print("pass")
    else:
        fail_count += 1
        print("fail")
print("Total students who passed:", pass_count)
print("Total students who failed:", fail_count)
