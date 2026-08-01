class Student:
    def __init__(self,name,mark):
        self.__name=name
        self.__mark=mark
    def get_name(self):
        return self.__name
    def get_mark(self):
        return self.__mark  
student1=Student("John",85)
print(student1.get_name())
print(student1.get_mark())