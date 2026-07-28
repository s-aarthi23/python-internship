class UPI():
    def pay(self):
        print("Paid using UPI")
class Card():
    def pay(self):
        print("Paid using card")
class Cash():
    def pay(self):
        print("Paid using cash")
methods=[UPI(),Card(),Cash()]
for i in  methods:
    i.pay()
                       