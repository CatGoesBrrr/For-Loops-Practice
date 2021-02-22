subtotal = 0

for i in range(3):
  price = float(input("Please enter the price of product " + str(i+1) + ": "))
  qty = int(input("Please enter the quantity of product " + str(i+1) + ": "))
  subtotal += price*qty

total = subtotal * 1.13
print("Your total is $" + str(round(total,2)))