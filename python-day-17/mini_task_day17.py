class Employee:
    def __init__(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        self.__salary=salary
emp=Employee(50000)
print(emp.get_salary()) 
emp.set_salary(60000)
print(emp.get_salary())        