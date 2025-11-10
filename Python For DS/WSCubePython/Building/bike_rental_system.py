class BikeShop:
    def __init__(self,stock):
        self.stock = stock
    
    def displayBikes(self):
        return f"Total Bikes, {self.stock}"
    
    def rentForBikes(self,quantity):
        if quantity<= 0:
            return "Enter Positive value or greater than zero"
        elif quantity > self.stock:
            return "Enter the value (less than stock)"
        else:
            return f"""Total Price:{quantity*100} & Total Stock:{self.stock-quantity}"""
            
while True:
    obj = BikeShop(100)
    uc = int(input("""
1 Display Stock
2 Rent a bike
3 Exit
"""))
    if uc == 1:
        bikes = obj.displayBikes()
        print(bikes)
    elif uc == 2:
        n = int(input("Enter the quantity: "))
        rb = obj.rentForBikes(n)
        print(rb)
    else:
        break

