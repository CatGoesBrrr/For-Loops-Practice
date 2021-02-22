
subtotal = 0

for i in range(3):
  price = float(input("Enter the price for item " + str(i+1) + ": "))
  qty = int(input("Enter the quantity for item " + str(i+1) + ": "))
  subtotal += price*qty

total = subtotal * 1.13
print(round(total,2))