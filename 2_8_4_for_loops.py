start = int(input("Enter start: "))
end = int(input("Enter end: "))

increment = 1

if start > end:
  increment = -1
  end = end - 1
else:
  end = end + 1

for i in range(start, end, increment):
  print(i)