products = ["Pen","Book","Bag"]
prices = [10,50,500]
quantities = [2,3,1]
for product,price,quantity in zip(products,prices,quantities):
    total = price*quantity
    print(product,"-",total)