i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#to print set of even numbers between 2 and 10
for num in range(2, 10):
  if num % 2 == 0:
    print("Found an even number", num)
    continue
    print("Found a number", num)