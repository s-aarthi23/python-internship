import random

secret = random.randint(1, 10)
guess = int(input("Guess the number:"))
if guess == secret:
    print("Congratulations! You guessed the number.")
else:
    print("Wrong! The number was", secret)    

