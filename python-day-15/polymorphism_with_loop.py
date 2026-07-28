class Dog():
    def sound(self):
        print("Dog:Barks")
class Cat():
    def sound(self):
        print("Cat:Meow") 
class Cow():
    def sound(self):
        print("Cow:Maaa") 
animals=[Dog(),Cat(),Cow()]
for i in animals:
    i.sound()                      