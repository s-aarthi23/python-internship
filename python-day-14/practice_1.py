class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person) :
    def __init__(self,name,age,roll_no):       
        super().__init__(name,age)
        self.roll_no=roll_no

    def display(self):
        print("name=",self.name)
        print("Age=",self.age)
        print("roll_no=",self.roll_no)
       
d1=Student("Aarthi",18,1)
d1.display()


