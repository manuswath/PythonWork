# tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#access tuple items
print(thistuple[1])
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.
# thistuple[1] = "blackcurrant"
# del thistuple also results in error
# The values will remain the same:
# print(thistuple)
# loop thru tuple
for x in thistuple:
  print(x)
#check if item exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#tuples length
print("Length of tuples is: ")
print(len(thistuple))
#creating tuples with constructor
constructedtuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(constructedtuple)
print("---------------------------")
# Tuples are immutable Lists are mutable
#new way of declaring tuples
t = 12345, 54321, 'hello!'
print(t)
print("---------------------------")

#nested tuples
u = t, (1, 2, 3, 4, 5)
print(u)