i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#to find a list of prime numbers between 2 and 10
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break
    else:
      # loop fell through without finding a factor
      print(n, 'is a prime number')