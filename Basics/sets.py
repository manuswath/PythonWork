# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in thisset:
  print(x)
#check if value present in this set
print("banana" in thisset)
# Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange")
print(thisset)
# Add multiple items to a set, using the update() method:
thisset.update(["melon", "mango", "grapes"])
print(thisset)
# length of set
print(len(thisset))
# creating set using constructor
constructedSet = set(("guava", "musk-melon", "strawberry")) # note the double round-brackets
print(constructedSet)
#remove item If the item to remove does not exist, remove() will raise an error. If the item to remove does not exist, discard() will NOT raise an error.
thisset.remove("banana")
print(thisset)
thisset.discard("melon")
print(thisset)
# Popping the element
x = thisset.pop()
print(x)
print(thisset)
# clear() method empties the set:
thisset.clear()
print(thisset)
print('##################################################################################################')
#declaring sets a different way
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print('##################################################################################################')
# del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) # results in error as this set is no longer there
