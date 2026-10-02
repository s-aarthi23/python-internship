text = "PythonProgramming"
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count += 1
print("Vowels:", count)