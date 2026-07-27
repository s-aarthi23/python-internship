class Mobile:
    def __init__(self,brand):
        self.brand=brand
        
class SmartPhone(Mobile):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model=model 
    def display(self):
        print("Brand=",self.brand)
        print("Model=",self.model)
        
d1=SmartPhone("Samsung","s24")        
d1.display()        