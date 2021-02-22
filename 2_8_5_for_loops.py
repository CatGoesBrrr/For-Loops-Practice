number = int(input("Enter number: "))
total = 0

for i in range (0, number):
  print(i)
  total = total + i
  
print("Sum: " + str(total))