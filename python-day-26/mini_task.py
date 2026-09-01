import random

characters = ["A", "B", "C", "1", "2", "3", "@", "#"]

password = ""

for i in range(6):
    password += random.choice(characters)

print(password)   
