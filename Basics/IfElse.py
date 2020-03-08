a = 33
b = 200
#IF
if b > a:
  print("b is greater than a")
#ELIF
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#ELSE
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#ELSE
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#Short hand if
if a > b: print("a is greater than b")
#Short Hand If ... Else
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
#AND
c = 15
if a > b and c > a:
  print("Both conditions are True")
#OR
if a > b or a > c:
  print("At least one of the conditions is True")

c = 15
