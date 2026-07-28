class Animal():
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog:Bark")  
class Cat(Animal):
    def sound(self):
        print("Cat:Meow")
dog=Dog()
cat=Cat()
dog.sound()
cat.sound()                      